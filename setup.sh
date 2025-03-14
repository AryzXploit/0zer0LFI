#!/bin/bash

# Cek apakah dijalankan sebagai root (hanya untuk Linux)
if [[ "$OSTYPE" == "linux-gnu"* ]] && [[ $EUID -ne 0 ]]; then
    echo "❌ This installer must be run as root!"
    exit 1
fi

# Deteksi OS & Versi
OS="Unknown"
OS_VERSION="Unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if [ -f "/data/data/com.termux/files/usr/bin/pkg" ]; then
        OS="Termux"
        OS_VERSION=$(getprop ro.build.version.release)
    else
        OS="Linux"
        OS_VERSION=$(lsb_release -d 2>/dev/null | cut -f2- -d":" | xargs)
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="MacOS"
    OS_VERSION=$(sw_vers -productVersion)
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    OS="Windows"
    OS_VERSION=$(wmic os get Caption,Version | awk 'NR==2 {print $1, $2}')
fi

echo "📌 Detected OS: $OS $OS_VERSION"

# Fungsi Install
install_0zer0LFI() {
    # Cek dependencies
    DEPENDENCIES=("curl" "python3" "pip3" "git" "nuclei" "ruby")
    echo "🔎 Checking dependencies..."
    MISSING=()

    for dep in "${DEPENDENCIES[@]}"; do
        if ! command -v $dep &> /dev/null; then
            MISSING+=("$dep")
        fi
    done

    if [ ${#MISSING[@]} -eq 0 ]; then
        echo "✅ All dependencies are installed."
    else
        echo "⚠️ Missing dependencies: ${MISSING[*]}"
        echo "🔄 Installing missing dependencies..."
        
        if [[ "$OS" == "Linux" ]]; then
            sudo apt-get update
            sudo apt-get install -y ${MISSING[*]}
        elif [[ "$OS" == "Termux" ]]; then
            pkg update
            pkg install -y ${MISSING[*]}
        elif [[ "$OS" == "MacOS" ]]; then
            brew install ${MISSING[*]}
        elif [[ "$OS" == "Windows" ]]; then
            echo "⚠️ Please install: ${MISSING[*]} manually."
        fi
    fi

    # Install Python modules
    echo "🐍 Installing Python dependencies..."
    pip install requests pyfiglet termcolor --break-system-packages

    # Install Nuclei jika belum ada
    if ! command -v nuclei &> /dev/null; then
        echo "⚡ Installing Nuclei..."
        wget https://github.com/projectdiscovery/nuclei/releases/latest/download/nuclei-linux-amd64 -O /usr/bin/nuclei
        chmod +x /usr/bin/nuclei
    fi

    # Setup 0zer0LFI
    echo "📂 Setting up 0zer0LFI..."
    mkdir -p /opt/0zer0LFI

    if [ -d "tools" ]; then
        cp -R tools/ /opt/0zer0LFI/
    else
        echo "⚠️ Warning: 'tools/' directory not found, skipping..."
    fi

    if [ -f "0zer0LFI.py" ]; then
        cp 0zer0LFI.py /opt/0zer0LFI/0zer0LFI.py
    else
        echo "⚠️ Warning: '0zer0LFI.py' not found, skipping..."
    fi

    if [ -f "0zer0Login.py" ]; then
        cp 0zer0Login.py /opt/0zer0LFI/0zer0Login.py
    else
        echo "⚠️ Warning: '0zer0Login.py' not found, skipping..."
    fi

    echo "#!/bin/bash" > /usr/bin/0zer0LFI
    echo "exec python3 /opt/0zer0LFI/0zer0LFI.py \"\$@\"" >> /usr/bin/0zer0LFI
    chmod +x /usr/bin/0zer0LFI

    echo "✅ 0zer0LFI has been successfully installed! Run '0zer0LFI' in your terminal."
}

# Fungsi Delete
delete_0zer0LFI() {
    echo "🗑️ Deleting 0zer0LFI..."
    rm -rf /opt/0zer0LFI
    rm -f /usr/bin/0zer0LFI
    echo "✅ 0zer0LFI has been removed!"
}

# Menu
echo ""
echo "📌 0zer0LFI Installer"
echo "1️⃣ Install 0zer0LFI"
echo "2️⃣ Delete 0zer0LFI"
echo "3️⃣ Exit"
read -p "👉 Choose an option: " OPTION

case $OPTION in
    1)
        install_0zer0LFI
        ;;
    2)
        delete_0zer0LFI
        ;;
    3)
        echo "👋 Exiting..."
        exit 0
        ;;
    *)
        echo "❌ Invalid option. Try again."
        ;;
esac

# 0zer0LFI - Local File Inclusion Scanner & Exploiter

🚀 **0zer0LFI** - Tools keren buat para bug hunter buat nge-scan dan exploitasi LFI (Local File Inclusion) secara otomatis! Ini bukan tools sembarangan, bro. Ini alat buat para elite buat nge-hack dan exploit dengan mudah. 💀💻

---

## 📌 Fitur
- 🔍 **Single URL Scan:** Scan satu URL buat ngecek kerentanan LFI.
- 🐜 **Auto Payload Injection:** Coba berbagai teknik bypass filter otomatis.
- 📝 **List Available LFI Payloads:** Liat payload yang ada beserta CVE ID-nya.
- 🔄 **Auto Exploit:** Bisa otomatis coba bypass filter seperti null byte, encoding, atau wrapper.
- 🔒 **Auth System:** Aman karena pake authentication check.
- 📂 **File Retrieval:** Bisa coba baca file sensitif kayak `/etc/passwd`, `wp-config.php`, dll.

---

## 🅿️ Update Terbaru (v1.x) - Authentication System
Sekarang **0zer0LFI** udah support sistem login & token authentication buat ningkatin keamanan dan tracking session user.

### 🔄 Update yang Ditambahkan:
1. **🔑 Sistem Login & Register**
   - User sekarang harus **register** sebelum bisa akses tools.
   - Setelah register, user bisa **login** dengan username & password yang udah didaftarin.

2. **🛡️ Token Authentication**
   - Setelah login, sistem bakal **generate token** yang berlaku selama **24 jam**.
   - Token ini disimpan di `~/.0zer0LFI/auth_status.json`.
   - Kalau token expired, user harus **login ulang** buat dapetin token baru.

3. **📂 Penyimpanan Data User**
   - Username & password disimpan di `~/.0zer0LFI/session.json`.
   - Token session disimpan di `~/.0zer0LFI/auth_status.json`.
   - **Semua data terenkripsi & aman buat digunakan.**

---

## 📂 Dependencies
- Python 3.x
- pip3
- Requests Library
- BeautifulSoup4 (untuk parsing)
- Nuclei (Opsional, untuk CVE scanning)

---

## 💻 Cara Install
Di Linux & Termux:
```bash
chmod +x setup.sh
./setup.sh
```

---

## 🚀 Cara Run
1. **Jalankan 0zer0Login.py untuk Register/Login:**
```bash
python3 0zer0Login.py
```
- Pilih **Register** buat akun baru.
- Pilih **Login** buat masuk dan generate token.

2. **Jalankan tools utama setelah login:**
```bash
0zer0LFI -u <target>
```

---

## 📌 Cara Gunain Update Baru
### 👅 1. Install/Update Tools
Kalau lo belum install, bisa clone ulang repo atau update via Git:
```bash
git pull origin main
```
Kalau lo manual, cukup replace file `0zer0Login.py` dengan versi terbaru.

---

### 🅿️ 2. Register Akun (Pertama Kali Pakai)
Kalau belum pernah daftar, jalankan tools dan pilih opsi **Register**:
```bash
python3 0zer0Login.py
```
- Masukin **Username**
- Masukin **Password**
- Kalau berhasil, bakal muncul:
  ```bash
  ✅ Registration successful! Please login.
  ```

---

### 🔑 3. Login & Generate Token
Setelah register, masukin username & password buat login:
```bash
python3 0zer0Login.py
```
- Kalau berhasil login, bakal muncul token:
  ```bash
  ✅ Login successful!
  🔑 Your current token: ABCD1234XYZ
  ```
- Token ini bakal **valid selama 24 jam**.
- Kalau token expired, user harus login ulang buat dapetin token baru.

---

### 📌 4. Jalankan Scan LFI
Setelah login, lo bisa langsung scan target pake perintah:
```bash
0zer0LFI -u https://target.com/index.php?file=
```
Fitur tambahan:
- **Scan otomatis:**  
  ```bash
  0zer0LFI -u https://target.com/index.php?file= --scan
  ```
- **Gunakan payload custom:**  
  ```bash
  0zer0LFI -u https://target.com/index.php?file= --payload custom.txt
  ```
- **Coba exploit file penting:**  
  ```bash
  0zer0LFI -u https://target.com/index.php?file= --exploit
  ```

---

## 👥 Tim Pengembang
- AryzXploit (Founder & Lead Developer)
- TimSecc (Contributor!)

---

## 📜 License
Cuman buat pembelajaran. Jangan buat tindakan ilegal, bro! 😜

---

## 🔗 Disclaimer
Gunakan dengan bijak! Penggunaan yang salah tanggung jawab lo sendiri.


# 0zer0LFI - Local File Inclusion Scanner & Exploiter

🚀 **0zer0LFI** - Tools keren buat para bug hunter buat nge-scan dan exploitasi LFI (Local File Inclusion) secara otomatis! Ini bukan tools sembarangan, bro. Ini alat buat para elite buat nge-hack dan exploit dengan mudah. 💀💻

---

## 📌 Fitur
- 🔍 **Single URL Scan:** Scan satu URL buat ngecek kerentanan LFI.
- 📜 **List Available LFI Payloads:** Liat payload yang ada beserta CVE ID-nya.
- 🔄 **Auto Exploit:** Bisa otomatis coba bypass filter seperti null byte, encoding, atau wrapper.
- 🔒 **Auth System:** Aman karena pake authentication check.
- 📂 **File Retrieval:** Bisa coba baca file sensitif kayak `/etc/passwd`, `wp-config.php`, dll.

---

## 🆕 Update Terbaru (v1.x) - Authentication System
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

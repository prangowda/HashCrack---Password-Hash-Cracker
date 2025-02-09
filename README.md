# HashCrack - Password Hash Cracker

## 🔍 Project Description
HashCrack is a **Python-based cybersecurity tool** designed to crack hashed passwords by comparing them with a **dictionary of common passwords**. It supports **MD5, SHA-1, SHA-256, and SHA-512 hashing algorithms** and helps security professionals test password strength.

---

## 🛠 Features
✅ Supports **multiple hash algorithms** (MD5, SHA-1, SHA-256, SHA-512)  
✅ Uses **wordlist/dictionary attack** for fast password recovery  
✅ Can be extended with **brute-force techniques**  
✅ Works on **Windows, Linux, and macOS**  

---

## 📜 Installation
Install the required dependency using pip:
```sh
pip install hashlib
```

---

## 📂 Usage
Run the tool and choose an option:
```sh
python hashcrack.py
```

### **1️⃣ Hash a Password**
- Enter the password to hash.  
- Choose a hashing algorithm (md5, sha1, sha256, sha512).  

### **2️⃣ Crack a Hashed Password**
- Enter the hashed password.  
- Provide a wordlist file (a file containing common passwords).  
- Choose a hashing algorithm.  

---

## 📊 Example Input & Output

### **🔹 Hashing a Password**
```
Enter password to hash: admin123
Enter hash algorithm: sha256
🔐 Hashed password: 7c222fb2927d828af22f592134e8932480637c0d
```

### **🔹 Cracking a Hashed Password**
```
Enter the hashed password: 7c222fb2927d828af22f592134e8932480637c0d
Enter path to wordlist file: wordlist.txt
Enter hash algorithm: sha256
✅ Password found: admin123
```

---

## 🚀 Future Enhancements
🔹 Add **brute-force attack** option (testing all possible combinations)  
🔹 Integrate **online hash lookup APIs**  
🔹 Create a **GUI version** for easy use  




# OPC UA Secure Client (Python) to KEPServerEX

Tutorial ini menjelaskan langkah **lengkap dari nol** untuk membuat **OPC UA Client menggunakan Python**
dengan **keamanan Certificate (Basic256Sha256 – Sign & Encrypt)** dan terhubung ke **KEPServerEX**.

---

## 📌 Tujuan
- Menghubungkan Python OPC UA Client ke KEPServerEX secara **secure**
- Menggunakan **X.509 Certificate**
- Memahami alur **PKI (Public Key Infrastructure)** OPC UA
- Menghindari error umum seperti:
  - `BadSecurityChecksFailed`
  - `BadCertificateUriInvalid`

---

## 🧰 Prasyarat
- Windows
- Python **3.10+**
- OpenSSL (tersedia di PATH)
- KEPServerEX (OPC UA Server aktif)
- Library Python:
  ```bash
  pip install opcua

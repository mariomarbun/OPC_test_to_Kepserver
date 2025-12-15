# OPC UA Secure Client Python to KEPServerEX

Complete step-by-step guide for creating a secure OPC UA Client using Python with Certificate-based security (Basic256Sha256 – Sign & Encrypt) to connect to KEPServerEX.

## 🎯 Objective

This document explains the complete process from scratch to build an OPC UA Client using Python with Certificate security until successfully connected to KEPServerEX.

## 📋 Prerequisites

- Windows 10 / 11
- Python 3.10 or newer
- OpenSSL available in PATH
- KEPServerEX OPC UA Server running
- Python library `opcua`

```bash
pip install opcua
```

## 📁 Project Folder Structure

```
opctestkepserver/
├── pki/
│   ├── own/
│   ├── trusted/
│   └── openssl.cnf
└── opctest.py
```

## 🔧 Setup Instructions

### Step 1: Create openssl.cnf

Create `openssl.cnf` file in the `pki/` folder:

```ini
[ req ]
default_bits = 2048
default_md = sha256
distinguished_name = dn
x509_extensions = v3_req
prompt = no

[ dn ]
CN = Python OPC UA Client
OU = Dev
O = AlfaSolution
L = City
C = ID

[ v3_req ]
subjectAltName = @alt_names
basicConstraints = CA:FALSE
keyUsage = digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth

[ alt_names ]
URI.1 = urn:OPCUA:PythonClient
```

### Step 2: Generate Private Key

```bash
openssl genrsa -out pki/own/client_key.pem 2048
```

### Step 3: Generate Certificate

```bash
openssl req -new -x509 \
  -key pki/own/client_key.pem \
  -out pki/own/client_cert.der \
  -outform DER \
  -days 365 \
  -sha256 \
  -config pki/openssl.cnf
```

### Step 4: Trust Server Certificate

Import the certificate from KEPServerEX (Server), then place it in the `pki/trusted/certs` folder.

### Step 5: Python OPC UA Client Code

Create `opctest.py`:

```python
from opcua import Client

client = Client("opc.tcp://EngineerASPL2:49320")
client.application_uri = "urn:OPCUA:PythonClient"
client.set_security_string(
    "Basic256Sha256,SignAndEncrypt,"
    "pki/own/client_cert.der,"
    "pki/own/client_key.pem"
)

try:
    client.connect()
    print("Connected securely")
except Exception as e:
    print("Connect failed:", e)
```

### Step 6: Run the Program

```bash
py opctest.py
```

## ✅ Expected Output

```
Requested session timeout to be 3600000ms, got 60000ms instead
Connected securely
```

## ⚠️ Common Errors

| Error | Solution |
|-------|----------|
| `BadSecurityChecksFailed` | Certificate not yet trusted on the server. Make sure to copy the certificate to the trusted folder and restart KEPServerEX |
| `BadCertificateUriInvalid` | Application URI doesn't match the URI in the certificate. Ensure the URI in code matches the one in `openssl.cnf` |

## 🎓 Conclusion

If all steps are followed correctly, the Python OPC UA Client will successfully connect to KEPServerEX using certificate-based security.

---

**Note:** Adjust the server URL (`opc.tcp://EngineerASPL2:49320`) according to your KEPServerEX configuration.
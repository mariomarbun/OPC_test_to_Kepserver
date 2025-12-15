from opcua import Client

client = Client("opc.tcp://EngineerASPL2:49320")
# isikan opc url dgn url dari kepserver yg digunakan
client.application_uri = "urn:OPCUA:PythonClient"
# uri nya pakai dari file openssl (bisadiubah sesuaidgnkeinginan)

client.set_security_string(
    "Basic256Sha256,SignAndEncrypt,"
    "own/client_cert.der,"
    "own/client_key.pem"
)

#security yg dipakai di kepserver lalu folder yang menyimpan sertifikat dari python

try:
    client.connect()
    print("Connected securely")
except Exception as e:
    print("First connect failed (normal):", e)
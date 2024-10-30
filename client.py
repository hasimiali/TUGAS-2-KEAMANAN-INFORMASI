import socket
from des import des_encrypt  

def main():
    # Server information
    host = '127.0.0.1'  # Localhost
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Pesan yang akan dienkripsi
    message = input("Masukkan pesan: ")

    # Kunci hardcoded (contoh)
    key = 0x0123456789ABCDEF

    # Enkripsi pesan
    encrypted_message = des_encrypt(message, key)
    print(f"Pesan terenkripsi: {encrypted_message}")

    # Mengirim pesan terenkripsi ke server
    client.send(encrypted_message.encode())

    client.close()

if __name__ == "__main__":
    main()

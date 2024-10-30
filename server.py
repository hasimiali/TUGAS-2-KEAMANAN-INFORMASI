import socket
from des import des_decrypt 

def main():
    # Server setup
    host = '127.0.0.1'  # Localhost
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print("Menunggu koneksi...")
    conn, addr = server.accept()
    print(f"Koneksi dari: {addr}")

    # Menerima data terenkripsi
    encrypted_message = conn.recv(1024).decode()
    print(f"Pesan terenkripsi diterima: {encrypted_message}")

    # Kunci hardcoded (contoh)
    key = 0x0123456789ABCDEF

    # Mendekripsi pesan
    decrypted_message = des_decrypt(encrypted_message, key)
    print(f"Pesan didekripsi: {decrypted_message}")

    conn.close()

if __name__ == "__main__":
    main()

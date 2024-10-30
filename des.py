from des_constants import IP, FP, PC1, PC2, SHIFTS  # Konstanta diambil dari kode sebelumnya

def permute(data, perm):
    result = 0
    for i in range(len(perm)):
        result <<= 1
        result |= (data >> (64 - perm[i])) & 1
    return result

def key_schedule(key):
    key = permute(key, PC1)
    left, right = key >> 28, key & 0x0FFFFFFF
    subkeys = []

    for shift in SHIFTS:
        left = ((left << shift) | (left >> (28 - shift))) & 0x0FFFFFFF
        right = ((right << shift) | (right >> (28 - shift))) & 0x0FFFFFFF
        combined = (left << 28) | right
        subkeys.append(permute(combined, PC2))

    return subkeys

def des_encrypt_block(data, key):
    subkeys = key_schedule(key)
    data = permute(data, IP)
    left, right = data >> 32, data & 0xFFFFFFFF

    for i in range(16):
        # Implementasikan logika round function di sini
        left, right = right, left  # Placeholder

    combined = (right << 32) | left
    return permute(combined, FP)

def des_decrypt_block(data, key):
    subkeys = key_schedule(key)[::-1]
    data = permute(data, IP)
    left, right = data >> 32, data & 0xFFFFFFFF

    for i in range(16):
        # Implementasikan logika round function di sini
        left, right = right, left  # Placeholder

    combined = (right << 32) | left
    return permute(combined, FP)

def pad(data):
    # PKCS#7 padding untuk memastikan panjang data kelipatan 8 byte
    padding_len = 8 - (len(data) % 8)
    padding = bytes([padding_len] * padding_len)  # Padding sebagai byte array
    return data.encode() + padding

def unpad(data):
    # Menghapus padding setelah dekripsi
    padding_len = data[-1]  # Ambil panjang padding dari byte terakhir
    if padding_len < 1 or padding_len > 8:
        raise ValueError("Invalid padding length")
    return data[:-padding_len].decode('utf-8', errors='ignore')




def des_encrypt(message, key):
    # Tambahkan padding sebelum enkripsi
    padded_message = pad(message)
    
    encrypted_message = ""
    for i in range(0, len(padded_message), 8):
        block_data = int.from_bytes(padded_message[i:i + 8].encode(), 'big')
        encrypted_message += f"{des_encrypt_block(block_data, key):016X}"

    return encrypted_message

def des_decrypt(encrypted_message, key):
    # Memecah pesan terenkripsi menjadi blok 16 karakter
    blocks = [encrypted_message[i:i + 16] for i in range(0, len(encrypted_message), 16)]
    
    decrypted_data = b""
    for block in blocks:
        block_data = int(block, 16)
        decrypted_data += block_data.to_bytes(8, 'big')

    try:
        # Hapus padding setelah dekripsi
        return unpad(decrypted_data.decode())
    except ValueError as e:
        print(f"Error saat unpadding: {e}")
        return ""



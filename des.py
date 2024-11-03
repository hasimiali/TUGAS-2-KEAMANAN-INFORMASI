from typing import List
from des_constants import *

def permute(block, table):
    return [block[x - 1] for x in table]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def left_rotate(bits, n):
    return bits[n:] + bits[:n]

def generate_keys(key):
    key = permute(key, PC1)  
    left, right = key[:28], key[28:]
    round_keys = []
    
    for shift in LEFT_SHIFTS:
        left = left_rotate(left, shift)
        right = left_rotate(right, shift)
        round_key = permute(left + right, PC2)
        round_keys.append(round_key)
    
    return round_keys

def feistel(right, subkey):
    expanded = permute(right, E)
    xored = xor(expanded, subkey)
    substituted = []
    for i in range(8):
        row = (xored[i*6] << 1) | xored[i*6 + 5]
        col = (xored[i*6 + 1] << 3) | (xored[i*6 + 2] << 2) | (xored[i*6 + 3] << 1) | xored[i*6 + 4]
        substituted.extend(bin(S_BOXES[i][row][col])[2:].zfill(4))
    return permute([int(bit) for bit in substituted], P)

def des_encrypt_decrypt(block, keys, decrypt=False):
    block = permute(block, IP)
    left, right = block[:32], block[32:]
    for round_key in (reversed(keys) if decrypt else keys):
        temp_right = xor(left, feistel(right, round_key))
        left, right = right, temp_right
    return permute(right + left, IP_INV)

def str_to_bin64(text: str) -> List[int]:
    bin_text = ''.join(f'{ord(char):08b}' for char in text)
    return [int(bit) for bit in bin_text.ljust(64, '0')[:64]]  

def bin64_to_str(bin_data: List[int]) -> str:
    chars = [chr(int(''.join(map(str, bin_data[i:i+8])), 2)) for i in range(0, len(bin_data), 8)]
    return ''.join(chars).rstrip('\x00')  

def hex_key_to_bin64(hex_key: str) -> List[int]:
    bin_key = bin(int(hex_key, 16))[2:].zfill(64)
    return [int(bit) for bit in bin_key[:64]] 

if __name__ == "__main__":
    plaintext = "HelloDES"
    hex_key = "133457799BBCDFF1"

    binary_plaintext = str_to_bin64(plaintext)
    binary_key = hex_key_to_bin64(hex_key)

    round_keys = generate_keys(binary_key)

    encrypted_bin = des_encrypt_decrypt(binary_plaintext, round_keys, decrypt=False)
    print("Encrypted binary:", ''.join(map(str, encrypted_bin)))

    decrypted_bin = des_encrypt_decrypt(encrypted_bin, round_keys, decrypt=True)
    decrypted_text = bin64_to_str(decrypted_bin)
    print("Decrypted text:", decrypted_text)

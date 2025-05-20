from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Buat kunci DES (harus 8 byte)
key = b'12345678'  # 8 bytes

# Bikin cipher object
cipher = DES.new(key, DES.MODE_ECB)

# Pesan yang mau dienkripsi
data = b'Merubah Deskripsi Menjadi Enkripsi'
padded_data = pad(data, DES.block_size)  # padding biar kelipatan 8

# Enkripsi
encrypted = cipher.encrypt(padded_data)
print("Encrypted:", encrypted.hex())

# Dekripsi
cipher2 = DES.new(key, DES.MODE_ECB)
decrypted_padded = cipher2.decrypt(encrypted)
decrypted = unpad(decrypted_padded, DES.block_size)
print("Decrypted:", decrypted.decode())

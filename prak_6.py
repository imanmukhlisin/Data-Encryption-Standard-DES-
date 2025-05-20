
!pip install pycryptodome
Defaulting to user installation because normal site-packages is not writeable
Collecting pycryptodome
  Downloading pycryptodome-3.23.0-cp37-abi3-win_amd64.whl.metadata (3.5 kB)
Downloading pycryptodome-3.23.0-cp37-abi3-win_amd64.whl (1.8 MB)
   ---------------------------------------- 0.0/1.8 MB ? eta -:--:--
   ----- ---------------------------------- 0.3/1.8 MB ? eta -:--:--
   ----------- ---------------------------- 0.5/1.8 MB 1.9 MB/s eta 0:00:01
   ----------------------- ---------------- 1.0/1.8 MB 1.9 MB/s eta 0:00:01
   ----------------------------- ---------- 1.3/1.8 MB 1.9 MB/s eta 0:00:01
   ---------------------------------- ----- 1.6/1.8 MB 1.7 MB/s eta 0:00:01
   ---------------------------------------- 1.8/1.8 MB 1.5 MB/s eta 0:00:00
Installing collected packages: pycryptodome
Successfully installed pycryptodome-3.23.0
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
Encrypted: e19b5531e6ecc27f6f4769e43d46cb09de2f8db3f8fccf8f95a4e9faf781bb8e8f04123eb1d87c83
Decrypted: Merubah Deskripsi Menjadi Enkripsi
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

ciphertext_hex = input("Masukkan ciphertext (hex): ")

ciphertext_bytes = bytes.fromhex(ciphertext_hex)

key = b'12345678'

cipher = DES.new(key, DES.MODE_ECB)

decrypted_padded = cipher.decrypt(ciphertext_bytes)

decrypted = unpad(decrypted_padded, DES.block_size)

print("Hasil dekripsi:", decrypted.decode())
Hasil dekripsi: Merubah Deskripsi Menjadi Enkripsi
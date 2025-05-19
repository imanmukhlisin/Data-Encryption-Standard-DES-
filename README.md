# DES Decryption Tool (Python)

Praktek untuk mendekripsi data terenkripsi menggunakan algoritma **DES (Data Encryption Standard)** dalam mode ECB.

## 📋 Deskripsi

Program ini memungkinkan pengguna untuk:
- Menginput ciphertext (hasil enkripsi dalam format heksadesimal)
- Mendekripsi ciphertext tersebut menggunakan kunci DES 8 byte
- Menampilkan hasil teks asli setelah dekripsi

> ⚠️ Pastikan ciphertext yang dimasukkan adalah hasil enkripsi DES dengan **mode ECB** dan menggunakan **kunci `b'12345678'`**.

## 🛠️ Teknologi yang Digunakan

- Python 3
- [pycryptodome](https://pypi.org/project/pycryptodome/)

## 📦 Instalasi

Pastikan Anda sudah menginstal `pycryptodome`. Jika belum, jalankan:

```bash
pip install pycryptodome

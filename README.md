# TUGAS-2-KEAMANAN-INFORMASI

# Aplikasi Klien-Server Enkripsi DES

Proyek ini mengimplementasikan aplikasi klien-server sederhana yang menggunakan algoritma enkripsi DES (Data Encryption Standard) untuk mengamankan data yang dikirim antara klien dan server. Server akan mengenkripsi pesan yang diterima, dan klien dapat mendekripsi pesan yang diterima untuk verifikasi.

## Ringkasan

- **Server**: Menerima teks dari klien, mengenkripsinya menggunakan DES, lalu mengirim kembali pesan yang sudah dienkripsi.
- **Klien**: Mengirim teks ke server, menerima pesan yang sudah dienkripsi, lalu mendekripsinya untuk verifikasi.
- **Algoritma DES**: Sebuah cipher blok dengan kunci simetris yang bekerja pada blok 64-bit dengan kunci 56-bit.

## Prasyarat

- **Python 3.7+** diperlukan untuk menjalankan proyek ini.

## Struktur Berkas

- `server.py` - Kode server yang mendengarkan koneksi dari klien, mengenkripsi teks yang diterima, dan mengirim kembali data yang sudah dienkripsi.
- `client.py` - Kode klien yang menghubungkan ke server, mengirim teks, menerima data yang sudah dienkripsi, lalu mendekripsinya secara lokal.
- `README.md` - Dokumentasi untuk aplikasi ini.

## Persiapan

1. Clone repositori ini atau unduh semua berkasnya.

2. Buka dua jendela terminal:
   - Satu untuk menjalankan server (`server.py`).
   - Satu lagi untuk menjalankan klien (`client.py`).

## Cara Menjalankan

### Langkah 1: Menjalankan Server

1. Di jendela terminal pertama, arahkan ke direktori proyek.
2. Jalankan server:

   ```bash
   python server.py
   ```
3. Jalankan client:

   ```bash
   python client.py
   ```

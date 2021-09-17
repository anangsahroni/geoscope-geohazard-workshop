![header_image](./figures/geoscope_header_cropped_sm.png)
# Geoscope Geohazard Workshop HMGF UGM
## *"Geophysical Python for Seismic Data Analysis"*

**Instruktur:**
Dr.rer.nat. Wiwit Suryanto, M.Si



**Waktu:**  
Sesi 1: 18 September 2021  
Sesi 2: 25 September 2021  

**Tempat:**
Zoom Meeting

**Agenda:**
Memberikan wawasan kepada mahasiswa Geofisika dalam pengolahan data Geofisika: pemrosesan data seismik menggunakan python.

## Luaran
1. Peserta dapat melakukan instalasi Python
2. Peserta dapat membuat dan menggunakan Jupyter Notebook
3. Peserta dapat membaca, memfilter, dan mengeplot peta dan statistik gempa bumi menggunakan modul umum Python seperti `numpy`, `scipy`, dan `matplotlib`
4. Peserta dapat menentukan parameter gempa menggunakan metode yang sederhana pada Python

## Peralatan untuk peserta
Laptop ataupun *Personal Computer* (PC) yang terkoneksi dengan internet.

## Data:
1. [Katalog Gempa Bumi](https://github.com/anangsahroni/geoscope-geohazard-workshop/blob/main/data/demo_data_BMKG_Mamuju.csv) Badan Meteorologi Klimatologi dan Geofisika (BMKG)
2. Titik-titik Stasiun untuk berbagai jaringan seismometer

## Jadwal
| **Topik** |
|:-----------|
| **SESI 1: 13 Februari 2021** |
| *[Instalasi Python dalam Miniconda](https://nbviewer.jupyter.org/github/anangsahroni/geoscope-geohazard-workshop/blob/main/1_Instalasi_Python_dalam_Miniconda.ipynb)* (atau [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/anangsahroni/geoscope-geohazard-workshop/HEAD))|
| 1. Instalasi Miniconda pada Windows, Linux, ataupun MacOS |  
| 2. Menjalankan Python Console melalui Anaconda Prompt |  
| 3. Menulis kode dalam editor (Integrated Development Environment/IDE) kode dan menjalankannya melalui Anaconda Prompt
| 4. Pengenalan IDE dan beberapa contohnya
| 5. Menginstall dan menjalankan Jupyter Notebook
| 6. Menjalankan kode sederhana di Jupyter Notebook
| 7. Memanggil fungsi bawaan python (`math`), mencoba, dan memanggil bantuan (`help`) untuk masing-masing fungsi
| 8. Memberikan catatan dan gambar dalam bentuk `Markdown` di Jupyter Notebook
| 9. Menyimpan notebook pada repositori Github dan menambahkan ke Binder
| 10. Mengupdate notebook dan melakukan commit ke repositori
| **EXERCISE:** Membuat panduan instalasi Miniconda pada Jupyter Notebook dan menambahkannya di repositori Github individu. |
||
| **SESI 2: 20 Februari 2021** |
| *[Materi Dasar Python](https://nbviewer.jupyter.org/github/anangsahroni/geoscope-geohazard-workshop/blob/main/2_Materi_Dasar_Python.ipynb)* (atau [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/anangsahroni/geoscope-geohazard-workshop/HEAD))|
| 1. Membuat dan mengaktifkan *virtual environment* (opsional) |
| 2. Menginstall `pandas`, `numpy`, `matplotlib`, `scipy`, `Cartopy`, dan `notebook` menggunakan Anaconda Prompt pada *virtual environment* |
| 3. Membaca data katalog menggunakan `pandas` |
| 4. Membedakan jenis-jenis data antar kolom pada katalog (`String`, `Integer`, dan `Float`) |
| 5. Mengambil salah satu kolom ke dalam bentuk `List` dan mempelajari metode-metode pada `List` (`indexing`, `slicing`, `append`, dan lain sebagainya) |
| 6. Menggunakan `for` *loop* untuk mengkonversi format `String` menjadi `datetime` untuk waktu kejadian |
| 7. Menggunakan `conditional` untuk memfilter katalog berdasarkan besar magnitudo atau waktu |
| 8. Membuat fungsi untuk memfilter katalog berdasarkan kedalaman dan menyimpannya menjadi modul siap impor |
| 9. Membuat plot magnitudo dengan jumlah kejadian dan waktu kejadian (dapat berupa G-R Plot atau plot sederhana) |
| 10. Mengkombinasikan `List` latitude dan longitude untuk mengeplot episenter |
| 11. Mengintegrasikan kolom magnitude untuk membedakan ukuran titik titik plot |
| 12. Mengintegrasikan kolom kedalaman untuk membedakan warna titik plot |
| 13. Menambahkan *basemap* pada plot Menggunakan `Cartopy` |
| 14. *Gridding*, Interpolasi, dan membuat kontur kedalaman menggunakan `scipy` (opsional) |
| **EXERCISE:** Membaca file titik stasiun, memfilter berdasarkan network, dan mengeplotnya bersama dengan titik-titik gempa. |
||


## Software untuk diinstall
1. **Miniconda**. Instalasi Python akan dilakukan menggunakan Anaconda Distribution dalam bentuk *lite* yaitu Miniconda. Dengan Miniconda instalasi paket atau modul pendukung untuk Python akan lebih mudah dan tertata. [Unduh installer Miniconda](https://docs.conda.io/en/latest/miniconda.html), pilih untuk versi Python 3.8.
2. Editor teks agar penulisan kode lebih mudah karena biasanya sudah disertai pewarnaan kode  (*syntax highlighting*) dan indentasi otomatis. Editor teks dapat menggunakan **Notepad++**, **SublimeText**, atau menggunakan IDE yang lebih kompleks seperti **PyCharm** dan **Visual Studio Code**.

Software-software yang dibutuhkan tersebut **sudah harus diinstall sebelum proses pemberian materi dimulai** karena ukurannya cukup besar.

## Akun Github
Peserta workshop dianjurkan mendaftarkan akun GitHub melalui [Daftar Github](http://github.com)

## Bacaan Tambahan:
Peserta dapat belajar pada Lesson di [Software Carpentry](https://software-carpentry.org/lessons/) dengan materi yang mendalam dan metode yang sama yaitu learning by doing. 

## *Acknowledgment*
Panduan ini disusun terinspirasi dari materi pada [Software Carpentry](https://software-carpentry.org/lessons/) dan panduan workshop Leonardo Uieda yang diunggah pada [repositori](https://github.com/leouieda/python-hawaii-2017) berikut ini.

## Lisensi
Konten di repositori ini berada di bawah lisensi:
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

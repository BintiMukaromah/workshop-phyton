Jika ingin menulis program yang lebih panjang, sebaiknya menggunakan editor teks untuk menyiapkan input untuk penerjemah dan menjalankannya dengan file tersebut sebagai input yang dikenal sebagai membuat skrip.
Python memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam instance interpreter yang interaktif. File seperti itu disebut modul. Sebuah modul dapat diimpor ke modul lain atau ke modul utama (kumpulan variabel yang dapat Anda akses dalam skrip yang dijalankan di tingkat atas dan dalam mode kalkulator).
Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran .py ditambahkan. Dalam sebuah modul, nama modul tersedia sebagai nilai dari variabel global **name**. Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Modul dapat mengimpor modul lain.

Setiap modul memiliki tabel simbol pribadinya sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, pembuat modul dapat menggunakan variabel global dalam modul tanpa mengkhawatirkan bentrokan yang tidak disengaja dengan variabel global pengguna. Di sisi lain, juga dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke fungsinya, modname.itemname.

Beberapa modul dibangun ke dalam juru bahasa, menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, modul winreg hanya tersedia di sistem Windows. Satu modul tertentu patut mendapat perhatian: sys, yang dibangun ke dalam setiap juru bahasa Python. Variabel sys.ps1 dan sys.ps2 mendefinisikan string yang digunakan sebagai prompt primer dan sekunder:

Paket adalah cara menyusun namespace modul Python dengan menggunakan "nama modul bertitik". Misalnya, nama modul AB menunjuk submodule bernama B dalam paket bernama A. Sama seperti penggunaan modul menyelamatkan penulis modul yang berbeda dari harus khawatir tentang nama variabel global masing-masing, penggunaan nama modul bertitik menyelamatkan penulis paket multi-modul seperti NumPy atau Bantal karena harus khawatir tentang nama modul masing-masing.

Misalkan ingin merancang kumpulan modul ("paket") untuk penanganan file suara dan data suara yang seragam. Ada banyak format file suara yang berbeda (biasanya dikenali dari ekstensinya, misalnya: .wav, .aiff, .au), jadi mungkin perlu membuat dan memelihara koleksi modul yang terus bertambah untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin dilakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, membuat efek stereo buatan), jadi selain itu akan menulis aliran modul yang tidak pernah berakhir untuk dilakukan operasi ini.
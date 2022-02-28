Python menggunakan pernyataan kontrol aliran biasa yang dikenal dari bahasa lain, dengan beberapa perubahan.
Kata kunci 'elif' adalah kependekan dari 'else if', dan berguna untuk menghindari lekukan yang berlebihan. Urutan if … elif … elif … adalah pengganti pernyataan switch atau case yang ditemukan dalam bahasa lain.

Pernyataan for dalam Python sedikit berbeda dari yang digunakan dalam C atau Pascal. Daripada selalu mengulangi progresi aritmatika angka (seperti dalam Pascal), atau memberi pengguna kemampuan untuk menentukan langkah iterasi dan kondisi penghentian (seperti C), pernyataan for Python beralih ke item dari urutan apa pun (daftar atau string), dalam urutan kemunculannya dalam urutan.

fungsi range() berguna jika perlu mengulangi urutan angka. Objek yang dikembalikan oleh range() seolah-olah itu adalah daftar, tetapi sebenarnya tidak. Ini adalah objek yang mengembalikan item berurutan dari urutan yang diinginkan ketika mengulanginya, tetapi itu tidak benar-benar membuat daftar, sehingga menghemat ruang.

Pernyataan kecocokan mengambil ekspresi dan membandingkan nilainya dengan pola berurutan yang diberikan sebagai satu atau lebih blok kasus. Mirip dengan pernyataan switch di C, Java atau JavaScript (dan banyak bahasa lainnya), tetapi juga dapat mengekstrak komponen (elemen urutan atau atribut objek) dari nilai ke dalam variabel.

Kata kunci def memperkenalkan definisi fungsi, harus diikuti dengan nama fungsi dan daftar parameter formal dalam kurung. Pernyataan-pernyataan yang membentuk badan fungsi dimulai dari baris berikutnya, dan harus diindentasi. Pernyataan pertama dari badan fungsi secara opsional dapat berupa string literal. string literal adalah string dokumentasi fungsi, atau docstring.

Parameter khusus : - Argumen Posisi-atau-Kata Kunci - Parameter Hanya Posisi - Argumen Hanya Kata Kunci - Contoh Fungsi - Rekap
Daftar Argumen sewenang-wenang : opsi yang paling jarang digunakan adalah menentukan bahwa suatu fungsi dapat dipanggil dengan sejumlah argumen yang berubah-ubah. Argumen-argumen ini akan dibungkus dalam sebuah tupel. Sebelum jumlah variabel argumen, nol atau lebih argumen normal dapat terjadi
Fungsi anonim kecil dapat dibuat dengan kata kunci lambda. Fungsi ini mengembalikan jumlah dari dua argumennya: lambda a, b: a+b. Fungsi Lambda dapat digunakan di mana pun objek fungsi diperlukan. Secara sintaksis terbatas pada satu ekspresi. Secara semantik, mereka hanyalah gula sintaksis untuk definisi fungsi normal. Seperti definisi fungsi bersarang, fungsi lambda dapat mereferensikan variabel dari cakupan yang berisi.

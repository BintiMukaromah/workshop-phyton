Metode objek daftar : list.append(x), list.extend(iterable), list.insert(i, x), list.remove(x), list.pop([i]), list.clear(), list.index(x[, start[, end]]), list.count(x), list.reverse(), list.copy()

Menggunakan Daftar sebagai Tumpukan
Metode daftar dapat digunakan sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("masuk terakhir, keluar pertama"). Untuk menambahkan item ke bagian atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit.

Menggunakan Daftar sebagai Antrian
Dapat juga menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, keluar pertama"); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan penyisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

Daftar Pemahaman
Daftar pemahaman menyediakan cara ringkas untuk membuat daftar. Aplikasi umum adalah untuk membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable, atau untuk membuat sub urutan dari elemen-elemen yang memenuhi kondisi tertentu.

Pemahaman Daftar Bersarang
Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi arbitrer, termasuk pemahaman daftar lainnya.

Pernyataan del
Ada cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya: pernyataan del. Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar.

Tuple dan Urutan
Kami melihat bahwa daftar dan string memiliki banyak properti umum, seperti operasi pengindeksan dan pengirisan. Mereka adalah dua contoh tipe data urutan (lihat Tipe Urutan — daftar, tupel, rentang). Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: tuple.

Set adalah kumpulan yang tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti serikat pekerja, persimpangan, perbedaan, dan perbedaan simetris. Untuk membuat set kosong harus menggunakan set(), bukan {}.

Tipe data lainnya yang dibangun ke dalam Python adalah kamus. Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci, yang dapat berupa tipe apa pun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci. Tuple dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung maupun tidak langsung, itu tidak dapat digunakan sebagai kunci. Tidak dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan penetapan indeks, penetapan irisan, atau metode seperti append() dan extend().

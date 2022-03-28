Kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama-sama. Membuat kelas baru membuat tipe objek baru, memungkinkan instance baru dari tipe itu dibuat. Setiap instance kelas dapat memiliki atribut yang dilampirkan untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode untuk memodifikasi statusnya.

Mekanisme kelas Python menambahkan kelas dengan sintaks dan semantik baru yang minimal. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat mengganti metode apa pun dari kelas atau kelas dasarnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama . Objek dapat berisi jumlah dan jenis data yang berubah-ubah. Seperti halnya modul, kelas mengambil bagian dari sifat dinamis Python: mereka dibuat saat runtime, dan dapat dimodifikasi lebih lanjut setelah pembuatan.

namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama namespace saat ini diimplementasikan sebagai kamus dictionary Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan itu mungkin berubah di masa depan.

Setiap saat selama eksekusi, setidaknya ada 3 atau 4 cakupan bersarang yang ruang nama-nya namespaces dapat diakses secara langsung:
• ruang lingkup scope terdalam, yang dicari pertama kali, berisi nama-nama lokal
• lingkup scope dari setiap fungsi penutup, yang dicari dimulai dengan lingkup penutup terdekat, berisi nama-nama non-lokal, tetapi juga non-global
• lingkup berikutnya next-to-last berisi nama global modul saat ini
• ruang lingkup scope terluar (dicari terakhir) adalah namespace yang mengandung nama bawaan

Objek kelas mendukung dua jenis operasi: referensi atribut dan instansiasi.
Attribute references menggunakan sintaks standar yang digunakan untuk semua referensi atribut dalam Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di namespace kelas saat objek kelas dibuat.
Satu-satunya operasi yang dipahami oleh objek instan adalah referensi atribut. Ada dua jenis nama atribut yang valid: atribut data, dan metode.

Python memiliki dua fungsi bawaan yang bekerja dengan warisan:
• Gunakan isinstance() untuk memeriksa jenis instance: isinstance(obj, int) akan menjadi True hanya jika obj.**class** adalah int atau beberapa kelas yang diturunkan dari int.
• Gunakan issubclass() untuk memeriksa warisan kelas: issubclass(bool, int)`adalah `True karena bool adalah subkelas dari int. Namun, issubclass(float, int) adalah False karena float bukan subkelas dari int.

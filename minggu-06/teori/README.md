Kesalahan sintaks atau syntax errors terjadi ketika Python tidak dapat mengerti apa yang kita perintahkan. Sedangkan pengecualian atau exceptions (kesalahan saat beroperasi) terjadi ketika Python mengerti apa yang kita perintahkan tetapi mendapatkan masalah saat mengikuti yang kita perintahkan (terjadi saat aplikasi sudah mulai beroperasi).

Exception tampil ketika suatu program memiliki error, dikarenakan kode yang salah atau masukan yang jelek.Ketika exception di python tampil maka program tersebut akan berhenti.
Exception yang berbeda-beda memiliki penyebab yang berbeda-beda pula.Exception yang biasa muncul yakni:
ImportError => sebuah import yang gagal
IndexError => array yang terindex tidak ada
NameError => variabel yang tidak diketahui digunakan
ValueError => Sebuah fungsi dipanggil karena nilai tipenya benar tetapi nilainya yang salah
TypeError => sebuah fungsi yang dipanggil menggunakan type nilai yang salah
SyntaxError => kode yang kita buat tidak bisa dijalankan.

Pada aplikasi Python yang kita buat bisa dilengkapi dengan penanganan terhadap pengecualian (exceptions handling) dari kelompok (tipe) kesalahan yang ditentukan. Proses penanganan pengecualian menggunakan pernyataan try yang berpasangan dengan except.

Pernyataan try berfungsi sebagai berikut.

- Pertama, klausa try (pernyataan antara kata kunci try dan kecuali) dieksekusi.
- Jika tidak ada pengecualian yang terjadi, klausa kecuali akan dilewati dan eksekusi pernyataan try selesai.
- Jika pengecualian terjadi selama eksekusi klausa try, sisa klausa akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai kata kunci kecuali, klausa kecuali dijalankan, dan kemudian eksekusi dilanjutkan setelah blok coba/kecuali.

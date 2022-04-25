Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venv biasanya akan menginstal versi Python terbaru yang Anda miliki. Jika Anda memiliki beberapa versi Python di sistem Anda, Anda dapat memilih versi Python tertentu dengan menjalankan python3 atau versi mana pun yang Anda inginkan.
Untuk membuat lingkungan virtual, tentukan direktori tempat Anda ingin meletakkannya, dan jalankan modul venv sebagai skrip

Lokasi direktori yang umum dipakai untuk lingkungan virtual adalah .venv. Nama ini membuat direktori biasanya tersembunyi di shell Anda dan dengan demikian terpencil sambil memberikan nama yang menjelaskan mengapa direktori itu ada. Ini juga mencegah bentrok dengan berkas definisi variabel lingkungan .env yang didukung beberapa peralatan.

Mengaktifkan lingkungan virtual akan mengubah prompt shell Anda untuk menunjukkan lingkungan virtual apa yang Anda gunakan, dan memodifikasi lingkungan sehingga menjalankan python akan membuat Anda mendapatkan versi dan instalasi Python tertentu

menginstal, mengupgrade, dan menghapus paket menggunakan program yang disebut pip. Secara bawaan pip akan menginstal paket dari Python Package Index, https://pypi.org. Anda dapat menelusuri Python Package Index dengan membukanya di peramban atau browser web
pip memiliki sejumlah sub-perintah: "install", "uninstall", "freeze", dls.

pip uninstall diikuti oleh satu atau beberapa nama paket akan menghapus paket-paket dari lingkungan virtual.
pip show akan menampilkan informasi tentang paket tertentu


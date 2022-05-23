Flask (Labu)
Dalam membuat environment maka langkah yang harus di lakukan : - conda create -n workshopy python=3.10 - aktifkan dengan : conda active workshopy - selanjutnya baru install flask dengan : conda install flask

Buat dengan mengimport Flask from flask untuk membuat sebuah tampilan dengan memberikan ucapan hello word
Menjalankan

flask run
Running on http://127.0.0.1:5000/ tersebut digunakan untuk menjalankan Flask_APP yang telah di buat
Server Terlihat Secara Eksternal
Akan melihat bahwa server hanya dapat diakses dari komputer sendiri, bukan dari komputer lain dalam jaringan. Ini adalah default karena dalam mode debugging, pengguna aplikasi dapat mengeksekusi kode Python sewenang-wenang di komputer

Jika labu python -m gagal atau labu tidak ada, ada beberapa alasan yang mungkin terjadi. Pertama-tama perlu melihat pesan kesalahan.

Versi Flask yang lebih lama dari 0.11 perintah flask tidak ada, begitu juga dengan python -m flask. Dalam hal ini Anda memiliki dua opsi: upgrade ke versi Flask yang lebih baru atau lihat Server Pengembangan

Variabel lingkungan FLASK_APP adalah nama modul yang akan diimpor saat labu dijalankan. Jika modul tersebut salah diberi nama, Anda akan mendapatkan kesalahan impor saat memulai (atau jika debug diaktifkan saat menavigasi ke aplikasi)

Perintah flask run dapat melakukan lebih dari sekadar memulai server pengembangan. Dengan mengaktifkan mode debug, server akan secara otomatis memuat ulang jika kode berubah, dan akan menampilkan debugger interaktif di browser jika terjadi kesalahan selama permintaan.

Saat mengembalikan HTML (tipe respons default di Flask), setiap nilai yang diberikan pengguna yang dirender dalam output harus diloloskan untuk melindungi dari serangan injeksi.
HTML Template yang di gunakan
from markupsafe import escape

@app.route("/<name>")
def hello(name):
return f"Hello, {escape(name)}!"

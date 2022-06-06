DataFrame adalah struktur data berlabel 2 dimensi dengan kolom dari jenis yang berpotensi berbeda. Seperti spreadsheet atau tabel SQL, atau dict objek Seri. Ini merupakan objek pandas yang paling umum digunakan. Seperti Seri, DataFrame menerima berbagai jenis input:

- Dict of 1D ndarrays, lists, dicts, or Series
- 2-D numpy.ndarray
- Structured or record ndarray
- A Series
- Another DataFrame

Perintah yang ada pada pandas :

Fungsi shape() digunakan untuk melihat berapa banyak baris dan kolom pada dataframe

Informasi statistik untuk setiap kolom seperti nilai minimum, nilai maksimum, standar deviasi, rata-rata dan sebagainya, dapat ditampilkan dengan mengikuti perintah berikut
df.describe(include='all')

Untuk mendapatkan informasi kolom, datatype dan informasi struktur lainnya menggunakan perintah df.info()

Untuk melihat jumlah data pada setiap kolom menggunakan perintah count()
df.count()

Fungsi sample() pada Pandas dapat digunakan jika kita ingin menampilkan data secara acak.
df.sample(5)

Jika ingin menampilkan seluruh data yang ada pada dataframe.
df

Penggunaan fungsi tail() sama seperti fungsi head() yang membedakannya hanya outputnya saja, fungsi tail() hanya untuk melihat data terakhir dari dataframe
df.tail()

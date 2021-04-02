print("SOAL 1 : Membuat program untuk menyapa pengunjung")

print("Siapakah nama anda?")
#input nama pengunjung
nama = input("Nama : ")

print("Apakah jenis kelamin anda? (L/P)?")
#input jenis kelamin
jenis_kelamin = input("Jenis kelamin : ")

if jenis_kelamin == 'L':
    print("Selamat datang, Tuan",nama,"!")
else :
    print("Selamat datang, Nyonya",nama,"!")

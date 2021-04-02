print("SOAL 2 : Membuat program grading nilai")

#input nama mahasiswa
nama = input('Nama : ')

#input nilai mahasiswa
nilai = input('Nilai : ')

if nilai > '85':
    print('Halo, ', nama,'! Nilai anda setelah dikonversi adalah A')
elif nilai > '80':
    print('Halo, ', nama,'! Nilai anda setelah dikonversi adalah A-')
elif nilai > '75':
    print('Halo, ', nama,'! Nilai anda setelah dikonversi adalah B+')
elif nilai > '70':
    print('Halo, ', nama,'! Nilai anda setelah dikonversi adalah B')
elif nilai > '65':
    print('Halo, ', nama,'! Nilai anda setelah dikonversi adalah C+')
elif nilai > '60':
    print('Halo, ', nama,'! Nilai anda setelah dikonversi adalah C')
else:
    pass
print()

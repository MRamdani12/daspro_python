#Identity Operator (Operator Identitas).
print('Nama: MRamdani \nNim: 17230207 \nKelas: 17.1C.04 \n')

#Operator "is".
#Operator ini akan true jika kedua variabel/operand mempunyai jenis dan isi/nilai yang sama.
angka1 = 10
angka2 = 10

print('=== Operator is ===')
#Hasil print ini akan true (Akan ditampilkan di print 1)
print(f'print 1 = {angka1 is angka2}')

#print ini akan false karna jenis angka2 adalah string dan bukan int (Akan ditampilkan di print 2)
angka2 = str(angka2)
print(f'print 2 = {angka1 is angka2}')

#print ini akan false karana nilai dari angka2 adalah 30 (Akan ditampilkan di print 3)
angka2 = int(angka2) + 20
print(f'Nilai angka 1 = {angka1} \nNilai angka 2 = {angka2}')
print(f'print 3 = {angka1 is angka2}')

#==================================================

#Operator "is not".
#Operator ini akan true jika kedua variabel/operand mempunyai jenis dan isi/nilai yang berbeda.
angka3 = 10
angka4 = 30

print('')
print('=== Operator is not ===')
#Hasil print ini akan true (Akan ditampilkan di print 1)
print(f'print 1 = {angka3 is not angka4}')

#print ini akan false karna nilai angka 3 dan 4 adalah sama (Akan ditampilkan di print 2)
angka3 = angka4
print(f'Nilai angka 3 = {angka3} \nNilai angka 4 = {angka4}')
print(f'print 2 = {angka3 is not angka4}')
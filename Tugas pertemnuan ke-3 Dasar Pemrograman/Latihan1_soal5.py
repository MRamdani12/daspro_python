#Membership Operator (Operator Keanggotaan)
print('Nama: MRamdani \nNim: 17230207 \nKelas: 17.1C.04 \n')

#Operator in.
#Operator ini akan true jika nilai dari suatu variable/objek ada didalam array/variable lainnya.
buahBuahan = ['pisang', 'apel', 'jeruk', 'mangga', 'kelapa']
buah1 = 'jeruk'
buah2 = 'salak'

print('=== Operator in ===')

#Print ini akan true karena buah1(jeruk) ada didalam array buah-buahan (Akan ditampilkan di print 1).
print(f'print 1 = {buah1 in buahBuahan}')

#Print ini akan false karena buah2(salak) tidak ada didalam array buah-buahan (Akan ditampilkan di print 2).
print(f'print 2 = {buah2 in buahBuahan}')

#=============================================================

print('')
#Operator not in.
#Operator ini akan true jika nilai dari suatu variable/objek tidak ada didalam array/variable lainnya.
buahBuahan = ['pisang', 'apel', 'jeruk', 'mangga', 'kelapa']
buah1 = 'mangga'
buah2 = 'sirsak'

print('=== Operator not in ===')

#Print ini akan false karena buah1(mangga) ada didalam array buah-buahan (Akan ditampilkan di print 1).
print(f'print 1 = {buah1 not in buahBuahan}')

#Print ini akan true karena buah2(sirsak) tidak ada didalam array buah-buahan (Akan ditampilkan di print 2).
print(f'print 2 = {buah2 not in buahBuahan}')


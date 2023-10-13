#Toko Mainan Anak
print('Nama: MRamdani \nNim: 17230207 \nKelas: 17.1C.04 \n')


print('\t\tTOKO MAINAN ANAK \n\t********************************')

namaPembeli = str(input('Masukan Nama Pembeli : \033[1;32;40m'))
kodeMainan = str(input('\033[0;37;40mMasukan Kode Mainan : \033[1;32;40m'))
harga = int(input('\033[0;37;40mMasukan Harga : \033[1;32;40m'))
jumlahBeli = int(input('\033[0;37;40mMasukan Jumlah Beli : \033[1;32;40m'))

print('\033[0;37;40m')
print('\n==========================================================\n')

print(f'Nama Pembeli = {namaPembeli}')
print(f'Kode Mainan  = {kodeMainan}')
print(f'Harga        = {harga:,}')
print(f'Jumlah Beli  = {jumlahBeli:,}')
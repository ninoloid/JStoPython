tanggal = 1
bulan = 12
tahun = 1993
validasi = False

validDay = tanggal >= 1 and tanggal <= 31
validMonth = bulan >= 1 and bulan <= 12
validYear = tahun >= 1900 and tahun <= 2200

if validDay and validMonth and validYear:
  validasi = True

if bulan == 1:
  bulan = 'Januari'
elif bulan == 2:
  bulan = 'Februari'
elif bulan == 3:
  bulan = 'Maret'
elif bulan == 4:
  bulan = 'April'
elif bulan == 5:
  bulan = 'Mei'
elif bulan == 6:
  bulan = 'Juni'
elif bulan == 7:
  bulan = 'Juli'
elif bulan == 8:
  bulan = 'Agustus'
elif bulan == 9:
  bulan = 'September'
elif bulan == 10:
  bulan = 'Oktober'
elif bulan == 11:
  bulan = 'November'
else:
  bulan = 'Desember'

if validasi:
  print(f'{tanggal} {bulan} {tahun}')
else:
  print('Harap masukkan angka yang benar \n Tanggal : 1 - 31 \n Bulan : 1 - 12 \n Tahun : 1900 - 2200')

# IN JS
# var tanggal = 1;
# var bulan = 12;
# var tahun = 1993;
# var validasi = false;

# switch (true) {
#   case tanggal >= 1 && tanggal <= 31 && bulan >= 1 && bulan <= 12 && tahun >= 1900 && tahun <= 2200:
#     validasi = true;
#     break;
#   default:
#     validasi = false;
# }

# switch (bulan) {
#   case 1:
#     bulan = 'Januari';
#     break;
#   case 2:
#     bulan = 'Februari';
#     break;
#   case 3:
#     bulan = 'Maret';
#     break;
#   case 4:
#     bulan = 'April';
#     break;
#   case 5:
#     bulan = 'Mei';
#     break;
#   case 6:
#     bulan = 'Juni';
#     break;
#   case 7:
#     bulan = 'Juli';
#     break;
#   case 8:
#     bulan = 'Agustus';
#     break;
#   case 9:
#     bulan = 'September';
#     break;
#   case 10:
#     bulan = 'Oktober';
#     break;
#   case 11:
#     bulan = 'November';
#     break;
#   case 12:
#     bulan = 'Desember';
#     break;
#   default:
#     validasi = false;
# }

# // USE SWITCH CASE
# // switch (true) {
# //   case validasi:
# //     console.log(tanggal + ' ' + bulan + ' ' + tahun);
# //     break;
# //   default:
# //     console.log('Harap masukkan angka yang benar \n Tanggal : 1 - 31 \n Bulan : 1 - 12 \n Tahun : 1900 - 2200');
# // }

# // WITHOUT SWITCH CASE
# validasi ? console.log(tanggal + ' ' + bulan + ' ' + tahun) : console.log('Harap masukkan angka yang benar \n Tanggal : 1 - 31 \n Bulan : 1 - 12 \n Tahun : 1900 - 2200');
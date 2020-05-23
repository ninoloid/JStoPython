nama = input('Masukkan nama kamu!\n')

if nama != '':
  peran = input('Masukkan peran yang akan kamu pilih. Peran yang tersedia : Ksatria, Tabib, Penyihir.\n')
  if peran == 'Ksatria' or peran == 'ksatria':
    print(f'Selamat datang di Dunia Proxytia, {nama} \nHalo, {peran} {nama}, kamu dapat menyerang dengan senjatamu!')
  elif peran == 'Tabib' or peran == 'tabib':
    print(f'Selamat datang di Dunia Proxytia, {nama} \nHalo, {peran} {nama}, kamu akan membantu temanmu yang terluka.')
  elif peran == 'Penyihir' or peran == 'penyihir':
    print(f'Selamat datang di Dunia Proxytia, {nama} \nHalo, {peran} {nama}, ciptakan keajaiban yang membantu kemenanganmu!')
  else:
    print(f'Halo {nama}, pilih peranmu untuk memulai game!')
else:
  print('Nama harus diisi!')
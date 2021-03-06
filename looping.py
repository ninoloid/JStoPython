i = 0
print('LOOPING PERTAMA')
while i <= 20:
  print(i, '- I love coding')
  i += 1
print('LOOPING KEDUA')
i -= 2
while i >= 0:
  print(i, '- I will become fullstack developer')
  i -= 2


# SOAL 2. MELAKUKAN LOOPING MENGGUNAKAN FOR

print('\n')
for i in range(21):
  print(i, '- I love coding')
for i in range(19, 0, -1):
  print(i, '- I will become fullstack developer')


# SOAL 3. ANGKA GANJIL DAN GENAP
print('\n')
for i in range(1, 11):
  if i % 2 == 0:
    print(i, '- Genap')
  else:
    print(i, '- Ganjil')

print('\n')
for i in range(101):
  if i % 3 == 0:
    if i % 6 == 0:
      print(i, '- Kelipatan 3 & Kelipatan 6')
    else:
      print(i, '- Kelipatan 3')
  elif i % 10 == 0:
    print(i, '- Kelipatan 10')
  else:
    print(i)



# IN JS
# let i = 2;
# console.log('LOOPING PERTAMA');
# while (i <= 20) {
#   console.log(i + ' - I love coding');
#   i += 2;
# }
# console.log('LOOPING KEDUA');
# i -= 2;
# while (i >= 2) {
#   console.log(i + ' - I will become fullstack developer');
#   i -= 2;
# }


# // SOAL 2. MELAKUKAN LOOPING MENGGUNAKAN FOR

# console.log('\nLOOPING PERTAMA');
# for (i = 1; i <= 20; i++) {
#   console.log(i + ' - I love coding');
# }
# console.log('LOOPING KEDUA');
# for (i = 20; i > 0; i--) {
#   console.log(i + ' - I will become fullstack developer');
# }


# // SOAL 3. ANGKA GANJIL DAN GENAP
# console.log('\n');
# for (let a = 1; a <= 10; a++) {
#   switch (true) {
#     case (a % 2 === 0):
#       console.log('GENAP');
#       break;
#     default:
#       console.log('GANJIL');
#   }
# }

# for (let a = 1; a <= 100; a += 2) {
#   switch (true) {
#     case (a % 3 === 0):
#       console.log(a + ' kelipatan 3');
#       break;
#     default:
#       console.log('');
#   }
# }

# for (let a = 1; a <= 100; a += 5) {
#   switch (true) {
#     case (a % 6 === 0):
#       console.log(a + ' kelipatan 6');
#       break;
#     default:
#       console.log('');
#   }
# }

# for (let a = 1; a <= 100; a += 9) {
#   switch (true) {
#     case (a % 10 === 0):
#       console.log(a + ' kelipatan 10');
#       break;
#     default:
#       console.log('');
#   }
# }
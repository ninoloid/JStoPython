def konversiMenit(menit):
  jam = menit // 60
  menit %= 60

  if menit < 10:
    menit = '0' + str(menit)
  
  return f'{jam}:{menit}'

print(konversiMenit(63)) # 1:03
print(konversiMenit(124)) # 2:04
print(konversiMenit(53)) # 0:53
print(konversiMenit(88)) # 1:28
print(konversiMenit(120)) # 2:00



# IN JS
# function konversiMenit(menit) {
#   let jam = parseInt(menit / 60);
#   menit %= 60;
#   switch (true) {
#     case menit < 10:
#       return jam + ':0' + menit;
#     default:
#       return jam + ':' + menit;
#   }
# }

# // TEST CASES
# console.log(konversiMenit(63)); // 1:03
# console.log(konversiMenit(124)); // 2:04
# console.log(konversiMenit(53)); // 0:53
# console.log(konversiMenit(88)); // 1:28
# console.log(konversiMenit(120)); // 2:00
def bandingkanAngka(angka1, angka2):
  if angka2 > angka1:
    return True
  elif angka2 < angka1:
    return False
  else:
    return -1

print(bandingkanAngka(5,8))
print(bandingkanAngka(5,3))
print(bandingkanAngka(4,4))
print(bandingkanAngka(3,3))
print(bandingkanAngka(17,2))


# IN JS
# function bandingkanAngka(angka1, angka2) {
#   switch (true) {
#     case angka2 > angka1:
#       return true;
#     case angka2 < angka1:
#       return false;
#     default:
#       return -1;
#   }
# }

# // TEST CASES
# console.log(bandingkanAngka(5, 8)); // true
# console.log(bandingkanAngka(5, 3)); // false
# console.log(bandingkanAngka(4, 4)); // -1
# console.log(bandingkanAngka(3, 3)); // -1
# console.log(bandingkanAngka(17, 2)); // false
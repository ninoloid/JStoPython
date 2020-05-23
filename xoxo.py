def xo(str_input):
  countX = 0
  countO = 0

  for i in str_input:
    if i == 'x':
      countX += 1
    elif i == 'o':
      countO += 1
    else:
      return 'Input salah, hanya menerima input \'x\' atau \'o\''
  
  if countX == countO:
    return True
  else:
    return False

print(xo('xoxoxo')) # true
print(xo('oxooxo')) # false
print(xo('oxo')) # false
print(xo('xxxooo')) # true
print(xo('xoxooxxo')) # true



# IN JS
# function xo(str) {
#   let countX = 0;
#   let countO = 0;
#   for (let i = 0; i < str.length; i++) {
#     switch (true) {
#       case str[i] === 'x':
#         countX += 1;
#         break;
#       case str[i] === 'o':
#         countO += 1;
#         break;
#       default:
#         return 'Input salah, hanya menerima input \'x\' atau \'o\'';
#     }
#   }
#   switch (true) {
#     case countX === countO:
#       return true;
#     default:
#       return false;
#   }
# }

# // TEST CASES
# console.log(xo('xoxoxo')); // true
# console.log(xo('oxooxo')); // false
# console.log(xo('oxo')); // false
# console.log(xo('xxxooo')); // true
# console.log(xo('xoxooxxo')); // true
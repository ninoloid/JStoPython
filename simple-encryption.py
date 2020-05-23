import re

letter = 'Ahmad Muhammad Satria Adiputra'

# enkripsi kata per huruf + 1, a = b, b = c, z = a dst..
def enkripsi(kata):
  result = ''
  a_to_y = re.compile('[a-y]+', re.IGNORECASE)
  only_z = re.compile('z', re.IGNORECASE)

  for i in kata:
    if a_to_y.match(i):
      result += chr(ord(i) + 1)
    elif only_z.match(i):
      result += chr(ord(i) - 25)
    else:
      result += i
  return result

print(enkripsi(letter))
print(enkripsi('XxYxZz'))


# let letter = 'Ahmad Muhammad Satria Adiputra';

# // enkripsi kata per huruf + 1, a = b, b = c, z = a dst..
# const enkripsi = kata => {
#   let temp = ''; // bisa juga pakai array. let arr = [], arr.push, arr.join('')
#   for (let i = 0, j = kata.length; i < j; i++) {
#     if (kata[i].match(/[a-y]/i)) {
#       temp += String.fromCharCode(kata[i].charCodeAt() + 1);
#     } else if (kata[i].match(/z/i)) {
#       temp += String.fromCharCode(kata[i].charCodeAt() - 25);
#     } else {
#       temp += kata[i];
#     }
#   }
#   return temp;
# }

# console.log(enkripsi(letter));
# console.log(enkripsi('XxYxZz'));
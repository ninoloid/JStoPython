rows1 = 5
for i in range(0, rows1):
  print('*')

rows2 = 5
for i in range(0, rows2):
  print('*' * rows2)

rows3 = 5
for i in range(1, rows3 + 1):
  print('*' * i)

rows4 = 5
for i in range(rows4, 0, -1):
  print('*' * i)

rows5 = 5
for i in range(1, rows5 + 1):
  print(' ' * int(rows5 - i) + '* ' * i)

rows6 = 5
for i in range(rows5, 0, -1):
  print(' ' * int(rows5 - i) + '* ' * i)



# IN JS
# var rows1 = 5;
# for (let i = 1; i <= rows1; i++) {
#   console.log('*');
# }

# // RESULT
# // *
# // *
# // *
# // *
# // *


# var rows2 = 5;
# var a = "";
# for (let i = 1; i <= rows2; i++) {
#   for (let j = 1; j <= rows2; j++) {
#     a += '*';
#   }
#   console.log(a);
#   a = "";
# }

# // RESULT
# // *****
# // *****
# // *****
# // *****
# // *****


# var rows3 = 5;
# var a = "";
# for (let i = 1; i <= rows3; i++) {
#   a += '*';
#   console.log(a);
# }

# // RESULT
# // *
# // **
# // ***
# // ****
# // *****
def balikKata(kata):
  result = ''
  for i in range(len(kata) - 1, -1, -1):
    result += kata[i]
  return result

print(balikKata('Hello World and Coders')) # sredoC dna dlroW olleH
print(balikKata('John Doe')) # eoD nhoJ
print(balikKata('I am a bookworm')) # mrowkoob a ma I
print(balikKata('Coding is my hobby')) # ybboh ym si gnidoC
print(balikKata('Super')) # repuS



# IN JS
# function balikKata(kata) {
#   let hasil = '';
#   for (let i = kata.length - 1; i >= 0; i--) {
#     hasil += kata[i];
#   }
#   return hasil;
# }

# // TEST CASES
# console.log(balikKata('Hello World and Coders')); // sredoC dna dlroW olleH
# console.log(balikKata('John Doe')); // eoD nhoJ
# console.log(balikKata('I am a bookworm')); // mrowkoob a ma I
# console.log(balikKata('Coding is my hobby')); // ybboh ym si gnidoC
# console.log(balikKata('Super')); // repuS
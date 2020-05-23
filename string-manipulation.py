# SOAL 1. LET'S FORM A SENTENCE

word = 'Python'
second = 'is'
third = 'awesome'
fourth = 'and'
fifth = 'I'
sixth = 'love'
seventh = 'it!'

print(f'{word} {second} {third} {fourth} {fifth} {sixth} {seventh}')


# SOAL 2. INDEX ACCESSING - 1 BY 1

word = 'wow JavaScript is so cool'
firstWord = word[0] + word[1] + word[2]
secondWord = word[4] + word[5] + word[6] + word[7] + word[8] + word[9] + word[10] + word[11] + word[12] + word[13]
thirdWord = word[15] + word[16]
fourthWord = word[18] + word[19]
fifthWord = word[21] + word[22] + word[23] + word[24]

print('First Word: ' + firstWord)
print('Second Word: ' + secondWord)
print('Third Word: ' + thirdWord)
print('Fourth Word: ' + fourthWord)
print('Fifth Word: ' + fifthWord)


# SOAL 3. BREAKING SENTENCE

word2 = 'wow JavaScript is so cool'
firstWord2 = word2[0:3]
secondWord2 = word2[4:14]
thirdWord2 = word2[15:17]
fourthWord2 = word2[18:20]
fifthWord2 = word2[21:26]

print('First Word: ' + firstWord2)
print('Second Word: ' + secondWord2)
print('Third Word: ' + thirdWord2)
print('Fourth Word: ' + fourthWord2)
print('Fifth Word: ' + fifthWord2)


# SOAL 4. BREAKING SENTENCE AND COUNT EACH LENGTH

firstWordLength = len(firstWord2)
secondWordLength = len(secondWord2)
thirdWordLength = len(thirdWord2)
fourthWordLength = len(fourthWord2)
fifthWordLength = len(fifthWord2)

print('First Word Length:', firstWordLength)
print('Second Word Length:', secondWordLength)
print('Third Word Length:', thirdWordLength)
print('Fourth Word Length:', fourthWordLength)
print('Fifth Word Length:', fifthWordLength)



# IN JS
# // SOAL 1. LET'S FORM A SENTENCE

# var word = 'JavaScript';
# var second = 'is';
# var third = 'awesome';
# var fourth = 'and';
# var fifth = 'I';
# var sixth = 'love';
# var seventh = 'it!';

# console.log(word + ' ' + second + ' ' + third + ' ' + fourth + ' ' + fifth + ' ' + sixth + ' ' + seventh);


# // SOAL 2. INDEX ACCESSING - 1 BY 1

# var word = 'wow JavaScript is so cool';
# var exampleFirstWord = word[0] + word[1] + word[2];
# var secondWord = word[4] + word[5] + word[6] + word[7] + word[8] + word[9] + word[10] + word[11] + word[12] + word[13]; // do your own!
# var thirdWord = word[15] + word[16]; // do your own!
# var fourthWord = word[18] + word[19]; // do your own!
# var fifthWord = word[21] + word[22] + word[23] + word[24]; // do your own!

# console.log('First Word: ' + exampleFirstWord);
# console.log('Second Word: ' + secondWord);
# console.log('Third Word: ' + thirdWord);
# console.log('Fourth Word: ' + fourthWord);
# console.log('Fifth Word: ' + fifthWord);


# // SOAL 3. BREAKING SENTENCE USING SUBSTRING

# var word3 = 'wow JavaScript is so cool';
# var exampleFirstWord3 = word3.substring(0, 3);
# var secondWord3 = word3.substring(4, 14); // do your own!
# var thirdWord3 = word3.substring(15, 17); // do your own!
# var fourthWord3 = word3.substring(18, 20); // do your own!
# var fifthWord3 = word3.substring(21, 26); // do your own!

# console.log('First Word: ' + exampleFirstWord3);
# console.log('Second Word: ' + secondWord3);
# console.log('Third Word: ' + thirdWord3);
# console.log('Fourth Word: ' + fourthWord3);
# console.log('Fifth Word: ' + fifthWord3);


# // SOAL 4. BREAKING SENTENCE AND COUNT EACH LENGTH

# var word4 = 'wow JavaScript is so cool';
# var exampleFirstWord4 = word4.substring(0, 3);
# var secondWord4 = word4.substring(4, 14); // do your own!
# var thirdWord4 = word4.substring(15, 17); // do your own!
# var fourthWord4 = word4.substring(18, 20); // do your own!
# var fifthWord4 = word4.substring(21, 26); // do your own!

# var firstWordLength = exampleFirstWord4.length;
# var secondWordLength = secondWord4.length;
# var thirdWordLength = thirdWord4.length;
# var fourthWordLength = fourthWord4.length;
# var fifthWordLength = fifthWord4.length;
# // create new variables around here

# console.log('First Word: ' + exampleFirstWord4 + ', with length: ' + firstWordLength);
# console.log('Second Word: ' + secondWord4 + ', with length: ' + secondWordLength);
# console.log('Third Word: ' + thirdWord4 + ', with length: ' + thirdWordLength);
# console.log('Fourth Word: ' + fourthWord4 + ', with length: ' + fourthWordLength);
# console.log('Fifth Word: ' + fifthWord4 + ', with length: ' + fifthWordLength);
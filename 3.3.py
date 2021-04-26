word = input(" Give A wORD : ")

output = []

for letter in word:
    if letter in 'aeiou' :
        output.append('ub' + letter)
    else:
        output.append(letter)
print(''.join(output))
word = input()
HR_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in HR_alphabet:
    word = word.replace(i, 'H')
print(len(word))

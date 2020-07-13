#Task1
from collections import Counter
print('Введіть перше слово:')
word1 = input()
print('Введіть друге слово:')
word2 = input()
print(False if Counter(word2) - Counter(word1) else True)

#Task2

from string import ascii_lowercase
text = input("Напишіть текст з цифр і літер латинського алфавіту:\n ")
golosni = 'aeiouy'
prygolosni = [i for i in ascii_lowercase if i not in golosni]
prygolosni_count = 0
golosni_count = 0
for i in text:
    if i in golosni:
        golosni_count += 1
    elif i in prygolosni:
        prygolosni_count += 1
if golosni_count == prygolosni_count:
    print('draw')
print('Приголосних більше' if prygolosni_count > golosni_count else 'Голосних більше')

#Task3

text = input("Введіть текст з латинських літер:\n ")
letters = sorted([i for i in text.lower() if i in 'aeiouy'])
for i in letters:
    print(i, end=' ')

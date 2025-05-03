#List biasa
buah = ['apel', 'jeruk', 'mangga']
print(buah)

#Loop pada list
buah = ['apel', 'jeruk', 'mangga']
for item in buah:
    print(item)

#while loop
i = 1
while i <= 5:
    print(i)
    i += 1

#range dalam for loop
for i in range(1, 6):
    print(i)

#nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f'i={i}, j={j}')
        
#break dalam loop
for i in range(10):
    if i == 5:
        break
    print(i)

#continue dalam loop
for i in range(5):
    if i == 2:
        continue
    print(i)

#else dalam loop
for i in range(3):
    print(i)
else:
    print("Loop selesai tanpa break.")

#looping pada list
angka = [10, 20, 30]
for a in angka:
    print(a)

#looping pada string
kata = "Python"
for huruf in kata:
    print(huruf)

#looping pada dictionary
data = {'nama': 'Ali', 'umur': 20}
for key, value in data.items():
    print(key, ":", value)

#loop pendek
kuadrat = [x**2 for x in range(1, 6)]
print(kuadrat)

#study case buat cetak segitiga angka
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

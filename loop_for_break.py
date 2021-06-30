# Menghentikan perulangan jika nilai x adalah 4
# Pada kode di bawah ini, jika nilai x sama dengan 4,
# maka perulangan akan dihentikan. Walaupun seharusnya
# perulangan akan berhenti setelah 5 kali berjalan.
for x in range(5):
    print(x)
    if x == 4:
        break
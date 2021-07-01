animals = ["Ayam", "Bebek", "Cicak"]

# Menambah item pada "Lists" dengan posisi (indexing) terakhir menggunakan function "append"
animals.append("Domba")
print(animals)  # ["Ayam", "Bebek", "Cicak", "Domba"]
animals.append("Harimau")
print(animals)

# Menambah item pada "Lists" dengan posisi (indexing) tertentu menggunakan function "insert"
# Contoh kita ingin menambahkan 1 item dengan posisi ketiga (indexing = 2)

animals.insert(2, "Buaya")

print(animals)  # ['Ayam', 'Bebek', 'Buaya', 'Cicak', 'Domba']

# menambahkan di list 0
animals.insert(0, "Sapi")
print(animals)

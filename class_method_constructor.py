# Membuat Class Cat dengan property color dan menambahkan method constructor
# Kita akan menambahkan method constructor untuk mengubah nilai dari properti color


# Test 1
class Cat:
    color = "black"

    def __init__(self, color):
        self.color = color


# Membuat objek baru
cat1 = Cat("orange")
print(cat1.color)  # orange


# Test 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
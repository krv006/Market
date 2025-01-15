# num1 = 3
# num2 = 5

data = 42          # Asl ma'lumot
key = 123          # Kalit

# Shifrlash
encrypted = data ^ key
print("Shifrlangan:", encrypted)

# Shifrdan chiqarish
decrypted = encrypted ^ key
print("Asliga qaytarildi:", decrypted)
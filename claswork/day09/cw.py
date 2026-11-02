# while loop - ის გამოყენებით დაბეჭდეთ რიცხვები 0 - დან 20 - მდე.
# 2. while loop - ის გამოყენებით დაბეჭდეთ რიცხვები 20 - დან 0 - მდე.
# 3. while loop - ის გამოყენებით დაბეჭდეთ რიცხვები 0 - დან 50 - მდე და გამოტოვეთ ყოველი მეორე რიცხვი.
# 4. while loop - ის გამოყენებით დაბეჭდეთ რიცხვები 50 - დან 0 - მდე და გამოყოვეთ სამ - სამი რიცხვი.
# 5. while loop - ის გამოყენებით დაებჭდეთ, თუ პაროლი არ უდრის მომხმარებლის შემოყვანილ პაროლს, მაშინ ყოველ ჯერზე შეეკითხეთ რომ შემოიყვანოს მომხმარებელმა პაროლი, სწორი პაროლის შემთხვევაში "correct password".

i = 0

while i <= 20:
    print(i)
    i += 1



i = 20

while i >= 0:
    print(i)
    i -= 1


i = 0

while i <= 50:
    print(i)
    i += 2

i = 50

while i >= 0:
    print(i)
    i -= 3

password = "12345"

user_password = input("Enter password: ")

while user_password != password:
    user_password = input("Wrong password! Try again: ")
print("Correct password")


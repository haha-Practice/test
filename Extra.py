# print("hello!")

print("================================ WELCOME TO KBC ================================")
contestant_name = input("Enter your name: ")
contestant_age = int(input("Enter your age: "))
print("\n")
print(f"Hello \033[1m{contestant_name} \033[0m, age {contestant_age}, welcome to KBC!")
print("\033[1m Let's start the game!\033[0m")

print("\n")
print("Question 1: What is the capital of France?")
print("a) Berlin")
print("b) Madrid")
print("c) Paris")
answer_1 = input("Your answer (a/b/c): ").lower()
if answer_1 == 'c':
    print("Correct! You have won $1000.")
else:
    print("Incorrect. The correct answer is c) Paris.")
    print("Thank you for playing KBC!")
    exit()


print("\n")
print("Question 2: What is 2 + 2?")
print("a) 3")
print("b) 4")
print("c) 5")
answer_2 = input("Your answer (a/b/c): ").lower()
if answer_2 == 'b':
    print("Correct! You have won $2000.")
else:
    print("Incorrect. The correct answer is b) 4.")
    print("Thank you for playing KBC!")
    exit()

print("\n")
print("What is your age after 5 years if your age is right now 5 years old then your 20 old Czn?")
ans = contestant_age + 5
print("a) 21")
print(f"b) {ans}")
print("c) 32")
print("d) 13")
print("e) 46")
print("f) 85")
user_age = int(input("Enter your age: "))
if user_age == ans:
    print("Correct! You have won $3000.")
else:
    print(f"Incorrect. The correct answer is b) {ans}.")
    print("Thank you for playing KBC!")
    exit()  


print("\n")
print("Congratulations! You have completed the game and won a total of $3000.")
print("3000 USD is approximately 841500 PKR.")
print("Thank you for playing KBC!")
print("================================ END OF KBC ================================")
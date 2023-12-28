import random
guess = 0
count = 0
answer = random.randint(1,100)
a=1
b=99

print("Guess Number (1-99) in 10 times")

while guess != answer:
    guess = int(input("Guess number: "))
    count += 1
    if answer < guess:
        b = guess
        print(f"wrong number,{a}-{b}")  
        
    if answer > guess:
        a = guess
        print(f"wrong number,{a}-{b}")
        
    if count == 10:
        break

if guess == answer:
    print("Congratulation,", "tries: ", count )

else:
    print("You failed, Answer is %d" %(answer))

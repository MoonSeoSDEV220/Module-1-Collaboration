# %%
#4.1
secret: int = 3
guess: int = 6

if guess > secret:
    print("Too high")
elif guess < secret:
    print("Too low")
elif guess == secret:
    print("Just right")
    
    

# %%
#4.2
small: bool = True
green: bool = True

if small and green:
    print("pea")
elif small and not green:
    print("Cherry")
elif not small and not green:
    print("Pumpkin")
elif not small and green:
    print("Watermelon") 
    


# %%
#6.1
list(range(3, -1, -1))


# %%
#6.2
guess_me: int = 7
number: int = 1

while True:
    if number > guess_me:
        print("oops")
        break
    elif number < guess_me:
        print(number)
        print("Too low")
        number += 1
    elif number == guess_me:
        print(number)
        print("Found it~")
        break
    
    


# %%
#6.3

guess_me: int = 5
for i in range(0, 10, 1):
    if i > guess_me:
        print("Oops")
        break
    if i == guess_me:
        print(i)
        print("Found it!")
        break
    if i < guess_me:
        print(i)
        print("Too low")
    
    




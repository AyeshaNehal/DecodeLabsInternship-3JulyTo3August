#this is the project to generate a randopm password made of number letters ( both cases ) and characters and the length should be user defined
import random
import string
#random Imports Python's random module, which lets us pick random characters.
#import string Imports the string module, which contains ready-made strings like all uppercase letters, lowercase letters, and digits.

print("------Secure Password Generator Program------")
length=int(input("Enter The Length Of The Password That You Want to Generate(Min=3):"))
if length<3:
    print("Incorrect Length - Password Must be Atleast 3 characters long")
else:
    password=[random.choice(string.ascii_uppercase),random.choice(string.ascii_lowercase),random.choice(string.digits)]

    characters=string.ascii_letters + string.digits
    while(len(password)) < length:
        password.append(random.choice(characters))
    random.shuffle(password)

    print("The Generated Password is: ","".join(password))

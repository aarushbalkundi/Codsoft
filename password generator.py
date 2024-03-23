import string
import random
dig = list(string.digits)  
upper = list(string.ascii_letters)  
spec = list(string.punctuation)

combine = dig+upper+spec

def random_gen(n):
    password = []
    for i in range(n):
        password.append(random.choice(combine))
    return password

def main():
    a = int(input('Enter number of characters in password:\t'))
    print("Random Password generated:\n"+''.join(random_gen(a)))

main()
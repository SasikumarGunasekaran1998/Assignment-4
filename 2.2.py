def func(char):
    vowels = ['a','e','i','o','u']
    if char in vowels:
        return True
    else:
        return False
if __name__ == "__main__":
    char = input("Enter a cahracter")
    print(func(char))
    

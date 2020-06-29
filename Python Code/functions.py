#Demonstrates how to use functions in Python

def exponent(x, y):
    total = 1
    for i in range(y):
        total *= x
    return total

#Main function is main part of code
def main():
    for i in range(5):
        print("{} to the power of {} is {}".format(i + 1, i + 1, exponent(i + 1, i + 1)))

#This runs main() if this file is being ran
#Doing as such allows for easy import of functions used here
if __name__ == "__main__":
    main()



def fizzbuzz(number):
    if not number % 3 and not number % 5:
        return "FizzBuzz"
    elif not number % 3:
        return "Fizz"
    elif not number % 5:
        return "Buzz" 
    else:
        return number

def main():
    number = 100
    fizzbuzz(number)

main()

# if __name__ == '__main__':
#     main()

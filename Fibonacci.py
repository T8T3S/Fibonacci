def get_fib_numbers(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return get_fib_numbers(number - 1) + get_fib_numbers(number - 2)

def main():
    print('The Fibonacci series for 16')
    for n in range(16):
       print(get_fib_numbers(n), end=", ")
    print("...")


if __name__ == "__main__":
    main()
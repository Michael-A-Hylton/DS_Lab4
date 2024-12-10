def fib(number:int):
    print(number)
    if (number<=1):
        return number
        
    else:
        return (fib(number-1)+fib(number-2))
    




def main():
    number=int(input("input the fibonocci number: "))
    print(fib(number))

main()

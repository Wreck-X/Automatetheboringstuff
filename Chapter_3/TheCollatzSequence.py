def collatz(number):
    if number % 2 ==0:
        number = number // 2
        return number
    if number % 2 != 0:
        number = 3 * number + 1
        return number

while True:
    try:
        num = int(input())
        print(collatz(num))
    except ValueError:
        print('ValueError')
def mylen(list):
    if list == []:
        return 0
    else:
        return 1 + mylen(list[1:])

def main():
    alist = [43, 76, 97, 86]
    print(mylen(alist))
main()


def intDivison(n, m):
    if n < 0:
        raise Exception("Dividend cannot be less than zero.")
    if m <= 0:
        raise Exception("Divisor cannot be equal to or less than zero.")
    if n < m:
        return n
    else:
        return intDivison(n - m, m)
    
def main():
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer divison', n, '//', m, '=', intDivison(n,m))
main()


def sumdigits(num):
    if num < 10:
        return num
    else:
        return (num % 10) + sumdigits(num // 10)

def main():
    number = int(input('Enter a number: '))
    if number < 0:
        raise Exception("Number must be a positive integer.")
    print(sumdigits(number))
main()


def reverseDisplay(num):
    if num > 0:
        print(num % 10, end = "")
        return reverseDisplay(num // 10)

def main():
    number = int(input('Enter a number: '))
    if number < 0:
        raise Exception("Number must be a positive integer.")
    reverseDisplay(number)
main()


def binary_search2(key, alist, low, high):
    if high < low: 
        return -1
    guess = (low + high)
    if key == alist[guess]:
        return guess
    elif key < alist[guess]:
        high = binary_search2(key, alist, low, guess - 1)
        if high == -1:
            return "Item is not in the list"
        return high
    else:
        low = binary_search2(key, alist, guess + 1, high)
        if low == -1:
            return "Item is not in the list"
        return low

def main():
    some_list = [-8, -2, 1, 3, 5, 7, 9]
    print(binary_search2(9, some_list, 0, len(some_list) - 1))
    print(binary_search2(-8, some_list, 0, len(some_list) - 1))
    print(binary_search2(4, some_list, 0, len(some_list) - 1))
main()
def check_palindrome(n):
    n_copy = n
    n_reversed = 0
    while n_copy > 0:
        n_reversed = n_reversed * 10 + (n_copy % 10)
        n_copy = n_copy // 10
    if n == n_reversed:
        return True
    return False



if __name__ == '__main__':
    number = int(input("Enter number: "))
    if check_palindrome(number):
        print("palindrom")
    else:
        print("nu e palindrome")

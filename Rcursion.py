#1
def multiply(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multiply(a, b - 1)
    elif b < 0:
        return -multiply(a, -b)
#2  
def sumOfDigits(n):
    if len(str(n)) == 1:
        return n
    elif len(str(n)) > 1:
        return sumOfDigits(n % 10) + sumOfDigits(n//10)
#3    
def power(a,b):
    if b == 0:
        return 1
    elif b > 0 :
        return a * power(a,b-1)
    else: 
        return 1/power(a, -b)


#4
def reversed(n):
    n_str = str(n)
    if len(n_str) == 1:
        return n_str
    else:
        return n_str[-1] + reversed(int(n_str[:-1])) 
        
#5

def findSum(arr, n):
    if n == 0:
        return 0
    return 1 + findSum(arr, n-1)
    
#6
def divide(a,b):
    if a < b:
        return 0
    return 1 + divide(a - b, b) 

#7
def isPalindrome(St):
    if len(St) <= 1:
        return True
    if St[0] == St[-1]:
        return isPalindrome(St[1:-1])
    else:
        return False
        
        
#8
def decimalToBinary(n):
    if n == 0:
        return ""
    return decimalToBinary(n // 2) + str(n % 2)
    

#9
#Euclid's algorithm
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

#10
def evenNumbers(n):
    if n <= 0:
        return 
    evenNumbers(n-2)
    if n % 2 == 0:
        print(n)
 
 
def main():
    print(multiply(4, 4))
    print(sumOfDigits(6765))
    print(power(-2,4))
    print(reversed(123))
    print(findSum([1,2,3,4,4],5))
    print(divide(10,2))
    print(isPalindrome("aba"))
    print(decimalToBinary(5))
    print(gcd(24,36))
    (evenNumbers(10))
if __name__ == "__main__": 
    main()

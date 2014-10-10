def nth_fibonacci(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)  
#print (nth_fibonacci(8))


def sum_of_digits(n):
    resoult = 0
    resoultList = []
    while n>10:
        resoultList.append(n%10)
        n = n//10
    resoultList.append(n)

    for digit in resoultList:
        resoult += digit
    return resoult
#print (sum_of_digits(1234))


def sum_of_divisors(n):
    a = 1
    resoult = 0
    while a <= n:
        if n % a == 0:
            resoult += a
        a = a + 1
    return resoult
    


def is_prime(n):
    if sum_of_divisors(n)==n+1:
        return True
    else:
        return False
#print (is_prime(4))


def num_of_divisors(n):
    a = 1
    resoult = 0
    while a <= n:
        if n % a == 0:
            resoult += 1
        a = a + 1
    return resoult


def prime_number_of_divisors(n):
    number = num_of_divisors(n)
    if is_prime(number) == True:
        return True
    else:
        return False
#print (prime_number_of_divisors(6))

arr = [1, 7 , 7 ,7 , 2, 4]
def sevens_in_a_row(arr, n):
    resoult = 0
    for num in arr:
        if num == 7:
            resoult += 1
    if resoult == n:
        return True
    else:
        return False
#print (sevens_in_a_row(arr, 4))

def is_int_palindrome(n):
    n_string = str(n)
    n_reversedString = n_string[::-1]
    n_reversed = int(n_reversedString)
    if n_reversed == n:
        return True
    else:
        return False
#print (is_int_palindrome(14))


def contains_digit(number, digit):
    nuberString = str(number)
    if str(digit) in nuberString:
        return True
    else:
        return False
#print (contains_digit(1234, 3))


def contains_digits(number, digits):
    flag = False
    numberString = str(number)
    for digit in digits:
        if str(digit) in numberString:
            flag = True
        else:
            flag = False
            break
    return flag
#print (contains_digits(4612, [1,2,4,6]))

def is_number_balanced(n):
    numList = []
    if n < 10:
        return True
    else:
        while n >= 10:
            numList.append(n%10)
            n = n // 10
        numList.append(n)
        print (numList)
        a = 0
        b = 0
        flag = False
        for digit in numList:
            if len(numList) % 2 == 0:
                if digit == numList[len(numList)//2]:
                    flag = True
                if not flag:
                    a+=digit
                elif flag:
                    b+=digit
            else:
                if digit == numList[len(numList)//2]:
                    flag = True
                    continue
                if not flag:
                    a+=digit
                elif flag:
                    b+=digit
        if a == b:
            return True
        else:
            return False
#print (is_number_balanced(132))

def count_substrings(haystack, needle):
    a = 0
    count = 0
    while a != -1:
        a = haystack.find(needle)
        if a != -1:
            count += 1
            haystack = haystack[a+len(needle):]
    return count
#print (count_substrings("Python is an awesome language to program in!", "o"))


def count_vowels(str):
    count = 0
    sub = str.lower()
    for char in sub:
        if char == 'a' or char == 'o' or char == 'e' or char == 'i' or \
        char == 'y':
            count +=1
    return count
#print (count_vowels("abcdfa"))

def count_consonants(str):
    count = 0
    sub = str.lower()
    for char in sub:
        if char == 'b' or char == 'c' or char == 'd' or char == 'f' or \
        char == 'g' or char == 'h' or char == 'j' or char == 'k' or \
        char == 'l' or char == 'm' or char == 'n' or char == 'p' or \
        char == 'q' or char == 'r' or char == 's' or char == 't' or \
        char == 'v' or char == 'w' or char == 'z' or char == 'z':
            count +=1
    return count
#print (count_consonants("Python"))

def number_to_list(n):
    a = []
    b = []
    while n>=10:
        a.append(n%10)
        n = n // 10
    a.append(n)
    for digit in reversed(a):
        b.append(digit)
    return b
#print (number_to_list(123))

def list_to_number(digits):
    a = len(digits)
    result = 0
    for digit in digits:
        b = int(digit)
        result = result + b*(10**(a-1))
        a = a - 1
    return result

#print (list_to_number([1,2,3]))


def biggest_difference(arr):
    min = max(arr)
    for num in arr:
        for a in range(1, len(arr)):
            if num - arr[a] < min:
                min = num - arr[a]
    return min
#print (biggest_difference([1,2,3,4,5]))


def is_increasing(seq):
    flag = True
    for i in range(1, len(seq)):
        if not seq[i] > seq[i-1]:
            flag = False
    return flag
#print (is_increasing([1]))


def is_decreasing(seq):
    flag = True
    for i in range(1, len(seq)):
        if not seq[i] < seq [i-1]:
            flag = False
    return flag
#print (is_decreasing([1,1,1,1]))

def zero_insert(n):                                                                 
    numString = str(n)
    for i in range(0, len(numString)*2):
        if i < len(numString)-1:
            if numString[i] == numString[i+1]:
                numString = numString[:i+1] + "0" + numString[i+1:]    
            else:
                if int(numString[i]) + int(numString[i+1]) == 10:
                    numString = numString[:i+1] + "0" + numString[i+1:]    
    return numString
#print (zero_insert(116437))


def sum_matrix(m):
    result = 0
    row = len(m)
    coloum = len(m[0])
    for i in range(row):
        for j in range(coloum):
            result += m[i][j]
    return result
#print (sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

def matrix_bombing_plan(m):
    result = {}
    return result

print (matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


    








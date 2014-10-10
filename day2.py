def count_words(arr):
    result = {}
    for element in arr:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result
#print (count_words(["apple", "banana", "apple", "pie"]))

def unique_words_count(arr):
    result = 0
    uniqueWords = []
    for word in arr:
        if word not in uniqueWords:
            uniqueWords.append(word)
    return len(uniqueWords)
#print (unique_words_count(["python", "python", "python", "ruby"]))

def groupby(func, seq):
    result = {}
    for item in seq:
        key = func(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]
    return result



def prepare_meal(number):
    a = 0
    if number % 3 == 0:
        while a < 10:
            if number % (3**a) == 0 and number % (3**(a+1)) != 0:
                if number % 5 != 0:
                    return 'spam '*a
                    break
                else:
                    return 'spam '*a + "and eggs"
                    break
            else:
                a += 1
    else:
        if number % 5 == 0:
            return 'eggs'
        else:
            return ''
#print (prepare_meal(5))

def reduce_file_path(path):
    a = 0
    while a != -1:
        a = path.find("//")
        if a != -1:
            path = path[:a] + path[a+1:]
    while a < 10:
        for i in range(len(path)):
            if i < len(path)-1:
                if path[i] == '.' and path[i+1] != '.':
                    path = path[:i-1] + path[i+1:]
                    i=i-2
                elif path[i] == '.' and path[i+1] == '.':
                    subPath1 = path[:i-1]
                    subPath2 = path[i+3:]
                    for i in range(len(subPath1)-1 , 0, -1):
                        if subPath1[i] == "/":
                            subPath1 = subPath1[:i+1]
                    path = subPath1 + subPath2
        a +=1
    return path   
#print (reduce_file_path("/a/aaa/../bb//b/./b/"))       


def is_an_bn(word):
    count = 0
    if not word:
        return True
    for char in word:
        if char != "a" and char != "b":
            return False
    for i in range(len(word)-1):
        if word[i] == "a":
            count += 1
        else:
            break        
    word = word[count:]
    if word != "b"*count:
        return False
    else:
        return True
#print (is_an_bn("aaaabbb"))

def simplify_fraction(fraction):
    a = fraction[0]
    b = fraction[1]
    result = ()
    for i in range(0, a):
        if a % (a-i) == 0 and b % (a-i) == 0:
            result = (a//(a-i), b//(a-i))
            break
    return result
#print (simplify_fraction((63,462)))

def sort_fractions(fractions):
    result = []
    for tupe in fractions:
        for i in range(len(tupe)-1):
            if i < len(tupe):
                if tupe[i] > tupe[i+1]:
                    tupe =(tupe[i+1], tupe[i])
                result.append(tupe) 

    for i in range(len(fractions)-1):       #could be optimised
        if result[i][0] > result[i+1][0]:
            temp = result[i+1]
            result[i+1] = result[i]
            result[i] = temp
    return result
#print (sort_fractions([(3, 2), (1, 2)]))










            
def examples(a):
    for i in range(0,a):
        print (i)
#examples(3)


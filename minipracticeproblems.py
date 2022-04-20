def first_and_last_swap(x):
    a = x[0]
    x[0] = x[-1]
    x[-1] = a
    return x
x = [1,2,3,4,7]
print(first_and_last_swap(x))
y = [1,2,3]
def swap(g, pos1, pos2):
    a = g[pos1]
    g[pos1] = g[pos2]
    g[pos2] = a
    return g
print(swap(y,1,2))

def max(a,b):
    if a>b:
        return a
    else:
        return b

print(max(-23,-5))

def is_palindrome(x):
    half = len(x) // 2
    length = len(x)
    i = 0
    while i <= half:
        if x[i] != x[length - i-1]:
            return False
        i += 1
    return True

print(is_palindrome("karen"))

def is_symetrical(x):
    if len(x)%2 == 0:
        for i in range(len(x) // 2):
            if x[i] != x[len(x) - len(x)//2 + i]:
                return False
    if len(x)%2 != 0:
        for i in range(len(x) // 2):
            if x[i] != x[len(x) - len(x)//2 + i]:
                return False
    return True

print(is_symetrical("fldifldi"))

def roman_to_int(roman):
    i = 0
    num = 0
    dict = {"I" : 1,"IV" : 4,"V" : 5,"IX" : 9,"X" : 10}
    while i < len(roman):
        if roman[i:i+2] in dict and i != len(roman) - 1:
            num = num + dict[roman[i:i+2]]
            i = i + 2
        else:
            num = num + dict[roman[i]]
            i = i + 1
    return num
print(roman_to_int("XX"))

def ransom_note(a,b):
    for i in range(len(a)):
        if a[i] in b:
            y = b.index(a[i])
            b = b[:y] + b[y+1:]
        else:
            return False
    return True

print(ransom_note("at", "bat"))

def how_long_to_reduce(num):
    count = 0
    while num > 0:
        if num%2 == 0:
            num = num//2
            count += 1
        if num%2 != 0:
            num = num - 1
            count += 1
    return count

print(how_long_to_reduce(4))


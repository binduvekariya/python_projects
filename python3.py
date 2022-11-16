

def most_frequent(st):
    dic1 = {}
    for key in st:
        if key not in dic1:
            dic1[key] = 1
        else:
            dic1[key] += 1

    a = dic1
    return a


str1 = input("Enter a string: ")
b = most_frequent(str1)
print(b)

dic = sorted(b.items(), key = lambda x : x[1] , reverse = True)

print(dic)









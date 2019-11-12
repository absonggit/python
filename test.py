ages = [13, 15, 32, 55]

sum = 0
for i in ages:
    sum += i

print(sum / len(ages))

sum = 0
for i in range(len(ages)):
    sum += ages[i]

print(sum / len(ages))

dict1 = {}
for i, d in enumerate(ages):
    dict1[i] = d

print(dict1)

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

for k, v in dict1.items():
    print(k, v)

keyword = input('输入关键字')
dict2 = {}
for value in "sss zioc ioc zkcop nouuyq sss".split(" "):
    str1 = dict2.get(value)
    if str1 == None:
        dict2[value] = 1
    else:
        dict2[value] += 1

print(dict2[keyword])
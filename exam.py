lists = [1, 2, 3, 4]

lists.append(5)
print(lists)
lists.remove(1)
print(lists)
lists.reverse()
print(lists)

lists.clear()
print(lists)

print('---'*10)

tuple = ('1234567')
print(len(tuple))

dict = {'name': "suraj", 'class': 'st1'}
print(len(dict))

for key, value in dict.items():
    print(f"{key}:{value}")


days = {
    'today': '2023/08/02',
    'tommorow': '2023/08/03',
    'yesterday': '2023/08/01',
}

for key, value in days.items():
    print(f"{key}:{value}")

# test = {1, 2, 3, 1}
test = set('1234565')
test.add(10)

print(test)
print(17 / 3)
print(17 // 3)
print(3**3)

for x in range(5):
    if x == 2:
        continue
    print(x)


subs = {'eng', 'math', 'sci'}
print('math' in subs)
print(type(subs))

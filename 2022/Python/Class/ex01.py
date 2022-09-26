input_number = input()
number_dict = {
    '0': 'ling',
    '1': 'yi',
    '2': 'er',
    '3': 'san',
    '4': 'si',
    '5': 'wu',
    '6': 'liu',
    '7': 'qi',
    '8': 'ba',
    '9': 'jiu'
}
sum = 0
result = ''
for iter in input_number:
    sum += int(iter)

for item in str(sum):
    result += number_dict[item] + ' '
print(result)
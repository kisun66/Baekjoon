input = input()
input = input.upper()
word_dict = {}

for i in range(len(input)):
    if input[i] in word_dict:
        word_dict[input[i]] += 1
    else:
        word_dict[input[i]] = 1

max_value = 0
max_key = ''

for i in word_dict:
    if word_dict.get(i) > max_value:
        max_value = word_dict.get(i)
        max_key = i
    elif word_dict.get(i) == max_value:
        max_key = '?'

print(max_key)
dictionary = {'Roburt': 25, 'Gabriela': 24}
print(dictionary)

if 'Ivan' not in dictionary:

    dictionary['Ivan'] = dictionary.get('ivan', 15) + 15

print("new dictionary\n", dictionary)
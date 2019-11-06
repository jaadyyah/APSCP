# description of function goes here
# input:  user sees list of not plural fruit
# output:  the function returns the plural of the fruits


def fruit_pluralizer(list_of_strings):
    new_fruits = []
    for item in list_of_strings:
        if item == '':
            item = 'No item'
            new_fruits.append(item)
        elif item[-1] == 'y':
            item = item[:-1] + 'ies'
            new_fruits.append(item)
        elif item[-1] == 'e':
            item1 = item + 's'
            new_fruits.append(item1)
        elif item[-2:] == 'ch':
            item2 = item + 'es'
            new_fruits.append(item2)
        else:
            item3 = item + 's'
            new_fruits.append(item3)
    return new_fruits


fruit_list = ['apple', 'berry', 'melon', 'peach']
print("Single Fruit: " + str(fruit_list))
new_fruits_list = fruit_pluralizer(fruit_list)
print("Plural Fruit: " + str(new_fruits_list))

# claire checked me based on the asssaignements she said I did a gud

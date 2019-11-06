# to do list: the key (first part) has to be a day of the week
# tis a list after the :

to_do = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}
start_up = input('What would you like to do? ')


if start_up == 'add':
    add = input('What day of the week would you like to add to? ')
    if add in to_do:
        to_add = input('What would you like add to this days work? ')
        (to_do[add].append(to_add))
    print(to_do[add])
if start_up == 'get':
    get = input('What day of the week would you like to look at? ')
    print(to_do[get])

# hi this is claire, the code works to add and get the to do lists,
# it also seems to fulfill all the requirements in the rubric

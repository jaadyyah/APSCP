# description of function goes here
# input:  string is given
# output: string gets reversed


def my_reverse(string_to_reverse):
    rev = input("Enter a sentence here: ")
    reverse_code = rev[::-1]
    print(reverse_code)
#    my_reverse(string_to_reverse)
    return reverse_code

finish = 'Done'
#print(my_reverse(finish))
finish = my_reverse(finish)

# luis: I typed a sentence next to where it told me to and then it would write my sentence backwards.
# it looks good according to the rubric

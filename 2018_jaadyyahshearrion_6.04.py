def frequency(paragraph):
    paragraph_lower = paragraph.lower()
    paragraph_lower_no_punctuation = paragraph_lower.replace(".", "")
    w_list = paragraph_lower_no_punctuation.split(" ")

# this code ^ makes sure that there isn't any punctuation or capitalization goes into the words that are being counted
# also it makes sure the computer knows that the string isn't one big chunk with split

    word_dic = {}
    for word in w_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return word_dic

# this ^ checks if any words we count are in the empty dict. if the word is in the dict it will add 1 to its value
# if not it will make it thw value of one to show that it has been counted


def find_max_value(dict):
    max_word = ''
    max_value = 0
    for word in dict:
        if dict[word] >= max_value:
            max_word = word
            max_value = dict[word]
    return max_word
# this code takes the key which is the first part of ' : ' then checks if it's empty or greater than a value that is
# already in the list we are making

para = frequency("It was a beautiful, beautiful, beautiful day in New York City. It smelled like poop poop.")
# by calling the frequency function it makes sure the function knows that its job is to make the sentence / paragraph
# is going to be lowercase and no punctuation and makes it not a glob


for p in range(4):
    key = find_max_value(para)
    print(key + 'has ' + str(para[key]))
    del para[key]
# this last bit of code helps me make the rest of the code work. Changing the range number changes how many times this
# code will run. the print statement is my way of keeping the frequency of the words kind a neat manner. the str part of
# this makes sure that the computer knows that the paragrpha aka the words in it are going to be the key in the dict
# the del statement is for the deletion of the key its kind of like a new line in a way its making sure it
# being the computer knows that its been counted

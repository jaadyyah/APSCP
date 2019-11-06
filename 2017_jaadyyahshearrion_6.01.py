meme_dic = {'lava': 'the floor is...', 'star': 'shooting star',
            'crack': 'cracking open a cold one with the boys', 'spongeBob': 'mocking spongeBob',
            'boyfriend': 'distracted boyfriend'}

question = input('What word / phrase would you like to look up in the meme dictionary?')

if question in meme_dic:
    print('This meme is in the dictionary')
    print(meme_dic[question])
else:
    print("This meme isn't in the dictionary")

#hi this is Claire I tested it and it works i tried a meme that was in it and one that wasn't and
#it told me whether or not it was in the dictionary

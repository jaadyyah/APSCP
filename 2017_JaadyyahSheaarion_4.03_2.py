def stars_and_stripes():
    estrella = '* '
    stripe = '- '
    for e in range(6):
        print('\n')
        for f in range(7):
            if e % 2 == 0:
                print(estrella, end='')
            if e % 2 == 1:
                print(stripe, end='')
stars_and_stripes()


# claire assisted me in giving an idea of how to get my code working properly

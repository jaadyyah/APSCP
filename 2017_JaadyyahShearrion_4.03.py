def draw_7():
    star = '* '
    for characters in range(7):
        print('\n')
        for item in range(7):
            print(star, end='')


(draw_7())


def increasing_triangle():
    num = 1
    for characters in range(7):
        print('\n')
        for num in range(1, num + 1):
            print(num, end='')
        num += 1
increasing_triangle()

# claire and Abbos tried to help me get tried of the 0s that print in the triangle

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

def stars_and_stripes():
    estrella = '*'
    stripe = '-'
    for e in range(6):
        print('\n')
        for f in range(6):
                print(stripe, estrella, end="")

stars_and_stripes()

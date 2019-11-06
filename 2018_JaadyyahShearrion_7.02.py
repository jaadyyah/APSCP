class Pet:
    def __init__(self, animal, color, food, noise, name):
        self.Animal = animal
        self.Color = color
        self.Food = food
        self.Noise = noise
        self.Name = name


def pet_picker():
    for p in pets:
        print(p.Name + ' eats ' + p.Food)

pets = [Pet('Cat', 'black ', 'milk', 'meow', 'Purrfect'),
        Pet('Human', 'White', 'mayo on Wonderbread', 'Donald Trump', 'Sprinkles'),
        Pet('Vampire Bat', 'blue', 'mice', 'screech', 'Woobat')]

pet_picker()

# Mikael ran it lke 10000 times to make sure the code didn't mess up at any point \:D

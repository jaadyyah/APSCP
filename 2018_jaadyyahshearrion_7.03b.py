class Kangaroo(object):
    def __init__(self, name):
        self.name = name
        self.pouch_contents = []

    def put_in_pouch(self, thing):
        self.pouch_contents.append(thing)

    def __str__(self):
        return str(self.pouch_contents)

thing = Kangaroo('Kanga')
thing.put_in_pouch('roo')
thing2 = Kangaroo('Roo')
thing2.put_in_pouch('Kanga')
thing3 = Kangaroo('Mike Tyson')
thing3.put_in_pouch('An Ear')
print(thing3)

# this code works so well it broke Ms. Atwood - Claire W.
# I mean I guess... ~Mikael :D

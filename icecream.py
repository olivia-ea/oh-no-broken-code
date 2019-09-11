# I want to print out my favorite ice cream flavors.

all_flavors = {'chocolate', 'mint', 'strawberry', 'caramel', 'pecan',
               'cookie dough', 'vanilla', 'lemon'}
my_faves = {'mint', 'caramel'}

for flavor in all_flavors:
    if flavor in my_faves:
        print(f"I like {flavor}!")

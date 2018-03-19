import plyvel

db = plyvel.DB('/tmp/journal/', create_if_missing=False)

def only_ascii(db_object):
    for key, value in db_object:
        print("key: ", key)
        print("------------------------------------")
        for char in value:
            # only print characters that are within the range of printable
            # characters of the ASCII table
            if char in range(32,128):
                print(chr(char), end="")
        print("------------------------------------")

def non_ascii(db_object):
    for key, value in db_object:
        print("key", key)
        print("------------------------------------")
        print("value", value)
        print("------------------------------------")

print('''Please enter one of the two options:
    1. list values with only ASCII printable characters.
    2. list value with both printable and non ASCII values.
''')

choice = int(input("Please put in a value and press enter: "))

if choice in range(1,3):
    if choice == 1:
        only_ascii(db)
    else:
        non_ascii(db)
else:
    print("wrong input")

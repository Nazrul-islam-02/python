

class Phone:
    def call(self):
        print("You can Call")
    
    def message(self):
        print("You can message")


class Samsung(Phone):

    def photo(self):
        print("You can take photo")


s1 = Samsung()
s1.photo()
s1.message()
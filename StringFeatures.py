
class StringFeatures:
    
    def __init__(self, text) -> None:
        self.text = text

    def string_len(self):
        print(len(self.text))

    def subset(self):
        my_string = 'Hellow World'
        print(my_string[4]) # characters at position 4
        print(my_string[1:5]) # from position 1 to 5
        print(my_string[:5]) # from start to position 5
        print(my_string[2:]) # from position 2 to the end
    
    def repeat_strings(self):
        print('*' * 10)
        print('Hi' * 10)

    def split_strings(self):
        title = 'The Good, the Bad, and the Ugly'
        print('Source string:', title)
        print('Split using a space:')
        print(title.split(' '))
        print('Split using a comma')
        print(title.split(','))

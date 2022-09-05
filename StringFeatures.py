
class StringFeatures:
    
    def __init__(self, text) -> None:
        self.text = text

    def stringLen(self):
        print(len(self.text))

    def subset(self):
        my_string = 'Hellow World'
        print(my_string[4]) # characters at position 4
        print(my_string[1:5]) # from position 1 to 5
        print(my_string[:5]) # from start to position 5
        print(my_string[2:]) # from position 2 to the end
    
    def repeatStrings(self):
        print('*' * 10)
        print('Hi' * 10)

    def splitStrings(self):
        title = 'The Good, the Bad, and the Ugly'
        print('Source string:', title)
        print('Split using a space:')
        print(title.split(' '))
        print('Split using a comma')
        print(title.split(','))

    def countStrings(self):
        my_string = 'Count, the number    of spaces'
        print("my_string.count(' '):", my_string.count(' '))

    def replaceStrings(self):
        welcome_message = 'Hello World!'
        print(welcome_message.replace("Hello", "Goodbye"))
    
    def findSubstrings(self):
        print('Edward Alun Rawlings'.find('Alun'))

    def convertToString(self):
        msg = 'Hello Lloyd you are' + str(21)
        print(msg)

    def otherFunctions(self):
        some_string = 'Hello World'
        print('some_string.swapcase()', some_string.swapcase())
        print('String leading, trailing spaces',"   xyz   ".strip())


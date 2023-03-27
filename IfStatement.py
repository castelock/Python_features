class IfStatement:

    def __init__(self) -> None:
        pass

    def working_if(self):
        num = int(input('Enter a number:'))
        if num>0:
            print(num, 'is positive')
            print(num, 'squared is', num*num)
        
        print('Bye')

    def use_elif(self):
        savings = int(input('Enter the savings:'))
        if savings == 0:
            print("Sorry no savings")
        elif savings < 500:
            print('well done')
        elif savings < 1000:
            print('That is a tidy sum')
        elif savings < 10000:
            print('Welcome Sir!')
        else:
            print('Thank you')


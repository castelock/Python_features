count = 0
print('Starting')
while count < 10:
    # The end parameter is because the method print add a newline after every statement by default.
    # If you want to continue writing in the same line you have to use the parameter end.
    print(count, ' ', end ='')
    count += 1
print()
print('Done')
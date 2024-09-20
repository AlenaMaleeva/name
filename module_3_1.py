calls = 0
def count_calls ():
    global calls
    if  count_calls:
        calls += 1
        return calls
count_calls()
calls = count_calls()
def string_info(*args):
    for word in args:
        print(len(word), word.lower(), word.upper(), end= " ")

count_calls()
def is_contains(*args: list):
    args = ['UrbaN', 'URBAN']
    for list1 in args:
        if list1.lower():
            print(True)
            break
        else:
            print(False)
count_calls()


print (string_info('Баракуда'))
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)










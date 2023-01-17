# A program to repeat a user inputed phrase

def main():
    user_phrase = input('Input your phrase: ')
    times_to_repeat = int(input('How many times should it be repeated? '))

    for i in range(times_to_repeat):
        print(f'{i+1} {user_phrase}')

main()
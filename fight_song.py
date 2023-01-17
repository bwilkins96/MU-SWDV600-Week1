# A program to print a fight song

def sing_intro():
    print('Go, team, go!')
    print('Defeat your foe.')

def sing_section():
    sing_intro()

    print('Simply the best,')
    print('Better than the rest.')

    sing_intro()

def sing_body():
    print()

    for i in range(2):
        sing_section()
        print()

def sing_fight_song():
    sing_intro()
    sing_body()
    sing_intro()

sing_fight_song()
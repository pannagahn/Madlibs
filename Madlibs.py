from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('MadLibs')
Label(root, text='LET\'S PLAY MADLIBS', font='arial 20 bold').pack()
Label(root, text='Choose a topic :', font='arial 15 bold').place(x=60, y=80)


def madlib1():
    toys = input('Enter a Toy : ')
    musical_instrument = input('Enter a Musical Instrument : ')
    noun1 = input('Enter a Noun :')
    dessert = input('Enter a dessert : ')
    snacks = input('Enter a Snack : ')
    verb3 = input('Enter a Verb : ')
    animal = input('Enter an animal : ')
    noun2 = input('Enter a Noun : ')
    number = input('Enter a number : ')
    noun3 = input('Enter a Noun : ')
    number1 = input('Enter a number : ')
    number2 = input('Enter a number : ')
    vehicle = input('Enter a vehicle : ')
    animal1 = input('Enter an animal : ')

    print('If I was principal of my school, I would put ' + toys + ' and ' + musical_instrument + ' in every ' + noun1 + 'and have the cafeteria serve ' + dessert + ' and ' + snacks + ' for lunch. We would have ' + verb3 + ' everyday, where students can bring ' + animal + ' and ' + noun2 + ' to share in class. Students would give teachers homework, like ' + number + ' page book reports about ' + noun3 + ' and ' + number1 + ' math problems. Recess would last for ' + number2 + ' hours, instead of buses, I would have ' + vehicle + ' and ' + animal1 + ' take the kids to and from school.')


def madlib2():
    noun = input('Enter a noun: ')
    plural_noun1 = input('Enter a Plural noun: ')
    verb1 = input('Enter a Verb in Present Tense: ')
    verb2 = input('Enter a Verb in Present Tense: ')
    part_of_body = input('Enter a Part of Body(Plural): ')
    adjective1 = input('Enter an adjective: ')
    plural_noun2 = input('Enter a Plural noun: ')
    adjective2 = input('Enter an Adjective: ')

    print('Today, every student has a computer small enough to fit into his ' + noun + '. He can solve any math problem by simply pushing the computers little ' + plural_noun1 + '. Compiters can add, multiply, divide and ' + verb1 + '. They can also ' + verb2 + ' better than a human. Some computers are ' + part_of_body + '. Others have a/an ' + adjective1 + ' screen that shows all kinds of ' + plural_noun2 + ' and ' + adjective2 + ' figures.')


Button(root, text='If I were a principal', font='arial 15', command=madlib1, bg='ghost white').place(x=60, y=140)
Button(root, text='The Computer', font='arial 15', command=madlib2, bg='ghost white').place(x=60, y=200)

root.mainloop()

def smails(x):
    with open('smails.txt', 'r') as sm:
        smail = sm.read()
    print(x.translate({ord(i): None for i in smail}))

smails('Привет🙅‍')
print('Привет👋')
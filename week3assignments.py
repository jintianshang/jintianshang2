import random

r = random.randint(1, 9)

messages1 = ['Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
messages2 = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',]

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

fortune = getAnswer(r)

def secondtime():
    messages = messages1 + messages2
    print(messages[random.randint(0, len(messages) - 1)])


print(fortune)
print(secondtime())
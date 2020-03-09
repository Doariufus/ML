import os


def sort(path, file_name):
    os.chdir(path)
    try:
        os.mkdir('spam')
        os.mkdir('ham')
    except OSError:
        pass
    else:
        pass
    file = open(file_name, 'r')
    ham_i = 0
    spam_i = 0
    for line in file:
        if line[0:3] == 'ham':
            ham_i += 1
            ham_file = open('./ham/' + str(ham_i) + '.txt', 'w')
            ham_file.write(line[4:])
        elif line[0:4] == 'spam':
            spam_i += 1
            spam_file = open('./spam/' + str(spam_i) + '.txt', 'w')
            spam_file.write(line[5:])




print(sort('/home/doa/PycharmProjects/lab1_1/SpamSMS', 'SMSSpamCollection.txt'))

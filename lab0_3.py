import os


def filesLength(path):
    os.chdir(path)
    file = open('./ham/' + str(1) + '.txt', 'r')
    max_len = min_len = len(file.read())
    sum_len = 0
    ham_i = 0
    spam_i = 0

    while True:
        ham_i += 1
        try:
            file = open('./ham/' + str(ham_i) + '.txt', 'r')
        except OSError:
            ham_i -= 1
            break
        else:
            file_len = len(file.read())
            if file_len > max_len:
                max_len = file_len
            if file_len < min_len:
                min_len = file_len
            sum_len += file_len

    while True:
        spam_i += 1
        try:
            file = open(os.path.join('./spam/', str(spam_i) + '.txt'), 'r')
        except OSError:
            spam_i -= 1
            break
        else:
            file_len = len(file.read())
            if file_len > max_len:
                max_len = file_len
            if file_len < min_len:
                min_len = file_len
            sum_len += file_len

    av_len = sum_len / (ham_i + spam_i)
    return (max_len, min_len, av_len)


print(filesLength(('/home/doa/PycharmProjects/lab1_1/SpamSMS')))


def symbols(path):
    os.chdir(path)
    ham_i = 0
    spam_i = 0
    symbol_counter = {}
    while True:
        ham_i += 1
        try:
            file = open('./ham/' + str(ham_i) + '.txt', 'r')
        except OSError:
            ham_i -= 1
            break
        else:
            while True:
                symbol = file.read(1)
                if symbol == '':
                    break
                try:
                    symbol_counter[symbol] += 1
                except KeyError:
                    symbol_counter[symbol] = 1
    while True:
        spam_i += 1
        try:
            file = open('./spam/' + str(spam_i) + '.txt', 'r')
        except OSError:
            spam_i -= 1
            break
        else:
            while True:
                symbol = file.read(1)
                if symbol == '':
                    break
                try:
                    symbol_counter[symbol] += 1
                except KeyError:
                    symbol_counter[symbol] = 1
    symbols_list = list(symbol_counter.items())
    symbols_list.sort(key=lambda i: i[1], reverse=True)
    return symbols_list


print(symbols('/home/doa/PycharmProjects/lab1_1/SpamSMS'))


def popular_words(path):
    os.chdir(path)
    ham_i = 0
    spam_i = 0
    marks = ('.', ',', ':', ';', '?', '!',)
    words_counter = {}
    while True:
        ham_i += 1
        try:
            file = open('./ham/' + str(ham_i) + '.txt', 'r')
        except OSError:
            ham_i -= 1
            break
        else:
            s = file.read()
            sss = []
            ss = s.split()
            for j in range(0, len(marks)):
                for i in range(0, len(ss)):
                    sss.append(ss[i].split(marks[j], 1)[0])
                ss.clear()
                ss = sss.copy()
                sss.clear()

            for i in range(0, len(ss)):
                try:
                    words_counter[ss[i]] += 1
                except KeyError:
                    words_counter[ss[i]] = 1

    while True:
        spam_i += 1
        try:
            file = open('./spam/' + str(spam_i) + '.txt', 'r')
        except OSError:
            ham_i -= 1
            break
        else:
            s = file.read()
            sss = []
            ss = s.split()
            for j in range(0, len(marks)):
                for i in range(0, len(ss)):
                    sss.append(ss[i].split(marks[j], 1)[0])
                ss.clear()
                ss = sss.copy()
                sss.clear()

            for i in range(0, len(ss)):
                try:
                    words_counter[ss[i]] += 1
                except KeyError:
                    words_counter[ss[i]] = 1

    words_list = list(words_counter.items())
    words_list.sort(key=lambda i: i[1], reverse=True)
    return words_list


print(popular_words('/home/doa/PycharmProjects/lab1_1/SpamSMS'))


import keras
from keras.models import Sequential
model = Sequential()
model.fit()
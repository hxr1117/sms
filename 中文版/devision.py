from sklearn.model_selection import train_test_split
import string
from calculation import Calculation
from verdict import Verdict
import codecs


# 英文标点过滤器
def en_filter(s):
    trantab = str.maketrans({key: None for key in string.punctuation})
    return s.translate(trantab)


def division():
    f = codecs.open('sms.txt', 'r', 'utf-8')
    lines = f.readlines()
    trains, tests = train_test_split(lines, test_size=1 / 4, random_state=0)
    # for i in range(len(tests)):
    #     tests[i] = tests[i].split('\t', 1)
    return trains, tests


def train():
    trains = division()[0]
    print(len(trains))
    cal = Calculation()
    cal.reading_sms_and_calculation(trains)


def test():
    tests = division()[1]
    v = Verdict()
    cal = 0
    spam = 0
    ham = 0
    for i in tests:
        if i[0] == 'spam':
            spam += 1
            if v.is_spam(i[1]) is True:
                cal += 1
        elif i[0] == 'ham':
            ham += 1
            if v.is_spam(i[1]) is False:
                cal += 1
        # print(i[0])
        # print(v.is_spam(i[1]))
    print(len(tests), cal, spam, ham, cal/len(tests))

train()
test()
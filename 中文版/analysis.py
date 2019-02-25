import jieba
import codecs
import string


def division(lines):
    # f = codecs.open('sms.txt', 'r', 'utf-8')
    # lines = f.readlines(30)
    for i in range(len(lines)):
        lines[i] = list(jieba.cut(lines[i], cut_all=True))
        while '' in lines[i]:
            lines[i].remove('')  # delete empty string
        lines[i] = lines[i][:-1]  # delete \n
        return lines[i]

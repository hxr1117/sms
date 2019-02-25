# 分词，分别计算每个词出现在spam和ham里的概率
import numpy as np
np.set_printoptions(suppress=True)
import codecs


class Calculation(object):
    def __init__(self):
        self.words_rate = {}
        self.train_num = 0
        self.ham_num = 0
        self.spam_num = 0

    # 读取短信数据集,将垃圾短信和有效短信分类
    # lines是已被划分的中文短信
    def reading_sms_and_calculation(self, lines):
        ham = []
        spam = []
        # from analysis import division
        # lines = division()
        self.train_num = len(lines)
        for i in range(len(lines)):
            if lines[i][0] == '0':
                ham.append(lines[i][1:-2])
            elif lines[i][0] == '1':
                spam.append(lines[i][1:-2])
            else:
                continue
        self.ham_num = len(ham)
        self.spam_num = len(spam)

        self.calculating_ham(ham)
        self.calculating_spam(spam)
        self.writing_num()
        self.words_calculating()

    def words_calculating(self):
        f = codecs.open('data/en_words_rate', 'w', 'utf-8')
        f.write(str(self.words_rate))
        f.close()

    # 计算每个词在有效短信中的概率
    def calculating_ham(self, ham_list):
        ham_rate = {}
        for i in range(len(ham_list)):
            ham_list[i] = list(set(ham_list[i]))  # 单词去重
            for j in ham_list[i]:
                if j in ham_rate:
                    ham_rate[j] += 1  # 记录该单词出现在有效短信的条数。如果一个单词出现多次则忽略
                else:
                    ham_rate[j] = 1
                self.rates(j)

        # 将概率写进文件
        f = codecs.open('data/en_ham_rate', 'w', 'utf-8')
        f.write(str(ham_rate))
        f.close()
        return ham_rate

    # 计算每个词在垃圾短信中的概率
    def calculating_spam(self, spam_list):
        spam_rate = {}
        for i in range(len(spam_list)):
            spam_list[i] = list(set(spam_list[i]))  # 单词去重
            for j in spam_list[i]:
                if j in spam_rate:
                    spam_rate[j] += 1
                else:
                    spam_rate[j] = 1
                self.rates(j)
        # 将出现次数写进文件
        f = codecs.open('data/en_spam_rate', 'w', 'utf-8')
        f.write(str(spam_rate))
        f.close()
        return spam_rate

    def rates(self, word):
        # self.words_rate
        if word in self.words_rate:
            self.words_rate[word] += 1
        else:
            self.words_rate[word] = 1

    def writing_num(self):
        f = codecs.open('data/num', 'w', 'utf-8')
        f.write(str(self.ham_num)+'\n')
        f.write(str(self.spam_num)+'\n')
        f.write(str(self.train_num)+'\n')
        f.close()




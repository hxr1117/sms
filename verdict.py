class Verdict(object):  # 判断是否是垃圾短信
    def __init__(self):
        self.read_data()

    def is_spam(self, sms):
        from filter import en_filter
        sms = sms.lower()
        sms = en_filter(sms).split()
        ham_possibility = spam_possibility = 1.0
        for i in sms:
            ham_possibility *= self.calculating_ham_possibility(i)
            spam_possibility *= self.calculating_spam_possibility(i)
        print(ham_possibility, '%f' % spam_possibility)
        return ham_possibility < spam_possibility

    # 读数据
    def read_data(self):
        f = open('data/en_ham_rate', 'r')
        self.ham = eval(f.readline())  # 单词次数字典
        self.ham_num = sum(self.ham[i] for i in self.ham.keys())
        f = open('data/en_spam_rate', 'r')
        self.spam = eval(f.readline())
        self.spam_num = sum(self.spam[i] for i in self.spam.keys())
        f = open('data/en_words_rate', 'r')
        self.words = eval(f.readline())
        # self.words_num = sum(self.words[i] for i in self.words.keys())
        # print(self.ham_num, self.spam_num, self.words_num)
        f = open('data/num', 'r')
        self.ham_num, self.spam_num, self.train_num = [int(i) for i in f.readlines()]
        f.close()

    def calculating_ham_possibility(self, word):
        if word in self.words:
            w = self.words[word]
            # print('ham', w)
        else:
            w = 1
        if word in self.ham:
            h = self.ham[word]
        else:
            h = 1
        # result = (w/self.words_num) * ((self.ham_num + 1) / (self.ham_num + self.spam_num + 1)) / (w / (self.ham_num + self.spam_num + 1))
        result = (h/self.ham_num)*((self.ham_num+1)/(self.train_num+1))/(w/self.train_num)
        # print(result)
        return result

    def calculating_spam_possibility(self, word):
        if word in self.words:
            w = self.words[word]
            # print('spam', w)
        else:
            w = 1
        if word in self.spam:
            s = self.spam[word]
        else:
            s = 1
        # result = (w/self.words_num) * ((self.spam_num + 1) / (self.ham_num + self.spam_num + 1)) / (w / (self.ham_num + self.spam_num + 1))
        result = (s / self.spam_num) * ((self.spam_num + 1) / (self.train_num + 1)) / (
                    w / self.train_num)
        # print(result)
        return result


from sklearn.model_selection import train_test_split
import codecs
from filter import en_filter
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


# 讲数据分成结果和数据
def devide_to_x_and_y():
    f = codecs.open('英文垃圾短信数据集/SMSSpamCollection', 'r', 'utf-8')
    lines = f.readlines()
    x = []
    y = []
    for i in lines:
        # print(i.split('\t'))
        x.append(en_filter(i.split('\t', 2)[1]))
        if i.split('\t', 2)[0] == 'ham':
            y.append(0)
        else:
            y.append(1)
    return x, y


# 将x,y分成训练数据和测试数据
def devide_to_train_and_test(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    # print(x_train, x_test)
    return x_train, x_test, y_train, y_test


def vectorizer(x):
    # https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction
    # 统计词语出现次数
    count_vect = CountVectorizer()
    x_counts = count_vect.fit_transform(x_train)
    # 使用tf-idf提取文本特征
    transformer = TfidfTransformer()
    x_tfidf = transformer.fit_transform(x_counts)
    return x_tfidf


if __name__ == '__main__':
    x, y = devide_to_x_and_y()
    x_train, x_test, y_train, y_test = devide_to_train_and_test(x, y)
    x_train_tfidf = vectorizer(x_train)
    x_test_tfidf = vectorizer(x_test)
    # multinomialNB
    clf = MultinomialNB().fit(x_train_tfidf, y_train)
    predicted = clf.predict(x_test_tfidf)
    count = 0
    for i, j in zip(y_test, predicted):
        if i == j:
            count += 1
    print(count/len(y_test))
    #
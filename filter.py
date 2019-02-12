# 英文标点过滤器
import string


def en_filter(s):
    trantab = str.maketrans({key: None for key in string.punctuation})
    return s.translate(trantab)
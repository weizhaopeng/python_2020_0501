import re
from re import compile, match


def main():
    reComplie = compile("a.b")

    string1 = 'a_ba4ba3cakdhkbkjsdka8ba b'
    regexReturn = match(r'a.b', string1)
    if regexReturn is not None:
        print(regexReturn.groups())

    # verify the username and qq in effect
    # username = input("please input username")
    # qq = input("please input the qq number")
    # 表示从开头和结尾是6-20位的字母数字或者下划线
    # m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    # if not m1:
    #     print("please reinput the username")
    # 表示从头到尾是4-11位的数字
    # m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    # if not m2:
    #     print("please reinput the qq number")
    # if m1 and m2:
    #     print("input in effect")

    # extract the phone number of China from a text
    # XXX 表示已1开头第二位是34578并且后面有9位
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，\
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。'''
    # findall这个函数是从文本中找出所有满足规则的字符串以列表的形式存储在mylist下
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print("******************")
    # get the match content with iterator
    # 可见编译的正则表达式可以通过finditer+字符串生成可迭代对象其中存储的就是匹配的对象
    # 也是一种实现方法
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('******************')
    # 编译后的正则表达式好像是一个正则表达式re类的对象，其中存储了过滤规则，能够执行re的所有的类方法
    # search方法就是找出所有符合要求的子串并存储为re.Match对象
    # 其实re.search也是先将匹配规则编译实例化出Pattern对象，然后调用其search方法
    m = pattern.search(sentence)
    while m:
        print(m.group())
        # end函数的作用:返回正则表达式中的组匹配的子字符串在原字符串中的结束位置，默认值为0示例：
        # 这里m.end()指定了匹配开始的位置，就是上个子串的结束后的位置
        # 因为search方法是发现第一个子串，m存储的是关于第一个子串的数据，那么m.end()是子串的结束位置后一位，m.start()应该是
        # 子串第一个字符开始的地方
        print(m.end())
        print(m.start())
        m = pattern.search(sentence, m.end())

    # 替换字符串中的不良内容
    sentence = "你丫是傻逼吗，我叼你妈的，fuck you, cnm"
    # sub函数是将匹配的单词（字）替换成响应的字符，同时忽略不匹配的内容
    # 注意：不能使用原始字符串这里并没有正则表达式范式，而是通过|来并且表示替换的内容
    purified = re.sub('操|叼|艹|fuck|shit|傻|逼|丫|妈|cnm', '*', sentence, flags=re.IGNORECASE)
    print(purified)

    # 拆分长字符串
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    # split函数就是通过给定了断开的字符，字符串，然后将其去除，把长字符串断开，如果最后也有字符，会出现空字符串
    sentence_list = re.split(r'[，。,.]', poem)
    print(sentence_list)
    # 去除空字符串的方法
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)
    

if __name__ == '__main__':
    main()

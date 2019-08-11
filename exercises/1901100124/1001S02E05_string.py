text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly. 
Explicit is better than implicit.
Simple is better than complex. 
Complex is better than complicated.
Flat is better than nested. 
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced. 
In the face of ambxiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!
'''

text=text.replace('better','worse')
#print('将字符串的better全部替换成worse',text)#括号里面的,前面要有说明
print(text)


words=text.split()
new=[]
for word in words:
    if word.find('ea')<0:
        new.append(word)
        print('剔除掉ea的text',new)


#题2[]生成的是列表，用列表推导式：[x for x in iterable]
swapcased=[i.swapcase() for i in new]
print('大小写翻转',swapcased)#跟第一题的格式相同，由于swapcase是放回字符串的副本，同时new是返回列表，于是使用列表推导式

print('顺序排序',sorted(swapcased))
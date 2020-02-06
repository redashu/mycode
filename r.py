import time
import matplotlib.pyplot as plt
x="""
hi  my name is hi and i am doing grt  hi name is my
ok cool hello world  hello hi my name is
"""
# str  to list
print(x)
time.sleep(3)
y=x.split()
words=[]
c=[]
for  i in  y:
	if i in words:
		continue 
	else :
		cc=y.count(i)
		words.append(i)
		c.append(cc)

print(words)
print(c)
plt.xlabel("words")
plt.ylabel("count")
plt.pie(c,labels=words,autopct='%1.1f%%',shadow=True)
plt.show()














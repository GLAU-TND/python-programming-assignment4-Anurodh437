s=input()
s1=eval(input())
ls1=[]
for i in s1:
	if i.startswith(s):
		ls1.append(i)
print(ls1)
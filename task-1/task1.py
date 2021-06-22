import re
nums=[]
s=input("Введіть рядок:")
numm=re.findall(r'\d+', s)
s=re.sub(r"\d+", "",s,flags=re. UNICODE)
numm=[int(i) for i in numm]
print("слова:", s, sep='')
print("числа:", numm, sep=''/n)

l=[]
l1, l2= l1.title(), ""
for i in l1.split():
	l3 += i[:1]+i[-1].upper() + ""
	l.append(l2[:-1])
print("Велика літера:", l[-1])

print("Найбільше число:",max(numm))
max_num=numm.index(max(numm))

i=0
for i in range(len(numm))
	if i==max_numm:
		continue
	a = numm[i] ** i
	nums.append(a)
print("Числа піднесені до степеня", nums)
	

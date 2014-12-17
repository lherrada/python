from math import sqrt 

pp=2
ep=[pp]
pp+=1
tp=[pp]
ss=[2]
lim=raw_input("\nGenerate prime numbers up to what number? : ")
while pp<int(lim):
	pp+=ss[0]
	test=True
	sqrtpp=sqrt(pp)
	for a in tp:
		if a>sqrtpp: break
		if pp%a==0:
                              test=False
                              break
	if test: tp.append(pp)

ep.reverse()
[tp.insert(0,a) for a in ep]

print tp

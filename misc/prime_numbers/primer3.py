pp=2
ps=[pp]
pp+=1
ps.append(pp)
lim=raw_input("\nGenerate prime numbers up to what number? : ")
while pp<int(lim):
	pp+=2
	test=True
	for a in ps:
		if pp%a==0:
                   test=False
                   break
		if test: ps.append(pp)

print ps

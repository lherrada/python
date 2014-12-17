pp = 2
ps = [pp]
lim = raw_input("\nGenerate prime numbers up to what number? : ")
while pp < int(lim):
   pp += 1
   for a in ps:
      if pp%a==0:
         break
      else:
         if pp not in ps:
            ps.append(pp)
print ps

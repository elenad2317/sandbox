import hyperloglog 

p = .1

h1 = hyperloglog.HyperLogLog(p)
h2 = hyperloglog.HyperLogLog(p)

for i in range(100): 
    h1.add(i)

for j in range(50, 150):
    h2.add(j)

l1 = h1.intersection(h2)
l2 = h2.intersection(h1)

print "Test 1: ", l1 < 100*(1+p) and l1 > 100*(1-p)
print "Test 2: ", l2 < 100*(1+p) and l2 > 100*(1-p)

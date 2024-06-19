s = "Hi*There*im*you#Kaus*i*Work#in*BY"
l= s.split("*")
for i in l:
    if "#" in i:
        z = i.split("#")
        # l[l.index(i):len(z)] = z
        l.insert(l.index(i),z)
        l.remove(i)
print(l)

s1= [9,2,[8,1,1],8]
a1 = s1.pop(2)
print(a1.pop(1))
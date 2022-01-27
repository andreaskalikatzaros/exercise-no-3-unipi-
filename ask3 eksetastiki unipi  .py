words=[]
k=[]
p=[]
max=0
with open("two_cities_ascii.txt", "r") as f:
    for line in f:
        words.extend(line.split())
for i in range(len(words)):
    a=words[i]
    if a.isalpha():
        k.append(a)
k = [x for x in k if len(x) != 19]
print(k)
for i in range (len(k)):
    if len(k[i])>max:
        max=len(k[i])
for i in range (max+1):
    p.append(0)
print(len(k))
for i in range (len(k)):
    e=k[i]
    o=len(e)
    p[o]=p[o]+1
print("h megalyterh leksi poy yparxei exei ",max+1,"grammata") 
for i in range (len(p)):
     print(i+1)
     print("grammata exoyn ",p[i],"lekseis")
words=[]
k=[]
p=[]
max=0
b=0
y=[]
with open("two_cities_ascii.txt", "r") as f:
    for line in f:
        words.extend(line.split())
for i in range(len(words)):   
     b=words[i]
     if b.isalpha():
        k.append(b)
for i in range(len(k)):
    q=i+1 
    if k[i]!="del" :
     for q in range(len(k)):
         if k[q]!="del":
          if (len(k[i])+len(k[q])==20):
            k[i]="del"
            k[q]="del"                     
k = [x for x in k if x!="del"]
for i in range (len(k)):
    if len(k[i])>max:
        max=len(k[i])
for i in range (max+1):
    p.append(0)
for i in range (len(k)):
    e=k[i]
    o=len(e)
    p[o]=p[o]+1
print("h megalyterh leksi poy yparxei exei ",max,"grammata") 
for i in range (len(p)):
     print(i)
     print("grammata exoyn ",p[i],"lekseis")

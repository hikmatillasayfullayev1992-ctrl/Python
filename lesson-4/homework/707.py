yil=int(input("Yilni kiriting "))
if yil%4==0:
    if yil%100==0 and yil%400!=0:
        print(f"Siz tanlagan {yil} yil kabisa yili emas")
    else:
        print(f"Siz tanlagan {yil} yil kabisa yili hisoblanadi")
else:
    print(f"Siz tanlagan {yil} yil kabisa yili emas")

## 1. Sort a Dictionary by Value
ls={'a':1,'b':2,'e':5,'d':4}
ls2=dict(sorted(ls.items(),key=lambda item: item[1]))
ls2=dict(sorted(ls.items(),key=lambda item: item[1], reverse=True))
print(ls2)
## 2. Add a Key to a Dictionary
ls={0: 10, 1: 20}
ls['2']=30
print(ls)
## 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1={**dic1,**dic2,**dic3}
print(dic1)
## 4. Generate a Dictionary with Squares
n=5
dic1 = {}
for i in range(1,n+1):
    dic1[i]=i**2
print(dic1)
## 5. Dictionary of Squares (1 to 15)
dic1 = {}
for i in range(1,16):
    dic1[i]=i**2
print(dic1)
### Set Exercises
## 1. Create a Set
a=[1,2,3,5,5,'asd']
b=set(a)
## 2. Iterate Over a Set
b={1,2,3,5,5,'asd'}
for i in b:
    print(i)
## 3. Add Member(s) to a Set
b={1,2,3,5,5,'asd'}
b.add(7)
print(b)

## 4. Remove Item(s) from a Set
a={1,2,3,5,5,'asd'}
a.remove(3)
print(a)

## Remove an Item if Present in the Set
a={1,2,3,5,5,'asd'}
try:
    a.remove(1)
except: Exception
print(a)

## 1 age kalkulyator
a=input("Ismingizni kiriting: ")
b=input("Tug`ilgan yilizni kiriting: ")
print(f"{a} sizning yoshingiz {2025-int(b)}da")
  ## 2. Extract Car Names
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])
## 3. Extract Car Names
txt = 'MsaatmiazD'
print(txt[::2])
print(txt[::-2])
### 4. Extract Residence Area
txt = "I'am John. I am from London"
print(txt[21:])
##### 5. Reverse String
a=input("So`z kiriting: ")
print(a[::-1])
## 6. Count Vowels
a="qwertyuiopasdfghjklzxcvbnm"
b=a.count("a")+a.count("o")+a.count("i")+a.count("e")+a.count("a")+a.count("u")                                                               
print(b)
## 7. Find Maximum Value
a=list(input(" Sonlarni kiriting "))
a.sort()
print(a[-1])
#### 8. Check Palindrome
a=input(" So`z kiriting ")
b=a[::-1]
print(a==b)
### 9. Extract Email Domain
a=input(" Elektron adres kiriting ")
b=a.index("@")
print(a[b:])
## 10. Generate Random Password
import random
alf=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
raq=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
cc=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
a=random.randint(5,12)
parol=""
while len(parol)<a:
    b=random.randint(0,len(alf)-1)
    c=random.randint(1,3)
    if c==1:
        parol=parol+alf[b]
    if c==2 and b<len(raq):
        parol=parol+raq[b]
    if c==3 and b<len(cc):
        parol=parol+cc[b]
print(parol)

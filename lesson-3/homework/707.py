## 1 . Create and Access List Elements
ls=['apple','peach','banana','grapes','anor']
print([2])

## 2. Concatenate Two Lists
ls1=[1,2,3,4,5,6]
ls2=[9,8,7,6,5,4]
ls3=ls1+ls2
print(ls3)

## 3. Extract Elements from a List
ls=[1,2,3,4,5,6,7]
nls=[]
nls.append(ls[0])
nls.append(ls[len(ls)//2])
nls.append(ls[-1])
print(nls)

## 4. Convert List to Tuple
ls=['ali','vali','dog','home','kino']
tup=tuple(ls)
print(tup)

## 5. Check Element in a List
ls=['Paris','London','Moscow','Tashkent']
if 'Paris' in ls:
    print('bor')
else:
    prinr('yoq')

## 6. Duplicate a List Without Using Loops
ls=[1,2,3,4]
ls2=ls*2
ls2=ls.copy()
print(ls2)

## 7. Swap First and Last Elements of a List
ls=[1,2,3,4]
ls[0],ls[-1]=ls[-1],ls[0]
print(ls)

## 8. Slice a Tuple
ls=(1,2,3,4,5,6,7,8,9,10)
print(ls[3:7])

## 9. Count Occurrences in a List
ls=('blue','red','yellow','blue')
cnt=ls.count('blue')
print(cnt)

## 10. Find the Index of an Element in a Tuple
ls=('blue','red','lion','blue')
print(ls.index('lion'))

## 11. Merge Two Tuples
ls=(1,2,3,4,5)
ls2=(7,8,9)
ls=ls+ls2
print(ls)

## 12. Find the Length of a List and Tuple
ls=(1,2,3,4,5)
ls2=[7,8,9]
print(len(ls),len(ls2))

## 13. Convert Tuple to List
ls=(1,2,3,4,5)
ls3=list(ls)
print(ls3)

## 14. Find Maximum and Minimum in a Tuple
ls=(8,1,2,7,3,4,5)
ls2=sorted(ls)
print(ls2[0],ls2[-1])

## 15. Reverse a Tuple
ls=('d','asdfg','ert','fghd','qwerty')
ls2=sorted(ls)
for j in range(1,len(ls)+1):
    print(ls[-1*j])
ls3=tuple(reversed(ls))
print(ls3)

numpy - numerical python
bu 'c' tilida yozilgan, hsuni uchun c tili qoidalariga rioya qiladi va pitondan 100 marta tez ishliydi  

ls=[1,2,3,4]
arr=np.array(ls)
print(ls)
print(arr)

b=arr**4    o`zgaruvchiga tenglashtirilsa spiskaga qaytadi
print(b)
  ndim    - number of dimensiom - o`lchamlar soni
ls2=[[1,2,3],[4,5,6]]
arr2=np.array(ls2)

arr2.size     - elementlar sonini ko`rsatadi 

arr2.nbytes    - hotirada eggalagan joyini ko`rsatadi

arr2.dtype - eggalagan joyidan kep chiqip taypini ko`rsatadi   sgu chiqadi >>>  dtype('int64')

  arr=arr.astype('int8')  --- ma'lumotti hotirada eggalaydigan joyini boshqarsa bo`ladi har bir element uchun qiladi

arr+100     har bir elementga 100 qo`shib chiqadi

arr4=np.arange(1,100,1)    - 1 dan 100 uacha 1 qadamdan iborat array qib beradi

arr4>50       - bunda shart bajarilsa True, bumasa False bo`lgan 1 dan 100 gacha array chiqadiarr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr1+arr2

arr4=np.arange(1,100,1)
filter1=arr4>50                  - agar filter qilinsa 50 dan kotta sonlardan iborat array chiqadi
arr4[filter1]

arr4=np.arange(1,100,1)
filter1=arr4%2==0              - juft sonlani chiqaradi
arr4[filter1]

filter1= arr4 <76
filter2= arr4 >37
filter3=filter1 & filter2    - ikkita filterri qo`shish uchun 
arr4[filter3]

filter3= (arr4 <76) & (arr4 >37)  -  ikkita filterri ishlatish uchun qavsda va & belgisi bilan qilinadi

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr1+arr2                       -    elementlar soni bur xil bo`lishi shart, elementlarni bir biriga qo`shadi      >>> array([ 6,  8, 10, 12])   chiqadi

ls5=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
arr5=np.array(ls5)
arr5[0][1][2]     bu    arr5[0,1,1]      bilan bir hil

arr5[0,0:2,1:]     intervalli chiqaradi

arr5[0:2,0,1:]   - birinchi vergulgacha == qaysi elementligi ko`rsatiladi, vergullar o`rtasidagi == qatorlar , ohirgi verguldan keyingisi qaysi ustun
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])

pip install pandas[excel]    ekzel bilan ishlash uchun shunaqa yozish kere

import pandas as pd
import numpy as np

ls=[1,2,3,4]
arr=np.array(ls)
ser=pd.Series(arr)
print(ls)
print(arr)
print(ser)
             >>>> [1, 2, 3, 4]
[1 2 3 4]
seriesniki 
0    1
1    2
2    3
3    4
dtype: int64          shunaqa chiqadi

df=pd.read_excel('examp.xlsx')
df

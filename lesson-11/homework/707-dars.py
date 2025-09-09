message="men pitonni o`rganyapman"
if __name__=="__main__":                  boshqa fayldan chaqirilsa tegidigi komanda u fayldan ishlamiydi
    print(message) 

__name__ qaysi piton faylda ishlavotgan busak usha faylli nomiga teng bo`ladi.
__main__ kod yozilip turgan faylni nomi

from datetime import date, time, datetime, timezone, timedelta
t=time()
sana=date(2025,8,30)         sanani ko`rsatadi
bugun=date.today()           bugungi sanani ko`rsatadi
print(bugun) 

start=datetime.fromtimestamp(0)    pitonda vaqt boshlangan vaqt
print(start)

1970-01-01 05:00:00   shu chiqadi

start=datetime.fromtimestamp(0)
tdy=datetime.now()
print(tdy-start)
20326 days, 15:48:05.871472          shu chiqadi

print(tdy.timestamp())         timestamp dan boshlab o`tgan sekundlar soni

timedel1=timedelta(weeks=2,days=3,hours=6)      vaqt oralig`i

tdy=datetime.now()
tdy_str=tdy.strftime("%d %B %Y")    sanani tekstga o`tkazishga
print(tdy_str)

san=datetime.strptime(tdy_str,"%d %B %Y")       tekstdan sanaga o`tkazadi

import pytz
local = datetime.now()
print("Tashkent",local)

tz_London=pytz.timezone("Europe/London")            Londonni vaqtini ko`rsatadi
London=datetime.now(tz_London)
print("London: ",London)

tz_new_york=pytz.timezone("America/New_york")
NewYork=datetime.now(tz_new_york)
print("New York: ",NewYork)

tz_japan=pytz.timezone("Asia/Tokyo")
japan=datetime.now(tz_japan)
print("Japan: ",japan)

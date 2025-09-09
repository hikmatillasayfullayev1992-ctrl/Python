students: 
        [
          {
              "id":1,                                doim ikkitali qo`shtirno ishlatiladi
              "name":"Alex",              key har doim string bo`ladi
              "Age":25
              "anilmals":["cat", "dog", "bird"]
              "scool_scores":{"math":70,"physics":85}
              "family_members":
                              [
                                {
                                  "name":"Josh",
                                  "Age":50,
                                  "Relative": "Father"
                                },
                                {
                                  "name": "Bob",
                                  "Age":45,
                                  "Relative":"Mather"
                                }
                              ]
            }
            {
                "id":1,                                doim ikkitali qo`shtirno ishlatiladi
                "name":"Alex",              key har doim string bo`ladi
                "Age":25
                "anilmals":["cat", "dog", "bird"]
                "scool_scores":{"math":70,"physics":85}
                "family_members":
                                [
                                  {
                                    "name":"Josh",
                                    "Age":50,
                                    "Relative": "Father"
                                  },
                                  {
                                    "name": "Bob",
                                    "Age":45,
                                    "Relative":"Mather"
                                  }
                                ]
              }
load - json file to python native type
loads - json format within str to python native

import json
with open("example.json") as f:
    data = f.read()                          json string qilib olib beradi
data2=json.loads(data)                       spiska, dictionary qib beradi
for i in data2["friends"]:
    if i["gender"]=="M":
        print(i["name"])

import json
with open("example.json") as f:
    data = json.load(f)                                  pryamo spiska qib beradi
data



import sqlite3                                                                                                    sql formatda tablisa yaratadi
connection=sqlite3.connect('my_database.sqlite')
cursor=connection.cursor()
create_query='''create table student (id int, name varchar(50),score int)'''                                  tablisa yaratadi
#cursor.execute(create_query)
insert_query='''insert into student values(1,'alex',89),(2,'john',100)'''                                    tablisaga ma'lumot joylaydi
cursor.execute(insert_query)
connection.commit()
cursor.close()
connection.close


import sqlite3
connection=sqlite3.connect('my_database.sqlite')
cursor=connection.cursor()
select_query='''select * from student'''                         tablisadigi ma'lumotlani op keladi
data=cursor.execute(select_query)
print(data.fetchall())
connection.commit()
cursor.close()
connection.close

import psycopg2


db = psycopg2.connect(dbname="#", user="#", password="#", host="127.0.0.1", port="5432")

con = db.cursor()
p_db = con

p_db.execute("create table post(id serial primary key,title text,text text);")
db.commit()

p_db.execute("insert into post (title,text) values ('A Home is Where Your Bot Lives','The truly smart home we’ve seen in sci-fi movies hasn’t arrived yet but its potential is huge and largely unfulfilled at the moment. While the future of Internet of Things probably not entirely arrived in our homes and we still don’t have fridges that order groceries the minute we run out of eggs and Greek yogurt, just be patient, thanks to the latest advancements in artificial intelligence and big data analytics, we are getting there.');")
p_db.execute("insert into post (title,text) values('Future of IoT And the Living in Smart Cities','But not only our homes or workplaces can be smart. How about whole cities designed to tackle traffic congestion, parking issues or even make our lifestyle greener.');")
p_db.execute("insert into post (title,text) values('Maybe You Can Drive My Smart Car?','By 2020 75% of all the cars around the world will be connected to the internet, and by 2025 100% of sold cars will be connected. But predictions don’t stop here. By 2020 the development of driverless cars is supposed to enter mass production.');")
p_db.execute("insert into post (title,text) values('Work Smarter, Not Harder','The main purpose of IoT in the workplace is to make the lives of workers more convenient and efficient. Artificial intelligence and advanced analytics can help create a more intelligent work environment.');")
db.commit()

p_db.execute("select * from post;")
posts  = con.fetchall()
for i in posts:
    print(i)

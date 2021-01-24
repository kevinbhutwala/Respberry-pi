import time
import paho.mqtt.client as mqtt
import sqlite3
import datetime

db = sqlite3.connect("external")
cur = db.cursor()

def on_message(client,userdata,msg):
    print(msg.topic+""+str(msg.payload)+"\n")
    decodeData = msg.payload.decode("utf-8")
    cur.execute("create table if not exists tblsubscribe(subID integer primary key autoincrement,msg text,created_dt current_timestamp)")
    sql = """insert into tblsubscribe(msg,created_dt) values(?,?)"""
    sql_data = (decodeData,datetime.datetime.now())
    cur.execute(sql,sql_data)
    db.commit()
    print(decodeData)
    
cur.execute("select * from tblsubscribe order by subID desc limit 10")
rows = cur.fetchall()
print("Data:")
for row in rows:
    print(row)
    time.sleep(1)
    
client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com",1883)
client.subscribe("bad",qos=0)
client.loop_forever()

from smbus import SMBus
import sqlite3
import datetime

db = sqlite3.connect("external")
cur = db.cursor()

#cur.execute("create table if not exists tbli2c(i2cID integer primary key autoincrement,message text,create_dt current_timestamp)")
#db.commit()
addr = 0x8
bus = SMBus(1)

num = 1

print("Enter 1 for ON or 0 for OFF")
while num == 1:
    ledstate = input(">>>>>    ")
    if ledstate == "1":
        bus.write_byte(addr,0x1)
        block = bus.read_byte_data(8,1)
        print(block)
        sql = """insert into tbli2c(message,create_dt) values(?,?);"""
        data_sql = (block,datetime.datetime.now())
        cur.execute(sql,data_sql)
        db.commit()
    elif ledstate == "0":
        bus.write(addr,0x0)
    else:
        num = 0
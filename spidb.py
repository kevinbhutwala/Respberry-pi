import spidev
import time
import datetime
import sqlite3

db = sqlite3.connect("external")
cur = db.cursor()

spi = spidev.SpiDev(0,0)
spi.open(0,0)
msg = 0xAA

spi.max_speed_hz = 115200
while 1:
    spi.writebytes([0x4,0x86])
    data = spi.readbytes(1)
    print(data)
    sql = """insert into tblspi(msg,created_dt) values(?,?);"""
    data_sql = (data,datetime.datetime.now())
    cur.execute(sql,data_sql)
    db.commit()
    time.sleep(1)
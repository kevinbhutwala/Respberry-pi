import sys
import adafruit_dht
import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN)

db = sqlite3.connect("external")
cur = db.cursor()

dhtDevice = adafruit_dht.DHT11(14)
while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9/5) + 32
        humidity = dhtDevice.humidity
        sql = """insert into tbldht(temp_c,temp_f,humidity,created_dt) values(?,?,?,?);"""
        data_sql = (temperature_c,temperature_f,humidity,datetime.datetime.now())
        cur.execute(sql,data_sql)
        db.commit()
        print("Temp: {:.1f} F/ {:.1f} C/ Humidity : {}%".format(temperature_f,temperature_c,humidity))
        time.sleep(1)
    except RuntimeError as error:
        print(error.args[0])
        
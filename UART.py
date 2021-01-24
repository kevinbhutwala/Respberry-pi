import serial
if __name__ == '__main__':
  ser = serial.Serial('dev/ttyACM0',9600,timeout= 1)#for cabled connection
  #ser = serial.Serial('dev/ttyS0',9600,timeout= 1)#for jumper wired connection
  ser.flush()
  while True:
    if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip()
      print(line)
      print("Arduino is Connected to Raspberry pi")

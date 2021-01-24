import paho.mqtt.publish as publish
import psutil
import sqlite3

db = sqlite3.connect("external")
cur = db.cursor()

cur.execute("select * from tblsubscribe")
rows = cur.fetchall()

channelID = "1288685" #change this channelID with your channelID
writeapiKey = "TK90L9OTLBQAH53H" #Change this write API Key with your write API Key
useUnsecuredTCP = False
useSSLWebsockets = True
mqttHost = "mqtt.thingspeak.com"

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':'/etc/ssl/certs/ca-certificates.crt','tls_version' : ssl.PROTOCOL_TLSv1}
    tPort = 443

topic = "channels/" + channelID + "/publish/" + writeapiKey
while(True):
    cpuPer = psutil.cpu_percent(interval=20)
    ramPer = psutil.virtual_memory().percent
    print("CPU= ",  cpuPer, " RAM: ", ramPer)
    for row in rows:
        tPayload = "field1=" + str(row[0])
        try:
            publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
        except (KeyboardInterrupt):
            break
        except:
            print("There was an error while publishing the data")
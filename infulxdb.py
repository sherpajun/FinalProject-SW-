#pip install influxdb before running this script
from influxdb import InfluxDBClient
from datetime import datetime

#Set up the InfluxDB connection
client = InfluxDBClient(host='localhost', port=8086, database='influxdb')
client.get_list_database() #확인하기
client.switch_database('influxdb')


#Setup Payload 넣을 데이터 불러와서 넣으면 될듯
json_payload = []
data = {
    "measurement": "DUST2",
    #"tags":{
    #}
}
json_payload.append(data)

#Send payload to InfluxDB 디비에 집어 넣는 명령어
client.write_points(json_payload)
from concurrent import futures
import logging

import grpc
import SensorService_pb2
import SensorService_pb2_grpc

sensorDB=[
 {
 'id':101,
 'date':'26/05/2001',
 'location': 'Brasil',
 'temperature':'20'
 },
 {
 'id':201,
 'date':'29/01/2001',
 'location': 'Argentina',
 'temperature':'30'
 }
 ]

class SensorServer(SensorService_pb2_grpc.SensorServiceServicer):

  def CreateSensor(self, request, context):
    dat = {
    'id':request.id,
    'date':request.date,
    'location': request.location,
    'temperature':request.temperature
    }
    sensorDB.append(dat)
    return SensorService_pb2.StatusReply(status='OK')

  def GetSensorDataFromID(self, request, context):
    usr = [ sensor for sensor in sensorDB if (sensor['id'] == request.id) ] 
    return SensorService_pb2.SensorData(id=usr[0]['id'], date=usr[0]['date'], location=usr[0]['location'], temperature=usr[0]['temperature'])

  def ListAllSensors(self, request, context):
    list = SensorService_pb2.SensorDataList()
    for item in sensorDB:
      sensor_data = SensorService_pb2.SensorData(id=item['id'], date=item['date'], location=item['location'], temperature=item['temperature']) 
      list.sensor_data.append(sensor_data)
    return list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_sensors=10))
    SensorService_pb2_grpc.add_SensorServiceServicer_to_server(SensorServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
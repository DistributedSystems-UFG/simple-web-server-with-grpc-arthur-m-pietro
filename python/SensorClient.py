from __future__ import print_function
import logging

import grpc
import SensorService_pb2
import SensorService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = SensorService_pb2_grpc.SensorServiceStub(channel)

        # Query an Sensor's data
        response = stub.GetSensorDataFromID(SensorService_pb2.SensorID(id=101))
        print ('Sensor\'s data: ' + str(response))

        # Add a new Sensor
        response = stub.CreateSensor(SensorService_pb2.SensorData(id=301, date='25/05/2001', location='Brazil', temperature='20'))
        print ('Added new sensor ' + response.status)

        # List all Sensors
        response = stub.ListAllSensors(SensorService_pb2.EmptyMessage())
        print ('All sensors: ' + str(response))

if __name__ == '__main__':
    logging.basicConfig()
    run()
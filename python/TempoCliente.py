from __future__ import print_function
import logging

import grpc
import TempoServico_pb2
import TempoServico_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = TempoServico_pb2_grpc.TempoServidorStub(channel)

        # Query an employee's data
        response = stub.GetTempoDataFromID(TempoServico_pb2.TempoID(id=101))
        print ('Tempo\'s data: ' + str(response))

        # Add a new employee
        response = stub.CreateTempo(TempoServico_pb2.TempoData(id=301, data='01/12/2022', localizacao=' Sao Paulo', valorTemperatura="30º C"))
        print ('Nova temperatura adicionada ' + response.status)
        
if __name__ == '__main__':
    logging.basicConfig()
    run()
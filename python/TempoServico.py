from concurrent import futures
import logging

import grpc
//import TempoServico_pb2
//import TempoServico_pb2_grpc

empDB=[
 {
 'id':101,
 'data':'21/11/2022',
 'localizacao':'Goiania',
 'valorTemperatura':'25º C'
 },
 {
 'id':201,
 'data':'11/12/2022',
 'localizacao':'Goiania',
 'valorTemperatura':'20º C'
 }
 ]

class TempoServidor(TempoServico_pb2_grpc.TempoServicoServicer):

  def CreateTempo(self, request, context):
    dat = {
    'id':request.id,
    'data':request.data,
    'localizacao':request.localizacao,
    'valorTemperatura':request.valorTemperatura
    }
    empDB.append(dat)
    return TempoServico_pb2.StatusReply(status='OK')

  def GetTempoDataFromID(self, request, context):
    usr = [ emp for emp in empDB if (emp['id'] == request.id) ] 
    return TempoServico_pb2.TempoData(id=usr[0]['id'], name=usr[0]['name'], title=usr[0]['title'])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TempoServico_pb2_grpc.add_TempoServicoServicer_to_server(TempoServidor(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

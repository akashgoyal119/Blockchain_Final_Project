from concurrent import futures
import time

import grpc

import registrar_pb2
import registrar_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Registrar(registrar_pb2_grpc.RegistrarServicer):

	def __init__(self):
		self.ip_addr_list = []

	def register(self, request, context):
		"""Returns null or single ip address
		   of the latest registered node.
		"""
		print(f'Registration request received from node: {request.addrMe}')
		if len(self.ip_addr_list) != 0:
			response = registrar_pb2.reg_reply()
			response.message.append(self.ip_addr_list[-1])
		else:
			response = registrar_pb2.reg_reply(message=None)
		self.ip_addr_list.append(request.addrMe)
		print(f"Registered nodes: {'  '.join(self.ip_addr_list)}\n")
		return response


def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	registrar_pb2_grpc.add_RegistrarServicer_to_server(Registrar(), server)
	server.add_insecure_port('[::]:50051')
	print('\n... Start DNS SEED server ...\n')
	server.start()
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		print('\n... Stop DNS SEED server ...\n')
		server.stop(0)


if __name__=='__main__':
	serve()
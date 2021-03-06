# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import send_info_pb2 as send__info__pb2


class SendInfoStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ContractDisplay = channel.unary_unary(
        '/SendInfo/ContractDisplay',
        request_serializer=send__info__pb2.ContractRequest.SerializeToString,
        response_deserializer=send__info__pb2.ContractReply.FromString,
        )
    self.TransactionCreation = channel.unary_unary(
        '/SendInfo/TransactionCreation',
        request_serializer=send__info__pb2.TransactionRequest.SerializeToString,
        response_deserializer=send__info__pb2.TransactionReply.FromString,
        )
    self.ContractCreation = channel.unary_unary(
        '/SendInfo/ContractCreation',
        request_serializer=send__info__pb2.ContractCreationRequest.SerializeToString,
        response_deserializer=send__info__pb2.ContractCreationReply.FromString,
        )


class SendInfoServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ContractDisplay(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TransactionCreation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContractCreation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SendInfoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ContractDisplay': grpc.unary_unary_rpc_method_handler(
          servicer.ContractDisplay,
          request_deserializer=send__info__pb2.ContractRequest.FromString,
          response_serializer=send__info__pb2.ContractReply.SerializeToString,
      ),
      'TransactionCreation': grpc.unary_unary_rpc_method_handler(
          servicer.TransactionCreation,
          request_deserializer=send__info__pb2.TransactionRequest.FromString,
          response_serializer=send__info__pb2.TransactionReply.SerializeToString,
      ),
      'ContractCreation': grpc.unary_unary_rpc_method_handler(
          servicer.ContractCreation,
          request_deserializer=send__info__pb2.ContractCreationRequest.FromString,
          response_serializer=send__info__pb2.ContractCreationReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SendInfo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

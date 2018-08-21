# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: full_node.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='full_node.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x66ull_node.proto\"Q\n\nhs_request\x12\x10\n\x08nVersion\x18\x01 \x01(\x05\x12\r\n\x05nTime\x18\x02 \x01(\x01\x12\x0e\n\x06\x61\x64\x64rMe\x18\x03 \x01(\t\x12\x12\n\nbestHeight\x18\x04 \x01(\x05\"\x1b\n\x08hs_reply\x12\x0f\n\x07message\x18\x01 \x03(\t\"E\n\x0bTransaction\x12\x1e\n\x16serialized_transaction\x18\x01 \x01(\x0c\x12\x16\n\x0e\x62roadcast_node\x18\x02 \x01(\t\"&\n\x13txn_broadcast_reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x05\x42lock\x12\x18\n\x10serialized_block\x18\x01 \x01(\x0c\"(\n\x15\x62lock_broadcast_reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"?\n\x08\x43ontract\x12\x1b\n\x13serialized_contract\x18\x01 \x01(\x0c\x12\x16\n\x0e\x62roadcast_node\x18\x02 \x01(\t\"+\n\x18\x63ontract_broadcast_reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"*\n\x17\x45xistingContractRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"5\n\x15\x45xistingContractReply\x12\x1c\n\x14serialized_contracts\x18\x01 \x03(\x0c\"$\n\x11\x42lockchainRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"#\n\x0f\x42lockchainReply\x12\x10\n\x08response\x18\x01 \x01(\x0c\x32\xc3\x03\n\x08\x46ullNode\x12%\n\thandshake\x12\x0b.hs_request\x1a\t.hs_reply\"\x00\x12\x41\n\x19new_transaction_broadcast\x12\x0c.Transaction\x1a\x14.txn_broadcast_reply\"\x00\x12\x37\n\x13new_block_broadcast\x12\x06.Block\x1a\x16.block_broadcast_reply\"\x00\x12<\n\x18\x65xisting_block_broadcast\x12\x06.Block\x1a\x16.block_broadcast_reply\"\x00\x12@\n\x16new_contract_broadcast\x12\t.Contract\x1a\x19.contract_broadcast_reply\"\x00\x12Q\n\x1bshow_all_existing_contracts\x12\x18.ExistingContractRequest\x1a\x16.ExistingContractReply\"\x00\x12\x41\n\x17\x64isplay_full_blockchain\x12\x12.BlockchainRequest\x1a\x10.BlockchainReply\"\x00\x62\x06proto3')
)




_HS_REQUEST = _descriptor.Descriptor(
  name='hs_request',
  full_name='hs_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nVersion', full_name='hs_request.nVersion', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nTime', full_name='hs_request.nTime', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addrMe', full_name='hs_request.addrMe', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bestHeight', full_name='hs_request.bestHeight', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=100,
)


_HS_REPLY = _descriptor.Descriptor(
  name='hs_reply',
  full_name='hs_reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='hs_reply.message', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=129,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_transaction', full_name='Transaction.serialized_transaction', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='broadcast_node', full_name='Transaction.broadcast_node', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=200,
)


_TXN_BROADCAST_REPLY = _descriptor.Descriptor(
  name='txn_broadcast_reply',
  full_name='txn_broadcast_reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='txn_broadcast_reply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=240,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_block', full_name='Block.serialized_block', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=275,
)


_BLOCK_BROADCAST_REPLY = _descriptor.Descriptor(
  name='block_broadcast_reply',
  full_name='block_broadcast_reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='block_broadcast_reply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=317,
)


_CONTRACT = _descriptor.Descriptor(
  name='Contract',
  full_name='Contract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_contract', full_name='Contract.serialized_contract', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='broadcast_node', full_name='Contract.broadcast_node', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=382,
)


_CONTRACT_BROADCAST_REPLY = _descriptor.Descriptor(
  name='contract_broadcast_reply',
  full_name='contract_broadcast_reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='contract_broadcast_reply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=427,
)


_EXISTINGCONTRACTREQUEST = _descriptor.Descriptor(
  name='ExistingContractRequest',
  full_name='ExistingContractRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='ExistingContractRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=429,
  serialized_end=471,
)


_EXISTINGCONTRACTREPLY = _descriptor.Descriptor(
  name='ExistingContractReply',
  full_name='ExistingContractReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_contracts', full_name='ExistingContractReply.serialized_contracts', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=526,
)


_BLOCKCHAINREQUEST = _descriptor.Descriptor(
  name='BlockchainRequest',
  full_name='BlockchainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='BlockchainRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=528,
  serialized_end=564,
)


_BLOCKCHAINREPLY = _descriptor.Descriptor(
  name='BlockchainReply',
  full_name='BlockchainReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='BlockchainReply.response', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=566,
  serialized_end=601,
)

DESCRIPTOR.message_types_by_name['hs_request'] = _HS_REQUEST
DESCRIPTOR.message_types_by_name['hs_reply'] = _HS_REPLY
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['txn_broadcast_reply'] = _TXN_BROADCAST_REPLY
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['block_broadcast_reply'] = _BLOCK_BROADCAST_REPLY
DESCRIPTOR.message_types_by_name['Contract'] = _CONTRACT
DESCRIPTOR.message_types_by_name['contract_broadcast_reply'] = _CONTRACT_BROADCAST_REPLY
DESCRIPTOR.message_types_by_name['ExistingContractRequest'] = _EXISTINGCONTRACTREQUEST
DESCRIPTOR.message_types_by_name['ExistingContractReply'] = _EXISTINGCONTRACTREPLY
DESCRIPTOR.message_types_by_name['BlockchainRequest'] = _BLOCKCHAINREQUEST
DESCRIPTOR.message_types_by_name['BlockchainReply'] = _BLOCKCHAINREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

hs_request = _reflection.GeneratedProtocolMessageType('hs_request', (_message.Message,), dict(
  DESCRIPTOR = _HS_REQUEST,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:hs_request)
  ))
_sym_db.RegisterMessage(hs_request)

hs_reply = _reflection.GeneratedProtocolMessageType('hs_reply', (_message.Message,), dict(
  DESCRIPTOR = _HS_REPLY,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:hs_reply)
  ))
_sym_db.RegisterMessage(hs_reply)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

txn_broadcast_reply = _reflection.GeneratedProtocolMessageType('txn_broadcast_reply', (_message.Message,), dict(
  DESCRIPTOR = _TXN_BROADCAST_REPLY,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:txn_broadcast_reply)
  ))
_sym_db.RegisterMessage(txn_broadcast_reply)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:Block)
  ))
_sym_db.RegisterMessage(Block)

block_broadcast_reply = _reflection.GeneratedProtocolMessageType('block_broadcast_reply', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK_BROADCAST_REPLY,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:block_broadcast_reply)
  ))
_sym_db.RegisterMessage(block_broadcast_reply)

Contract = _reflection.GeneratedProtocolMessageType('Contract', (_message.Message,), dict(
  DESCRIPTOR = _CONTRACT,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:Contract)
  ))
_sym_db.RegisterMessage(Contract)

contract_broadcast_reply = _reflection.GeneratedProtocolMessageType('contract_broadcast_reply', (_message.Message,), dict(
  DESCRIPTOR = _CONTRACT_BROADCAST_REPLY,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:contract_broadcast_reply)
  ))
_sym_db.RegisterMessage(contract_broadcast_reply)

ExistingContractRequest = _reflection.GeneratedProtocolMessageType('ExistingContractRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXISTINGCONTRACTREQUEST,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:ExistingContractRequest)
  ))
_sym_db.RegisterMessage(ExistingContractRequest)

ExistingContractReply = _reflection.GeneratedProtocolMessageType('ExistingContractReply', (_message.Message,), dict(
  DESCRIPTOR = _EXISTINGCONTRACTREPLY,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:ExistingContractReply)
  ))
_sym_db.RegisterMessage(ExistingContractReply)

BlockchainRequest = _reflection.GeneratedProtocolMessageType('BlockchainRequest', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKCHAINREQUEST,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:BlockchainRequest)
  ))
_sym_db.RegisterMessage(BlockchainRequest)

BlockchainReply = _reflection.GeneratedProtocolMessageType('BlockchainReply', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKCHAINREPLY,
  __module__ = 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:BlockchainReply)
  ))
_sym_db.RegisterMessage(BlockchainReply)



_FULLNODE = _descriptor.ServiceDescriptor(
  name='FullNode',
  full_name='FullNode',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=604,
  serialized_end=1055,
  methods=[
  _descriptor.MethodDescriptor(
    name='handshake',
    full_name='FullNode.handshake',
    index=0,
    containing_service=None,
    input_type=_HS_REQUEST,
    output_type=_HS_REPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='new_transaction_broadcast',
    full_name='FullNode.new_transaction_broadcast',
    index=1,
    containing_service=None,
    input_type=_TRANSACTION,
    output_type=_TXN_BROADCAST_REPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='new_block_broadcast',
    full_name='FullNode.new_block_broadcast',
    index=2,
    containing_service=None,
    input_type=_BLOCK,
    output_type=_BLOCK_BROADCAST_REPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='existing_block_broadcast',
    full_name='FullNode.existing_block_broadcast',
    index=3,
    containing_service=None,
    input_type=_BLOCK,
    output_type=_BLOCK_BROADCAST_REPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='new_contract_broadcast',
    full_name='FullNode.new_contract_broadcast',
    index=4,
    containing_service=None,
    input_type=_CONTRACT,
    output_type=_CONTRACT_BROADCAST_REPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='show_all_existing_contracts',
    full_name='FullNode.show_all_existing_contracts',
    index=5,
    containing_service=None,
    input_type=_EXISTINGCONTRACTREQUEST,
    output_type=_EXISTINGCONTRACTREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='display_full_blockchain',
    full_name='FullNode.display_full_blockchain',
    index=6,
    containing_service=None,
    input_type=_BLOCKCHAINREQUEST,
    output_type=_BLOCKCHAINREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FULLNODE)

DESCRIPTOR.services_by_name['FullNode'] = _FULLNODE

# @@protoc_insertion_point(module_scope)

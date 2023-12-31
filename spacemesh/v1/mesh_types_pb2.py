# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacemesh/v1/mesh_types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from spacemesh.v1 import types_pb2 as spacemesh_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dspacemesh/v1/mesh_types.proto\x12\x0cspacemesh.v1\x1a\x18spacemesh/v1/types.proto\"\x14\n\x12GenesisTimeRequest\"@\n\x13GenesisTimeResponse\x12)\n\x08unixtime\x18\x01 \x01(\x0b\x32\x17.spacemesh.v1.SimpleInt\"\x15\n\x13\x43urrentLayerRequest\"C\n\x14\x43urrentLayerResponse\x12+\n\x08layernum\x18\x01 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\"\x15\n\x13\x43urrentEpochRequest\"C\n\x14\x43urrentEpochResponse\x12+\n\x08\x65pochnum\x18\x01 \x01(\x0b\x32\x19.spacemesh.v1.EpochNumber\"\x12\n\x10GenesisIDRequest\"\'\n\x11GenesisIDResponse\x12\x12\n\ngenesis_id\x18\x01 \x01(\x0c\"\x17\n\x15\x45pochNumLayersRequest\"F\n\x16\x45pochNumLayersResponse\x12,\n\tnumlayers\x18\x01 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\"\x16\n\x14LayerDurationRequest\"B\n\x15LayerDurationResponse\x12)\n\x08\x64uration\x18\x01 \x01(\x0b\x32\x17.spacemesh.v1.SimpleInt\"!\n\x1fMaxTransactionsPerSecondRequest\"W\n MaxTransactionsPerSecondResponse\x12\x33\n\x12max_txs_per_second\x18\x01 \x01(\x0b\x32\x17.spacemesh.v1.SimpleInt\"e\n\x15\x41\x63\x63ountMeshDataFilter\x12+\n\naccount_id\x18\x01 \x01(\x0b\x32\x17.spacemesh.v1.AccountId\x12\x1f\n\x17\x61\x63\x63ount_mesh_data_flags\x18\x02 \x01(\r\"\x85\x01\n\x0f\x41\x63\x63ountMeshData\x12\x39\n\x10mesh_transaction\x18\x01 \x01(\x0b\x32\x1d.spacemesh.v1.MeshTransactionH\x00\x12.\n\nactivation\x18\x02 \x01(\x0b\x32\x18.spacemesh.v1.ActivationH\x00\x42\x07\n\x05\x64\x61tum\"S\n\x1c\x41\x63\x63ountMeshDataStreamRequest\x12\x33\n\x06\x66ilter\x18\x01 \x01(\x0b\x32#.spacemesh.v1.AccountMeshDataFilter\"M\n\x1d\x41\x63\x63ountMeshDataStreamResponse\x12,\n\x05\x64\x61tum\x18\x01 \x01(\x0b\x32\x1d.spacemesh.v1.AccountMeshData\"\xa5\x01\n\x1b\x41\x63\x63ountMeshDataQueryRequest\x12\x33\n\x06\x66ilter\x18\x01 \x01(\x0b\x32#.spacemesh.v1.AccountMeshDataFilter\x12,\n\tmin_layer\x18\x02 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\x12\x13\n\x0bmax_results\x18\x03 \x01(\r\x12\x0e\n\x06offset\x18\x04 \x01(\r\"b\n\x1c\x41\x63\x63ountMeshDataQueryResponse\x12+\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1d.spacemesh.v1.AccountMeshData\x12\x15\n\rtotal_results\x18\x02 \x01(\r\"r\n\x12LayersQueryRequest\x12.\n\x0bstart_layer\x18\x01 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\x12,\n\tend_layer\x18\x02 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\"9\n\x13LayersQueryResponse\x12\"\n\x05layer\x18\x01 \x03(\x0b\x32\x13.spacemesh.v1.Layer\"\x14\n\x12LayerStreamRequest\"9\n\x13LayerStreamResponse\x12\"\n\x05layer\x18\x01 \x01(\x0b\x32\x13.spacemesh.v1.Layer\"#\n\x12\x45pochStreamRequest\x12\r\n\x05\x65poch\x18\x01 \x01(\r\"=\n\x13\x45pochStreamResponse\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.spacemesh.v1.ActivationId\"@\n\x12MalfeasanceRequest\x12\x13\n\x0bsmesher_hex\x18\x01 \x01(\t\x12\x15\n\rinclude_proof\x18\x02 \x01(\x08\"D\n\x13MalfeasanceResponse\x12-\n\x05proof\x18\x01 \x01(\x0b\x32\x1e.spacemesh.v1.MalfeasanceProof\"1\n\x18MalfeasanceStreamRequest\x12\x15\n\rinclude_proof\x18\x01 \x01(\x08\"J\n\x19MalfeasanceStreamResponse\x12-\n\x05proof\x18\x01 \x01(\x0b\x32\x1e.spacemesh.v1.MalfeasanceProof*\x8e\x01\n\x13\x41\x63\x63ountMeshDataFlag\x12&\n\"ACCOUNT_MESH_DATA_FLAG_UNSPECIFIED\x10\x00\x12\'\n#ACCOUNT_MESH_DATA_FLAG_TRANSACTIONS\x10\x01\x12&\n\"ACCOUNT_MESH_DATA_FLAG_ACTIVATIONS\x10\x02\x42\x34Z2github.com/spacemeshos/api/release/go/spacemesh/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spacemesh.v1.mesh_types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/spacemeshos/api/release/go/spacemesh/v1'
  _globals['_ACCOUNTMESHDATAFLAG']._serialized_start=2010
  _globals['_ACCOUNTMESHDATAFLAG']._serialized_end=2152
  _globals['_GENESISTIMEREQUEST']._serialized_start=73
  _globals['_GENESISTIMEREQUEST']._serialized_end=93
  _globals['_GENESISTIMERESPONSE']._serialized_start=95
  _globals['_GENESISTIMERESPONSE']._serialized_end=159
  _globals['_CURRENTLAYERREQUEST']._serialized_start=161
  _globals['_CURRENTLAYERREQUEST']._serialized_end=182
  _globals['_CURRENTLAYERRESPONSE']._serialized_start=184
  _globals['_CURRENTLAYERRESPONSE']._serialized_end=251
  _globals['_CURRENTEPOCHREQUEST']._serialized_start=253
  _globals['_CURRENTEPOCHREQUEST']._serialized_end=274
  _globals['_CURRENTEPOCHRESPONSE']._serialized_start=276
  _globals['_CURRENTEPOCHRESPONSE']._serialized_end=343
  _globals['_GENESISIDREQUEST']._serialized_start=345
  _globals['_GENESISIDREQUEST']._serialized_end=363
  _globals['_GENESISIDRESPONSE']._serialized_start=365
  _globals['_GENESISIDRESPONSE']._serialized_end=404
  _globals['_EPOCHNUMLAYERSREQUEST']._serialized_start=406
  _globals['_EPOCHNUMLAYERSREQUEST']._serialized_end=429
  _globals['_EPOCHNUMLAYERSRESPONSE']._serialized_start=431
  _globals['_EPOCHNUMLAYERSRESPONSE']._serialized_end=501
  _globals['_LAYERDURATIONREQUEST']._serialized_start=503
  _globals['_LAYERDURATIONREQUEST']._serialized_end=525
  _globals['_LAYERDURATIONRESPONSE']._serialized_start=527
  _globals['_LAYERDURATIONRESPONSE']._serialized_end=593
  _globals['_MAXTRANSACTIONSPERSECONDREQUEST']._serialized_start=595
  _globals['_MAXTRANSACTIONSPERSECONDREQUEST']._serialized_end=628
  _globals['_MAXTRANSACTIONSPERSECONDRESPONSE']._serialized_start=630
  _globals['_MAXTRANSACTIONSPERSECONDRESPONSE']._serialized_end=717
  _globals['_ACCOUNTMESHDATAFILTER']._serialized_start=719
  _globals['_ACCOUNTMESHDATAFILTER']._serialized_end=820
  _globals['_ACCOUNTMESHDATA']._serialized_start=823
  _globals['_ACCOUNTMESHDATA']._serialized_end=956
  _globals['_ACCOUNTMESHDATASTREAMREQUEST']._serialized_start=958
  _globals['_ACCOUNTMESHDATASTREAMREQUEST']._serialized_end=1041
  _globals['_ACCOUNTMESHDATASTREAMRESPONSE']._serialized_start=1043
  _globals['_ACCOUNTMESHDATASTREAMRESPONSE']._serialized_end=1120
  _globals['_ACCOUNTMESHDATAQUERYREQUEST']._serialized_start=1123
  _globals['_ACCOUNTMESHDATAQUERYREQUEST']._serialized_end=1288
  _globals['_ACCOUNTMESHDATAQUERYRESPONSE']._serialized_start=1290
  _globals['_ACCOUNTMESHDATAQUERYRESPONSE']._serialized_end=1388
  _globals['_LAYERSQUERYREQUEST']._serialized_start=1390
  _globals['_LAYERSQUERYREQUEST']._serialized_end=1504
  _globals['_LAYERSQUERYRESPONSE']._serialized_start=1506
  _globals['_LAYERSQUERYRESPONSE']._serialized_end=1563
  _globals['_LAYERSTREAMREQUEST']._serialized_start=1565
  _globals['_LAYERSTREAMREQUEST']._serialized_end=1585
  _globals['_LAYERSTREAMRESPONSE']._serialized_start=1587
  _globals['_LAYERSTREAMRESPONSE']._serialized_end=1644
  _globals['_EPOCHSTREAMREQUEST']._serialized_start=1646
  _globals['_EPOCHSTREAMREQUEST']._serialized_end=1681
  _globals['_EPOCHSTREAMRESPONSE']._serialized_start=1683
  _globals['_EPOCHSTREAMRESPONSE']._serialized_end=1744
  _globals['_MALFEASANCEREQUEST']._serialized_start=1746
  _globals['_MALFEASANCEREQUEST']._serialized_end=1810
  _globals['_MALFEASANCERESPONSE']._serialized_start=1812
  _globals['_MALFEASANCERESPONSE']._serialized_end=1880
  _globals['_MALFEASANCESTREAMREQUEST']._serialized_start=1882
  _globals['_MALFEASANCESTREAMREQUEST']._serialized_end=1931
  _globals['_MALFEASANCESTREAMRESPONSE']._serialized_start=1933
  _globals['_MALFEASANCESTREAMRESPONSE']._serialized_end=2007
# @@protoc_insertion_point(module_scope)

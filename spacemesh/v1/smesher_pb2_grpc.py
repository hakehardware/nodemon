# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spacemesh.v1 import smesher_types_pb2 as spacemesh_dot_v1_dot_smesher__types__pb2


class SmesherServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IsSmeshing = channel.unary_unary(
                '/spacemesh.v1.SmesherService/IsSmeshing',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.IsSmeshingResponse.FromString,
                )
        self.StartSmeshing = channel.unary_unary(
                '/spacemesh.v1.SmesherService/StartSmeshing',
                request_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.StartSmeshingRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.StartSmeshingResponse.FromString,
                )
        self.StopSmeshing = channel.unary_unary(
                '/spacemesh.v1.SmesherService/StopSmeshing',
                request_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.StopSmeshingRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.StopSmeshingResponse.FromString,
                )
        self.SmesherID = channel.unary_unary(
                '/spacemesh.v1.SmesherService/SmesherID',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.SmesherIDResponse.FromString,
                )
        self.Coinbase = channel.unary_unary(
                '/spacemesh.v1.SmesherService/Coinbase',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.CoinbaseResponse.FromString,
                )
        self.SetCoinbase = channel.unary_unary(
                '/spacemesh.v1.SmesherService/SetCoinbase',
                request_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.SetCoinbaseRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.SetCoinbaseResponse.FromString,
                )
        self.MinGas = channel.unary_unary(
                '/spacemesh.v1.SmesherService/MinGas',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.MinGasResponse.FromString,
                )
        self.SetMinGas = channel.unary_unary(
                '/spacemesh.v1.SmesherService/SetMinGas',
                request_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.SetMinGasRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.SetMinGasResponse.FromString,
                )
        self.EstimatedRewards = channel.unary_unary(
                '/spacemesh.v1.SmesherService/EstimatedRewards',
                request_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.EstimatedRewardsRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.EstimatedRewardsResponse.FromString,
                )
        self.PostSetupStatus = channel.unary_unary(
                '/spacemesh.v1.SmesherService/PostSetupStatus',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupStatusResponse.FromString,
                )
        self.PostSetupStatusStream = channel.unary_stream(
                '/spacemesh.v1.SmesherService/PostSetupStatusStream',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupStatusStreamResponse.FromString,
                )
        self.PostSetupProviders = channel.unary_unary(
                '/spacemesh.v1.SmesherService/PostSetupProviders',
                request_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupProvidersRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupProvidersResponse.FromString,
                )
        self.PostConfig = channel.unary_unary(
                '/spacemesh.v1.SmesherService/PostConfig',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.PostConfigResponse.FromString,
                )
        self.UpdatePoetServers = channel.unary_unary(
                '/spacemesh.v1.SmesherService/UpdatePoetServers',
                request_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.UpdatePoetServersRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.UpdatePoetServersResponse.FromString,
                )


class SmesherServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def IsSmeshing(self, request, context):
        """Returns true iff node is currently smeshing
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartSmeshing(self, request, context):
        """Starts smeshing, after completing the post setup.
        Changing of the post setup options (e.g., number of units), after initial setup, is supported.
        Returns success if request is accepted by node , failure if it fails
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopSmeshing(self, request, context):
        """Stops smeshing, or the preceding post setup session, and optionally attempt to
        delete the post setup data files(s).
        Returns success if request is accepted by node, failure if it fails
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SmesherID(self, request, context):
        """Get the current smesher id generated by the node
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Coinbase(self, request, context):
        """Get the current coinbase
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCoinbase(self, request, context):
        """Set the coinbase
        Returns success if request succeeds, failure if it fails
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MinGas(self, request, context):
        """Get the current min gas for including txs in blocks by this smesher
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMinGas(self, request, context):
        """Set a min gas units for including txs in blocks by this smesher
        Returns success if request succeeds, failure if it fails
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimatedRewards(self, request, context):
        """Estimate smeshing rewards over the next upcoming epoch
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostSetupStatus(self, request, context):
        """Returns the Post setup status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostSetupStatusStream(self, request, context):
        """Returns a stream of updates for the Post setup status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostSetupProviders(self, request, context):
        """Returns a list of available Post setup providers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostConfig(self, request, context):
        """Returns the Post protocol config
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePoetServers(self, request, context):
        """UpdatePoetServers updates poet servers
        All existing PoET servers will be substituted with this new list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SmesherServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IsSmeshing': grpc.unary_unary_rpc_method_handler(
                    servicer.IsSmeshing,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.IsSmeshingResponse.SerializeToString,
            ),
            'StartSmeshing': grpc.unary_unary_rpc_method_handler(
                    servicer.StartSmeshing,
                    request_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.StartSmeshingRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.StartSmeshingResponse.SerializeToString,
            ),
            'StopSmeshing': grpc.unary_unary_rpc_method_handler(
                    servicer.StopSmeshing,
                    request_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.StopSmeshingRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.StopSmeshingResponse.SerializeToString,
            ),
            'SmesherID': grpc.unary_unary_rpc_method_handler(
                    servicer.SmesherID,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.SmesherIDResponse.SerializeToString,
            ),
            'Coinbase': grpc.unary_unary_rpc_method_handler(
                    servicer.Coinbase,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.CoinbaseResponse.SerializeToString,
            ),
            'SetCoinbase': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCoinbase,
                    request_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.SetCoinbaseRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.SetCoinbaseResponse.SerializeToString,
            ),
            'MinGas': grpc.unary_unary_rpc_method_handler(
                    servicer.MinGas,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.MinGasResponse.SerializeToString,
            ),
            'SetMinGas': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMinGas,
                    request_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.SetMinGasRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.SetMinGasResponse.SerializeToString,
            ),
            'EstimatedRewards': grpc.unary_unary_rpc_method_handler(
                    servicer.EstimatedRewards,
                    request_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.EstimatedRewardsRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.EstimatedRewardsResponse.SerializeToString,
            ),
            'PostSetupStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.PostSetupStatus,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupStatusResponse.SerializeToString,
            ),
            'PostSetupStatusStream': grpc.unary_stream_rpc_method_handler(
                    servicer.PostSetupStatusStream,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupStatusStreamResponse.SerializeToString,
            ),
            'PostSetupProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.PostSetupProviders,
                    request_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupProvidersRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupProvidersResponse.SerializeToString,
            ),
            'PostConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.PostConfig,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.PostConfigResponse.SerializeToString,
            ),
            'UpdatePoetServers': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePoetServers,
                    request_deserializer=spacemesh_dot_v1_dot_smesher__types__pb2.UpdatePoetServersRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_smesher__types__pb2.UpdatePoetServersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spacemesh.v1.SmesherService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SmesherService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def IsSmeshing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/IsSmeshing',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.IsSmeshingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartSmeshing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/StartSmeshing',
            spacemesh_dot_v1_dot_smesher__types__pb2.StartSmeshingRequest.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.StartSmeshingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopSmeshing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/StopSmeshing',
            spacemesh_dot_v1_dot_smesher__types__pb2.StopSmeshingRequest.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.StopSmeshingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SmesherID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/SmesherID',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.SmesherIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Coinbase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/Coinbase',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.CoinbaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCoinbase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/SetCoinbase',
            spacemesh_dot_v1_dot_smesher__types__pb2.SetCoinbaseRequest.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.SetCoinbaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MinGas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/MinGas',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.MinGasResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetMinGas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/SetMinGas',
            spacemesh_dot_v1_dot_smesher__types__pb2.SetMinGasRequest.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.SetMinGasResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimatedRewards(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/EstimatedRewards',
            spacemesh_dot_v1_dot_smesher__types__pb2.EstimatedRewardsRequest.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.EstimatedRewardsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostSetupStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/PostSetupStatus',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostSetupStatusStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spacemesh.v1.SmesherService/PostSetupStatusStream',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupStatusStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostSetupProviders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/PostSetupProviders',
            spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupProvidersRequest.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.PostSetupProvidersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/PostConfig',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.PostConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePoetServers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.SmesherService/UpdatePoetServers',
            spacemesh_dot_v1_dot_smesher__types__pb2.UpdatePoetServersRequest.SerializeToString,
            spacemesh_dot_v1_dot_smesher__types__pb2.UpdatePoetServersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

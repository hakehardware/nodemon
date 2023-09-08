import grpc
import binascii
from google.protobuf.empty_pb2 import Empty
from spacemesh.v1 import activation_pb2_grpc
from spacemesh.v1 import admin_pb2_grpc
from spacemesh.v1 import node_pb2_grpc
from spacemesh.v1 import smesher_pb2_grpc
from spacemesh.v1 import debug_pb2_grpc
from spacemesh.v1 import global_state_pb2_grpc
from spacemesh.v1 import mesh_pb2_grpc

import json
import time
import threading
from google.protobuf.json_format import MessageToDict


class ActivationClient(object):
    def __init__(self, ip_address_with_port):
        self.channel = grpc.insecure_channel(ip_address_with_port)
        self.stub = activation_pb2_grpc.ActivationServiceStub(self.channel)

    def get_highest_atx(self):
        request = Empty()
        response = self.stub.Highest(request)
        return binascii.hexlify(response.atx.id.id).decode() 
    
class AdminClient(object):
    def __init__(self, ip_address_with_port):
        self.channel = grpc.insecure_channel(ip_address_with_port)
        self.stub = admin_pb2_grpc.AdminServiceStub(self.channel)
        self.streams = None

    def _cancel_stream(self):
        time.sleep(15)
        self.streams.cancel()

    def get_event_stream(self):
        request = Empty()
        self.streams = self.stub.EventsStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

    def get_peer_event_stream(self):
        request = Empty()
        self.streams = self.stub.PeerInfoStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

    def get_checkpoint_stream(self):
        request = Empty()
        self.streams = self.stub.CheckpointStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

class NodeClient(object):
    def __init__(self, ip_address_with_port):
        self.channel = grpc.insecure_channel(ip_address_with_port)
        self.stub = node_pb2_grpc.NodeServiceStub(self.channel)
        self.streams = None

    def _cancel_stream(self):
        time.sleep(15)
        self.streams.cancel()

    # Must include message - doesn't work
    def get_echo(self):
        request = Empty()
        response = self.stub.Echo(request)
        return MessageToDict(response)

    def get_version(self):
        request = Empty()
        response = MessageToDict(self.stub.Version(request))
        return response["versionString"]["value"]

    def get_build(self):
        request = Empty()
        response = MessageToDict(self.stub.Build(request))
        return response["buildString"]["value"]

    def get_node_status(self):
        request = Empty()
        response = self.stub.Status(request)
        return MessageToDict(response)
    
    def get_node_info(self):
        request = Empty()
        response = self.stub.NodeInfo(request)
        return MessageToDict(response)

    def get_status_stream(self):
        request = Empty()
        self.streams = self.stub.StatusStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

    def get_error_stream(self):
        request = Empty()
        self.streams = self.stub.ErrorStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

class SmesherClient(object):
    def __init__(self, ip_address_with_port):
        self.channel = grpc.insecure_channel(ip_address_with_port)
        self.stub = smesher_pb2_grpc.SmesherServiceStub(self.channel)

    def _cancel_stream(self):
        time.sleep(15)
        self.streams.cancel()

    def get_is_smeshing(self):
        request = Empty()
        response = self.stub.IsSmeshing(request)
        return MessageToDict(response)

    def get_smesher_id(self):
        request = Empty()
        response = self.stub.SmesherID(request)
        return MessageToDict(response)
    
    def get_coinbase(self):
        request = Empty()
        response = self.stub.Coinbase(request)
        return MessageToDict(response)
    
    # Not implemented
    def get_estimated_rewards(self):
        request = Empty()
        response = self.stub.EstimatedRewards(request)
        return MessageToDict(response)
    
    def get_post_setup_status(self):
        request = Empty()
        response = self.stub.PostSetupStatus(request)
        return MessageToDict(response)
    
    def get_post_setup_status_stream(self):
        request = Empty()
        self.streams = self.stub.PostSetupStatusStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))
    
    def get_post_setup_status_providers(self):
        request = Empty()
        response = self.stub.PostSetupProviders(request)
        return MessageToDict(response)

    def get_post_config(self):
        request = Empty()
        response = self.stub.PostConfig(request)
        return MessageToDict(response)
    
class DebugClient(object):
    def __init__(self, ip_address_with_port):
        self.channel = grpc.insecure_channel(ip_address_with_port)
        self.stub = debug_pb2_grpc.DebugServiceStub(self.channel)

    def _cancel_stream(self):
        time.sleep(15)
        self.streams.cancel()

    def get_accounts(self):
        request = Empty()
        response = self.stub.Accounts(request)
        print(MessageToDict(response))

    def get_network_info(self):
        request = Empty()
        response = self.stub.NetworkInfo(request)
        print(MessageToDict(response))

    def get_active_set(self):
        request = Empty()
        response = self.stub.ActiveSet(request)
        print(MessageToDict(response))

    def get_proposal_stream(self):
        # ProposalsStream
        request = Empty()
        self.streams = self.stub.ProposalsStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

class GlobalStateClient(object):
    def __init__(self, ip_address_with_port):
        self.channel = grpc.insecure_channel(ip_address_with_port)
        self.stub = global_state_pb2_grpc.GlobalStateServiceStub(self.channel)

    def _cancel_stream(self):
        time.sleep(15)
        self.streams.cancel()

    def get_global_state_hash(self):
        #GlobalStateHash
        request = Empty()
        response = self.stub.GlobalStateHash(request)
        print(MessageToDict(response))

    # Needs AccountID - Not working
    def get_global_state_account(self):
        #GlobalStateHash
        request = Empty()
        response = self.stub.Account(request)
        print(MessageToDict(response))

    # Needs Filter - Not working
    def global_state_account_data_query(self):
        #GlobalStateHash
        request = Empty()
        response = self.stub.AccountDataQuery(request)
        print(MessageToDict(response))

    # Says Deprecated
    def global_state_smesher_data_query(self):
        #GlobalStateHash
        request = Empty()
        response = self.stub.SmesherDataQuery(request)
        print(MessageToDict(response))

    def global_state_account_data_stream(self):
        request = Empty()
        self.streams = self.stub.AccountDataStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

    def global_state_smesher_reward_stream(self):
        request = Empty()
        self.streams = self.stub.SmesherRewardStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

    def global_state_app_event_stream(self):
        request = Empty()
        self.streams = self.stub.AppEventStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

    def global_state_stream(self):
        request = Empty()
        self.streams = self.stub.GlobalStateStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

class MeshClient(object):
    def __init__(self, ip_address_with_port):
        self.channel = grpc.insecure_channel(ip_address_with_port)
        self.stub = mesh_pb2_grpc.MeshServiceStub(self.channel)

    def _cancel_stream(self):
        time.sleep(15)
        self.streams.cancel()

    def get_genesis_time(self):
        request = Empty()
        response = self.stub.GenesisTime(request)
        return MessageToDict(response)
    
    def get_current_layer(self):
        request = Empty()
        response = self.stub.CurrentLayer(request)
        return MessageToDict(response)

    def get_current_epoch(self):
        request = Empty()
        response = self.stub.CurrentEpoch(request)
        return MessageToDict(response)

    def get_genesis_id(self):
        request = Empty()
        response = self.stub.GenesisID(request)
        return MessageToDict(response)

    def get_epoch_num_layers(self):
        request = Empty()
        response = self.stub.EpochNumLayers(request)
        return MessageToDict(response)
    
    def get_layer_duration(self):
        request = Empty()
        response = self.stub.LayerDuration(request)
        return MessageToDict(response)

    def get_max_transaction_per_second(self):
        request = Empty()
        response = self.stub.MaxTransactionsPerSecond(request)
        return MessageToDict(response)

    # Something about filter - doesn't work
    def get_account_mesh_data_query(self):
        request = Empty()
        response = self.stub.AccountMeshDataQuery(request)
        return MessageToDict(response)

    def get_layers_query(self):
        request = Empty()
        response = self.stub.LayersQuery(request)
        return MessageToDict(response)

    def get_account_mesh_data_stream(self):
        request = Empty()
        self.streams = self.stub.AccountMeshDataStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

    def get_layer_stream(self):
        request = Empty()
        self.streams = self.stub.LayerStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

    def get_epoch_stream(self):
        request = Empty()
        self.streams = self.stub.EpochStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))

    # Expecting Smesher ID
    def get_malfeasance_query(self):
        request = Empty()
        response = self.stub.MalfeasanceQuery(request)
        return MessageToDict(response)

    def get_malfeasance_stream(self):
        request = Empty()
        self.streams = self.stub.MalfeasanceStream(request)

        cancellation_thread = threading.Thread(target=self._cancel_stream)
        cancellation_thread.start()
        data = []
        try:
            for r in self.streams:
                data.append(MessageToDict(r))

        except Exception as e:
            pass

        print(f"Got {len(data)} entries.")

        for d in data:
            time.sleep(1)
            print(json.dumps(d))



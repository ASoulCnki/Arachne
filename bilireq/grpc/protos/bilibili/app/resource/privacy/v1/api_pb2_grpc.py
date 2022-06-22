# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibili.app.resource.privacy.v1 import api_pb2 as bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2


class PrivacyStub(object):
    """隐私
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PrivacyConfig = channel.unary_unary(
                '/bilibili.app.resource.privacy.v1.Privacy/PrivacyConfig',
                request_serializer=bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.NoArgRequest.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.PrivacyConfigReply.FromString,
                )
        self.SetPrivacyConfig = channel.unary_unary(
                '/bilibili.app.resource.privacy.v1.Privacy/SetPrivacyConfig',
                request_serializer=bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.SetPrivacyConfigRequest.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.NoReply.FromString,
                )


class PrivacyServicer(object):
    """隐私
    """

    def PrivacyConfig(self, request, context):
        """获取隐私设置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPrivacyConfig(self, request, context):
        """修改隐私设置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PrivacyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PrivacyConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.PrivacyConfig,
                    request_deserializer=bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.NoArgRequest.FromString,
                    response_serializer=bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.PrivacyConfigReply.SerializeToString,
            ),
            'SetPrivacyConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPrivacyConfig,
                    request_deserializer=bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.SetPrivacyConfigRequest.FromString,
                    response_serializer=bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.NoReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bilibili.app.resource.privacy.v1.Privacy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Privacy(object):
    """隐私
    """

    @staticmethod
    def PrivacyConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.resource.privacy.v1.Privacy/PrivacyConfig',
            bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.NoArgRequest.SerializeToString,
            bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.PrivacyConfigReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPrivacyConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.resource.privacy.v1.Privacy/SetPrivacyConfig',
            bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.SetPrivacyConfigRequest.SerializeToString,
            bilibili_dot_app_dot_resource_dot_privacy_dot_v1_dot_api__pb2.NoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

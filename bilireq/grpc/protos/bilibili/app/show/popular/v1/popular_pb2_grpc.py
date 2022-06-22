# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibili.app.show.popular.v1 import popular_pb2 as bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_popular__pb2


class PopularStub(object):
    """热门
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Index = channel.unary_unary(
                '/bilibili.app.show.v1.Popular/Index',
                request_serializer=bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_popular__pb2.PopularResultReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_popular__pb2.PopularReply.FromString,
                )


class PopularServicer(object):
    """热门
    """

    def Index(self, request, context):
        """热门列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PopularServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Index': grpc.unary_unary_rpc_method_handler(
                    servicer.Index,
                    request_deserializer=bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_popular__pb2.PopularResultReq.FromString,
                    response_serializer=bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_popular__pb2.PopularReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bilibili.app.show.v1.Popular', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Popular(object):
    """热门
    """

    @staticmethod
    def Index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.show.v1.Popular/Index',
            bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_popular__pb2.PopularResultReq.SerializeToString,
            bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_popular__pb2.PopularReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
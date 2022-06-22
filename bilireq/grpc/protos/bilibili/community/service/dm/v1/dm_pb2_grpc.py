# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibili.community.service.dm.v1 import dm_pb2 as bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2


class DMStub(object):
    """弹幕
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DmSegMobile = channel.unary_unary(
                '/bilibili.community.service.dm.v1.DM/DmSegMobile',
                request_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegMobileReq.SerializeToString,
                response_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegMobileReply.FromString,
                )
        self.DmView = channel.unary_unary(
                '/bilibili.community.service.dm.v1.DM/DmView',
                request_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmViewReq.SerializeToString,
                response_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmViewReply.FromString,
                )
        self.DmPlayerConfig = channel.unary_unary(
                '/bilibili.community.service.dm.v1.DM/DmPlayerConfig',
                request_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmPlayerConfigReq.SerializeToString,
                response_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.Response.FromString,
                )
        self.DmSegOtt = channel.unary_unary(
                '/bilibili.community.service.dm.v1.DM/DmSegOtt',
                request_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegOttReq.SerializeToString,
                response_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegOttReply.FromString,
                )
        self.DmSegSDK = channel.unary_unary(
                '/bilibili.community.service.dm.v1.DM/DmSegSDK',
                request_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegSDKReq.SerializeToString,
                response_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegSDKReply.FromString,
                )
        self.DmExpoReport = channel.unary_unary(
                '/bilibili.community.service.dm.v1.DM/DmExpoReport',
                request_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmExpoReportReq.SerializeToString,
                response_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmExpoReportRes.FromString,
                )


class DMServicer(object):
    """弹幕
    """

    def DmSegMobile(self, request, context):
        """获取分段弹幕
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DmView(self, request, context):
        """客户端弹幕元数据 字幕、分段、防挡蒙版等
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DmPlayerConfig(self, request, context):
        """修改弹幕配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DmSegOtt(self, request, context):
        """ott弹幕列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DmSegSDK(self, request, context):
        """SDK弹幕列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DmExpoReport(self, request, context):
        """
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DMServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DmSegMobile': grpc.unary_unary_rpc_method_handler(
                    servicer.DmSegMobile,
                    request_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegMobileReq.FromString,
                    response_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegMobileReply.SerializeToString,
            ),
            'DmView': grpc.unary_unary_rpc_method_handler(
                    servicer.DmView,
                    request_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmViewReq.FromString,
                    response_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmViewReply.SerializeToString,
            ),
            'DmPlayerConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.DmPlayerConfig,
                    request_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmPlayerConfigReq.FromString,
                    response_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.Response.SerializeToString,
            ),
            'DmSegOtt': grpc.unary_unary_rpc_method_handler(
                    servicer.DmSegOtt,
                    request_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegOttReq.FromString,
                    response_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegOttReply.SerializeToString,
            ),
            'DmSegSDK': grpc.unary_unary_rpc_method_handler(
                    servicer.DmSegSDK,
                    request_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegSDKReq.FromString,
                    response_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegSDKReply.SerializeToString,
            ),
            'DmExpoReport': grpc.unary_unary_rpc_method_handler(
                    servicer.DmExpoReport,
                    request_deserializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmExpoReportReq.FromString,
                    response_serializer=bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmExpoReportRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bilibili.community.service.dm.v1.DM', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DM(object):
    """弹幕
    """

    @staticmethod
    def DmSegMobile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.community.service.dm.v1.DM/DmSegMobile',
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegMobileReq.SerializeToString,
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegMobileReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DmView(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.community.service.dm.v1.DM/DmView',
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmViewReq.SerializeToString,
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmViewReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DmPlayerConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.community.service.dm.v1.DM/DmPlayerConfig',
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmPlayerConfigReq.SerializeToString,
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DmSegOtt(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.community.service.dm.v1.DM/DmSegOtt',
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegOttReq.SerializeToString,
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegOttReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DmSegSDK(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.community.service.dm.v1.DM/DmSegSDK',
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegSDKReq.SerializeToString,
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmSegSDKReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DmExpoReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.community.service.dm.v1.DM/DmExpoReport',
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmExpoReportReq.SerializeToString,
            bilibili_dot_community_dot_service_dot_dm_dot_v1_dot_dm__pb2.DmExpoReportRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

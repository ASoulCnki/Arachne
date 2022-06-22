from ..protos.bilibili.main.community.reply.v1.reply_pb2 import (
    MainListReply,
    MainListReq,
    DetailListReply,
    DetailListReq,
    CursorReq,
    Mode
)

from ..protos.bilibili.main.community.reply.v1.reply_pb2_grpc import ReplyStub
from ..utils import grpc_request


@grpc_request
async def grpc_get_replies(
        oid: int, type: int, next: int = 0, **kwargs) -> MainListReply:
    stub = ReplyStub(kwargs.pop("_channel"))
    cursor = CursorReq(next=next, mode=Mode.MAIN_LIST_TIME)
    req = MainListReq(oid=oid, type=type, cursor=cursor)
    resp: MainListReply = await stub.MainList(req, **kwargs)
    return resp


@grpc_request
async def grpc_get_detail_list(
        oid: int, type: int, root: int, next: int = 0, **kwargs) -> DetailListReply:
    stub = ReplyStub(kwargs.pop("_channel"))
    cursor = CursorReq(next=next)
    req = DetailListReq(oid=oid, type=type, root=root, cursor=cursor)
    return await stub.DetailList(req, **kwargs)

import asyncio
import sys
from pathlib import Path
from pprint import pprint

sys.path.append(str(Path(__file__).parent.parent))

from bilireq.grpc.dynamic import grpc_get_user_dynamics  # noqa
from bilireq.grpc.relpy import grpc_get_replies, grpc_get_detail_list  # noqa


async def detail_replies():
    """楼中楼回复"""
    next = 0
    count = 0
    pn = 1
    while 1:
        replies = await grpc_get_detail_list(oid=673426231954243639, type=17, root=117454834832, next=next)
        for i in replies.root.replies:
            print(i.member.name, i.content.message)
            count += 1
        next = replies.cursor.next
        if replies.cursor.isEnd:
            break
        pn += 1


async def all_replies():
    """评论区主楼"""
    next = 0
    count = 0
    pn = 1
    while 1:
        replies = await grpc_get_replies(oid=673426231954243639, type=17, next=next)
        for i in replies.replies:
            print(i.member.name, i.content.message)
            count += 1
            count += i.count
        pn += 1
        next = replies.cursor.next
        if replies.cursor.isEnd:
            break


asyncio.run(all_replies())

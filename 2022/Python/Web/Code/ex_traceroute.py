# -*- coding=utf-8 -*-
# @Author: CarpeDiem
# @Date: 230423
# @Version: 1.0
# @Description: 基于ICMP协议Traceroute实现

from kamene.all import *
import time
import re

def Tracert_one(dst,dport,ttl_no):
    '''发一个Traceroute包，参数需要目的地址，目的端口，TTL'''
    send_time = time.time()         # 记录发送时间
    Tracert_one_reply = sr1(IP(dst=dst, ttl=ttl_no)/UDP(sport=6600, dport=dport)/b'my traceroute!!!', timeout = 1, verbose=False)
    # Scapy中UDP默认源目端口53，需要将源端口也改掉，否则中间设备将不回应
    try:
        if Tracert_one_reply.getlayer(ICMP).type == 11 and Tracert_one_reply.getlayer(ICMP).code == 0:
            # 如果收到TTL超时
            hop_ip = Tracert_one_reply.getlayer(IP).src
            received_time = time.time()
            time_to_passed = (received_time - send_time) * 1000
            return 1, hop_ip, time_to_passed        # 返回1表示并未抵达目的地
        elif Tracert_one_reply.getlayer(ICMP).type == 3 and Tracert_one_reply.getlayer(ICMP).code == 3:
            # 如果收到端口不可达
            hop_ip = Tracert_one_reply.getlayer(IP).src
            received_time = time.time()
            time_to_passed = (received_time - send_time) * 1000
            return 2, hop_ip, time_to_passed    # 返回2表示抵达目的地
    except Exception as e:
        if re.match('.*NoneType.*',str(e)):
            return None     # 测试失败返回None,没有回包

def MY_Tracert(dst,hops):
    dport = 33434           # Traceroute的目的端口从33434开始计算
    hop = 0
    while hop < hops:
        dport = dport + hop
        hop += 1
        Result = Tracert_one(dst,dport,hop)
        if Result == None:      # 如果测试失败就打印‘*’
            print(str(hop) + ' *',flush=True)
        elif Result[0] == 1:    # 如果未抵达目的，就打印这一跳和消耗的时间
            time_to_pass_result = '%4.2f' % Result[2]
            print(str(hop) + ' ' + str(Result[1]) + ' ' + time_to_pass_result + 'ms')
        elif Result[0] == 2:    # 如果抵达目的，就打印这一跳和消耗的时间，并且跳出循环！
            time_to_pass_result = '%4.2f' % Result[2]
            print(str(hop) + ' ' + str(Result[1]) + ' ' + time_to_pass_result + 'ms')
            break
        time.sleep(1)

if __name__ == '__main__':
    conf.route.add(net='172.16.10.0/24',gw='192.168.10.115')    # 为Scapy添加路由
    destIP=input("目标IP>>>")
    hops=input("最大跳数>>>")
    MY_Tracert(destIP, int(hops))
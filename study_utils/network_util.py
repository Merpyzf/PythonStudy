# -*- coding:utf-8 -*-

# 获取电脑的ip地址，mac地址
import socket
import uuid
import fcntl
import struct


# Linux下获取电脑的ip地址
def get_ip_address():
    return socket.gethostbyname(socket.getfqdn(socket.gethostname()))


# 获取电脑的mac地址
def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:].upper()
    return mac


if __name__ == '__main__':
    print 'ip地址', get_ip_address()
    print 'mac地址', get_mac_address()

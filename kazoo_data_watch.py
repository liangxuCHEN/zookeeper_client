# coding=utf-8
from kazoo.client import KazooClient
import time


if __name__ == '__main__':

    zk = KazooClient(hosts='master:2181')
    zk.start()

    # 这是装修器，调用zk.DataWatch 监控数据变化
    @zk.DataWatch('/my/favorite_2')
    def my_func(data, stat):
        print ('Data has change:', data)
        print('version: ', stat.version)


    while True:
        time.sleep(10)
        print('Programme is running and listening the node : /my/favorite_2')
        """
        在Console里面模拟数据的变化,然后可以触发监控：
        from kazoo.client import KazooClient
        zk.start()
        zk.set('/my/favorite_2', '{"info": 1}')
        zk.set('/my/favorite_2', '{"Status": "OK"}')
        zk.stop()
        zk.close()
        """

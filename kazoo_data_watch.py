# coding=utf-8
from kazoo.client import KazooClient
import time


if __name__ == '__main__':

    zk = KazooClient(hosts='master:2181')
    zk.start()

    # 这是装修器，调用zk.DataWatch 监控数据变化
    @zk.DataWatch('/my/favorite/node')
    def my_func(data, stat):
        print ('Data has change:', data)
        print('stat: ', stat)


    # 这是装修器，调用zk.DataWatch 监控
    @zk.ChildrenWatch("/my/favorite")
    def watch_children(children):
        print("Children are now: %s" % children)


    while True:
        time.sleep(15)
        print('Programme is running and listening the node : /my/favorite')
        """
        在Console里面模拟数据的变化,然后可以触发监控：
        Zookeeper CRUD 例子:
        from kazoo.client import KazooClient
        zk.start()
        zk.ensure_path("/my/favorite")
        zk.create('/my/favorite/node', '{"info": 1}')
        zk.set('/my/favorite/node', '{"Status": "OK"}')
        zk.exists("/my/favorite")
        zk.get_children("/my/favorite")
        zk.delete("/my/favorite/node", recursive=True)
        zk.stop()
        zk.close()
        """

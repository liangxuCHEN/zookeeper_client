# coding=utf-8
from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.retry import KazooRetry



if __name__ == '__main__':

    zk = KazooClient(hosts='master:2181')

    def my_listener(state):
        if state == KazooState.LOST:
            print('Register somewhere that the session was lost')
        elif state == KazooState.SUSPENDED:
            print('Handle being disconnected from Zookeeper')
        else:
            print('Handle being connected/reconnected to Zookeeper')

    # Handle being connected/reconnected to Zookeeper
    zk.add_listener(my_listener)

    zk.start()
    kr = KazooRetry(max_tries=3, ignore_expire=False)
    result = kr(zk.get, "/my/favorite")
    print(result)
    zk.stop()
    zk.close()


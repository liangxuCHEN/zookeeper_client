# coding=utf-8
from kazoo.client import KazooClient
import time

if __name__ == '__main__':
    zk = KazooClient(hosts='master:2181')
    """
    Zookeeper 3.4 and above supports the sending of multiple commands at once that
    will be committed as a single atomic unit. Either they will all succeed or
    they will all fail. The result of a transaction will be a list of the success/failure
    results for each command in the transaction.
    """
    zk.start()
    transaction = zk.transaction()
    transaction.check('/node/a', version=3)
    transaction.create('/node/b', b"a value")
    results = transaction.commit()
    print(results)
    zk.stop()
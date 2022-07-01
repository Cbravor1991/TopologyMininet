
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
from topo import MyTopo

# from firewall import Firewall
'''
sudo mn --custom topo.py --topo mytopo,3 --mac --arp --switch ovsk --controller remote
h2 iperf -s -u -p 5001
h1 iperf -c 10.0.0.2 -u -p 5001
'''


def run():
    n = input('Ingresar cantidad de switches: ')
    c = RemoteController('c', '0.0.0.0', 6633)
    net = Mininet(topo=MyTopo(n), controller=None)
    net.addController(c)
    net.start()

    client = CLI(net, script='./config.txt')

    net.stop()


# if the script is run directly (sudo custom/optical.py):
if __name__ == '__main__':
    setLogLevel('info')
    run()

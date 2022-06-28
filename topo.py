"""

   host1 ---                                   --- host3
            |                                 |
            --- switch1 --- .n. --- switchn --- 
            |                                 |
   host2 ---                                   --- host4

"""

from mininet.topo import Topo
import sys

class MyTopo( Topo ):

    def build( self,n):

        switches = []
        # Add hosts and switches
        leftUpperHost = self.addHost( 'h1' )
        leftDownHost = self.addHost('h2')
        rightUpperHost = self.addHost( 'h3' )
        rightDownHost = self.addHost( 'h4' )
        
        for i in range(n):
            switches.append(self.addSwitch('s' + str(i)))
            if i > 0:
                self.addLink( switches[i], switches[i-1])

        # Add links left
        self.addLink( leftUpperHost, switches[0] )
        self.addLink( leftDownHost, switches[0] )



        # Add links right
        self.addLink( rightUpperHost, switches[-1] )
        self.addLink( rightDownHost, switches[-1] )
        print(sys.argv)


topos = { 'mytopo': ( lambda n: MyTopo(n) ) }
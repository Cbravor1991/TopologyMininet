'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment: Layer-2 Firewall Application
Professor: Nick Feamster
Teaching Assistant: Arpit Gupta
'''

from nis import match
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
import pox.forwarding.l2_learning
from pox.lib.addresses import EthAddr
from collections import namedtuple
import pox.lib.packet as pkt
import os


log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ['HOME']


@staticmethod
def log_icmp_msg(icmp_msg):
    log.debug('Type: %d' % icmp_msg.type)
    log.debug('Code: {:#x}'.format(icmp_msg.code))
    log.debug('Checksum: {:#x}'.format(icmp_msg.csum))
    log.debug('Payload: {}'.format(icmp_msg.payload))


class Firewall (EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def filter_UDP_port_80(self, event):
        match = of.ofp_match()
        match.dl_type = pkt.ethernet.IP_TYPE
        match.nw_proto = pkt.ipv4.UDP_PROTOCOL
        match.tp_dst = 80
        msg_port = of.ofp_flow_mod(match=match)
        event.connection.send(msg_port)

    def filter_TCP_port_80(self, event):
        match = of.ofp_match()
        match.dl_type = pkt.ethernet.IP_TYPE
        match.nw_proto = pkt.ipv4.TCP_PROTOCOL
        match.tp_dst = 80
        msg_port = of.ofp_flow_mod(match=match)
        event.connection.send(msg_port)

    def filter_h1(self, event):
        my_match = of.ofp_match()
        my_match.dl_src = EthAddr('00:00:00:00:00:01')
        my_match.dl_type = pkt.ethernet.IP_TYPE
        my_match.tp_dst = 5001
        my_match.nw_proto = pkt.ipv4.UDP_PROTOCOL
        msg = of.ofp_flow_mod(match=my_match)
        event.connection.send(msg)

    def _handle_ConnectionUp(self, event):
        self.filter_UDP_port_80(event)
        self.filter_TCP_port_80(event)
        self.filter_h1(event)

        self.log_event(event)

    def log_event(self, event):
        log.debug('Ofp: {}'.format(event.ofp.ports.port_no))
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))


def launch():
    '''
    Starting the Firewall module
    '''
    pox.forwarding.l2_learning.launch()
    core.registerNew(Firewall)

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


rules = (

    {'dl_type': pkt.ethernet.IP_TYPE, 'tp_dst': 80,
     'nw_proto': pkt.ipv4.TCP_PROTOCOL},

    {'dl_type': pkt.ethernet.IP_TYPE, 'tp_dst': 80,
     'nw_proto': pkt.ipv4.UDP_PROTOCOL},

    {'dl_src': EthAddr('00:00:00:00:00:01'), 'dl_type': pkt.ethernet.IP_TYPE,
     'tp_dst': 5001, 'nw_proto': pkt.ipv4.UDP_PROTOCOL},
)


class Firewall (EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp(self, event):
        for rule in rules:
            match = of.ofp_match(**rule)
            msg = of.ofp_flow_mod(match=match)
            event.connection.send(msg)
            self.log_event(event)
            log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

    def log_event(self, event):
        log.debug('Ofp: {}'.format(event.ofp.ports.port_no))


def launch():
    '''
    Starting the Firewall module
    '''
    pox.forwarding.l2_learning.launch()
    core.registerNew(Firewall)

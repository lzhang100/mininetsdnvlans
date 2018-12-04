#!/usr/bin/python		

from mininet.topo import Topo		
from mininet.net import Mininet		
from mininet.util import dumpNodeConnections		
from mininet.log import setLogLevel	
from mininet.cli import CLI	

class MyFirstTopo( Topo ):		
	"Simple topology example."		
	def build( self ):		
		# Add hosts and switches		
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')		
		s1 = self.addSwitch( 's1' )		
		
		# Add links		
		self.addLink( h1, s1 )		
		self.addLink( h2, s1 )			
		self.addLink( h3, s1 )		
		self.addLink( h4, s1 )			

def runExperiment():		
	"Create and test a simple experiment"		
	topo = MyFirstTopo( )		
	net = Mininet(topo)		
	net.start()	
	
	h1, h2, h3, h4, s1 = \
      net.get('h1', 'h2', 'h3', 'h4', 's1')
	
	#Remove the default ip address on the interfaces
	h1.cmd("ifconfig h1-eth0 0")
	h2.cmd("ifconfig h2-eth0 0")
	h3.cmd("ifconfig h3-eth0 0")
	h4.cmd("ifconfig h4-eth0 0")
	
	#Create a vlan interface with id 100 and 200
	h1.cmd("vconfig add h1-eth0 100")
	h2.cmd("vconfig add h2-eth0 200")
	h3.cmd("vconfig add h3-eth0 100")
	h4.cmd("vconfig add h4-eth0 200")
	
	#Assign and update the default host interface with the newly created vlan interface
	newName = 'h1-eth0.100'
	intf = h1.defaultIntf()
	intf.name = newName
	h1.nameToIntf[newName] = intf
	
	newName2 = 'h2-eth0.200'
	intf2 = h2.defaultIntf()
	intf2.name = newName2
	h2.nameToIntf[newName2] = intf2
	
	newName3 = 'h3-eth0.100'
	intf3 = h3.defaultIntf()
	intf3.name = newName3
	h3.nameToIntf[newName3] = intf3
	
	newName4 = 'h4-eth0.200'
	intf4 = h4.defaultIntf()
	intf4.name = newName4
	h4.nameToIntf[newName4] = intf4
	
	#Assign the host with an ip address 
	h1.cmd("ifconfig h1-eth0.100 10.0.10.1 netmask 255.255.255.0")
	h2.cmd("ifconfig h2-eth0.200 10.0.10.2 netmask 255.255.255.0")
	h3.cmd("ifconfig h3-eth0.100 10.0.10.3 netmask 255.255.255.0")
	h4.cmd("ifconfig h4-eth0.200 10.0.10.4 netmask 255.255.255.0")
	
	#Make sure that the vlan interfaces are up
	h1.cmd("ifconfig add h1-eth0.100 up")
	h2.cmd("ifconfig add h2-eth0.200 up")
	h3.cmd("ifconfig add h3-eth0.100 up")
	h4.cmd("ifconfig add h4-eth0.200 up")
	
	CLI(net)
	net.stop()		

if __name__ == '__main__':		
	# Tell mininet to print useful information		
	#setLogLevel('info')		
	runExperiment()

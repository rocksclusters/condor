#$Id: __init__.py,v 1.2 2010/09/07 23:53:12 bruno Exp $
# 
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.4 (Maverick)
# 
# Copyright (c) 2000 - 2010 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log: __init__.py,v $
# Revision 1.2  2010/09/07 23:53:12  bruno
# star power for gb
#
# Revision 1.1  2009/12/07 19:53:09  phil
# Add a command to easily print the ip (interface in condor speak) of
# a network.
#
#

import rocks.commands
import rocks.ip

class Command(rocks.commands.HostArgumentProcessor,
	rocks.commands.report.command):
	"""
	Output the host IP address associated with a named subnet on a 
        particular host. 

	<arg type='string' name='host'>
	One host name.
	</arg>

	<arg type='string' name='subnet'> 
	subnet to match
	</arg> 

	<example cmd='report host condor interface compute-0-0 private'>
	Output the the IP Address of the private interface on compute-0-0.
	Suitable for using in Condor Configuration Files
	</example>

	<example cmd='report host condor interface vm-container-0-0 private'>
	Output the the IP Address of the private interface on vm-container-0-0.
        If multiple interfaces are attached to the private interface (e.g. VLAN
        bridges) pick the interface with a configured address in the named
        subnet.
	</example>
	"""

	def run(self, params, args):


		(args, subnet) = self.fillPositionalArgs(('subnet',))
		hosts = self.getHostnames(args)
		if not subnet:
			self.abort('missing subnet')
		if len(hosts) < 1:
			self.abort('must supply at least one host')
		self.beginOutput()
	

		# get the information about the subnet 
		self.db.execute("""select subnet,netmask from 
				subnets where name='%s'""" % (subnet))
		network,netmask = self.db.fetchone()

                for host in hosts:
			self.printIP(host,subnet,network,netmask)
		self.endOutput()
		
	def printIP(self, host, subnet, network, netmask):
		mask = rocks.ip.IPAddr(netmask)

		self.db.execute("""select distinctrow net.ip from
			networks net, nodes n, subnets s where net.node = n.id
			and if(net.subnet, net.subnet = s.id, true) and
			n.name = "%s" and s.name= "%s" """ % (host,subnet))

		for row in self.db.fetchall():
			ip, = row
		        if ip != None: 
				ipaddr = rocks.ip.IPAddr(ip)
				calcnet = rocks.ip.IPAddr(ipaddr & mask)
                        	strnet = "%s" % calcnet
			else:
				strnet = "NOT FOUND"

			if strnet == network:	
				self.addOutput(host, ip)


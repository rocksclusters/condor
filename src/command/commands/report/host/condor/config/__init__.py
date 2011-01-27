#$Id: __init__.py,v 1.8 2011/01/27 23:28:01 phil Exp $
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
# Revision 1.8  2011/01/27 23:28:01  phil
# Support submission to EC2
#
# Revision 1.7  2010/10/26 16:37:28  phil
# Fixes to really respect attributes.
#
# Revision 1.6  2010/09/15 23:40:03  phil
# Add the plugin capability of the Rocks command line to reporting the condor host config
#
# Revision 1.5  2010/09/13 20:49:06  phil
# Ready for Rocks 5.4 beta. Updated to new version. Now has a sync host condor similar to sync host network. Small updates on the docs.
#
# Revision 1.4  2010/09/07 23:53:12  bruno
# star power for gb
#
# Revision 1.3  2010/03/03 17:24:39  phil
# 1st stab at automatic integration of condor node running in EC2 to local
# collector.
#
# Revision 1.2  2010/02/27 01:39:39  phil
# Nearly done with removal of CondorConf
#
# Revision 1.1  2010/02/26 06:36:14  phil
# Work in progress to replace CondorConf
#
#

import sys
import os
import pwd
import string
import types
import rocks.commands
from syslog import syslog

class Command(rocks.commands.HostArgumentProcessor,
	rocks.commands.report.command):
	"""

	Output the Condor Local Configuration
 	Uses Rocks Attributes: Condor_Master, Condor_MasterNetwork, 
        Condor_ClientNetwork, Kickstart_PrivateDNSDomain

	<arg type='string' name='host'>
	One host name.
	</arg>

	<param type='string' name='type'>
	How this node will function - [Manager, Worker] - Default: Worker
	</param>

	<param type='string' name='UIDdomain'>
	Override UIDdomain of the Rocks Kickstart_PrivateDNSDomain attribute
	</param>

	<param type='string' name='ConfigFile'>
	Defaults to: /opt/condor/etc/condor_config.local
	</param>

	<example cmd='report host condor config compute-0-0 type=Worker'>
	Create the Condor Configuration for compute-0-0 as a Worker Node
	</example>
	"""

	def writeConfigFile(self, dictList, configFile):
		self.addOutput(self.host, '<file name="%s">' % (configFile))
		keys = dictList.keys()
                keys.sort()
		for key in keys:
			self.addOutput(self.host,'%s = %s' %(key,dictList[key]))
		self.addOutput(self.host, '</file>')


	def initializeDictionary(self):
		### These are the Condor Parameters that we will 
                ### Define. When Adding new ones, Add them here.
		self.dict = {}
		self.dict['ALLOW_WRITE']         = '$(HOSTALLOW_WRITE)' 
		self.dict['COLLECTOR_NAME']      = None
		self.dict['COLLECTOR_SOCKET_CACHE_SIZE']      = 1000 
		self.dict['CONDOR_ADMIN']        = None
		self.dict['CONDOR_DEVELOPERS']   = 'NONE'
		self.dict['CONDOR_DEVELOPERS_COLLECTOR'] = 'NONE'
		self.dict['CONDOR_HOST']         = None
		self.dict['CONDOR_IDS']          = None
		self.dict['CONDOR_SSHD']         = '/usr/sbin/sshd'
		self.dict['CONDOR_SSH_KEYGEN']   = '/usr/bin/ssh-keygen'
		self.dict['CONTINUE']            = 'True'
		self.dict['DAEMON_LIST']         = None
		self.dict['EMAIL_DOMAIN']        = '$(FULL_HOSTNAME)'
		self.dict['FILESYSTEM_DOMAIN']   = None 
		self.dict['HOSTALLOW_WRITE']     = None 
		self.dict['JAVA']                = None
		self.dict['KILL']                = 'False'
		self.dict['LOCK']                = '/tmp/condor-lock.$(HOSTNAME)'
		self.dict['MAIL']                = None
		self.dict['NEGOTIATOR_INTERVAL'] = '120'
		self.dict['NETWORK_INTERFACE']   = None 
		self.dict['PREEMPT']             = 'False'
		self.dict['RANK']                = None
		self.dict['RELEASE_DIR']         = '/opt/condor'
		self.dict['START']               = 'True'
		self.dict['STARTD_EXPRS']        = '$(STARTD_EXPRS)'
		self.dict['SUSPEND']             = 'False'
		self.dict['UID_DOMAIN']          =  None
		self.dict['UPDATE_COLLECTOR_WITH_TCP']  = 'True'
		self.dict['WANT_SUSPEND']        = 'False'
		self.dict['WANT_VACATE']         = 'False'

	def fillFromRocksAttributes(self):
		self.dict['COLLECTOR_NAME'] = "Collector at %s" % \
			(self.db.getHostAttr('localhost', 'Condor_Master'))

		self.dict['DAEMON_LIST'] = \
			self.db.getHostAttr(self.host,'Condor_Daemons')

		self.dict['FILESYSTEM_DOMAIN'] = \
			self.db.getHostAttr('localhost','Kickstart_PublicDNSDomain')

		if self.db.getHostAttr(self.host,'Condor_PortLow') > 0:
			self.dict['LOWPORT'] = \
				self.db.getHostAttr(self.host,'Condor_PortLow')

		if self.db.getHostAttr(self.host,'Condor_PortHigh') > 0:
			self.dict['HIGHPORT'] = \
				self.db.getHostAttr(self.host,'Condor_PortHigh')

		if self.dict['UID_DOMAIN'] is None:
			self.dict['UID_DOMAIN'] =  \
				self.db.getHostAttr('localhost', \
                                'Kickstart_PrivateDNSDomain')

	def fillFromDerived(self):
		## Get the Condor User ID, Group ID
		self.getUID()
		self.dict['CONDOR_IDS'] = '%s.%s' % (self.uid, self.gid)

		self.dict['CONDOR_ADMIN']                = 'condor@%s' % self.cm_fqdn
		self.dict['CONDOR_HOST']                 = self.cm_fqdn
	
	def defineInternalStateVars(self):
		self.user = "condor"
		self.cm_fqdn = self.db.getHostAttr('localhost', 'Condor_Master')
		self.cm_domainName = self.cm_fqdn[string.find(self.cm_fqdn, '.')+1:]
		self.localDomain = self.db.getHostAttr('localhost','Kickstart_PrivateDNSDomain')
	def getUID(self):
		""" finds condor's uid and gid """
		try:
			info = pwd.getpwnam(self.user)
		except KeyError:
			print 'User %s does not exist\n' % self.user
			sys.exit(-1)

		self.uid = info[2]
		self.gid = info[3]

	def setDefaults(self):
		""" set condor location and config files """
		self.user = 'condor'
		self.releaseDir = '/opt/condor'
		self.configMain = self.releaseDir + '/etc/condor_config'
		self.configLocal = self.releaseDir + '/etc/condor_config.local' 
		self.confTemplate = self.releaseDir + '/etc/examples/condor_config.generic'
		self.getUID()

	def find_executable(self, executable, path=None):
		""" find a path to the executable """
		if os.path.isfile(executable):
			return executable

		if path is None:
			path = os.environ['PATH']
		paths = string.split(path, os.pathsep)
	
		for path in paths:
			fullname = os.path.join(path, executable)
			if os.path.isfile(fullname):
				return fullname
		return ''

	def setDedicated(self, dict): 
		if not self.dedicated:
			return

		dict['DedicatedScheduler']  = '"DedicatedScheduler@%s"' % self.cm_fqdn
		dict['MPI_CONDOR_RSH_PATH'] = '$(LIBEXEC)'
		dict['STARTD_EXPRS']        = '$(STARTD_EXPRS), DedicatedScheduler'
		dict['CONDOR_SSHD'] = '/usr/sbin/sshd'
		dict['CONDOR_SSH_KEYGEN'] = '/usr/bin/ssh-keygen'
		self.setPolicy2(dict)


	def setPolicy1(self, dict): 
		# settings for policy 'only allow dedicated jobs'
		dict['START']        = 'True'
		dict['SUSPEND']      = 'False'
		dict['CONTINUE']     = 'True'
		dict['PREEMPT']      = 'False'
		dict['KILL']         = 'False'
		dict['WANT_SUSPEND'] = 'False'
		dict['WANT_VACATE']  = 'False'
		dict['RANK']         = 'Scheduler =?= $(DedicatedScheduler)'


	def setPolicy2(self, dict): 
		# settings for policy 'always run jobs but prefer dedicated ones'
		dict['START']        = 'True'


	def makeConfigLocal(self): 
		""" create a local config file """
		self.dict['CONDOR_DEVELOPERS']           = 'NONE'
		self.dict['CONDOR_DEVELOPERS_COLLECTOR'] = 'NONE'
		self.dict['NEGOTIATOR_INTERVAL']         = '120'
		self.dict['LOCK']                        = '/tmp/condor-lock.$(HOSTNAME)'
		self.dict['RELEASE_DIR']                 = '/opt/condor'
		self.dict['LOCAL_DIR']                   = '/var/opt/condor'
		self.dict['EMAIL_DOMAIN']                = '$(FULL_HOSTNAME)'
		self.dict['RELEASE_DIR']                 = self.releaseDir
		self.dict['MAIL']                        = self.find_executable('mail')
		self.dict['JAVA']                        = self.find_executable('java')
		condorIface = self.command('report.host.condor.interface',
			['%s' % self.host, 
				'%s' % self.db.getHostAttr(self.host, 'Condor_Network')])
		self.dict['NETWORK_INTERFACE']           = condorIface.rstrip()
 
		self.dict['CONDOR_ADMIN']                = 'condor@%s' % self.cm_fqdn
		self.dict['CONDOR_HOST']                 = self.cm_fqdn
		self.dict['HOSTALLOW_WRITE'] = '%s, *.%s, *.%s' % (self.cm_fqdn,self.localDomain,self.dict['UID_DOMAIN'])
		allowHosts=self.db.getHostAttr(self.host, 'Condor_HostAllow')
		allowHosts.lstrip()
		if len(allowHosts) > 1:
			if allowHosts.find('+') == 0:
				self.dict['HOSTALLOW_WRITE'] += "," + allowHosts.lstrip('+')
			else:
				self.dict['HOSTALLOW_WRITE'] = allowHosts

	
		self.localDir = self.dict['LOCAL_DIR']
		# if self.node == 'frontend':
		#	self.dict['COLLECTOR_NAME'] = 'Collector at %s' % self.host

		#self.setDedicated(dict)

	def Config(self):
		""" configuration driver """
		self.setDefaults()
		self.makeConfigLocal()



	def run(self, params, args):

		self.initializeDictionary()
		self.type, self.UIDdomain, self.ConfigFile = self.fillParams([('type','Worker'),('UIDdomain',),('ConfigFile','/opt/condor/etc/condor_config.local') ])
		self.defineInternalStateVars()
		self.beginOutput()

                for host in self.getHostnames(args):
			self.host = host
			self.fillFromDerived()
			self.fillFromRocksAttributes()
			self.Config()
			self.runPlugins((host,self.dict))
			self.writeConfigFile(self.dict, self.configLocal)

		self.endOutput(padChar='')

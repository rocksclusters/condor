# $Id: plugin_shared_secret.py,v 1.4 2011/07/23 02:30:55 phil Exp $
# 
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.4.3 (Viper)
# 
# Copyright (c) 2000 - 2011 The Regents of the University of California.
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
# 	Development Team at the San Diego Supercomputer Center at the
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
# $Log: plugin_shared_secret.py,v $
# Revision 1.4  2011/07/23 02:30:55  phil
# Viper Copyright
#
# Revision 1.3  2010/10/26 16:37:28  phil
# Fixes to really respect attributes.
#
# Revision 1.2  2010/10/21 00:11:17  phil
# Slightly more relaxed acceptance of local nodes.
#
# Revision 1.1  2010/10/16 00:40:28  phil
# Use a shared secret file of Condor_PasswordAuth attribute is set
#
# Revision 1.3  2009/05/01 19:07:00  mjk
# chimi con queso
#
# Revision 1.2  2009/04/23 17:12:29  bruno
# cleanup 'rocks remove host' command
#
# Revision 1.1  2009/03/13 22:19:56  mjk
# - route commands done
# - cleanup of rocks.host plugins
#
# Revision 1.2  2009/03/06 21:28:12  bruno
# need to look at node_attributes table.
#
# Revision 1.1  2008/12/18 20:01:33  mjk
# attribute commands
#

import rocks.commands

class Plugin(rocks.commands.Plugin):

	def provides(self):
		return 'shared_secret'

	def run(self, argv):
		# Argv contains the hostname and the in memory key-value store
	        # that is eventually written to 
		# /opt/condor/etc/condor_config.local
		# plugins can add/change/remove keys from the store

		# 1. Get the hostname and the key-value store, which
		#    is a python dictionary 
		host, kvstore = argv 

		authbypass=self.owner.db.getHostAttr(host,"Condor_PasswordAuth")
		if  authbypass is None or not (authbypass.lower() == "yes" or authbypass.lower() == "true"):
			return

		# The following would add CONDOR_SAMPLE=Sample Plugin
		# the key = value dictionary (kvstore)  that is written out
		#
		# Example 1. Read an attribute from the database and set 
		# the values
		value = self.db.getHostAttr(host, 'Condor_Master')
		kvstore['SEC_PASSWORD_FILE'] = '/var/opt/condor/pool_password'
		kvstore['SEC_ADVERTISE_STARTD_AUTHENTICATION'] = 'REQUIRED'
		kvstore['SEC_ADVERTISE_STARTD_INTEGRITY'] = 'REQUIRED'
		kvstore['SEC_ADVERTISE_STARTD_AUTHENTICATION_METHODS'] = "PASSWORD"
		kvstore['SEC_CLIENT_AUTHENTICATION_METHODS'] = "FS, PASSWORD, KERBEROS, GSI"

		kvstore['ALLOW_ADVERTISE_STARTD'] = 'condor_pool@$(UID_DOMAIN)/*.%s' % (kvstore['UID_DOMAIN'])
		allowHosts=self.db.getHostAttr(host, 'Condor_HostAllow')
		allowHosts.lstrip()
		if len(allowHosts) > 1:
			if allowHosts.find('+') == 0:
				allowHosts = allowHosts.lstrip('+')
				for host in allowHosts.split(','):
					kvstore['ALLOW_ADVERTISE_STARTD'] += "," + \
					"condor_pool@$(UID_DOMAIN)/%s" % host


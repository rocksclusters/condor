#!/bin/sh
#
# This file should remain OS independent
#
# $Id: bootstrap.sh,v 1.14 2012/11/27 00:48:54 phil Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 6.2 (SideWinder)
# 
# Copyright (c) 2000 - 2014 The Regents of the University of California.
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
# $Log: bootstrap.sh,v $
# Revision 1.14  2012/11/27 00:48:54  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.13  2012/05/06 05:48:53  phil
# Copyright Storm for Mamba
#
# Revision 1.12  2011/07/23 02:30:55  phil
# Viper Copyright
#
# Revision 1.11  2010/09/07 23:53:12  bruno
# star power for gb
#
# Revision 1.10  2009/05/01 19:07:13  mjk
# chimi con queso
#
# Revision 1.9  2008/10/18 00:56:06  mjk
# copyright 5.1
#
# Revision 1.8  2008/10/15 20:13:03  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.7  2008/04/30 14:24:40  phil
# Bootstrap correctly so that examples will build
#
# Revision 1.6  2008/03/06 23:41:49  mjk
# copyright storm on
#
# Revision 1.5  2007/06/23 04:03:31  mjk
# mars hill copyright
#
# Revision 1.4  2006/09/11 22:47:53  mjk
# monkey face copyright
#
# Revision 1.3  2006/08/10 00:10:10  mjk
# 4.2 copyright
#
# Revision 1.2  2006/08/08 20:44:41  bruno
# more bootstrapping needed
#
# Revision 1.1  2006/08/07 21:36:19  bruno
# bootstrap condor
#
# Revision 1.5  2006/07/25 23:44:55  mjk
# add evl bootstrap
#
# Revision 1.4  2006/02/14 21:47:09  mjk
# use dmx from centos
#
# Revision 1.3  2006/02/14 20:52:14  mjk
# FlightGear bootstrapping
#
# Revision 1.2  2006/02/07 22:01:31  mjk
# add bootstrapping
#
# Revision 1.1  2006/02/07 22:00:47  mjk
# add bootstrapping
#


if [ ! -f "$ROLLSROOT/../../bin/get_sources.sh" ]; then
       echo "To compile this roll on Rocks 6.1.1 or older you need to install a newer rocks-devel rpm.
Install it with:
rpm -Uvh https://googledrive.com/host/0B0LD0shfkvCRRGtadUFTQkhoZWs/rocks-devel-6.2-3.x86_64.rpm 
If you need an older version of this roll you can get it from:
https://github.com/rocksclusters-attic" 
	exit 1
fi
if [ ! -f "$ROLLSROOT/../../bin/get_sources.sh" ]; then
	echo "To compile this roll on Rocks 6.1.1 or older you need to install a newer rocks-devel rpm.
Install it with:
rpm -Uvh https://googledrive.com/host/0B0LD0shfkvCRRGtadUFTQkhoZWs/rocks-devel-6.2-3.x86_64.rpm
If you need an older version of this roll you can get it from:
https://github.com/rocksclusters-attic"
	exit 1
fi

. $ROLLSROOT/etc/bootstrap-functions.sh

compile_and_install htcondor
compile rocks
install rocks-condor

install_os_packages htcondor

# Make sure we have the condor account
# will complain if condor already exists, can ignore
/usr/sbin/useradd -u 407 -c "Condor Daemon Account" condor

# Get the Condor Environment
. /etc/profile.d/rocks-condor.sh


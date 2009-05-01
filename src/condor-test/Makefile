#
# $Id: Makefile,v 1.25 2009/05/01 19:07:14 mjk Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		       version 5.2 (Chimichanga)
# 
# Copyright (c) 2000 - 2009 The Regents of the University of California.
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
# $Log: Makefile,v $
# Revision 1.25  2009/05/01 19:07:14  mjk
# chimi con queso
#
# Revision 1.24  2008/12/10 21:37:40  bruno
# - condor roll is now buildable outside rocks source tree
#
# - updated bits to v7.0.5
#
# Revision 1.23  2008/10/18 00:56:06  mjk
# copyright 5.1
#
# Revision 1.22  2008/07/30 23:07:06  bruno
# very simple test case
#
# Revision 1.21  2008/04/30 14:24:41  phil
# Bootstrap correctly so that examples will build
#
# Revision 1.20  2008/03/06 23:41:49  mjk
# copyright storm on
#
# Revision 1.19  2007/06/23 04:03:32  mjk
# mars hill copyright
#
# Revision 1.18  2007/06/14 19:27:05  phil
# Build tutorial even if MPI is not installed
#
# Revision 1.17  2006/09/11 22:47:55  mjk
# monkey face copyright
#
# Revision 1.16  2006/08/10 00:10:12  mjk
# 4.2 copyright
#
# Revision 1.15  2005/10/12 18:08:57  mjk
# final copyright for 4.1
#
# Revision 1.14  2005/09/16 01:02:32  mjk
# updated copyright
#
# Revision 1.13  2005/06/23 00:32:55  nadya
# add flag for compiling test program (for std universe) from tutorial in 32-bit mode
#
# Revision 1.12  2005/06/22 04:04:23  nadya
# add examples of condor tests and submit files for different universes
#
# Revision 1.11  2005/06/21 18:17:34  nadya
# workaround to give flag to ld to compile test program
# only in 32bit because for 64bit there are no libs
#
# Revision 1.10  2005/06/21 02:25:12  nadya
# compile test program for each platform
#
# Revision 1.9  2005/06/16 01:17:24  nadya
# give cat a full name
#
# Revision 1.8  2005/05/24 21:22:07  mjk
# update copyright, release is not any closer
#
# Revision 1.7  2004/07/13 02:58:35  nadya
# rm SEDSPEC entries
#
# Revision 1.6  2004/03/03 21:43:01  bruno
# add the small test to the test suite
#
# Revision 1.5  2004/02/09 23:55:18  nadya
# fix SEDSPEC
#
# Revision 1.4  2004/02/09 23:26:30  nadya
# add rules
#
# Revision 1.3  2003/11/14 01:00:46  nadya
# add seq data files
#
# Revision 1.2  2003/11/14 00:56:40  nadya
# typo
#
# Revision 1.1  2003/11/14 00:43:36  nadya
# initial revision
# added condor testing dir
#
#

PKGROOT		= /opt/condor
REDHAT.ROOT	= $(PWD)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk


build:
	mkdir -p $(ROOT)/$(PKGROOT)/tests
	cp hello.* $(ROOT)/$(PKGROOT)/tests


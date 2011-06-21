# 
# $Id: Makefile,v 1.28 2011/06/21 22:19:11 phil Exp $
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
# $Log: Makefile,v $
# Revision 1.28  2011/06/21 22:19:11  phil
# Update condor to version 7.6.1
#
# Revision 1.27  2010/10/24 04:05:21  bruno
# can't have white space after a '\', *phil*!
#
# jeez, i mean, seriously? is this
# your first rodeo? and, "make" has only been around since 1977
# (http://en.wikipedia.org/wiki/Make_(software)). hell that, was even before
# disco (which i know you love -- dancing queen!). you remember 1977. carter
# became president (that worked out!), Fleetwood Mac released "Rumors" (you
# *totally* made out to "you make lovin' fun"), KLM and Pan Am 747's collide
# at Tenerife (sad), The Clash releases their debut album (which you love,
# which makes up for your Fleetwood Mac obsession), in may, you go to see this
# little known movie "Star Wars", and you say, "i liked it, but i don't think
# it will stand up to the test of time", you attended Elvis Presley's concert
# at Indiana's Market Square Arena and you said "looks like that brother needs
# a banana peanut butter sandwich  (turns out, it was Elvis's last concert),
# new york has a blackout for 25 hours (you were quoted as saying, "i dare
# you to pee on this!"), you look at the TRS-80 and say "that should be called
# the TRASH-80!), while in geneva, you eye the new porche 928 and say "i like
# that", then you watch Reggie Jackson hit 3, count 'em 3!, homeruns against
# the Dodgers (Dodgers suck!), lockhead's stealth fighter makes it's first
# flight and you respond "i don't see a future in it".
#
# regardless, i love you man.
#
# Revision 1.26  2010/10/22 20:43:55  phil
# Updated to 7.4.4 (released Oct 18, 2010).
# Keep 7.4.3 Tarballs in tree.
# Support pool password creation.
# Adjust graph to properly respect Condor_Client attribute
#
# Revision 1.25  2010/09/07 23:53:12  bruno
# star power for gb
#
# Revision 1.24  2009/05/01 19:07:14  mjk
# chimi con queso
#
# Revision 1.23  2008/12/10 21:36:04  bruno
# - condor roll is now buildable outside rocks source tree
#
# - updated bits to v7.0.5
#
# Revision 1.22  2008/10/18 00:56:06  mjk
# copyright 5.1
#
# Revision 1.21  2008/04/29 21:56:40  phil
# Update to 7.0.1. Build under V
#
# Revision 1.20  2008/04/29 20:35:39  phil
# Get rid of specific spec file
#
# Revision 1.19  2008/03/06 23:41:49  mjk
# copyright storm on
#
# Revision 1.18  2007/06/23 04:03:32  mjk
# mars hill copyright
#
# Revision 1.17  2006/09/11 22:47:55  mjk
# monkey face copyright
#
# Revision 1.16  2006/08/10 00:10:12  mjk
# 4.2 copyright
#
# Revision 1.15  2006/07/23 05:27:51  phil
# Move to version 6.8.0
#
# Revision 1.14  2005/12/07 19:12:58  nadya
# deal with mpi-related scripts via patch-files
#
# Revision 1.13  2005/10/30 02:01:32  nadya
# add mpi scripts for handling parallel jobs
#
# Revision 1.12  2005/10/30 01:47:45  nadya
# latest release. Not sure if it's stable
#
# Revision 1.11  2005/10/12 18:08:57  mjk
# final copyright for 4.1
#
# Revision 1.10  2005/09/16 01:02:32  mjk
# updated copyright
#
# Revision 1.9  2005/06/16 01:14:07  nadya
# give cat a full name
#
# Revision 1.8  2005/05/24 21:22:07  mjk
# update copyright, release is not any closer
#
# Revision 1.7  2005/05/12 02:11:24  nadya
# revert to making from downloaded binaries, new verison 6.7.6
# add making *wsdd. files, etc (was not in previous condor version)
#
# Revision 1.6  2005/03/28 22:16:05  nadya
# compilie condor from source
#
# Revision 1.5  2005/03/23 20:42:39  nadya
# clean old entries, reorganize dirs
#
# Revision 1.4  2004/07/13 02:57:27  nadya
# rm SEDSPEC entries
#
# Revision 1.3  2004/02/09 23:55:17  nadya
# fix SEDSPEC
#
# Revision 1.2  2004/02/09 23:20:10  nadya
# add rules
#
# Revision 1.1  2003/10/14 20:28:33  nadya
# initial revision
#
#


PKGROOT		= /opt/condor
REDHAT.ROOT	= $(PWD)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

TESTARCH =	x86_64
ifeq ($(ARCH),$(TESTARCH))
X86_64	=	_64
else
X86_64	=
endif

NAME = condor
EXT  = x86$(X86_64)_rhap_5-stripped
TARBALL = $(NAME)-$(VERSION)-$(EXT)

version.mk: version.mk.in
	/bin/cat version.mk.in ../version.mk > version.mk
build::

install::
	mkdir -p $(ROOT)/$(PKGROOT)
	$(TAR) xzvf $(TARBALL).tar.gz -C $(ROOT)
	( 	cd $(ROOT)/$(NAME)-$(VERSION)-$(EXT); 	\
		mv * $(ROOT)/$(PKGROOT);	\
		cd ..; 				\
		rmdir $(NAME)-$(VERSION)-$(EXT)	\
	)

clean::
	rm -rf $(NAME)-$(VERSION)-$(EXT)
	rm -f version.mk


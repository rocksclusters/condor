#! /bin/bash
#
# remove requirement that htcondor requires libvirt
/usr/lib/rpm/find-requires $* | sed -e '/libvirt\.*/d' | sed -e '/^[[:space:]]*$/d' | sed -e '/^#/d'


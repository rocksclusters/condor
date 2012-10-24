#!/bin/bash
#
# Test vm machines
#
# prerequisite 2 vm-container already up and running
#
# no virtual compute already installed
#
# maxrun time 2 hours

function reportError {
	echo $1
	exit -1
}


function Pause {
	echo $1 press any key to continue execution
	OLDCONFIG=`stty -g`
	stty -icanon -echo min 1 time 0
	dd count=1 2>/dev/null
	stty $OLDCONFIG
}


TESTUSER=testcondor

#echo creating user test
#useradd -m $TESTUSER
#rocks sync users
#
#

cp -p scripts/job.sh scripts/script.dag /home/$TESTUSER/
chown $TESTUSER /home/$TESTUSER/job.sh /home/$TESTUSER/script.dag
su - $TESTUSER -c "condor_submit script.dag " || reportError "Unable to run condor_submit"

su - $TESTUSER -c "condor_wait log.log"
if [ ! -f /home/$TESTUSER/testcondor ];then
	reportError "Condor job did not create the test file."
fi

 

#!/bin/bash
#
# Test Condor submit
#
# maxrun time 2 minutes

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

echo creating user test
useradd -m $TESTUSER
rocks sync users

while [ true ]; do
	sleep 5
	if [ -d /home/$TESTUSER/ ];then
		break
	fi
done

cp -p scripts/job.sh scripts/script.dag /home/$TESTUSER/
chown $TESTUSER /home/$TESTUSER/job.sh /home/$TESTUSER/script.dag
su - $TESTUSER -c "condor_submit script.dag " || reportError "Unable to run condor_submit"

su - $TESTUSER -c "condor_wait log.log"
if [ ! -f /home/$TESTUSER/testcondor ];then
	reportError "Condor job did not create the test file."
fi

 

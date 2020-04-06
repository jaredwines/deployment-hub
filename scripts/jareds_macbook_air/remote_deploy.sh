#!/bin/bash
if [ ! -z "$1" ]
then
	remote_deploy_script="$1"
	if [ $remote_deploy_script == "jaredwines.com" ]
	then
		ssh jaredwines.com /home/jaredw/.scripts/remote_deploy_jaredwines.com.sh "$2"
	fi

else
	echo "First arg can NOT be empty, try [remote_deploy.sh $remote_deploy_script]."
fi
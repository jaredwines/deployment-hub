#!/bin/bash
if [ ! -z "$1" ]
then
	remote_deploy="$1"

	if [ $remote_deploy == "jaredwines.com" ]
	then
		echo "Connection to $remote_deploy."
		ssh -q $host exit
		result="$?"
		if [ $result == "0" ]
		then
			echo "Successfully connected to $remote_deploy."
			ssh jaredwines.com /home/jaredw/.scripts/remote_deploy_jaredwines.com.sh "$2"
		else
			echo "Failed to connect to $remote_deploy (Error code: $result)."
	fi

else
	echo "First arg can NOT be empty, try [remote_deploy.sh $remote_deploy]."
fi
#!/bin/bash
excute_remote_script(){
h="$1"
p="$2"
a="$3"

echo "Connection to $remote_deploy."
ssh -q $host exit
result="$?"
if [ $result == "0" ]
then
	echo "Successfully connected to $remote_deploy."
	ssh "$h" "$p" "$a"
else
	echo "Failed to connect to $remote_deploy (Error code: $result)."
fi
}

if [ ! -z "$1" ]
then
	remote_deploy="$1"
	arg="$2"
	if [ $remote_deploy == "jaredwines.com" ]
	then
		host=jaredwines.com
		path_to_script=/home/jaredw/.scripts/remote_deploy_jaredwines.com.sh
		excute_remote_script() "$host" "$path_to_script" "$arg"
	fi

else
	echo "First arg can NOT be empty, try [remote_deploy.sh $remote_deploy]."
fi
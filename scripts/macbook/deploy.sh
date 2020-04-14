#!/bin/bash
excute_remote_script(){
host="$1"
path_to_script="$2"
arg="$3"

echo "Connecting to $remote_deploy."
ssh -q $host exit
result="$?"
if [ $result == "0" ]
then
	echo "Successfully connected to $remote_deploy."
	ssh "$host" "$path_to_script" "$arg"
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
		path_to_script=/home/jaredw/.scripts/deploy_jaredwines.com.sh
		excute_remote_script "$host" "$path_to_script" "$arg"
	else
		echo "Could not find $1."
	fi

else
	echo "Arg can NOT be empty, try [deploy nameofhost]."
	echo "Valited host are [ jaredwines.com ] and [ local ]."
fi
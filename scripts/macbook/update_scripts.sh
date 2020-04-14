#!/bin/bash
shopt -s extglob
update_scripts(){
	git_repo=git@github.com:jaredwines/deployment.git
	scripts_dir=.scripts
	scripts_repo_dir="$1"
	host="$1"

	tmp_deployment_path=$HOME/.tmp_process_update_scripts
	scripts_path=$HOME/$scripts_dir
	scripts_repo_path=$tmp_deployment_path/scripts/$scripts_repo_dir

	echo "Starting update for $host's scripts."
	echo "Downloading script(s) to $host."
	if [ -d "$tmp_deployment_path" ]; then
		rm -rf $tmp_deployment_path
	fi
	mkdir $tmp_deployment_path

	if git clone $git_repo $tmp_deployment_path
	then
		echo "Download completed."
	else
		echo "Download failed."
		exit 1
	fi

	echo "Installing script(s) to $host."
	if [ -d "$scripts_path" ] || [ "$(ls -A $scripts_path)" ]
	then
		rm -rf $scripts_path/*
	elif [ ! -d "$scripts_path" ]
	then
		mkdir $scripts_path
	fi

	if ( mv $scripts_repo_path/* $scripts_path && chmod +x $scripts_path/*.sh && rm -rf $tmp_deployment_path )
	then
		echo "Successfully installed script(s) to $host."
	else
		echo "Failed to install script(s) to $host."
		exit 1
	fi

	echo "Finshed update for $host's scripts."
}

if [ $1 == "local" ]
then
update_scripts $(hostname -s)
elif [ $# -lt 3 ]
then
	host="$1"
	update_local_scripts="$2"

	if [ "$update_local_scripts" == "-l" ]
	then
		update_scripts $(hostname -s)
	fi

	echo "Connection to $host."
	ssh -q $host exit
	result="$?"
	if [ $result == "0" ]
	then
		echo "Successfully connected to $host."
		ssh $host "$(typeset -f update_scripts); update_scripts $1"
	else
		echo "Failed to connect to $host (Error code: $result)."
		exit 1
	fi
else
	echo "Must be aleast two agurment, examples [update_scripts nameofhost] [update_scripts nameofhost -l]."
fi
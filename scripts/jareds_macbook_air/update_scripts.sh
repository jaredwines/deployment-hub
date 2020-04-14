#!/bin/bash
shopt -s extglob

update_scripts(){
	git_repo=git@github.com:jaredwines/deployment.git
	scripts_dir=.scripts
	scripts_repo_dir="$1"

	tmp_deployment_path=$HOME/.tmp_process_update_scripts
	scripts_path=$HOME/$scripts_dir
	scripts_repo_path=$tmp_deployment_path/scripts/$scripts_repo_dir

	echo "Downloading script(s) to $scripts_repo_dir."
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

	echo "Installing script(s) to $scripts_repo_dir."
	if [ -d "$scripts_path" ] || [ "$(ls -A $scripts_path)" ]
	then
		rm -rf $scripts_path/*
	elif [ ! -d "$scripts_path" ]
	then
		mkdir $scripts_path
	fi

	if ( mv $scripts_repo_path/* $scripts_path && chmod +x $scripts_path/*.sh && rm -rf $tmp_deployment_path )
	then
		echo "Successfully installed script(s) to $scripts_repo_dir."
	else
		echo "Failed to install script(s) to $scripts_repo_dir."
		exit 1
	fi
}

if [ $# -eq 0 ]
then
	update_scripts jareds_macbook_air
else
	host="$1"
	run_update_scripts_jareds_macbook_air="$2"

	echo "Connection to $host."
	ssh -q $host exit
	result="$?"
	if [ $result == "0" ]
	then
		echo "Successfully connected to $host."
		ssh $host "$(typeset -f update_scripts); update_scripts $1"
		if [ "$run_update_scripts_jareds_macbook_air" == "-l" ]
		then
			update_scripts jareds_macbook_air
		fi
	else
		echo "Failed to connect to $host (Error code: $result)."
		exit 1
	fi
fi
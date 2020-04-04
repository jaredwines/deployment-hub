#!/bin/bash
shopt -s extglob

git_repo=git@github.com:jaredwines/deployment.git
scripts_repo_dir=scripts
scripts_dir_name=.scripts

tmp_deployment_dir=$HOME/.tmp_process_update_scripts
scripts_dir=$HOME/$scripts_dir_name

echo "Downloading script(s)."
if [ -d "$tmp_deployment_dir" ]; then
	rm -rf $tmp_deployment_dir
fi
mkdir $tmp_deployment_dir

if git clone $git_repo $tmp_deployment_dir
then
	echo "Download complete."
else
	echo "Download fail."
	exit 1
fi

echo "Installing script(s)."
if [ -d "$scripts_dir" ] && [ "$(ls -A $scripts_dir)" ]
then
	rm -rf $scripts_dir/*
elif [ ! -d "$scripts_dir" ]
then
	mkdir $scripts_dir
fi

if mv $tmp_deployment_dir/$scripts_repo_dir/* $scripts_dir && chmod +x $scripts_dir/*.sh!(ssh.*) && rm -rf $tmp_deployment_dir
then
	echo "Successfully installed script(s)."
else
	echo "Failed to install script(s)."
	exit 1
fi
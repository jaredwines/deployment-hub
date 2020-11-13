#!/bin/bash
shopt -s extglob


git_repo=git@github.com:jaredwines/homeassistant-config.git
dir_name=homeassistant
app_name=homeassistant

tmp_deploy_dir=$HOME/.tmp_process_deploy_$app_name
app_dir=/home/pi/$dir_name

# Create temporary directory for repository.
echo "Downloading $app_name."
if [ -d "$tmp_deploy_dir" ]; then
	rm -rf $tmp_deploy_dir
fi
mkdir $tmp_deploy_dir

# Clone repository.
if git clone $git_repo $tmp_deploy_dir
then
	echo "Download completed."
else
	echo "Download failed."
	exit 1
fi

# Clear directory.
echo "Deploying $app_name."
if [ -d "$app_dir" ] && [ "$(ls -A $app_dir)" ]
then
	rm -rf $app_dir/*
elif [ ! -d "$app_dir" ]
then
	mkdir $app_dir
fi

# Move souce data from temporary directory to app directory then delete temporary folder
if ( mv $tmp_deploy_dir/*!(.git*) $app_dir && rm -rf $tmp_deploy_dir )
then
	echo "Successfully deployed $app_name."
else 
	echo "Failed to deploy $app_name."
	exit 1
fi
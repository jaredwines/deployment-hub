#!/bin/bash
git_repo=git@github.com:jaredwines/jaredwines.com.git
website_dir_name=jaredwines.com
website_url=www.jaredwines.com
maintenance_mode="$1"

ssh jaredw@jaredwines.com /bin/bash << EOF
	shopt -s extglob

	tmp_deploy_dir=$HOME/.tmp_process_deploy_$website_url
	website_dir=$HOME/$website_dir_name

	echo "Downloading $website_url."
	if [ -d "$tmp_deploy_dir" ]; then
		rm -rf $tmp_deploy_dir
	fi
	mkdir $tmp_deploy_dir

	if git clone $git_repo $tmp_deploy_dir
	then
		echo "Download complete."
	else
		echo "Download fail."
		exit 1
	fi

	echo "Deploying $website_url."
	if [ -d "$website_dir" ] && [ "$(ls -A $website_dir)" ]
	then
		rm -rf $website_dir/*
	elif [ ! -d "$website_dir" ]
	then
		mkdir $website_dir
	fi

	if mv $tmp_deploy_dir/*!(.git*) $website_dir && rm -rf $tmp_deploy_dir
	then
		echo "Successfully deployed $website_url."
	else 
		echo "Failed to deploy $website_url."
		exit 1
	fi

	# Maintenance Mode
	if [ maintenance_mode == "-m" ]
	then
		sed -i 's/RewriteEngine Off/RewriteEngine On/g' $HOME/.htaccess
		echo "Maintenance mode is on."
	else
		sed -i 's/RewriteEngine On/RewriteEngine Off/g' $HOME/.htaccess
	fi
EOF

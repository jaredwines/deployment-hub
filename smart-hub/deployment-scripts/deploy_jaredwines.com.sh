#!/bin/bash
shopt -s extglob

git_repo=git@github.com:jaredwines/jaredwines.com.git
branch=master

website_dir_name=jaredwines.com
website_url=www.jaredwines.com

tmp_deploy_dir=$HOME/.tmp_process_deploy_$website_url
website_dir=$HOME/$website_dir_name

maintenance_mode=false

while [ ! -z "$1" ]; do
  case "$1" in
     --maintenance|-m)
         shift
         maintenance_mode=true
         ;;
     --branch|-b)
         shift
         branch=${@: -1} 
         ;;
  esac
shift
done

# Create temporary directory for repository.
echo "Downloading $website_url."
if [ -d "$tmp_deploy_dir" ]; then
	rm -rf $tmp_deploy_dir
fi
mkdir $tmp_deploy_dir

# Clone website repository.
if git clone -b $branch $git_repo $tmp_deploy_dir
then
	echo "Download completed."
else
	echo "Download failed."
	exit 1
fi

# Clear website directory.
echo "Deploying $website_url."
if [ -d "$website_dir" ] && [ "$(ls -A $website_dir)" ]
then
	rm -rf $website_dir/*
elif [ ! -d "$website_dir" ]
then
	mkdir $website_dir
fi

# Move website souce data from temporary directory to website directory then delete temporary folder
if ( mv $tmp_deploy_dir/*!(.git*) $website_dir && rm -rf $tmp_deploy_dir )
then
	# Enable maintenance mode if arg="-m" else disable maintenance mode.
	if [ $maintenance_mode == true ]
	then
		sed -i 's/RewriteEngine Off/RewriteEngine On/g' $HOME/.htaccess
		echo "Maintenance mode is enable."
	else
		sed -i 's/RewriteEngine On/RewriteEngine Off/g' $HOME/.htaccess
		echo "Maintenance mode is disable."
	fi
	echo "Successfully deployed $website_url."
else 
	echo "Failed to deploy $website_url."
	exit 1
fi
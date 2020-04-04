#!/bin/bash
shopt -s extglob

git_repo=git@github.com:jaredwines/jaredwines.com.git
website_dir_name=jaredwines.com
website_url=www.jaredwines.com

tmp_deploy_dir=$HOME/.tmp_process_deploy_$website_url
website_dir=$HOME/$website_dir_name

echo "Downloading $website_url."
if [ -d "$tmp_deploy_dir" ]; then
	rm -rf $tmp_deploy_dir
fi
mkdir $tmp_deploy_dir

git clone $git_repo $tmp_deploy_dir
echo "Download complete."

echo "Deploying $website_url."
if [ -d "$website_dir" ]
then
	rm -rf $website_dir/*
else
	mkdir $website_dir
fi

mv $tmp_deploy_dir/*!(.git*) $website_dir
rm -rf $tmp_deploy_dir
echo "Successfully deployed $website_url."

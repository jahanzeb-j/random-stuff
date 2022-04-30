#!/bin/bash

echo " #### Backup started... #### "

# get curr date

currDate=$(date +'%m.%d')

echo "Current date -- $currDate"

mkdir ./backups/$currDate || errCopy=false

echo "Folder created" || echo "ERROR"

echo "### Copying Started..  ###"

cp -r ./*.txt ./backups/$currDate/ || errCopy=false

echo "### Copied ... ####"

$errCopy || echo "ERROR"

$errCopy && echo "SUCCESS.."
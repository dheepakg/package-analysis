#!/usr/bin/env bash

init_file=./packages.csv

echo "start of program"


while IFS=, read -r status package_name
do

	if [[ $status = 'Y' ]]; then
		echo $package_name" is already processed (No actions needed)"
		
	else
		echo $package_name $status
#		sed -i.bak "s/$status,$package_name/P,pkg33/g" $init_file && rm $init_file.bak
		sed -i.bak "s/$status,$package_name/P,$package_name/g" $init_file && rm $init_file.bak
		#echo "some Processing Put your Py code here"
		#var_py=$(python test.py 'Inside ' ' python code')
		#echo $var_py is true then execute below statement
		sed -i.bak "s/P,$package_name/Y,$package_name/g" $init_file && rm $init_file.bak


	fi

done <$init_file		


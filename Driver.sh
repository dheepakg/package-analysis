#!/usr/bin/env bash

init_file=./packages.csv

echo "start of program"


echo 0>qry.sql


while IFS=, read -r status package_name
do

	if [[ $status = 'Y' ]]; then
		echo $package_name" is already processed (No actions needed)"
		
	else
		echo $package_name $status
#		sed -i.bak "s/$status,$package_name/P,pkg33/g" $init_file && rm $init_file.bak
		sed -i.bak "s/$status,$package_name/P,$package_name/g" $init_file && rm $init_file.bak
		#echo "some Processing Put your Py code here"
		echo 'python3 main.py' $package_name
		var_py=$(python3 main.py $package_name)
		
		echo $var_py>> qry.sql 
		sed -i.bak "s/P,$package_name/Y,$package_name/g" $init_file && rm $init_file.bak


	fi

done <$init_file		

cat qry.sql

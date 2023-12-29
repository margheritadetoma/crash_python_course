#! /bin/bash


mkdir bandpass_margherita #make a dir called bandpasso_margherita
cp -r bandpass_raw bandpass_margherita

#Move in the right directory
cd bandpass_margherita

#Find only the files type in the directory whose name ends with a certain extension,
#then the 'sed' commands effectively extracts the file extension.
#Then we sort the extension in alphabetic order and count the number of occurrences 
#of each unique file extension.

find . -type f -name '*.*' | sed 's|.*\.||' | sort | uniq -c
ext=$(find . -type f -name '*.*' | sed 's|.*\.||' | sort | uniq)

#Print the extensions and their occurances
echo $ext


#Create an empty array
extensions=()

#Find the extensions and save them in the array 'extensions'
for i in $ext; do extensions+=($i); done


#For each different extension 'e', it finds all the file with
#that extension and go to read the second line.
#Then it renames the file as required (with photons/energy) and
#adds the '.filt' extension.

for e in ${extensions[@]}; do
	for file in *.$e; do
		x=$(sed -n '2p' $file)
		
		new_string=$(echo "$x" | tr -d '#') #strip the ash
		new_string=${new_string// /} #strip the space
	
		if [[ $new_string =~ [[:alpha:]] ]]; then #check to control if the string that we got contains alphabet
			mv -- "$file" "${file%.$e}.$new_string.filt"
		else
			mv -- "$file" "${file%.$e}._.filt" #if it does not contain an alphabet word, it put just an underscore
		fi
			
		done
	done

cd ..

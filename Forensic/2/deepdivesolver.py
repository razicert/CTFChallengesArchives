 #!/bin/bash
target="flag.txt"
while(true)
do 
    type=$(file $target)
    if [[ "$type" == *"POSIX tar archive"*  ]];
    then
        mv $target flag.tar
        tar -xvf flag.tar
        rm flag.tar
    fi
    if [[ "$type" == *"Zip"* ]];
    then
        mv $target flag.zip
        unzip flag.zip
        rm flag.zip
    fi
    if [[ "$type" == *"bzip2"* ]];
    then
        mv $target flag.bz2
        bzip2 -dk flag.bz2
        rm flag.bz2
        mv flag.txt.out flag.txt
        mv flag flag.txt
    fi
    if [[ "$type" == *"gzip compressed data"* ]];
    then
        mv $target flag.gz
        gunzip -d flag.gz
        rm flag.gz
        mv flag* flag.txt
    fi
    if [[ "$type" == *"XZ"* ]];
    then
        mv $target flag.xz
        tar -xf flag.xz
        rm flag.xz
    fi
    if [[ "$type" == *"ASCII"* ]];
    then
        echo $type
        break
    fi
done
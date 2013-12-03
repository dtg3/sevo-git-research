#!/bin/bash

while read p
do
	name=${p%*.git}
	name=${name##*/}

	[[ ! -d "$name" ]] && git clone "$p" "$name"
done < repos.txt

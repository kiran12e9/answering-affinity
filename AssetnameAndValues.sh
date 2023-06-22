#!/bin/bash

wget -q "https://www.amfiindia.com/spages/NAVAll.txt" -O NAVAll.txt


tail -n +3 NAVAll.txt | while IFS=';' read -r scheme_code _ _ scheme_name net_asset_value _
do
    
    if [[ $scheme_code =~ ^[0-9]+$ ]]; then
        echo -e "$scheme_name\t$net_asset_value" >> outputfinal.tsv
    fi
done

echo "Extraction completed and assetname and values saved succesfully."

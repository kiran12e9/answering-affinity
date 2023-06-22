# answering-affinity

# 1. AssetNameAndValuesExtractor.sh

This file contains the unix script for extracting the data from the link and stores the data <br> 
in tabular spaced format in the local file.

  For running the script on Windows OS (I have used Windows OS for executing the script) :<br>
  Download and Install Cygwin <br>
  Open the Cygwin terminal <br>
  Navigate to the folder containing the script <br>
  ``` cd "DownloadedFileLocation" ```
  
  Run <br> ``` ./AssetNameAndValuesExtractor.sh ``` in the terminal <br>

And the data will be saved to the outputfinal.txt file on your machine. <br>

Code Explanation : <br>

 - wget command is used to download the file from the provided URL and saves it as NAVAll.txt. <br>
 - Then It starts reading line by line with a delimiter as semicolon and splits the values <br>
   and saves the asset name and values to the given file name. <br>
 - It ignores the blank lines or other text lines and considers only those lines in the script which starts <br> with a number. 


# 2. outputfinal.txt

The extracted data is stored in the file name "outputfinal.txt".

# 3. address_validator.py 

Address validator contains the python script for validating the address by using the postal api details .<br>

It first checks whether pin code is present or not in the given address, if not it outputs invalid.
<br> If present,then it checks atleast there is a state and a city presnet in the address then if minimum conditions are met, <br>
It requests the api for the postal details of given pincode <br>
Then, it cchecks whether the city state region are indeed corressponds to the given pincode in the address.
If no pincode is found, It outputs the error.

To run the file in the command prompt: <br>
Open the terminal,Navigate to the file location <br>
Then run 
```
python address_validator.py
```


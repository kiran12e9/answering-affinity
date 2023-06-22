
# code is almost self explanatory , it first finds out
# whether there is pincode present or not in the given address
#Then, it extracts the pin code 
#After fetching the postal details, it validates the city and state and region present in the given address.


import requests
import re

address = input("Enter the address you want to deliver: ")
address=address.lower()

address_without_delimiters=""

def extract_pin_code(input_address):
    pincode = ""
    address_without_delimiters = re.split(r',\s*|\s+', input_address)
    is_pincode_present_in_address = False
    counter=0
    for counter in range(len(address_without_delimiters)):
        address_part=address_without_delimiters[counter]
        if address_part.isdigit():
            is_pincode_present_in_address = True
            pincode = address_part
        if address_part =="bengaluru" :
            address_without_delimiters[counter]="bangalore"
        if address_part=="mysuru":
                address_without_delimiters[address_part]="mysore"                      
    if is_pincode_present_in_address:
        min_address_requirement_check(address_without_delimiters,pincode)
    else:
        print("Invalid Address - No Pincode is found in the address")


def min_address_requirement_check(address_without_delimiters,pincode):
    if len(address_without_delimiters)<4 :
        print("Invalid Address - Minimum address details like pincode, state, region/city, h.no/appartment are necessary")
    else:
        get_post_office_details(pincode,address_without_delimiters)


def get_post_office_details(pincode,address_without_delimiters):
    api_url = f"http://www.postalpincode.in/api/pincode/{pincode}"
    try:
        pin_code_details = requests.get(api_url)
        pin_code_details_in_json = pin_code_details.json()
        if pin_code_details_in_json["Status"] == "Error":
            print(pin_code_error)
        else:
            post_offices = pin_code_details_in_json["PostOffice"]
            validate_address(post_offices,address_without_delimiters)
    except:
        print(api_request_error)


def validate_address(post_offices,address_without_delimiters):
    valid_address = False
    state=post_offices[0]["State"].lower()
    city=post_offices[0]["Region"].lower()
    if " " in city:
        city=(city.split())[0]
    for offices in post_offices:
        office_name = offices["Name"]
        office_name=office_name.lower()
        if  office_name in address:
            valid_address = True
            break 
    address_without_delimiters_as_string = ' '.join(address_without_delimiters)     
    if state not in address_without_delimiters_as_string :
        valid_address=False
    if city not in address_without_delimiters_as_string:
        valid_address=False
    if valid_address:
        print("Valid Address.")
    else:           
        print("Invalid address.")
        






pin_code_error = "Are you trying to deliver outside India? 😊 😊 😊 Because the PIN code does not match any city 🫤 🫤"
api_request_error = "Exception occurred while getting the postal details. It's not your fault; it's the API server's fault!"


extract_pin_code(address)
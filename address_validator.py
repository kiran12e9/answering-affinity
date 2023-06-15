import requests
import re


address_part_without_delimiters = ""
pin_code_error = "Are you trying to deliver outside India? 😊 😊 😊 Because the PIN code does not match any city 🫤 🫤"
api_request_error = "Exception occurred while getting the postal details. It's not your fault; it's the API server's fault!"

address = input("Enter the address you want to deliver: ")
address=address.lower()



def extract_pin_code(input_address):
    pincode = ""
    address_without_comma = input_address.replace(","," ")
    address_without_delimiters=address_without_comma.split(" ")
    is_pincode_present_in_address = False
    for address_part in address_without_delimiters:
        if address_part.isdigit() and len(address_part) == 6:
            is_pincode_present_in_address = True
            pincode = address_part
            if address_part =="bengaluru" or address_part=="bangalore":
                address_part="bangalore"
            if address_part=="mysuru":
                address_part="mysore"           
    if is_pincode_present_in_address:
        get_post_office_details(pincode)
    else:
        print("No Pincode is found in the address")


def get_post_office_details(pincode):
    api_url = f"http://www.postalpincode.in/api/pincode/{pincode}"
    try:
        pin_code_details = requests.get(api_url)
        pin_code_details_in_json = pin_code_details.json()
        if pin_code_details_in_json["Status"] == "Error":
            print(pin_code_error)
        else:
            post_offices = pin_code_details_in_json["PostOffice"]
            validate_address(post_offices)
    except:
        print(api_request_error)


def validate_address(post_offices):
    valid_address = False
    state=post_offices[0]["State"].lower()
    city=post_offices[0]["Region"].lower()
    print("hello",address_part_without_delimiters)
    for offices in post_offices:
        office_name = offices["Name"]
        office_name=office_name.lower()

        if  office_name in address:
            valid_address = True
            break
        
    if state in address :
        print("state ok")
    else:
        print("state differs")

    if city in address: 
        print("city ok")
    else:
        print("city differs",city)               
    if valid_address:
        print("Address is valid!")
    else:
        print("Invalid address.")
        

extract_pin_code(address)

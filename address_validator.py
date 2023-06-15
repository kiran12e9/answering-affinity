import requests

address_part_without_delimiters = ""
pin_code_error = "Are you trying to deliver outside India? 😊 😊 😊 Because the PIN code does not match any city 🫤 🫤"
api_request_error = "Exception occurred while getting the postal details. It's not your fault; it's the API server's fault!"

address = input("Enter the address you want to deliver: ")
address_inputted=address.split(" ")

def extract_pin_code(address):
    pincode = ""
    address_parts_without_comma = address.split(",")
    is_pincode_present_in_address = False
    for part in address_parts_without_comma:
        address_part_without_delimiters = part.split(" ")
        for address_part in address_part_without_delimiters:
            if address_part.isdigit():
                is_pincode_present_in_address = True
                pincode = address_part
    if is_pincode_present_in_address:
        get_post_office_details(pincode)
    else:
        print("No PIN code is found in the address")


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
    for offices in post_offices:
        office = offices["Name"]
        office_name_without_space = office.split(" ")
        for office_name in office_name_without_space:
            if office_name in address_inputted:
                valid_address = True
                break
            else:
                print(office_name)
    if valid_address:
        print("Address is valid!")
    else:
        print("Invalid address.")
        

extract_pin_code(address)

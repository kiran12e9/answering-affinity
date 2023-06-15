import requests

address_part_without_delimiters=""
pin_code_error="Are you are trying to deliver outside India? 😊 😊 😊..  because pin code does not match to any city 🫤 🫤"
api_request_error="Exception in getting the postal details , Its not your fault, Its the api server fault !!"



address=input("Enter the address you want to deliver !")


def extract_pin_code(address):
    pincode=""
    address_parts_without_comma=address.split(",")
    is_pincode_present_in_address=False
    for part in address_parts_without_comma:
        address_part_without_delimiters=part.split(" ")
        for address_part in address_part_without_delimiters:
            if address_part.isdigit():
                is_pincode_present_in_address=True
                pincode=address_part
    if is_pincode_present_in_address:
        get_post_office_details(pincode)  
    else:
        print("No pincode is found in the address")    


def get_post_office_details(pincode):
    api_url = f"http://www.postalpincode.in/api/pincode/{pincode}"
    try:
        pin_code_details = requests.get(api_url)
        pin_code_details_in_json= pin_code_details.json()
        if pin_code_details_in_json["Status"]=="Error":
            print(pin_code_error)
        else:
           print(pin_code_details_in_json) 
    except:
        print(api_request_error)


        

           








extract_pin_code(address)



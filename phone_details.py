import phonenumbers
from phonenumbers import carrier,geocoder,timezone

mobile_no = input("Enter your mobile number: ")
mobile_no = phonenumbers.parse(mobile_no)

# get timeZone a phone number

print(timezone.time_zones_for_number(mobile_no))

# getting carrier of a phone number

print(carrier.name_for_number(mobile_no,"en"))

# getting region information

print(geocoder.description_for_number(mobile_no,"en"))

# validating a phone number

print("Valid mobile number: ",phonenumbers.is_valid_number(mobile_no))

# checking possibility of a number

print("Checking possibility of a number : ",phonenumbers.is_possible_number(mobile_no))


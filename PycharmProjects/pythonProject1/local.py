import phonenumbers
from phonenumbers import geocoder, carrier

number = "+254748959831"

try:

    phone_number = phonenumbers.parse(number)


    if phonenumbers.is_valid_number(phone_number):

        location = geocoder.description_for_number(phone_number, "en")

        service_provider = carrier.name_for_number(phone_number, "en")

        print(f"Location: {location}")
        print(f"Carrier: {service_provider}")
    else:
        print("The phone number is not valid.")
except phonenumbers.phonenumberutil.NumberParseException as e:
    print(f"Error parsing phone number: {e}")

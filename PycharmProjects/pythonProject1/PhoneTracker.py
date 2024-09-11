import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+254765414120")
phone_number2 = phonenumbers.parse("+254748959831")
phone_number3 = phonenumbers.parse("+254720247149")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));



import phonenumbers
from phonenumbers import geocoder, carrier, timezone, format_number, format_number, is_valid_number, is_possible_number
number = input("Enter phone number: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
carrier = carrier.name_for_number(phone, "en")
region = geocoder.description_for_number(phone, "en")
valid = is_valid_number(phone)
possible = is_possible_number(phone)
print("Region: ", region)
print("Carrier: ", carrier)
print("Timezone: ", time)
print("Valid: ", valid)
print("Possible: ", possible)

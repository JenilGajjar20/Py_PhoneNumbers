import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier


# Parsing string to Phone number
# Phone number format: (+Country Code)
p_num = phonenumbers.parse("+917600697082")  # Enter your Phone Number


# This will print the Phone number and the basic details
print(p_num)
# Output: 
# Country Code: 91 National Number: 760069XXXX


#Pass the parsed number in the below function
timeZone = timezone.time_zones_for_number(p_num)
print(timeZone)
# Output: 
# ('Asia/Calcutta',)


# Getting carrier of a phone number
Carrier = carrier.name_for_number(p_num, "en")
print(Carrier)


# Getting region information
Region = geocoder.description_for_number(p_num, "en")
print(Region)


# Validating a phone number
Valid = phonenumbers.is_valid_number(p_num)
print(Valid)
# Output: Boolean(True/False)


# Checking possibility of a number
Possible = phonenumbers.is_possible_number(p_num)
print(Possible)
# Output: Boolean(True/False)

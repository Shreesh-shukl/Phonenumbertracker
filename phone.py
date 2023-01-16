import phonenumbers
from the_number import number
from phonenumbers import geocoder
country_belong = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(country_belong, "en"))
from phonenumbers import carrier
sp_serviceprovider=phonenumbers.parse(number, "RO")
print(carrier.name_for_number(sp_serviceprovider, "en"))
# import geocoder

# # Get the current location based on IP address
# ip_location = geocoder.ip('192.168.240.114')

# # Print the country and city
# print("Country:", ip_location.country)
# print("City:", ip_location.city)



# import phonenumbers
# from geopy.geocoders import Nominatim

# # Example phone number
# # phone_number = "+923493410285"
# phone_number = "+201026659150"

# # Parse the phone number
# parsed_number = phonenumbers.parse(phone_number)

# # Get the country code
# country_code = phonenumbers.region_code_for_number(parsed_number)

# # Initialize geocoder
# geolocator = Nominatim(user_agent="phone_locator")

# # Get the country name
# country_name = geolocator.geocode(country_code).address

# # Get the city name
# location = geolocator.geocode(parsed_number)

# if location:
#     city = location.address.split(",")[-3]
# else:
#     city = "Unknown"

# # Print the results
# print("Country Code:", country_code)
# print("Country Name:", country_name)
# print("City:", city)



# import phonenumbers
# from phonenumbers import geocoder
# phone1 = phonenumbers.parse("+923207931466")
# print("phone number  ")
# print(geocoder.description_for_number(phone1,"en"))




# # Example phone number
# phone_number = "+393205750310"

# # Parse the phone number
# parsed_number = phonenumbers.parse(phone_number)

# # Print the country code and national number
# print("Country Code:", parsed_number.country_code)
# print("National Number:", parsed_number.national_number)
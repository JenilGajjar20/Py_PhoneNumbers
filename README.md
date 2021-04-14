# Py_PhoneNumbers

## Phonenumbers module in python
Python is a very powerful language and also very rich in libraries. 
<b>phonenumbers</b> is one of the modules that provides numerous features like providing basic information of a phone number, validation of a phone number etc.

## Installation 
Install the phonenumbers module by typing the following command in command prompt.<br>
<b>pip install phonenumbers</b>

## 1. Convert String to Phonenumber:
To explore the features of the phonenumbers module, we need to take the phonenumber of a user in the phonenumber format.
Input must be of a <b>string type</b> and country code must be added before phonenumber.

## 2. Get timezone:
Here, import the timezone module using phonenumbers module eg:-> <b> from phonenumbers import timezone </b>.<br>
First, we do parse the string input to phonenumber format, and then we use an in-built function to get the timezone of the user.
It gives the output for valid numbers only.

## 3. Carrier and Region of a phonenumber:
Import the modules using phonenumbers module eg:-> <b> from phonenumbers import carrier, geocoder </b>.

## 4. Validation of a phonenumber:
To check whether a given phone number is valid or not use --> <b> is_valid_number() </b> method and 
to check whether a given phone number is possible or not use --> <b> is_possible_number() </b> method


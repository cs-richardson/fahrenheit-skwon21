# This program converts an inputted celsius value into farenheit and displays the farenheit value
# San Kwon

# the user should input a celcius value that is a minimum of -273.15

celsius = input("C: ")
farenheit = ((float(celsius)* 9) / 5) + 32
print("F: " + str(farenheit))

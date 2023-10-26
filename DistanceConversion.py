distance = float(input("Enter the distance between the cities (in kilometers): "))

# Conversion factors
meter_conversion_factor = 1000
feet_conversion_factor = 3280.84
inch_conversion_factor = 39370.1
centimeter_conversion_factor = 100000

# Convert distance to different units
meters = distance * meter_conversion_factor
feet = distance * feet_conversion_factor
inches = distance * inch_conversion_factor
centimeters = distance * centimeter_conversion_factor

# Print the converted distances
print("Distance in meters:", meters)
print("Distance in feet:", feet)
print("Distance in inches:", inches)
print("Distance in centimeters:", centimeters)

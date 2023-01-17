# A program to convert °F to °C 3 times

def temp_converter():
    tempInF = float(input("\nEnter the temperature in °F: "))
    tempInC = (tempInF - 32) * (5/9)
    
    print("The temperature in °C is", tempInC, "degrees")

for i in range(3):
    temp_converter()
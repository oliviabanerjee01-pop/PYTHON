temperature = int(input("enter the current temperature in your surrounding:"))
degree = input("choose your measure Celsius, Fahrenheit or Kelvin: ")
if degree == "Celsius":
    
    print("the temperature in fahrenheit is",temperature*1.8+32, "F")
    print("the temperature in kelvin is", temperature + 273.18, "K")

elif degree == "Farenheit":
    print("the temperature in celsius is", [temperature-32]*0.55, "°C")
    print("the temperature in kelvin is",[temperature - 32]*0.55+32, "K")
elif degree == "Kelvin":
    print("the temperature in celsius is", temperature-273.15, "°C")
    print("the temperature in fahrenheit is", [temperature-273.15]*1.8+32, "F")

else:
    print("please input the proper terms")
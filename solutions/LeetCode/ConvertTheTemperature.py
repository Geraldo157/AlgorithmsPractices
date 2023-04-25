class Solution(object):
    def convertTemperature(self, celsius):
        calculo_kelvin = celsius + 273.15
        calculo_fahrenheit = (celsius * 1.8) + 32
        kelvin = round(calculo_kelvin, 5)
        fahrenheit = round(calculo_fahrenheit, 5)
        conversions = [kelvin, fahrenheit]
        return conversions

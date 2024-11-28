class TemperatureConverter:
    def __init__(self, temperature, scale="Celsius"):
        self.temperature = temperature
        self.scale = scale.lower()

    def celsius_to_fahrenheit(self):
        if self.scale == "celsius":
            return (self.temperature * 9/5) + 32
        else:
            return "Температурата трябва да бъде в Целзий."

    def fahrenheit_to_celsius(self):
        if self.scale == "fahrenheit":
            return (self.temperature - 32) * 5/9
        else:
            return "Температурата трябва да бъде във Фаренхайт."

    def set_temperature(self, temperature, scale="Celsius"):
        self.temperature = temperature
        self.scale = scale.lower()

temp1 = TemperatureConverter(25, "Celsius")
print(f"25 Целзий в Фаренхайт: {temp1.celsius_to_fahrenheit()}°F")

temp2 = TemperatureConverter(77, "Fahrenheit")
print(f"77 Фаренхайт в Целзий: {temp2.fahrenheit_to_celsius()}°C")

temp1.set_temperature(100, "Celsius")
print(f"100 Целзий в Фаренхайт: {temp1.celsius_to_fahrenheit()}°F")

temp2.set_temperature(212, "Fahrenheit")
print(f"212 Фаренхайт в Целзий: {temp2.fahrenheit_to_celsius()}°C")
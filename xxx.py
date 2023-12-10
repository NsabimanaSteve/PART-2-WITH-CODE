class Weather:
    def __init__(self,day,temp,sunny):
        self.day=day
        self.temp=temp
        self.sunny=sunny
    def __str__(self):
        return f"Day: {self.day}, temperature(in ceisius): {self.temp} Sunny:{self.sunny}"
    def convert(self):
        return (self.temp*(9/5))+32
if __name__ == "__main__":
    weather1=Weather("Monday",29,"sunny"==True)
    weather2=Weather("Tuesday ",36,"sunny"==True)
    weather3=Weather("Sunday",23,"sunny"==True)
    weather_list=[weather1,weather2,weather3]
    
    
    def hottest_sunny(weathers):
        max_tem=0
        return_obj=None
        for weather in weathers:
            if weather.sunny:
                if weather.tem > max_temp:
                    max_temp=weather.temp
        return return_obj
    
    print(hottest_sunny(weather_list))
    print(weather1,weather2,weather3)
    print(Weather.convert(weather2))

    
    
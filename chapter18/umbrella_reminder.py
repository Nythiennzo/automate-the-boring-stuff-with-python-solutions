import requests, bs4, ezgmail

weather_url = 'https://forecast.weather.gov/MapClick.php?textField1=40.76&textField2=-74'
email_address=''

weather_response = requests.get(weather_url)
weather_response.raise_for_status()

soup = bs4.BeautifulSoup(weather_response.text, 'lxml')
day_forecast_elements = soup.select('.forecast-text')[:2]

day_forecast = '|'.join([day_forecast_element.getText().lower() for day_forecast_element in day_forecast_elements])

if ('rain' in day_forecast or 'showers' in day_forecast):
    ezgmail.send(email_address, 'Rain Alert!', 'Don''t forget to pack an umbrella before leaving the house.')
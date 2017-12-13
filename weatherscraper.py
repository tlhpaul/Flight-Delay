import pandas as pd
import numpy as np 
import requests

cities = {'Philadelphia': 'KPHL' ,
          'New York': 'KNYC',
          'Atlanta': 'KFTY',
          'San Francisco': 'KSFO',
          'Miami': 'KMIA',
          'Los Angeles': 'KCQT',
          'Seattle': 'KSEA',
          'Houston':'KMCJ',
          'Boston': 'KBOS',
          'Chicago': 'KORD',
          'WashingtonDC':''
         }

test = {'Philadelphia': 'KPHL'} 
features = ['Mean TemperatureF', 'Mean VisibilityMiles', 'Mean Wind SpeedMPH', 'PrecipitationIn', 'CloudCover']
             
# url = 'https://www.wunderground.com/history/airport/KPHL/2017/1/17/CustomHistory.html?dayend=17&monthend=3&yearend=2017&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo='
url = 'https://www.wunderground.com/history/airport/{}/{}/CustomHistory.html?dayend=1&monthend=1&yearend={}&req_city={}&reqdb.zip=&reqdb.magic=&reqdb.wmo='

def get_temperature(cities, url, desired_features):
  end_year = "2017"
  start_date = "2016/1/1"

  for key, val in cities.iteritems():

    formatted_url = url.format(val, start_date, end_year, key)
    print formatted_url

    df_list = pd.read_html(formatted_url)
    df = df_list[1]
    print df.head()

    temp_req = requests.get(formatted_url)
    filename = "{}_weather.csv".format(str(key))

    with open(filename, 'w') as weatherfile:
      weatherfile.write(temp_req.text)

    weather_df = pd.read_csv(filename)
    weather_df["Date"] = pd.to_datetime(weather_df["EST"], infer_datetime_format=True) 
    weather_df = weather_df[desired_features]
    print (weather_df.head())


get_temperature(test, url, features)


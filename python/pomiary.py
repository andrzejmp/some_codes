import pandas as pd
import urllib.request, json
import numpy as np
import matplotlib.pyplot as plt
#-------------------------------------------------------------
#Dane wejściowe - Zakres dwudniowy wskazany
loc = 1
day1 = '2022-07-21'
day2 = '2022-04-27'
#-------------------------------------------------------------

if loc == 1:    
    place ='Warszawa'    
elif loc == 2:
    place = 'Jarosław'
 
file_name = place[0:2]+'_'+day1+'--'+day2
path =  'imgs/' + file_name
#-------------------------------------------------------------
query=str(loc)+'/'+day1+'T00%3A00%3A00/'+day2+'T23%3A59%3A59'
url = 'http://app-homeairmonitor-220218202242.azurewebsites.net/air-pollution/get/' + query
 
 
response = urllib.request.urlopen(url)
raw_data = response.read()
 
#encoding = response.info().get_content_charset('utf8')  # JSON default
#data = json.loads(raw_data.decode(encoding))
 
raw_data_str = str(raw_data)
raw_data_str=raw_data_str[2:-1]
 
with open('tmp.json', 'w') as f:
    f.write(raw_data_str)
raw_data_str = pd.read_json ('tmp.json')
raw_data_str.to_csv ('raw_data_str.csv', index = None)
 
print(raw_data_str)
 
pm2 = pd.read_csv("raw_data_str.csv", parse_dates =['timestamp'])
#pm2['timestamp'] = pm2['timestamp'] + datetime.timedelta(hours=2)
 
import datetime
pm2['hour'] = pd.to_datetime(pm2["timestamp"]).dt.strftime('%H:%M')
pm2['date'] = pd.to_datetime(pm2["timestamp"]).dt.strftime('%d:%m')
pm2['time'] = pm2['date']+', '+ pm2['hour']
 
plt.style.use('ggplot')
plt.figure(figsize=(18,6))
pm2.set_index('time')["pm1"].tail(150).plot(color="orange")
pm2.set_index('time')["pm10"].tail(150).plot(color="red")
pm2.set_index('time')["pm25"].tail(150).plot(color="blue")
plt.style.use('ggplot')
plt.title('Pomiary zanieczyszczeń, ' + day1 + '-' + day2 + ', ' + place)
plt.legend()
plt.yticks(np.arange(0, max(pm2.pm10), step=max(pm2.pm10)//10))
plt.xlabel('czas pomiaru')
plt.savefig(path) #pliki zapisywany do katalogi imgs
print('W katalogu imgs zapisano wykres: ' + file_name+'.png')

'''
#westerplatte2022()
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
bc5161dc2509ad6576627449ddd8e7da
https://api.themoviedb.org/3/movie/550?api_key=bc5161dc2509ad6576627449ddd8e7da
eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYzUxNjFkYzI1MDlhZDY1NzY2Mjc0NDlkZGQ4ZTdkYSIsInN1YiI6IjYyNGZlNGFmNWEwN2Y1MDA1MGY4NmZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2Sd1TRgq8Vw790CytK8qJlnhmPrFuwu5HH9l0jcHr4s
https://stackoverflow.com/questions/9745854/sphinx-pdf-themes
https://pypi.org/project/sphinx-business-theme/
'''

#https://openbase.com/python/sphinx-business-theme

# pip3 install -U sphinx-business-theme

#https://github.com/cookiecutter/cookiecutter

#https://openbase.com/python/sphinx-business-theme

#https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html#the-doc-role


import csv
from typing import DefaultDict
from datetime import datetime
import matplotlib.pyplot as plt

open_file_sitka = open("sitka_weather_2018_simple.csv", "r")
open_file_deathv = open("death_valley_2018_simple.csv", "r")

csv_file_sitka = csv.reader(open_file_sitka, delimiter=",")
csv_file_deathv = csv.reader(open_file_deathv, delimiter=",")

header_row_sitka= next(csv_file_sitka)
header_row_deathv = next(csv_file_deathv)
print(type(header_row_sitka))
print(type(header_row_deathv))

for index, column_header in enumerate(header_row_sitka):
    print(index, column_header)
for index, column_header in enumerate(header_row_deathv):
    print(index, column_header)   

mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')

highs_sitka = []
dates_sitka = []
lows_sitka = []
title_sitka = []

for row in csv_file_sitka:
    highs_sitka.append(int(row[5]))
    lows_sitka.append(int(row[6]))
    the_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates_sitka.append(the_date)
    title_sitka.append(str(row[1]))

highs_deathv = []
dates_deathv = []
lows_deathv = []
title_deathv = []

for row in csv_file_deathv:
    try:
        the_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:  
        highs_deathv.append(high)
        lows_deathv.append(low)
        dates_deathv.append(the_date)
        title_deathv.append(str(row[1]))


plt.subplot(2,1,1)
plt.plot(dates_sitka,highs_sitka,c='red')
plt.plot(dates_sitka, lows_sitka, c="blue")
plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor= 'blue', alpha=0.1)
plt.title(title_sitka[1])

plt.subplot(2,1,2)
plt.plot(dates_deathv,highs_deathv,c='red')
plt.plot(dates_deathv, lows_deathv, c="blue")
plt.fill_between(dates_deathv, highs_deathv, lows_deathv, facecolor= 'blue', alpha=0.1)
plt.title(title_deathv[1])

plt.suptitle(f"Temperature comparison between {title_sitka[1]} and {title_deathv[1]}")

plt.show()

README

FILE LIST
1) 201508_status_data.csv – approx. 37 million records of bike and dock availability by minute
2) 201508_station_data.csv – 70 records – station ID, name, latitude, longitude, dockcount, city, installation date
3) 201508_trip_data.csv – approx. 354,000 records of individual trips
4) 201508_weather_data.csv – 1,825 records of daily weather by city

Files contain data from 9/1/14 to 8/31/15. This is the second year of Bay Area Bike Share's operation. The first year of data can be downloaded separately from the website.

1) STATUS DATA
FILE = "201508_status_data.csv"
-station_id: station ID number (use "201508_station_data.csv" to find corresponding station information)
-bikes_available: number of available bikes
-docks_available: number of available docks
-time: date and time, PST

2) STATION INFORMATION
FILE = "201508_station_data.csv"
-station_id: station ID number (corresponds to "station_id" in "201508_status_data.csv")
-name: name of station
-lat: latitude
-long: longitude
-dockcount: number of total docks at station
-landmark: city (San Francisco, Redwood City, Palo Alto, Mountain View, San Jose)
-installation: original date that station was installed. If station was moved, it is noted below.

Note: Station names and locations listed on "201508_station_data.csv" represent data that was collected on 8/31/15. However, please note that during 9/1/14 and 8/31/15, 5 stations were moved and 1 station stayed in the same location but changed name. 

Station 23: From 9/1/14 – 10/22/14: This station was located at (37.488501, -122.231061). 
Station 25: From 9/1/14 – 10/22/14: This station was located at (37.486725, -122.225551). It was previously named “Broadway at Main.”
Station 49: From 9/1/14 - 2/5/15: This station was located at (37.789625, -122.390264). 
Station 69: From 9/1/14 – 3/11/15: This station was located at (37.776377,-122.39607). 
Station 72: Moved twice. From 9/1/14 – 2/12/15, this station was located at (37.780356, -122.412919). From 2/13/15 to 6/3/15, the station was located at (37.780353, -122.41226). 
Station 80: On 9/1/14, this station changed names from "San Jose Government Center" to "Santa Clara County Civic Center." It did not move.

3) TRIP DATA
FILE = "201508_trip_data.csv"
-Trip ID: numeric ID of bike trip
-Duration: time of trip in seconds
-Start Date: start date of trip with date and time, in PST
-Start Station: station name of start station
-Start Terminal: numeric reference for start station
-End Date: end date of trip with date and time, in PST
-End Station: station name for end station
-End Terminal: numeric reference for end station
-Bike #: ID of bike used
-Subscription Type: Subscriber = annual or 30-day member; Customer = 24-hour or 3-day member
-Zip Code: Home zip code of subscriber (customers can choose to manually enter zip at kiosk however data is unreliable) 

4) WEATHER DATA
FILE = "201508_weather_data.csv"
Daily weather information per service area, provided from Weather Underground in PST. Weather is listed from north to south (San Francisco, Redwood City, Palo Alto, Mountain View, San Jose).
	
-Precipitation_In 	"numeric, in form x.xx but alpha ""T""= trace when amount less than .01 inch"	
-Cloud_Cover 	"scale of 0-8, 0=clear"	
-Zip: 94107=San Francisco, 94063=Redwood City, 94301=Palo Alto, 94041=Mountain View, 95113= San Jose"
-No data recorded on 8/8/2015 for 94301
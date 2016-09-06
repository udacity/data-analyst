FILE LIST
1) 201408_status_data.csv – approx. 18 million records of status data (bike and dock availability)
2) 201408_station_data.csv – 70 records – station latitude, longitude, name, dockcount, installation date
3) 201408_trip_data.csv – approx. 171,000 records of individual trips
4) 201408_weather_data.csv – 920 records of daily weather by city

Files contain data from  3/1/14 to 8/31/14.

1) STATUS DATA
FILE = "201408_status_data.csv"
-station_id: station ID number (use "201408_station_data.csv" to find corresponding station information)
-bikes_available: number of available bikes
-docks_available: number of available docks
-time: date and time, PST

2) STATION INFORMATION
FILE = "201408_station_data.csv"
-station_id: station ID number (corresponds to "station_id" in "201408_status_data.csv")
-name: name of station
-lat: latitude
-long: longitude
-dockcount: number of total docks at station
-landmark: city (San Francisco, Redwood City, Palo Alto, Mountain View, San Jose)
-installation: date that station was installed 

3) TRIP DATA
FILE = "201408_trip_data.csv"
-Trip ID: numeric ID of bike trip
-Duration: time of trip in seconds
-Start Date: start date of trip with date and time, in PST
-Start Station: station name of start station
-Start Terminal: numeric reference for start station
-End Date: end date of trip with date and time, in PST
-End Station: station name for end station
-End Terminal: numeric reference for end station
-Bike #: ID of bike used
-Subscription Type: Subscriber = annual member; Customer = 24-hour or 3-day member
-Zip Code: Home zip code of user (only available for annual members)

4) WEATHER DATA
FILE = "201408_weather_data.csv"
Daily weather information per service area. Weather is listed from north to south (San Francisco, Redwood City, Palo Alto, Mountain View, San Jose).
	
-Max_Visibility_Miles 	
-Mean_Visibility_Miles 	
-Min_Visibility_Miles 	 		
-Precipitation_In 	"numeric, in form x.xx but alpha ""T""= trace when amount less than .01 inch"	
-Cloud_Cover 	"scale of 0-8, 0=clear"	
-Events	"text field - entries: rain, fog, thunderstorm"	
-zip code: 94107=San Francisco, 94063=Redwood City, 94301=Palo Alto, 94041=Mountain View, 95113= San Jose"	
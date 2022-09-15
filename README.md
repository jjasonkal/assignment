# Data Engineering Exercise - **Margera**


## [https://github.com/jjasonkal/assignment](https://github.com/jjasonkal/assignment)


# Instructions

Make sure you have installed docker (version 20.10.18) and docker-compose (version 1.27.0).

Create .env file in the root folder in which you will store sensitive information about the mateomatics Weather API authentication and the Database Management System connection.


```
API_USERNAME=duth_kaltsikis
API_PASSWORD=ZeE4e6h75P

DB_DATABASE=postgres
DB_SERVER=localhost
DB_USERNAME=postgres
DB_PASSWORD=postgres
```


Everything is ready to build the FastAPI image and the PostgreSQL image and deploy them:


```bash
docker-compose build

docker-compose up
```


If everything works correctly you can find a UI version of the API in:

**[http://127.0.0.1/docs](http://127.0.0.1/docs)**

It is time to create the tables in the database and then to input 3 locations to get hourly forecasts for a period of 7 days for each of them. These forecasts will then automatically get stored in the PostgreSQL database that we previously defined and in particular in the “forecasts” table.

It is recommended to use docker to run the Python scripts.


```bash
docker build -t filler .

docker run -it --network host filler
```


Or you can run them directly if you have installed all the requirements from requirements.txt.


```bash
python3 create_tables.py

python3 forecasts.py
```


Enter a total of three valid city names.

These forecasts now are stored in the database and they are ready to retrieve from the **endpoints** in the API that have been created.

## Be careful: 

The project uses **Python 3.8**. If you use later versions of Python the **psycopg2** package may have some problems installing. 

If you have any trouble with the library decouple make sure that you uninstall **decouple**:

 


```bash
pip uninstall decouple
```


And ensure you have **python-decouple** installed:


```bash
pip install python-decouple
```





## API Endpoints


### Last hour weekly forecast

_Lists the latest (last hour) forecast for each location for every day._

Request URL -> **[http://127.0.0.1/weather/last-hour-weekly-forecast](http://127.0.0.1/weather/last-hour-weekly-forecast)**


#### Example Response


```
{
  "rome": [
	{
  	"t_2m": 19.1,
  	"absolute_humidity_2m": 16.2,
  	"dew_point_2m": 18.9,
  	"date": "2022-09-15T23:00:00+00:00",
  	"since": "2022-09-15T08:23:07.281858+00:00"
	},
	{
  	"t_2m": 21.5,
  	"absolute_humidity_2m": 16,
  	"dew_point_2m": 18.8,
  	"date": "2022-09-16T23:00:00+00:00",
  	"since": "2022-09-15T08:23:07.281858+00:00"
	},
...............................................................
...............................................................
],
"athens": [
        {
  	"t_2m": 22.7,
  	"absolute_humidity_2m": 16.2,
  	"dew_point_2m": 19.1,
  	"date": "2022-09-15T23:00:00+00:00",
  	"since": "2022-09-15T02:35:29.472319+00:00"
	},
	{
  	"t_2m": 23.1,
  	"absolute_humidity_2m": 18.4,
  	"dew_point_2m": 21.2,
  	"date": "2022-09-16T23:00:00+00:00",
  	"since": "2022-09-15T02:35:29.472319+00:00"
	},
...............................................................
...............................................................
}
```



### Average of last 3 forecasts

_Lists the average of the last 3 forecasts for each location for every day._

Request URL -> **[http://127.0.0.1/weather/average-of-last-3-forecasts](http://127.0.0.1/weather/average-of-last-3-forecasts)**


#### Example Response


```
{
  "rome": [
	{
  	"t_2m": 22.2,
  	"absolute_humidity_2m": 13.35,
  	"dew_point_2m": 16.1,
  	"date": "2022-09-15T00:00:00+00:00"
	},
	{
  	"t_2m": 22.75,
  	"absolute_humidity_2m": 13.1,
  	"dew_point_2m": 15.75,
  	"date": "2022-09-15T01:00:00+00:00"
	},
...............................................................
...............................................................
],
"athens": [
	{
  	"t_2m": 21.6,
  	"absolute_humidity_2m": 12.6,
  	"dew_point_2m": 15,
  	"date": "2022-09-15T00:00:00+00:00"
	},
	{
  	"t_2m": 21,
  	"absolute_humidity_2m": 12.4,
  	"dew_point_2m": 14.8,
  	"date": "2022-09-15T01:00:00+00:00"
	},
...............................................................
...............................................................
}
```



### 


### Top n locations of each metric

_Gets the top n locations based on each available metric._


<table>
  <tr>
   <td>parameters
   </td>
   <td>type
   </td>
  </tr>
  <tr>
   <td>n
   </td>
   <td>INT (REQUIRED)
   </td>
  </tr>
</table>


Request URL (n=2) -> **[http://127.0.0.1/weather/top-n-locations-of-each-metric?n=2](http://127.0.0.1/weather/top-n-locations-of-each-metric?n=2)**


#### Example Response


```
{
  "t_2m": [
	{
  	"name": "dubai",
  	"maximum": 39.5
	},
	{
  	"name": "nicosia",
  	"maximum": 35.8
	}
  ],
  "absolute_humidity_2m": [
	{
  	"name": "dubai",
  	"maximum": 29.4
	},
	{
  	"name": "chania",
  	"maximum": 21.2
	}
  ],
  "dew_point_2m": [
	{
  	"name": "dubai",
  	"maximum": 29.5
	},
	{
  	"name": "chania",
  	"maximum": 23.8
	}
  ]
}
```



### Latest weekly forecast (extra)

_Lists the latest available forecasts since calling _meteomatics weather API_ for each location for every day._

Request URL -> **[http://127.0.0.1/weather/latest-weekly-forecast](http://127.0.0.1/weather/latest-weekly-forecast)**


#### Example Response


```
{
  "rome": [
	{
  	"t_2m": 22.1,
  	"absolute_humidity_2m": 13.7,
  	"dew_point_2m": 16.5,
  	"date": "2022-09-15T00:00:00+00:00",
  	"since": "2022-09-15T08:23:07.281858+00:00"
	},
	{
  	"t_2m": 22.7,
  	"absolute_humidity_2m": 12.9,
  	"dew_point_2m": 15.5,
  	"date": "2022-09-15T01:00:00+00:00",
  	"since": "2022-09-15T08:23:07.281858+00:00"
	},
...............................................................
...............................................................
],
  "athens": [
	{
  	"t_2m": 21.6,
  	"absolute_humidity_2m": 12.6,
  	"dew_point_2m": 15,
  	"date": "2022-09-15T00:00:00+00:00",
  	"since": "2022-09-15T02:35:29.472319+00:00"
	},
	{
  	"t_2m": 21,
  	"absolute_humidity_2m": 12.4,
  	"dew_point_2m": 14.8,
  	"date": "2022-09-15T01:00:00+00:00",
  	"since": "2022-09-15T02:35:29.472319+00:00"
	},
...............................................................
...............................................................
}
```



## Tables


### forecasts


<table>
  <tr>
   <td>Column Name
   </td>
   <td>Data type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>date
   </td>
   <td>DATETIME(30)
   </td>
   <td>date of the forecast
   </td>
  </tr>
  <tr>
   <td>t_2m
   </td>
   <td>FLOAT(5)
   </td>
   <td>temperature 2 meters above ground (Celsius)
   </td>
  </tr>
  <tr>
   <td>absolute_humidity_2m
   </td>
   <td>FLOAT(5)
   </td>
   <td>absolute humidity 2 meters above ground (gm3)
   </td>
  </tr>
  <tr>
   <td>dew_point_2m
   </td>
   <td>FLOAT(5)
   </td>
   <td>instantaneous value of the dew point temperature 2 meters above ground (Celsius)
   </td>
  </tr>
  <tr>
   <td>since
   </td>
   <td>DATETIME(30)
   </td>
   <td>date that this forecast was retrieved from meteomatics weather API
   </td>
  </tr>
  <tr>
   <td>city_id 
   </td>
   <td>INT
   </td>
   <td>id of the city, (ForeignKey('cities.id')
   </td>
  </tr>
</table>



### cities


<table>
  <tr>
   <td>Column Name
   </td>
   <td>Data type
   </td>
   <td>Description
   </td>
  </tr>
  <tr>
   <td>id
   </td>
   <td>INT
   </td>
   <td>id of the city
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td>VARCHAR(30)
   </td>
   <td>name of the city
   </td>
  </tr>
</table>





# Process of completing the task


## Get the forecasts for any 3 locations and for a period of 7 days



1. Find the API call from meteomatics weather API that returns hourly weekly forecasts for a location(latitude, longitude)
2. Use geopy library to extract latitude and longitude from a city name
3. Handle user’s input
4. Create .env file to secure sensitive information
5. Get local variables from .env
6. Decide the format (JSON) in which will receive the forecasts
7. Handle the response according to its status
8. Dockerize Python scripts


## Store the data in a relational database 



1. Define a function that takes as an argument the forecasts retrieved in the previous step
2. Create an engine that connects with the Database Management System (PostgreSQL) and takes the sensitive connection information from the .env file.
3. Decide the appropriate schema
4. Create a Pandas Dataframe which will have the necessary columns. 
5. Append this Dataframe to the Database in the ‘forecasts’ table
6. Use two related tables “forecasts” and “cities”


## Create an API that uses the database data



1. Decide on which API framework to use (FastAPI)
2. Create Dockefile for the API
3. Deploy both FastAPI and Postgres with docker-compose
4. Configure FastAPI with Postgres using .env file to retrieve sensitive information
5. Create SQL queries for the API endpoints
6. Create Models for the response type of the API
7. Create the endpoints using the previous queries and models
8. Create tests for the endpoints
9. Refactor SQL queries in separate .sql files for better maintenance





## SQL queries


### Last hour weekly forecast

Rank forecasts with the same DATE of timestamp date ordered by date and since. Use the row number to select only those with rn=1 which are the last hour forecasts of each day. It returns the last hour's weekly forecast only for a specific city_id.


```
WITH ranked_messages AS (
   SELECT
       m.*,
       ROW_NUMBER() OVER (PARTITION BY DATE(date) ORDER BY date desc, since DESC) AS rn
   FROM
       forecasts AS m
   where
       city_id = {city_id})
SELECT
   *
FROM
   ranked_messages
WHERE
   rn = 1 and
   DATE(date) >= DATE(NOW())
ORDER BY
   rn,city_id, date;
```





### Average of last 3 forecasts

Select the 3 last forecasts for a specific city_id ordered by since and filter the top 3 rows. Group by date and city_id so it can find the average for each metric of these 3 last forecasts. It returns the average of the last 3 forecasts only for a specific city_id.


```
SELECT
   date,
   CAST(avg(t_2m) AS decimal(5,2)) as t_2m,
   CAST(avg(dew_point_2m) AS decimal(5,2)) as dew_point_2m,
   CAST(avg(absolute_humidity_2m) AS decimal(5,2)) as absolute_humidity_2m
FROM forecasts
WHERE
   city_id = {city_id} and
   since in (
       SELECT distinct
           since
       FROM
           forecasts
       WHERE
           city_id = {city_id}
       ORDER BY
           since DESC
       LIMIT 3) and
   DATE(date) >= DATE(NOW())
GROUP BY
   forecasts.date, forecasts.city_id
ORDER BY
   date;
```





### Top n locations of each metric

Join table “cities” with table “forecasts” to have access to cities’ names. Group by name of the city and find the maximum value of metric ordered by the same. Filter the top n rows. It returns the top n locations only for a specific metric ({value}).


```
SELECT
   cities.name,
   max({value}) as maximum
FROM
   forecasts
JOIN cities on cities.id = forecasts.city_id
WHERE
   DATE(date) >= DATE(NOW())
GROUP BY
   name
ORDER BY
   max({value}) DESC limit {n};
```





### Latest weekly forecast (extra)

Select the last available forecasts for a specific city_id ordered by since and filter the top row for each date. It returns the latest weekly forecast only for a specific city_id.


```
SELECT
   forecasts.*
FROM
   forecasts
WHERE
   city_id = {city_id} and
   since = (
       SELECT DISTINCT
           since
       FROM
           forecasts
       WHERE
           city_id = {city_id}
       ORDER BY
           since DESC
       limit 1) and
   DATE(date) >= DATE(NOW())
```






## Key problems



* Decide the appropriate schema, two related tables “forecasts” and “cities”
* Fill the tables using Python scripts
* Deploy both FastAPI and Postgres with docker-compose
* Decide how endpoints should use SQL queries
* Create SQL queries for the API endpoints
* Dockerize Python scripts


## What slowed you down



* Run the application on a virtualized operating system (docker)
* Trying to handle every possible exception and error
* Ambiguous and vague API endpoint’s descriptions


## Tools and techniques



* meteomatics Weather API
* FastAPI
* SQL
* docker
* PostgreSQL
* psycopg2
* sqlalchemy
* Pandas
* geopy.geocoders.Nominatim
* JSON
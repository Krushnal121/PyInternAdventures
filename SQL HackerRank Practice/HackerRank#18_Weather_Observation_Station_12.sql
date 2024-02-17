/*Problem Link:https://www.hackerrank.com/challenges/weather-observation-station-12/problem*/

SELECT DISTINCT(CITY)
FROM STATION
WHERE SUBSTR(CITY, 1, 1) NOT IN ('A', 'E', 'I', 'O', 'U') AND SUBSTR(CITY, -1, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
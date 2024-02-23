/*Problem Link:https://www.hackerrank.com/challenges/weather-observation-station-18/problem*/

SELECT ABS(ROUND((MIN(LAT_N)-MAX(LAT_N))+(MIN(LONG_W)-MAX(LONG_W)),4)) FROM STATION
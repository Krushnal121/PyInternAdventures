/*Problem Link:https://www.hackerrank.com/challenges/asian-population/problem*/

SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE IN (SELECT CODE FROM COUNTRY WHERE CONTINENT="Asia")
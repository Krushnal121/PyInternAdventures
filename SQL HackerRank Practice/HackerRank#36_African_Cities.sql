/*Problem Link:https://www.hackerrank.com/challenges/african-cities/problem*/

SELECT NAME FROM CITY WHERE COUNTRYCODE IN (SELECT CODE FROM COUNTRY WHERE CONTINENT="Africa")
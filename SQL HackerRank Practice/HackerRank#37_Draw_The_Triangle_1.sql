/*Problem Link:https://www.hackerrank.com/challenges/draw-the-triangle-1/problem*/

SET @TEMP:=21;
SELECT REPEAT('* ', @TEMP:= @TEMP - 1)
FROM INFORMATION_SCHEMA.TABLES;
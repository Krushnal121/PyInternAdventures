/*Problem Link:https://www.hackerrank.com/challenges/draw-the-triangle-2/problem*/

SET @TEMP:=0;
SELECT REPEAT('* ', @TEMP:= @TEMP + 1)
FROM INFORMATION_SCHEMA.TABLES
WHERE @TEMP < 20;
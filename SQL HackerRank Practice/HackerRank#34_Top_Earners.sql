/*Problem Link:https://www.hackerrank.com/challenges/earnings-of-employees/problem*/

SELECT MAX(SALARY*MONTHS), COUNT(EMPLOYEE_ID) FROM EMPLOYEE WHERE (SALARY*MONTHS) = (SELECT MAX(SALARY*MONTHS) FROM EMPLOYEE);
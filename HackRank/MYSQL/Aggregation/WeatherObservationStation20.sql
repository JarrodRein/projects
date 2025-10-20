SET NULL "NULL";
SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;
SET PAGES 0;
SET DEFINE OFF;

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT ROUND(MEDIAN(LAT_N), 4)
FROM STATION;
exit;


/* or DB2
    Enter your query here.
    Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT ROUND(AVG(LAT_N), 4)
FROM (
    SELECT LAT_N,
           ROW_NUMBER() OVER (ORDER BY LAT_N) AS rn,
           COUNT(*) OVER () AS total
    FROM STATION
) tmp
WHERE rn IN (CEIL(total / 2.0), FLOOR(total / 2.0) + 1);

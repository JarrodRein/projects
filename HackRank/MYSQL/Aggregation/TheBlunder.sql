
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

SELECT CEIL(
         ABS(
             AVG(SALARY) 
           - AVG(CAST(REPLACE(SALARY,'0','') AS DECIMAL))
         ) / 12
       ) AS error
FROM EMPLOYEES;
/* MYSQL not DB2 
*/
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
WITH RECURSIVE numbers AS (
  SELECT 2 AS n
  UNION ALL
  SELECT n + 1 FROM numbers WHERE n < 1000
)
SELECT GROUP_CONCAT(n SEPARATOR '&')
FROM numbers
WHERE n NOT IN (
  SELECT a.n
  FROM numbers a, numbers b
  WHERE b.n < a.n AND b.n > 1 AND MOD(a.n, b.n) = 0
);

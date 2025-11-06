
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
-- Step 1: find (hacker_id, challenge_id) pairs where the hacker hit full score
WITH full_scores AS (
  SELECT
      s.hacker_id,
      s.challenge_id
  FROM Submissions AS s
  JOIN Challenges  AS c ON c.challenge_id      = s.challenge_id
  JOIN Difficulty  AS d ON d.difficulty_level  = c.difficulty_level
  GROUP BY s.hacker_id, s.challenge_id
  HAVING MAX(s.score) = MAX(d.score)   -- d.score is constant per challenge
)

-- Step 2: count full-score challenges per hacker, filter > 1, join to names, order
SELECT
    fs.hacker_id,
    h.name,
    COUNT(*) AS total_full_scores
FROM full_scores AS fs
JOIN Hackers     AS h  ON h.hacker_id = fs.hacker_id
GROUP BY fs.hacker_id, h.name
HAVING COUNT(*) > 1
ORDER BY total_full_scores DESC, fs.hacker_id ASC;
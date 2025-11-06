
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
SELECT h.hacker_id, h.name
FROM Hackers h
JOIN Challenges c ON h.hacker_id = c.hacker_id
JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
JOIN Submissions s ON c.challenge_id = s.challenge_id
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, h.hacker_id

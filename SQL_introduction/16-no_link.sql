-- List named records from highest score to lowest.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

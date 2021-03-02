-- Import in hbtn_0c_0 database a table dump
-- displays avg temp (F) by city ordered by temp descending
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;

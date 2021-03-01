-- lists all records of the table second_table
-- no rows without name value, restuls displayed by descending score
SELECT score, name FROM second_table WHERE name is not null ORDER BY score DESC;

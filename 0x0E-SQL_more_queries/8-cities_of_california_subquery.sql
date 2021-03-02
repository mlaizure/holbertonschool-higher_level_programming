-- lists all the cities of California that can be found in hbtn_0d_usa
-- results stored in ascending order by cities.id
SELECT cities.id, cities.name FROM cities, states
WHERE states.name = 'California' AND cities.state_id = states.id;

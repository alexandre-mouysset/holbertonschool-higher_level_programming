-- script that list all the cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states_id
ORDER BY cities.id ASC;
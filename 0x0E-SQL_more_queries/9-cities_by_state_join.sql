-- list all cities in database with 1 select statement
SELECT A.id AS id, A.name AS name, B.name AS name
FROM cities A, states B
WHERE A.state_id = B.id
ORDER BY A.id ASC;


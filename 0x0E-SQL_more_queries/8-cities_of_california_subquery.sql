-- joins states and cities on state_id, and returns all californian cities
SELECT A.id AS id, A.name AS name FROM cities A, states B
WHERE A.state_id = B.id AND B.name = 'California'
ORDER BY A.id ASC;

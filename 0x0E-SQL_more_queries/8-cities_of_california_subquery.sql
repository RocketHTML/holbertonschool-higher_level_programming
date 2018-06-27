-- joins states and cities on state_id, and returns all californian cities
SELECT A.id as id, A.name as name from cities A, states B
where A.state_id = B.id;

-- shows the highest temperature for each state
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state` ORDER BY `max_temp` DESC;

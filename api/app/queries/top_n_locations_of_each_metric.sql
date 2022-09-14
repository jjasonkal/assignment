SELECT
    cities.name,
    max({value}) as maximum
FROM
    forecasts
JOIN cities on cities.id = forecasts.city_id
WHERE
    DATE(date) >= DATE(NOW())
GROUP BY
    name
ORDER BY
    max({value}) DESC limit {n};
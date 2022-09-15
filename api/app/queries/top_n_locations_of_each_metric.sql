SELECT
    {table_cities}.name,
    max({value}) as maximum
FROM
    {table_forecasts}
JOIN {table_cities} on {table_cities}.id = {table_forecasts}.city_id
WHERE
    DATE(date) >= DATE(NOW())
GROUP BY
    name
ORDER BY
    max({value}) DESC limit {n};
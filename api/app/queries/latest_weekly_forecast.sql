SELECT
    forecasts.*
FROM
    forecasts
WHERE
    city_id = {city_id} and
    since = (
        SELECT DISTINCT
            since
        FROM
            forecasts
        WHERE
            city_id = {city_id}
        ORDER BY
            since DESC
        limit 1) and
    DATE(date) >= DATE(NOW())
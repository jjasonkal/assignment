SELECT
    date,
    CAST(avg(t_2m) AS decimal(5,2)) as t_2m,
    CAST(avg(dew_point_2m) AS decimal(6,2)) as dew_point_2m,
    CAST(avg(absolute_humidity_2m) AS decimal(5,2)) as absolute_humidity_2m
FROM forecasts
WHERE
    city_id = {city_id} and
    since in (
        SELECT distinct
            since
        FROM
            forecasts
        WHERE
            city_id = {city_id}
        ORDER BY
            since DESC
        LIMIT 3) and
    DATE(date) >= DATE(NOW())
GROUP BY
    forecasts.date, forecasts.city_id
ORDER BY
    date;
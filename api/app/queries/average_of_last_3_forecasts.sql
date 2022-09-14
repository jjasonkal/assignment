SELECT
    date,
    avg(t_2m) as t_2m,
    avg(dew_point_2m) as dew_point_2m,
    avg(absolute_humidity_2m) as absolute_humidity_2m
FROM forecasts
WHERE
    name = '{name}' and
    since in (
        SELECT distinct
            since
        FROM
            forecasts
        WHERE
            name = '{name}'
        ORDER BY
            since DESC
        LIMIT 3) and
    DATE(date) >= DATE(NOW())
GROUP BY
    forecasts.date, forecasts.name
ORDER BY
    date;
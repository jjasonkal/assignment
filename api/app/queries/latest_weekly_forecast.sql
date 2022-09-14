SELECT
    *
FROM
    forecasts
WHERE
    name = '{name}' and
    since = (
        SELECT DISTINCT
            since
        FROM
            forecasts
        WHERE
            name = '{name}'
        ORDER BY
            since DESC
        limit 1) and
    DATE(date) >= DATE(NOW())
WITH ranked_messages AS (
    SELECT
        m.*,
        ROW_NUMBER() OVER (PARTITION BY DATE(date) ORDER BY date desc, since DESC) AS rn
    FROM
        {table_forecasts} AS m
    where
        city_id = {city_id})
SELECT
    *
FROM
    ranked_messages
WHERE
    rn = 1 and
    DATE(date) >= DATE(NOW())
ORDER BY
    rn,city_id, date;
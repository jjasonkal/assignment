WITH ranked_messages AS (
    SELECT
        m.*,
        ROW_NUMBER() OVER (PARTITION BY DATE(date) ORDER BY date DESC) AS rn
    FROM
        forecasts AS m)
SELECT
    *
FROM
    ranked_messages
WHERE
    rn = 1 and
    DATE(date) >= DATE(NOW())
ORDER BY
    date;
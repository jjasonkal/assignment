SELECT DISTINCT
    name
FROM
    forecasts
WHERE
    DATE(date) >= DATE(NOW());
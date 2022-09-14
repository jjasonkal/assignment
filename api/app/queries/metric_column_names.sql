SELECT
    column_name
FROM
    INFORMATION_SCHEMA.columns
WHERE
    TABLE_NAME = N'forecasts' and
    column_name like('%2m')
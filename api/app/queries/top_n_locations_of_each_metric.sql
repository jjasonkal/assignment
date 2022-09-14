Select
    name,
    max({value}) as maximum
From
    forecasts
where
    DATE(date) >= DATE(NOW())
Group By
    name
order by
    max({value}) desc limit {n};
# Q1 -->

 ## Command 1: 
    docker run -it \
    --rm \
    --entrypoint=bash \
    python:3.13

## Command 2 : pip --version


## Answer : pip 26.1.2


# Q2 -->

## Answer : postgres:5432 and db:5432

# Q3 -->
SELECT COUNT(*) 
FROM public.green_tripdata_2025_11 t
WHERE t.trip_distance <= 1 
  AND t.lpep_pickup_datetime >= '2025-11-01' 
  AND t.lpep_pickup_datetime < '2025-12-01';

## Answer : 8,007

# Q4 --> 
SELECT 
    lpep_pickup_datetime::DATE AS pickup_day, 
    MAX(trip_distance) AS longest_distance
FROM 
    public.green_tripdata_2025_11
WHERE 
    trip_distance < 100
GROUP BY 
    lpep_pickup_datetime::DATE
ORDER BY 
    longest_distance DESC
LIMIT 1;

## Answer : 2025-11-14

# Q5 --> 
SELECT 
	zpu."Zone",
	SUM(t.total_amount) AS Total,
	CAST(t.lpep_pickup_datetime AS DATE) as Day
FROM public.green_tripdata_2025_11 t 
	JOIN public.taxi_zone_lookup zpu ON t."PULocationID" = zpu."LocationID"
WHERE CAST(t.lpep_pickup_datetime AS DATE) = '2025-11-18'
GROUP BY zpu."Zone",
		 CAST(t.lpep_pickup_datetime AS DATE)
ORDER BY Total DESC;

## Answer : East Harlem North

# Q6 --> 
SELECT 
    zdo."Zone" AS dropoff_zone,
    t.tip_amount
FROM 
    public.green_tripdata_2025_11 t
JOIN 
    public.taxi_zone_lookup zpu ON t."PULocationID" = zpu."LocationID"
JOIN 
    public.taxi_zone_lookup zdo ON t."DOLocationID" = zdo."LocationID"
WHERE 
    zpu."Zone" = 'East Harlem North'
ORDER BY 
    t.tip_amount DESC
LIMIT 1;

	
## Answer : Yorkville West

# Q7 --> 

## Answer : terraform init, terraform apply -auto-approve, terraform destroy
import time
import clickhouse_driver
 
# Connect to ClickHouse
conn = clickhouse_driver.connect(
    host='localhost',
    port=9000,
    user='default',
    password='',
    database='default'
)
 
# Query to get the most expensive queries
query = '''
SELECT query, max_memory_usage
FROM system.processes
WHERE query != ''
ORDER BY max_memory_usage DESC
LIMIT 10
'''
 
while True:
    cursor = conn.cursor()
    cursor.execute(query)
 
    print('Top 10 most expensive queries:')
    for row in cursor:
        print(f'Query: {row[0]} \t Memory usage: {row[1]}')
 
    # Wait for 5 seconds before running the query again
    time.sleep(5)

# Monitoring-ClickHouse-Queries
Monitoring Expensive ClickHouse Queries

Download file and edit following rows.
<pre id="example"><code class="language-lang"  style="color: #333; background: #f8f8f8;"> 
conn = clickhouse_driver.connect(
    host='localhost',
    port=9000,
    user='default',
    password='',
    database='default'
)
</code></pre>

Then run the script
<pre id="example"><code class="language-lang"  style="color: #333; background: #f8f8f8;"> 
python listQueries.py 

or

python3 listQueries.py 
</code></pre>

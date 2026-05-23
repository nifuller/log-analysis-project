## May 21, 2026
Downloaded the NASA dataset and manually reviewing it. 

parsed each line into five columns; host, timestamp, request, status and bytes

saved it as a pandas dataframe and a csv

exploring the data now in the jupyter notebook

## May 22, 2026
looking and researching sqlite 

creating a sqlite database with my logs dataframe

using sql commands to manipulate the database

used count query and got 1891714

## May 23, 2026
created multiple sqlite queries that:

- found ipaddress and their number of requests
- found number of 404 per ip address
- counted the number of 500
- found unusual ip requests during off hours
- investigated the top 4 ip addresses and see what they were requesting

in the process of writing up a full report once visuals are created

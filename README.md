# bd-assignment-7
##### Topic: Frequent itemset mining
> Name:
> Gautam Gadipudi
>
> RIT mail:
> gg7148@rit.edu


## Question 1
Run the following in the root of the repo after connecting to your postgreSQL server through PSQL
```bash
\i 'q1/q1.sql'
```

## Question 2
Run the following in the root of the repo after connecting to your postgreSQL server through PSQL
```bash
\i 'q2/q2.sql'
```

## Question 3
Run the following in the root of the repo after connecting to your postgreSQL server through PSQL
```bash
\i 'q3/q3.sql'
```

## Question 4
Run the following in the root of the repo after connecting to your postgreSQL server through PSQL
```bash
\i 'q4/q4.sql'
```

## Question 5
Run the following in the folder q5. **Please note: you have to be inside the folder q5**. Note `python3 q5/main.py` 
won't work as I messed up relative path of config file in the last minute.

Assuming the table `popular_movie_actors` exists.
```bash
python3 main.py
```
The frequent item sets in each level are as follows:

|Level|Frequent itemsets|
|---|---|
|1|17055|
|2|2462|
|3|276|
|4|71|
|5|27|
|6|5|
|7|0|

Find the actor names in the table named `final_level`.
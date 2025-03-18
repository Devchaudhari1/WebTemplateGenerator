//command to read all column name

select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='users' and TABLE_SCHEMA ='miniproject';

//command to read all column name with data type

select COLUMN_NAME ,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='users' and TABLE_SCHEMA ='miniproject';


//command to read all TABLE_NAME data
select TABLE_NAME ,COLUMN_NAME ,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA ='miniproject' order by TABLE_NAME asc;


//command to describe enum also 
select COLUMN_NAME , COLUMN_TYPE FROM information_schema.columns where table_name = 'activities' and table_schema= 'miniproject';

//change {name}Id every time in controllers by searching in sql sheet
//command to read all column name with description from mysql

//Copy only the tuples like
| busID           | varchar(10)   |
| operator        | varchar(100)  |
| type            | varchar(50)   |
| origin          | varchar(50)   |
| destination     | varchar(50)   |
| originArea      | varchar(50)   |
| destinationArea | varchar(50)   |
| departure       | time          |
| arrival         | time          |
| seats           | int           |
| windows         | int           |
| fare            | decimal(10,2) |
| seatsAvailable  | int           |
| noofbookings    | int           |


//don't copy ------+------+ or |COLUMN_NAME |COLUMN_TYPE |


select COLUMN_NAME , COLUMN_TYPE FROM information_schema.columns where table_name = 'activities' and table_schema= 'miniproject';



Additional commands
npm init -y
npm i express , mysql2 , axios 

npx install -D tailwindcss@3 
npx tailwindcss@3 -i ./views/input.css -o ./views/output.css --watch 







//change {name}Id every time in controllers by searching in sql sheet

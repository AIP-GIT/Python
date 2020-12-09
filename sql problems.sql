1.employee (empid,empname,deptid,salary).Select all the employees whose salary >=5000 or<=10000.
SELECT emp_id, emp_name,dep_id ,emp_salary FROM EMPLOYEES_TABLE 
WHERE salary BETWEEN 5000 AND 10000;

2. Select the employees whose experience is greater than 5.

SELECT * FROM EMPLOYEES_TABLE WHERE experience > 5;

3.Select the employees whose name ends with letter ‘A’, belongs to deptid 10 or 30 and salary between 5000 and 10000.
SELECT  * employee_name  where ends_'%A'
FROM employees  
WHERE department_id = 10 or 30  and
 Salary  = 5000 BETWEEN 10000
 
 4.Select the employees whose name starts with ‘A’ and ends with ‘A’ but not both.
 
 select * from EMPLOYEES_TABLE where first_name like 'A%' and last_name like '%A' AND  first_name or last_name NOT LIKE ( 'A%a' );
 
 5.Find all the employees whose experience in the company is more than 6 months and on bench.
 SELECT * FROM EMP9 WHERE EXP > 6 ;
 
 6.Find the students and their total marks.                                                                              Studid       Name        S1                  S2             S3
101            A              70                 80 
102            B              50                 60             100     
103            C              30                                   60
                                                                                     
 CREATE STUDENT_TABLE{
 stud_id , Name , S1,S2,S3
 };
 INSERT INTO STD VALUES (101, 'A' ,70,80,NULL);
 INSERT INTO STD VALUES (102, 'B' ,50,60,100);
 INSERT INTO STD VALUES (103, 'C' ,30,NULL,60);                                 
 SELECT * FROM STUDENT_TABLE;   
 select  sum(nvl(std_s1,0)+(nvl(std_s2,0)+(nvl(std_s3,0) as total from std;
 

 Q 5.Select all the employees whose name is Joe irrespective of whether it is JOE/joe/Joe/-----. 
 
 Select * from employees where NAME='%joe%'
 
 Q 6.Select the second maximum salary of the employees.
 SELECT * FROM Employees_TABLE 
WHERE SECOND_MAX(salary)

Q.7 Count the number of null values in the columns(A,B).
 NUMBER_OF_NULL_VALUE from employeeTable
 
 Q.8 Find the average salary of employees.
 
 SELECT AVG(salary),
     FROM employees_Table;
	 
Q.9 Get the count of employees, department wise  and only for ,where the count is   greater than 5.
SELECT 
    COUNT(*)
FROM
    employees
WHERE
     COUNT(*) > 5

Q 10.Create table Employee with columns
      Empid    number => Primary Key
      Name     char     =>  size 20
      Deptid   number =>size 3
      Salary                       =>number
      Locationid    number =>size 2
  i)Modify the table to accommodate name to 30 characters.
  ii)Insert 5 records in to the table.
 iii)Update salary and depid of employee => 103
 iv)Employee105 left the company do necessary changes in the table.
  v)Write a query to get count of employees and those who belong  to either dept(10,20,30,40) and their name has letter ‘B’ and count in each dept and location greater than

CREATE TABLE EMP10(
                   EMP_ID INT Primary key, 
                   EMPNAME VARCHAR(20), 
                   EXP INT,
                   Depid INT,
                   SALARY INT,
                   loc_id INT
);
INSERT INTO EMP10 VALUES(101,'%ALIYA',6,01,10000,11);
INSERT INTO EMP10 VALUES(102,'arJoey',9,02,10000,12);
INSERT INTO EMP10 VALUES(103,'sstjoe',5,03,10000,13);
INSERT INTO EMP10 VALUES(104,'newton%',6,04,10000,14
INSERT INTO EMP10 VALUES(105,'nertonp%',12,08,13000,17);
SELECT * FROM EMP10  
ALTER TABLE EMP10 MODIFY EMPNAME VARCHAR(30);
UPDATE EMP10 SET SALARY = 15000 ,Depid = 05 WHERE EMP_ID = 103; 
DELETE FROM EMP10 WHERE Depid = 04;
SELECT * FROM EMP10 WHERE Depid =01;
SELECT COUNT        (EMP_ID)

Q.11 Write a query to get name and deptname.
        Employee(Empid,Name,Deptid)
        Department(Deptid,Deptname,Location)

SELECT EMPNAME
FROM EMP1 a
SELECT deptname
FROM DPT
UNION ALL
SELECT deptname
FROM DPT e;

Q.12 Write a query to get name,location.
        Employee(Empid,Name,Deptid)
        Department(Deptid,Deptname,Locid)
        Location(Locid,Location,Country)

SELECT EMPNAME
FROM EMP1 a
SELECT deptname
FROM DPT
UNION ALL
SELECT deptname
FROM DPT e;SELECT EMPNAME
FROM EMP1 a

Q.13 Write a query to find all the employees who has ‘%’ in their name. 

SELECT * FROM EMP1 WHERE EMPNAME LIKE '%';

Q.14 When will ROW_NUMBER and RANK give different results?Give Example.

CREATE TABLE Cars1
(
id INT,
name VARCHAR(50) NOT NULL,
company VARCHAR(50) NOT NULL,
power INT NOT NULL
);


USE ShowRoom
INSERT INTO Cars1
VALUES
INSERT INTO Cars1 VALUES(1, 'Corrolla', 'Toyota', 1800);
INSERT INTO Cars1 VALUES(2, 'City', 'Honda', 1500);
INSERT INTO Cars1 VALUES(3, 'C200', 'Mercedez', 2000);
INSERT INTO Cars1 VALUES(4, 'Vitz', 'Toyota', 1300);

SELECT name,company, power,
RANK() OVER(ORDER BY power DESC) AS PowerRank
FROM Cars1

Q 15.why would I use DENSE_RANK instead of RANK ? What about RANK instead of DENSE_RANK?

RANK: This gives you the ranking within your ordered partition. ... 
DENSE_RANK: This gives you the ranking within your ordered partition, 
but the ranks are consecutive in it. Also, no ranks are skipped if there are ranks with multiple items.

Q 16.LAG and LEAD  is especially used in what type of scenario?

The LAG function is used to access data from a previous row, 
while the LEAD function is used to return data from rows further down the result set.

Q 17.For dealing with NULL values, what would I choose to use IFNULL vs. CASE WHEN?

The IFNULL function returns a string or a numeric based on the context where it is used.

Q 18.Do temp tables make your code cleaner and faster , one of the two or none?WHY?

When we use temporary table it gets created in another database tempdb which is a performance overhead. 
But if we create normal table in stored procedure in place of temp table then 
it will get created in its own database.

Q 19.Write an SQL query to fetch “FIRST_NAME” from Worker table using the alias name as <WORKER_NAME>.

Select FIRST_NAME AS WORKER_NAME from Worker;

Q 20.Write an SQL query to fetch “FIRST_NAME” from Worker table in upper case.

Select upper(FIRST_NAME) from Worker;

Q 21. Write an SQL query to print the first three characters of  FIRST_NAME from Worker table.

Select substring(FIRST_NAME,1,3) from Worker;

Q 22.Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from Worker table.
 
 Select INSTR(FIRST_NAME, BINARY'a') from Worker where FIRST_NAME = 'ALIYA';
 
Q 23.Write an SQL query to print the FIRST_NAME from Worker table after removing white spaces from the right side.
 
 Select RTRIM(FIRST_NAME) from Worker;
 
Q 24.Write an SQL query to print the DEPARTMENT from Worker table after removing white spaces from the left side.
 
 Select LTRIM(DEPARTMENT) from Worker;
 
Q 25.Write an SQL query that fetches the unique values of DEPARTMENT from Worker table and prints its length.
 
 Select distinct length(DEPARTMENT) from Worker;

Q 26 .Write an SQL query to print the FIRST_NAME from Worker table after replacing ‘a’ with ‘A’.

Select REPLACE(FIRST_NAME,'a','A') from Worker;

Q 27.Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending.

Select * from Worker order by FIRST_NAME asc,DEPARTMENT desc;

Q 28.Write an SQL query to print details for Workers with the first name as “Vipul” and “Satish” from Worker table.

Select * from Worker where FIRST_NAME not in ('Vipul','Satish');

Q 29.Write an SQL query to print details of workers excluding first names, “Vipul” and “Satish” from Worker table.

Select * from Worker where FIRST_NAME not in ('Vipul','Satish');

Q 30.Write an SQL query to print details of the Workers whose FIRST_NAME contains ‘a’.

Select * from Worker where FIRST_NAME like '%a%';

Q 31.Write an SQL query to fetch the names of workers who earn the highest salary.

SELECT  worker_name, MAX(salary) as salary FROM employee 

Q 32.Write an SQL query to fetch departments along with the total salaries paid for each of them.

SELECT department_id, SUM(salary) 
FROM  employees 
GROUP BY  department_id;

Q 33.Write an SQL query to fetch nth max salaries from a table.
SELECT TOP 1 salary
FROM (
SELECT DISTINCT TOP N salary
FROM #Employee
ORDER BY salary DESC
) AS temp
ORDER BY salary

Q 34.Write an SQL query to fetch three min salaries from a table.
SELECT *
FROM
  ( SELECT e.*, Dense_Rank() over (order by salary DESC) rn FROM employee e
  )
WHERE rn = 3;

Q 35.Write an SQL query to fetch three max salaries from a table.

SELECT *
FROM
  ( SELECT e.*, Dense_Rank() over (order by salary DESC) rn FROM employee e
  )
WHERE rn = 3;

Q 36.Write an SQL query to print the name of employees having the highest salary in each department.

SELECT *
FROM employees
WHERE salary IN
    (SELECT max(salary)
	
Q 37.Write an SQL query to fetch the last five records from a table

SELECT employee_id, last_name 
    FROM employees  LIMIT 5;
	
Q.
 
 
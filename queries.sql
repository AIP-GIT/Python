/*Employee (empid,empname,deptid,salary).Select all the employees whose           salary >=5000 or<=10000.*/
SELECT EMPLOYEE_ID,FIRST_NAME,DEPARTMENT_ID,SALARY FROM HR.EMPLOYEES;
WHERE SALARY BETWEEN 5000 AND 10000

/*Select the employees whose experience is greater than 5.*/
CREATE TABLE ABC(
              EMP_NAME VARCHAR(255),
              EMP_ID INT,
              EXP INT
);
INSERT INTO ABC VALUES('SONI',01,5);
INSERT INTO ABC VALUES('MONI',02,4);
INSERT INTO ABC VALUES('CONI',03,6);
INSERT INTO ABC VALUES('OONI',04,8);
INSERT INTO ABC VALUES('PONI',05,2);
SELECT * FROM ABC;
SELECT EMP_NAME,EMP_ID FROM ABC WHERE EXP > 5;


/*Select the employees whose name ends with letter ‘A’, belongs to deptid 10 or 30 and salary between 5000 and 10000.*/
WHERE FIRST_NAME LIKE '%a'
AND DEPARTMENT_ID = 10 OR DEPARTMENT_ID = 30
AND SALARY BETWEEN 5000 AND 10000;

/*Select the employees whose name starts with ‘A’ and ends with ‘A’ but not both.*/
SELECT * FROM HR.EMPLOYEES
WHERE(upper(FIRST_NAME) LIKE
'A%' OR upper(FIRST_NAME) LIKE 
'%A') AND upper(FIRST_NAME) NOT 
LIKE ('A%A');


/*Find all the employees whose experience in the company is more than 6 months and on bench.*/
CREATE TABLE ABC(
              EMP_NAME VARCHAR(255),
              EMP_ID INT,
              EMP_EXP INT,
              EMP_BENCH VARCHAR(255)
);
INSERT INTO ABC VALUES('SONI',01,4,'NOT_ON_BENCH');
INSERT INTO ABC VALUES('MONI',02,7,'ON_BENCH');
INSERT INTO ABC VALUES('CONI',03,8,'NOT_ON_BENCH');
INSERT INTO ABC VALUES('OONI',04,9,'ON_BENCH');
INSERT INTO ABC VALUES('PONI',05,3,'ON_BENCH');
SELECT * FROM ABC;
SELECT EMP_NAME,EMP_ID FROM ABC WHERE EMP_EXP > 6 AND
EMP_BENCH = 'ON_BENCH';

/*Find the students and their total marks.*/                                                                              
Studid       Name        S1                  S2             S3
101            A         70                  80 
102            B         50                  60             100     
103            C         30                                 60

CREATE TABLE STD(
                STD_ID INT,
                STD_NAME VARCHAR(255),
                STD_S1 INT,
                STD_S2 INT,
                STD_S3 INT
);
INSERT INTO STD VALUES(101,'A',70,80,NULL);
INSERT INTO STD VALUES(102,'B',50,60,100);
INSERT INTO STD VALUES(103,'C',30,NULL,60);
SELECT * FROM STD;
SELECT SUM(STD_S1) FROM STD;
SELECT sum(nvl(STD_S1,0)+nvl(STD_S2,0)+nvl(STD_S3,0)) AS TOTAL FROM STD;

/*Select all the employees whose name is Joe irrespective of whether it is JOE/joe/Joe/-----.*/
CREATE TABLE xyZ(
              EMP_NAME VARCHAR(255),
              EMP_ID INT,
              EMP_si INT
);
INSERT INTO xyZ VALUES('JOE',01,4);
INSERT INTO xyZ VALUES('RAjoe',02,7);
INSERT INTO xyZ VALUES('Joe',03,8);
INSERT INTO xyZ VALUES('JOE',04,9);
SELECT * FROM xyZ;
SELECT EMP_ID,EMP_SI,EMP_NAME FROM XYZ WHERE UPPER(EMP_NAME) ='JOE';


/*Select the second maximum salary of the employees.*/
CREATE TABLE xyZ(
              EMP_NAME VARCHAR(255),
              EMP_SI INT,
              EMP_SALARY INT
);
INSERT INTO XYZ VALUES('SOPI',1,6000);
INSERT INTO XYZ VALUES('KOLI',2,5000);
INSERT INTO XYZ VALUES('SAPNA',3,5000);
INSERT INTO XYZ VALUES('ROHIT',4,5100);
SELECT * FROM XYZ;
SELECT MAX(EMP_SALARY) FROM XYZ
WHERE EMP_SALARY<(SELECT MAX(EMP_SALARY) FROM XYZ);

/*Find the average salary of employees.*/
CREATE TABLE ABC(
              EMP_NAME VARCHAR(255),
              EMP_ID INT,
              SALARY INT
);
INSERT INTO ABC VALUES('joe',01,5000);
INSERT INTO ABC VALUES('JOE',02,4800);
INSERT INTO ABC VALUES('rejoeic',03,6000);

SELECT * FROM ABC;
SELECT AVG(SALARY) FROM ABC;


/*Get the count of employees, department wise  and only for ,where the count is   greater than 5.*/
SELECT EMPLOYEE_ID,DEPARTMENT_ID FROM HR.EMPLOYEES;
SELECT DEPARTMENT_ID,COUNT(EMPLOYEE_ID)
FROM HR.EMPLOYEES
GROUP BY DEPARTMENT_ID
HAVING COUNT(EMPLOYEE_ID)>5

/*Display employee salary and commission for all the employees  if commission is not present print ‘Not Available’.(INT DATATYPE USED)
*/
create table aaa(
               emp_name varchar(255),
               emp_id int,
               emp_com int,
               salary int
);
insert into aaa values('aaa',01,11,100);
insert into aaa values('abb',02,null,200);
insert into aaa values('aab',03,13,300);
insert into aaa values('bbb',04,null,500);
select * from aaa;
select salary,nvl(cast(emp_com as varchar(255)),'not available') from aaa; 


/*Create table Employee with columns
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
*/
create table cc(
             emp_id int,
             emp_name varchar(255),
             dept_id int,
             salary int,
             loc_id int
);
insert into cc values(1,'aaa',101,2000,11);
insert into cc values(2,'abb',102,3000,12);
insert into cc values(3,'aab',103,400,13);
insert into cc values(4,'aba',104,500,14);
insert into cc values(5,'bbb',105,6000,15);
select * from cc;
ALTER TABLE cc MODIFY emp_name varchar(30);
update cc set salary=4500 where dept_id=103; 
delete cc where emp_id=4 ;
select dept_id,count(emp_id) from cc where dept_id between 103 and 105 and emp_name like '%a'
group by dept_id having count(dept_id)>=104 and count(loc_id)>=14;

/*          Write a query to get name and deptname.
        Employee(Empid,Name,Deptid)
        Department(Deptid,Deptname,Location)
*/
CREATE TABLE EMP(
              EMP_NAME VARCHAR(255),
              EMP_ID INT,
              DPT_ID INT
);
INSERT INTO EMP VALUES('SONI',01,5);
INSERT INTO EMP VALUES('MONI',02,4);
INSERT INTO EMP VALUES('CONI',03,6);

SELECT * FROM EMP;
CREATE TABLE DPT(
              DPT_NAME VARCHAR(255),
              DPT_ID INT,
              LOC_ID INT
);
INSERT INTO DPT VALUES('AA',5,11);
INSERT INTO DPT VALUES('BB',4,12);
INSERT INTO DPT VALUES('CC',6,13);
SELECT * FROM DPT;
SELECT E.EMP_NAME,D.DPT_NAME
FROM EMP E, DPT D
WHERE E.DPT_ID =D.DPT_ID;

/*Write a query to get name,location.
        Employee(Empid,Name,Deptid)
        Department(Deptid,Deptname,Locid)
        Location(Locid,Location,Country)
*/
CREATE TABLE EMP(
              EMP_NAME VARCHAR(255),
              EMP_ID INT,
              DPT_ID INT
);
INSERT INTO EMP VALUES('SONI',01,5);
INSERT INTO EMP VALUES('MONI',02,4);
INSERT INTO EMP VALUES('CONI',03,6);

SELECT * FROM EMP;
CREATE TABLE DPT(
              DPT_NAME VARCHAR(255),
              DPT_ID INT,
              LOC_ID INT
);
INSERT INTO DPT VALUES('AA',5,11);
INSERT INTO DPT VALUES('BB',4,12);
INSERT INTO DPT VALUES('CC',6,13);
SELECT * FROM DPT;
CREATE TABLE LOC(
             LOC_NAME VARCHAR(255),
             LOC_CITY varchar(255),
              LOC_ID INT
);
INSERT INTO LOC VALUES('AA','GOA',11);
INSERT INTO LOC VALUES('BB','DELHI',12);
INSERT INTO LOC VALUES('CC','MEGH',13);
SELECT * FROM LOC;
SELECT E.EMP_NAME,L.LOC_NAME
FROM EMP E, DPT D, LOC L
WHERE E.DPT_ID = D.DPT_ID AND D.LOC_ID=L.LOC_ID;

/*Write a query to find all the employees who has ‘%’ in their name. */
CREATE TABLE EMP(
                ESI INT,
                ENAME VARCHAR(255),
                EID INT
);
INSERT INTO EMP VALUES(01,'%CHERI',101);
INSERT INTO EMP VALUES(02,'MERI',102);
INSERT INTO EMP VALUES(03,'KHERI',103);
SELECT * FROM EMP;
SELECT ESI,EID FROM EMP WHERE ENAME='/%/';

/*When will ROW_NUMBER and RANK give different results?*/
Row_number:It returns a unique number for each row starting with 1. 
For rows that have duplicate values,numbers are arbitarily assigned.

Rank :It assigns a unique number for each row starting with 1,except for rows 
that have duplicate values,in which case the same ranking is assigned and a gap appears in the sequence for each duplicate ranking 

example:-WITH T(StyleID, ID)
     AS (SELECT 1,1 UNION ALL
         SELECT 1,1 UNION ALL
         SELECT 1,1 UNION ALL
         SELECT 1,2)
SELECT *,
       RANK() OVER(PARTITION BY StyleID ORDER BY ID)       AS 'RANK',
       ROW_NUMBER() OVER(PARTITION BY StyleID ORDER BY ID) AS 'ROW_NUMBER',
       DENSE_RANK() OVER(PARTITION BY StyleID ORDER BY ID) AS 'DENSE_RANK'
FROM   T  


/*why would I use DENSE_RANK instead of RANK ? What about RANK instead of DENSE_RANK?*/
We use Dense_Rank() SQL function because it generates next number instead of generating row_number.


Rank() SQL function generates rank of the data within ordered set of values but next rank after previous 
rank is row_number of that particular row. 


/*LAG and LEAD  is especially used in what type of scenario?*/
The LAG and LEAD analytic functions were introduced in 8.1.6 to give access to multiple rows within a table, without the need for a self-join.
The LAG function is used to access data from a previous row. 
The LEAD function is used to return data from rows further down the result set.

/*For dealing with NULL values, what would I choose to use IFNULL vs. CASE WHEN?*/
MySQL IFNULL function is one of the MySQL control flow functions that accepts two arguments and returns 
the first argument if it is not NULL. Otherwise, the IFNULL function returns the second argument.

The two arguments can be literal values or expressions.

The following illustrates the syntax of the IFNULL function:

IFNULL(expression_1,expression_2);

The IFNULL function returns expression_1 if expression_1 is not NULL ; otherwise, it returns expression_2.

The IFNULL function returns a string or a numeric based on the context where it is used.

If you want to return a value based on TRUE or FALSE condition other than NULL, you should use the IF function.

/*Do temp tables make your code cleaner and faster , one of the two or none?WHY?*/
When we use temporary table it gets created in another database tempdb which is a performance overhead. 
But if we create normal table in stored procedure in place of temp table then it will get created in its own database


/*Write an SQL query to fetch “FIRST_NAME” from Worker table using the alias name as <WORKER_NAME>.*/
SELECT FIRST_NAME AS "EMPLOYEE NAME" FROM HR.EMPLOYEES;

/*Write an SQL query to fetch “FIRST_NAME” from Worker table in upper case.*/
SELECT upper(FIRST_NAME) from HR.EMPLOYEES;

/*Write an SQL query to fetch unique values of DEPARTMENT from Worker table.*/
SELECT DISTINCT department_id FROM HR.EMPLOYEES;

/*Write an SQL query to print the first three characters of  FIRST_NAME from Worker table.*/
Select substr(FIRST_NAME,1,3) from HR.EMPLOYEES;

/*
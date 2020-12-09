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


                                                                                                                                                                                                    
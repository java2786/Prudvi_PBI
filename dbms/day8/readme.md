# Basics of MySql  
  
## Start mysql  
- start -> services.msc -> search mysql -> start (if stopped)  
  
## Create connection with mysql from cmd  
```cmd  
mysql -u root -p  
  
mysql --host ip --port 3306 -u root -p  
```  
  
## Create database  
```sql  
show databases;  
drop database if exists tutorial;  
create database tutorial;  
use tutorial;  
```  
  
## Create tables for school and insert data  
```sql  
-- Student table  
create table Students(  
	roll int primary key auto_increment,  
	name varchar(20),  
    class varchar(5) not null  
);  
  
-- Subject table  
create table Subjects(  
	id int primary key auto_increment,  
	name varchar(20)  
);  
  
-- Scores table  
create table Scores(  
	marks int,  
	student_id int,  
	sub_id int,  
	foreign key(student_id) references Students(roll),  
	foreign key(sub_id) references Subjects(id),  
	primary key(student_id, sub_id)  
);  
  
-- Insert data in tables  
insert into Students(name, class) values  
('Ramesh', '9A'),   
('Mahesh', '10B'),   
('Suresh', '9A'),   
('Mukesh', '8B');  
  
insert into Subjects(name) values('Hindi'), ('Math');  
  
insert into Scores(marks, student_id, sub_id) values  
(78, 3, 1),  
(88, 2, 2),  
(99, 4, 1);  
  
-- Error because student 4 and subject 1 already has score  
-- insert into Scores(marks, student_id, sub_id) values(91, 4, 1);  
  
insert into Scores(marks, student_id, sub_id) values  
(92, 4, 2);  
  
select * from Students;  
select * from Subjects;  
select * from Scores;  
```  
  
## Interview Questions  
- Select all the student from class 9A  
```sql  
select * from Students where class = '9A'  
```  
- Find all the students with marks < 80 in any subject  
```sql  
select * from Students where roll = (select student_id from Scores where marks < 80);  
```  
- Find all the students with marks >=80 in any subject  
```sql  
-- part 1  
select student_id from Scores where marks >= 80;  
  
-- part 2  
select * from Students where roll in (select student_id from Scores where marks >= 80);  
  
```  
- Find all the students with marks >=80 in math subject  
```sql  
-- part 1  
select id from Subjects where name='Math';  
  
-- part 2  
select student_id from Scores where marks >= 80 and sub_id = 2;  
select student_id from Scores where marks >= 80 and sub_id = (select id from Subjects where name='Math');  
  
-- part 3  
select * from Students where roll in (select student_id from Scores where marks >= 80 and sub_id = (select id from Subjects where name='Math'));  
```  
  
- Count the students in class 9A  
```sql  
--part 1  
select count(*), class from Students group by class;  
  
--part 2 - condition with group by => having  
select count(*), class from Students group by class having class='9A';  
  
  
select count(*) from Students group by class having class='9A';  
```  
  
  
## Basic Interview Queries  
- List all students from class 9b  
- List names of all students whose name starts with 'M'  
- List names of all students whose name ends with 'esh'  
- Show all distinct classes - display all the class only once  
- show count of all classes  
- find average score of Mukesh  
  

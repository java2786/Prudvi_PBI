# Subquery    
### Database is used from previous session    
    
## Find records from all the tables    
- name from Students    
- marks from Scores    
- sub from Subjects    
    
Subject table -> math -> subject_id => Scores table -> score, std_id using sub_id => Student table -> roll    
    
Find all students who scored highest marks in any subject.    
    
```sql    
select max(marks) from Scores where sub_id=(select id from Subjects where name = 'Math');    
    
select name from Students where roll in (select student_id from Scores where marks = (select max(marks) from Scores where sub_id=(select id from Subjects where name = 'Math')));    
    
```    
    
    
## Show name and marks    
    
```sql    
select name as student_name, (select marks from Scores where Students.roll = student_id and sub_id=(select id from Subjects where name = 'Math')) as Marks, (select name from Subjects where name = 'Math') as subject_name from Students;    
```    
    
## Using Join    
```sql    
select Students.name, Scores.marks from Students    
left join Scores    
on Scores.student_id = Students.roll and Scores.sub_id=2;    
```    
    
    
    
## Problems to practice    
1. List all students from class '9A'    
2. List names of all students whose name starts with 'A'    
3. Find the students who scored ≥80 in any subject    
4. List students who scored below 35 (fail) in any subject    
5. Find the student IDs who scored more than 90 marks    
6. List the top 5 highest marks in the Scores table    
7. Count total students in class '10A'    
8. Count the number of distinct classes    
9. Find how many subjects are listed in the Subjects table    
10. Find the average marks scored by student with roll = 2    
11. List all student roll numbers who appeared for at least 2 subjects    
12. List all subject IDs for which marks are more than 80    
13. Get the minimum and maximum marks recorded in Scores table    
14. Find how many students are there in each class    
15. List all student IDs who got full marks (100)    
16. Find the student with the least marks in the Scores table    
17. Find students whose names are exactly 4 characters long    
18. Find the student(s) who got highest marks in any subject    
19. Find all students who scored ≥80 in subject 'Math'    
20. List students whose names contain 'e' and are from class '10B'    

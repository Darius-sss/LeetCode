__time__ = '2021/9/19'
__author__ = 'ZhiYong Sun'

"""
简单查询----一个国家的面积超过 300 万平方公里，或者人口超过 2500 万，那么这个国家就是大国家,输出表World中所有大国家的名称、人口和面积
+-----------------+------------+------------+--------------+---------------+
| name            | continent  | area       | population   | gdp           |
+-----------------+------------+------------+--------------+---------------+
| Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
| Albania         | Europe     | 28748      | 2831741      | 12960000      |
| Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
| Andorra         | Europe     | 468        | 78115        | 3712000       |
| Angola          | Africa     | 1246700    | 20609294     | 100990000     |
+-----------------+------------+------------+--------------+---------------+
select name, population, area 
from World
where area > 3000000 or population > 25000000
"""



"""
根据特定字段删除重复列----删除重复邮箱
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id 是这个表Person的主键。
# 自连接版本----Person p1 == Person as p1 
delete p1
from Person p1, Person p2
where p1.Email = p2.Email and p1.Id > p2.Id
# 子查询版本----需要注意不能先select同一个表的某些值，然后再update这个表。--select的结果再通过一个中间表select多一次，就可以避免这个错误
delete
from Person
where id not in (select id from (select min(Id) as id from Person group by Email) as m)     
"""



"""
查找所有至少连续出现三次的数字。
+----+-----+
| Id | Num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
id 是这个表Logs的主键。
select l1.num res
from Logs l1, Logs l2, Logs l3
where l1.id = l2.id - 1 and l2.id = l3.id - 1 and l1.num = l2.num and l1.num = l3.num
"""



"""
变更性别----有m=男性和f=女性的值。交换所有的f和m值（例如，将所有 f 值更改为 m，反之亦然）。要求只使用一个更新（Update）语句，并且没有中间的临时表。
salary 表：
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
update salary
set sex = char(ASCII(sex) ^ ASCII('f') ^ ASCII('m'))
"""



"""
组合两个表
表1: Person
+-------------+---------+
| 列名         | 类型     |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId 是上表主键
表2: Address
+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId 是上表主键
编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供 person 的以下信息： FirstName, LastName, City, State
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
"""



"""
小美是一所中学的信息科技老师，她有一张 seat座位表，平时用来储存学生名字和与他们相对应的座位 id。
其中纵列的id是连续递增的 
小美想查询改变相邻俩学生的座位后的结果。
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
# 在使用 row_number() over()函数时候，over()里头的分组以及排序的执行晚于 where 、group by、  order by 的执行。
select 
    row_number() over(order by (id + 1 - 2 * power(0, id % 2))) as id,
    student
from 
    seat
"""



"""
编写一个 SQL查询，找出表cinema中所有影片描述为非 boring (不无聊) 的并且 id 为奇数 的影片，结果请按等级 rating 排列。
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
# 先where再order by   desc降序，asc升序，且放在后面
select * 
from cinema
where id % 2 = 1 and description != 'boring' 
order by rating desc
"""



"""
Employee表包含所有员工，他们的经理也属于员工。每个员工都有一个 Id，此外还有一列对应员工的经理的 Id。
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
给定Employee表，编写一个 SQL 查询，该查询可以获取收入超过他们经理的员工的姓名。在上面的表格中，Joe 是唯一一个收入超过他的经理的员工。
select t1.name Employee
from Employee t1, Employee t2
where t1.ManagerId = t2.id and t1.Salary > t2.Salary
"""



"""
有一个courses 表 ，有: student(学生) 和 class (课程)。
请列出所有超过或等于5名学生的课。
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
# where 和having之后都是筛选条件，但是有区别的：
# 1.where在group by前， having在group by 之后
# 2.聚合函数（avg、sum、max、min、count），不能作为条件放在where之后，但可以放在having之后
# distinct仅仅列出不同的值
select class
from courses
group by class
having count(distinct student) >= 5
"""



"""
某网站包含两个表，Customers 表和 Orders 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。
Customers 表：
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders 表：
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
select name Customers 
from Customers
where id not in (select CustomerId from Orders)
"""



"""
编写一个 SQL 查询，查找Person 表中所有重复的电子邮箱。
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
select distinct t1.email
from Person t1, Person t2
where t1.email = t2.email and t1.id != t2.id
"""



"""
Employee 表包含所有员工信息，每个员工有其对应的Id, salary 和 department Id。
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department表包含公司所有部门的信息。
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
编写一个 SQL 查询，找出每个部门工资最高的员工。对于上述表，您的 SQL 查询应返回以下行（行的顺序无关紧要）。
select t2.Name as Department , t1.Name as Employee, t1.salary
from Employee t1 inner join Department t2
where t1.DepartmentId = t2.id


select 
  
"""



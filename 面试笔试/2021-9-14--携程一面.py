__time__ = '2021/9/14'
__author__ = 'ZhiYong Sun'

'''
sql
学生表：姓名，学号，班级
成绩表：学号，学科，得分
教师表：班级，教师姓名
查询： 教师所有班级每个学科的平均得分


select 学生表.班级, 成绩表.学科, avg(成绩表.得分)
From 学生表, 成绩表
group by 学生表.班级, 成绩表.学科
where 学生表.学号=成绩表.学号 and 学生表.班级 in (select 班级 where 教师姓名=给定名字 from 教师表)

'''

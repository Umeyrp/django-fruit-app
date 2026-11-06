from django.db import models

# Create your models here.


class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)


class StudentID(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)


class Professor(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)


class CourseDescription(models.Model):
    description = models.CharField(max_length=200)


class Semester(models.Model):
    name = models.CharField(max_length=30)
    year = models.SmallIntegerField()


class Course(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=40)
    description = models.OneToOneField(CourseDescription, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

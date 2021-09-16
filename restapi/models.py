from django.db import models

class Kafedra(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    kafedra = models.ForeignKey(Kafedra, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.last_name} {self.last_name}"


class Faculty(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name



class Group(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL )

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    group = models.ForeignKey(Group,null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.last_name} {self.last_name}"




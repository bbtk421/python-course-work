from django.db import models


# Create your models here.
class djangoClasses(models.Model):
    Title = models.CharField(max_length=50, default='')
    CourseNumber = models.IntegerField(max_length=50, default='')
    InstructorName = models.CharField(max_length=50, default='')
    Duration = models.FloatField(max_length=50, default='')
    course = models.Manager()

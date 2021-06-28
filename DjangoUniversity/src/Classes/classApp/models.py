from django.db import models

"""
     The below sets up the class of djangoClasses
     it has 4 values that consist of 2 srings 1 intiger and one float value. each denoted by the charfield, integerfield
     and floatfield. 
"""


class djangoClasses(models.Model):
    Title = models.CharField(max_length=50)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=50)
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__ (self):
        return self.Title
    # this should make it use the name of the claseses
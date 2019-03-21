from django.db import models

# Create your models here.


class Member(models.Model):
    """Member Model

    Arguments:
        models {[type]} -- [description]
    """
    name = models.CharField("Name", max_length=200)
    week1task = models.TextField("Task Doing This Week")
    WEEKS = (('Week1', 'Week 1'),
             ('Week2', 'Week 2'),
             ('Week3', 'Week 3'),
             ('Week4', 'Week 4'),
             ('Week5', 'Week 5'),
             ('Week6', 'Week 6')
             )
    leaderforWeek = models.CharField(
        'Leader of Week', max_length=50, choices=WEEKS)

    def __str__(self):
        return self.name

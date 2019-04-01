from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=1024)
    category = models.CharField(max_length=64)
    main_category = models.CharField(max_length=64)
    currency = models.CharField(max_length=16)
    deadline = models.DateTimeField()
    goal = models.IntegerField()
    launched = models.DateTimeField()
    pledged = models.FloatField()
    state = models.CharField(max_length=16)
    backers = models.IntegerField()
    country = models.CharField(max_length=64)
    usd_pledged = models.FloatField()
    usd_pledged_real = models.FloatField()
    usd_goal_real = models.FloatField()

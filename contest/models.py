from django.db import models


# class Movie(models.Model):
#     title = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)
#     year = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

#     class Meta:
#         ordering = ['-id']

class Users(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    user_id = models.IntegerField()


    def __str__(self):
        return self.firstname

class Utc(models.Model):
    user_id = models.IntegerField()
    ticket = models.CharField(max_length= 50)
    contest = models.CharField(max_length= 50)

    def __str__(self):
        return self.ticket

class All_Contests(models.Model):
    contest_name = models.CharField(max_length=50)
    contest_prize = models.CharField(max_length=50)
    winner = models.CharField(max_length=50, blank = True)
    start_date =  models.DateTimeField( blank=True)
    end_date =  models.DateTimeField( blank=True)


    def __str__(self):
        return self.contest_name




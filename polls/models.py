from django.db import models

# Create your models here.
class User(models.Model):    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 15)
    password = models.DateTimeField(max_length = 32)
    email = models.CharField(max_length = 30)
    


    

class Game(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    
class Comment(models.Model):
    user_id =  models.Foreign(User,on_delete = models.Cascade)
    id =  models.Foreign(User,on_delete = models.Cascade)
    text = models.CharField(max_length = 400)

class Vote(models.Model):
    user_id =  models.Foreign(User,on_delete = models.Cascade)
    game_id =  models.Foreign(User,on_delete = models.Cascade)
    vote = models.IntegerField(default = 0)
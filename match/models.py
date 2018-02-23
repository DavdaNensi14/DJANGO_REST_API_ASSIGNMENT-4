from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
       Token.objects.create(user=instance)


class Team(models.Model):
	
	team_name = models.CharField(max_length=200)
	team_logo = models.ImageField(upload_to='post_images/', null=True, blank=True)


	def __str__(self):
		return self.team_name


class Favourite(models.Model):
	
	user = models.ForeignKey(User,related_name='Favourite')
	team_name =  models.ManyToManyField(Team)
	
	def __str__(self):
		return self.user.username 




class Venue(models.Model):

	

	image = models.ImageField(upload_to='post_images/', null=True, blank=True)
	address=models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	capacity=models.IntegerField()


	def __str__(self):
		return self.city




class Match(models.Model):

	time = (
			('1', 'Day(4 pm)'),
			('2', 'Night(8 pm)'), 
			
		)

	

	date = models.DateField()
	# time = models.TimeField(default=timezone.now)
	time = models.CharField(choices=time, max_length=2)
	home_team = models.ForeignKey(Team,related_name='home_team')
	away_team = models.ForeignKey(Team,related_name='away_team')
	venue = models.ForeignKey(Venue,related_name='venu')
	day = models.CharField(max_length=10 ,blank=True , null = True)



	def __str__(self):
		return self.home_team.team_name

	
	
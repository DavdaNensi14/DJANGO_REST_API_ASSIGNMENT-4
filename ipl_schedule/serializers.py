from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from match.models import *
import datetime
from datetime import timedelta
from datetime import datetime as date

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')





class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team


class venueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue

class matchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Match
        


class favouriteSerializer(serializers.ModelSerializer):
    team_name = teamSerializer(many=True, read_only = True)
    class Meta:
        model = Favourite
        fields=['user', 'team_name']





# class matchlistSerializer(serializers.ModelSerializer):
#     day = serializers.SerializerMethodField()
#     # count_school = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Match
#         fields = ('day','date','time','home_team','away_team','venue')

#     def get_day(self, obj):
#        date1= obj.date
#         print "****"
#         print date1
#         a = int('0' + date1)
#         ans = datetime.date(a)
#         print ans.strftime("%A")



#         # year , month, day = (int(x) for x in date1.split('-'))    
#         # ans = datetime.date(year, month, day)
#         return ans.strftime("%A")
        
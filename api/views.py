from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from ipl_schedule.serializers import UserSerializer,teamSerializer,venueSerializer,matchSerializer,favouriteSerializer
from django.views.decorators.csrf import csrf_exempt
from match.models import *
from rest_framework.authentication import TokenAuthentication
from django.db.models import Count
import datetime
from django.db.models import Q
from datetime import timedelta
from datetime import datetime as date




@api_view(['POST'])
def user_login(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_Register(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@csrf_exempt
@api_view(['POST'])
def team_create(request):
	data = request.data
	serializer = teamSerializer(data=data)
	team = Team.objects.all().count()
	if team < 8:
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({'error': 'You can not add more than 8 team'}, status=status.HTTP_400_BAD_REQUEST)





@csrf_exempt
@api_view(['GET'])
def team_list(request):
	team = Team.objects.all()
	serializer = teamSerializer(team, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def team_details(request, pk):
	try:
		team = Team.objects.get(id=pk)
	except:
		return Response({'error': 'Team id not found'}, status=status.HTTP_400_BAD_REQUEST)

	serializer = teamSerializer(team, many=False)
	return Response(serializer.data, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def team_update(request, pk):
	try:
		team = Team.objects.get(id=pk)
	except:
		return Response({'error': 'team id not found'}, status=status.HTTP_400_BAD_REQUEST)
	serializer = teamSerializer(team, data=request.data, many=False)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['DELETE'])
def team_delete(request, pk):
	try:
		team = Team.objects.get(id=pk)
	except:
		return Response({'error': 'team id not found'}, status=status.HTTP_400_BAD_REQUEST)
	team.delete()
	return Response({'success': 'team deleted successfully'}, status=status.HTTP_200_OK)
	
   
	


@csrf_exempt
@api_view(['POST'])
def venue_create(request):
	data = request.data
	serializer = venueSerializer(data=data)
	venue = Venue.objects.all().count()
	if venue < 8:
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({'error': 'You can not add more than 8 venue'}, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET'])
def venue_list(request):
	venue = Venue.objects.all()
	serializer = venueSerializer(venue, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def venue_details(request, pk):
	try:
		venue = Venue.objects.get(id=pk)
	except:
		return Response({'error': 'venue id not found'}, status=status.HTTP_400_BAD_REQUEST)

	serializer = venueSerializer(venue, many=False)
	return Response(serializer.data, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def venue_update(request, pk):
	try:
		venue = Venue.objects.get(id=pk)
	except:
		return Response({'error': 'venue id not found'}, status=status.HTTP_400_BAD_REQUEST)
	serializer = venueSerializer(venue, data=request.data, many=False)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['DELETE'])
def venue_delete(request, pk):
	try:
		venue = Venue.objects.get(id=pk)
	except:
		return Response({'error': 'venue id not found'}, status=status.HTTP_400_BAD_REQUEST)
	venue.delete()
	return Response({'success': 'venue deleted successfully'}, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['POST'])
def match_create(request):
	data = request.data
	serializer = matchSerializer(data=data)
	home_team=request.data.get("home_team")
	away_team=request.data.get("away_team")
	date1 = request.data.get("date")
	year , month, day = (int(x) for x in date1.split('-'))    
	ans = datetime.date(year, month, day)
	print ans.strftime("%A")
	if home_team == away_team:
		return Response({'error': 'match can between same team'}, status=status.HTTP_400_BAD_REQUEST)
	else:

		if serializer.is_valid():
			obj.day = ans
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET'])
def match_list(request):
	try:
		team = request.GET['team']
		print team
	except:
		team = []
		print "8888"
	try:
		venue = request.GET['venue']
	except:
		venue = []
	try:
		day = request.GET['day']
		print day
	except:
		day = []

	if team == venue ==  []:
		match = Match.objects.all()
	else:
		match = Match.objects.filter(Q(home_team=team) | Q(away_team=team) | Q(venue=venue) | Q(time__icontains=day)  )
		#discussion = Discussion.objects.filter(Q(title__icontains=title) & Q(text__icontains=text) & Q(title_type__icontains=title_type))
	
	serializer = matchSerializer(match, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def match_details(request, pk):
	try:
		match = Match.objects.get(id=pk)
	except:
		return Response({'error': 'match id not found'}, status=status.HTTP_400_BAD_REQUEST)

	serializer = matchSerializer(match, many=False)
	return Response(serializer.data, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def match_update(request, pk):
	try:
		match = Match.objects.get(id=pk)
	except:
		return Response({'error': 'match id not found'}, status=status.HTTP_400_BAD_REQUEST)
	serializer = matchSerializer(match, data=request.data, many=False)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['DELETE'])
def match_delete(request, pk):
	try:
		match = Match.objects.get(id=pk)
	except:
		return Response({'error': 'match id not found'}, status=status.HTTP_400_BAD_REQUEST)
	match.delete()
	return Response({'success': 'match deleted successfully'}, status=status.HTTP_200_OK)
	





@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def fav_list(request):
	print "in list"
	if request.user.is_authenticated():
		fav = Favourite.objects.filter(user=request.user)
		print fav
		serializer = favouriteSerializer(fav, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)









@csrf_exempt
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def fav_add(request):
	if request.user.is_authenticated():
		serializer = favouriteSerializer(data=request.data)

		teams = request.data.get("team_name","").strip().split(',')
		print teams
		if serializer.is_valid():
			u_id = request.user.id
			
			fav = Favourite.objects.get(user_id=u_id)
			print fav
			e = Favourite.objects.filter(user_id=u_id).exists()
			
			if e:
				return Response({'error': 'You already added favourite teams earlier.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
			else:
				l = len(teams)
 				if l < 4:
					obj = serializer.save()
					obj.team_name = teams if teams else []
					obj.save()
					serializer = favouriteSerializer(obj)
					return Response(serializer.data, status=status.HTTP_201_CREATED)
 				else:
					return Response({'error': 'You can not add more than 3 teams to favourite.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)







@csrf_exempt
@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def fav_update(request, pk):
    if request.user.is_authenticated():
	    try:
		    favourite = Favourite.objects.get(id=pk)
		    teams = request.data.get("team_name","").strip().split(',')

	    except:
		    return Response({'error': 'favourite id not found'}, status=status.HTTP_400_BAD_REQUEST)

	    serializer = favouriteSerializer(favourite, data=request.data, many=False)
	    if serializer.is_valid():
		    obj = serializer.save()
		    obj.team_name = teams if teams else []
		    obj.save()
		    serializer = favouriteSerializer(obj)
		    return Response(serializer.data, status=status.HTTP_201_CREATED)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)






@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def fav_details( request, pk):
	try:
		fav = Favourite.objects.get(id=pk)
		print fav
	except:
		return Response({'error': 'Favourite id not found'}, status=status.HTTP_400_BAD_REQUEST)

	usr = request.user
	owner = fav.user
		
	if usr == owner:
		serializer = favouriteSerializer(fav, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response({"error": "You are not authenticated to view other user's favourite teams."}, status=status.HTTP_401_UNAUTHORIZED)




@csrf_exempt
@api_view(['DELETE'])
@authentication_classes((TokenAuthentication,))
def fav_delete(request, pk):
	if request.user.is_authenticated():
		try:
			favourite = Favourite.objects.get(id=pk, user=request.user)
		except:
			return Response({'error': 'favourite id not found'}, status=status.HTTP_400_BAD_REQUEST)

		favourite.delete()
		return Response({'success': 'favourite deleted successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)





@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def match_today(request):
	if request.user.is_authenticated():
		f_team = Favourite.objects.values_list('team_name__id',flat=True).filter(user=request.user)
		match = Match.objects.filter(Q(date = date.today()) & (Q(home_team__id_in=f_team) | Q(away_team__id_in=f_team)))
		serializer = matchSerializer(match, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)




@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def match_nextweek(request):
	if request.user.is_authenticated():
		f_team = Favourite.objects.values_list('team_name__id',flat=True).filter(user=request.user)
		start_date = datetime.datetime.now()
 		end_date=start_date+timedelta(days=5)
		match = Match.objects.filter(Q(date__range=(start_date,end_date)) & (Q(home_team__id_in=f_team) | Q(away_team__id_in=f_team)))
		serializer = matchSerializer(match, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)
		

		
		


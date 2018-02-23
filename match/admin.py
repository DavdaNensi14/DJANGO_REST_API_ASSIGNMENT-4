from django.contrib import admin
from .models import * 

# Register your models here.
class MatchAdmin(admin.ModelAdmin):
	actions = ['enable']

	search_fields = ('date','home_team','away_team','time')
	ordering = ('date',)
	list_display = ('date','home_team','away_team','time')
	list_display_links = ('home_team',)
	list_filter = ('date','home_team','away_team','time')

	


admin.site.register(Match, MatchAdmin)
admin.site.register(Team)
admin.site.register(Favourite)
admin.site.register(Venue)
from django.shortcuts import render
from django.http import HttpResponse
from models import Cafe, Rating, Comment
from datetime import datetime, timedelta, time, date

from django.template import RequestContext, loader
import pytz
# Create your views here.

def home(request):
	cafes = Cafe.objects.all()
	cafe_dict = {}
	for cafe in cafes:
		ratings = Rating.objects.filter(cafe = cafe)
		average = float(sum(rating.value for rating in ratings))/len(ratings)
		cafe_dict[cafe] = average



	# display cafes with ratings
	context = {'cafe_dict': cafe_dict}
	return render(request, 'cafe_hop/index.html', context)











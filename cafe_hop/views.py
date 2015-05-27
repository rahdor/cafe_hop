from django.shortcuts import render
from django.http import HttpResponse
from models import Cafe, Rating, Comment
from datetime import datetime, timedelta, time, date

from django.template import RequestContext, loader
import pytz
# Create your views here.

def home(request):
	cafes = Cafe.objects.all()
	# display cafes with ratings
	context = {'cafe_list': cafes}
	return render(request, 'cafe_hop/index.html', context)








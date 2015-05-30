from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Cafe, Rating, Comment
from datetime import datetime, timedelta, time, date
from django.template import RequestContext, loader
import pytz
from forms import RatingForm
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):

	cafes = Cafe.objects.all()
	cafe_dict = {}
	for cafe in cafes:
		CHECKTIME = datetime.now()-timedelta(minutes=30)
		ratings = Rating.objects.filter(cafe = cafe, time__gte = CHECKTIME)
		try:
			average = float(sum(rating.value for rating in ratings))/len(ratings)
		except ZeroDivisionError:
			average = 'No ratings available'
		cafe_dict[cafe] = average

	# display cafes with ratings
	context = {'cafe_dict': cafe_dict}
	return render(request, 'cafe_hop/index.html', context)


def rate(request, cafe_id):
	
	print request.POST
	if request.method == 'POST':
		value = int(request.POST['rating'])
		cafe = Cafe.objects.get(id = cafe_id)
		now = datetime.now()
		rating = Rating(value = value, cafe = cafe, time = now)
		rating.save()
		# form = RatingForm(request.POST)
		# form.value = value
		# if form.is_valid():
		# 	return HttpResponseRedirect('/')	
	else:
		form = RatingForm()


	return redirect('/cafe_hop/')

	# return render(request, 'cafe_hop/rate.html', {'form': form})



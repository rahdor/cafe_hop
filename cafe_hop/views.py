from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Cafe, Rating, Comment
from datetime import datetime, timedelta, time, date
from django.template import RequestContext, loader

from forms import RatingForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from collections import OrderedDict
import pytz
import json

CHECKTIME = datetime.now()-timedelta(minutes=30)


def average_ratings(cafe, time):
	ratings = Rating.objects.filter(cafe = cafe, time__gte = time)
	try:
		average = float(sum(rating.value for rating in ratings))/len(ratings)
	except ZeroDivisionError:
		average = 'No ratings available'
	return [average, len(ratings)]


def moving_average_ratings(cafe, time):
	ratings = Rating.objects.filter(cafe = cafe, time__gte= time)
	try:
		num = 0.0
		den = 0.0
		for rating in ratings:
			then = datetime.utcnow().replace(tzinfo = pytz.utc)-timedelta(minutes = 30)
			val = (rating.time-then).seconds/60.0
			print (val, rating.time, rating.value)
			num += (rating.value)*val
			den += val
		average = num/den
	except ZeroDivisionError:
		average = 'No ratings available'
	return [average, len(ratings)]


def home(request):
	# get cafes, store in ordered dictionary with key: cafe value: [average rating, number of ratings]
	cafes = Cafe.objects.order_by('name')
	cafe_dict = OrderedDict()

	# trying
	cafe_dict_2 = OrderedDict()
	for cafe in cafes:
		cafe_dict_2[cafe.name] = moving_average_ratings(cafe, CHECKTIME)
	print(json.dumps(cafe_dict_2))	

	# end trying

	for cafe in cafes:
		cafe_dict[cafe] = moving_average_ratings(cafe, CHECKTIME)
		
	# display cafes with ratings and con
	context = {'cafe_dict': cafe_dict}
	# print(str(json.dumps(context)))
	return render(request, 'cafe_hop/index.html', context)




def rate(request, cafe_id):
	# create a rating object for a cafe from POST data
	if request.method == 'POST':
		try:
			# get the value of the rating value from the form, redirect if value is invalid
			value = int(request.POST['rating'])
		except ValueError:
			messages.add_message(request, messages.INFO, 'please choose a valid rating')
			return redirect('/cafe_hop/')
		# create new rating object for current cafe with datetime set to current
		cafe = Cafe.objects.get(id = cafe_id)
		now = datetime.now()
		# throw error/redirect if rating > 5 or < 0
		if (value > 5 or value < 0):
			messages.add_message(request, messages.INFO, 'please choose rating from 1-5')
			return redirect('/cafe_hop/')
		rating = Rating(value = value, cafe = cafe, time = now)
		rating.save()
	else:
		form = RatingForm()
	return redirect('/cafe_hop/')



def cafe(request, cafe_id):
	#display cafe information
	cafe = Cafe.objects.get(id = cafe_id)
	value_list = average_ratings(cafe, CHECKTIME)
	comment_list = Comment.objects.filter(cafe = cafe, time__gte = CHECKTIME).order_by('-time')
	context = {'cafe': cafe, 'value': value_list, 'comment_list': comment_list}
	return render(request, 'cafe_hop/cafe.html', context)
	


def comment(request, cafe_id):
	# controller action for submitting comments
	if request.method == 'POST':
		try:
			text = request.POST['comment']
		except ValueError:
			messages.add_message(request, messages.INFO, 'please enter a valid comment')
			return redirect('/cafe_hop/')
		cafe = Cafe.objects.get(id = cafe_id)
		now = datetime.now()		
		comment = Comment(text = text, cafe = cafe, time = now)
		comment.save()
		return redirect('/cafe_hop/cafes/' + cafe_id + '/')
	else:
		return redirect('/cafe_hop/')

def music(request):
	# redirects to music
	return render(request, 'cafe_hop/music.html', {})
	
def about(request):
	return render(request, 'cafe_hop/about.html', {})



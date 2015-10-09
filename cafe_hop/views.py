from django.shortcuts import render, redirect
from django.core.serializers.json import DateTimeAwareJSONEncoder

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
			then = datetime.utcnow().replace(tzinfo = pytz.utc)-timedelta(minutes = 60)
			val = (rating.time-then).seconds/60.0
			num += (rating.value)*val
			den += val
		average = round(((num/den)/5*100), 1)
	except ZeroDivisionError:
		average = 'No ratings available'
	return [average, len(ratings)]



def home(request):
	# get cafes, store in ordered dictionary with key: cafe value: [average rating, number of ratings]
	CHECKTIME = datetime.now()-timedelta(minutes=60)
	cafes = Cafe.objects.order_by('name')
	cafe_dict = OrderedDict()

	# trying
	cafe_dict_2 = OrderedDict()
	for cafe in cafes:
		cafe_dict_2[cafe.name] = moving_average_ratings(cafe, CHECKTIME)


	# end trying

	for cafe in cafes:
		cafe_dict[cafe] = moving_average_ratings(cafe, CHECKTIME)
		
	# display cafes with ratings and con
	context = {'cafe_dict': cafe_dict}
	# print(str(json.dumps(context)))
	return render(request, 'cafe_hop/index.html', context)


def validate(session, cafe_id):
	# check if cafe is in sessions dictionary
	if cafe_id not in session.keys():
		session[cafe_id] = encodeDateTime(datetime.now() + timedelta(minutes = 1))
	else:
		checkdate = decodeDateTime(session[cafe_id])
		if datetime.now() > checkdate:
			print("checkdate " + str(checkdate))
			print("now " + str(datetime.now()))
			print("rated")
			session[cafe_id] = encodeDateTime(datetime.now() + timedelta(minutes = 1))
			return True
		else:
			
			print("checkdate " + str(checkdate))
			print("now " + str(datetime.now()))
			print("did not rate")

			return False

def encodeDateTime(d):
	return str(d)

def decodeDateTime(d):
	return datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f")

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
			return redirect('/')
		if validate(request.session, cafe_id):
			rating = Rating(value = value, cafe = cafe, time = now)
			rating.save()
		else:
			messages.add_message(request, messages.INFO, 'please wait before you rate again')
			return redirect('/')
	else:
		form = RatingForm()
	return redirect('/')

def thanks(request):
	context = {}
	return render(request, 'cafe_hop/thanksbitch.html', context)

def cafe(request, cafe_id):
	CHECKTIME = datetime.now()-timedelta(minutes=60)
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
		return redirect('/')

def music(request):
	# redirects to music
	return render(request, 'cafe_hop/music.html', {})
	
def about(request):
	return render(request, 'cafe_hop/about.html', {})



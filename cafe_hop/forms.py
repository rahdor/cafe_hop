from django import forms
from models import Cafe, Rating, Comment
from django.core.validators import MaxValueValidator, MinValueValidator



class RatingForm(forms.Form):
	value = forms.IntegerField(label = 'How full is this cafe?', 
		initial = 0,
		validators = [
			MaxValueValidator(5),
			MinValueValidator(1)
			]
		)
	



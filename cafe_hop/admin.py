from django.contrib import admin
from cafe_hop.models import Cafe, Rating, Comment

# Register your models here.


#for displaying ratings
class RatingAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['value', 'cafe']}),
	]


class CommentAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['text']}),
	]

class CafeAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['name']}),
	]


admin.site.register(Cafe, CafeAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Comment, CommentAdmin)

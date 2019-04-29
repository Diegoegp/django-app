
# Register your models here.

from django.contrib import admin
from api.music.models.models import Songs, Genres
from api.music.models.MorosoModel import User, Moroso

admin.site.register(Songs)
admin.site.register(Genres)
admin.site.register(User)
admin.site.register(Moroso)

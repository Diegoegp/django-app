
# Register your models here.

from django.contrib import admin
from api.music.models.models import Songs, Genres

admin.site.register(Songs)
admin.site.register(Genres)

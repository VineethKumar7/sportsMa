from django.contrib import admin
from .models import UserProfile,Player, Tournament, Awards
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(Awards)

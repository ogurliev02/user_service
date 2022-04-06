from django.contrib import admin
from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'favorite_colors')


admin.site.register(Profile, ProfileAdmin)

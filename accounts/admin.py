from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'bio', 'get_username', 'get_email']

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = 'Email'

    def delete_model(self, request, obj):
        user=obj.user
        obj.delete()
        user.delete()


admin.site.register(Profile, ProfileAdmin)

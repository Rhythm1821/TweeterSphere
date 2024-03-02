from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Profile,Tweet

# Register your models here.
admin.site.unregister(Group)


# Mix Profile info into User info
class ProfileInline(admin.StackedInline):
    model = Profile

    
class UserAdmin(admin.ModelAdmin):
    model=User
    fields=['username']
    inlines=[ProfileInline]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

admin.site.register(Tweet)

from django.contrib import admin
from .models import LongtoShort,UserProfile
# Register your models here.

admin.site.register([LongtoShort,UserProfile])
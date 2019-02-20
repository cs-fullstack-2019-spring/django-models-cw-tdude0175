from django.contrib import admin
from .models import Dogs
from .models import Account

# importing from models to use in admin
admin.site.register(Dogs)
admin.site.register(Account)

from django.contrib import admin
from .models import User, Transactions

# Register your models here.

#admin.site.register(checkbookApp)
admin.site.register(User)
admin.site.register(Transactions)
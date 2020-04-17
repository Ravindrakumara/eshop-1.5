from django.contrib import admin
from.models import Registration
from.models import item
from.models import Brands
from.models import Categories
from.models import User

# Register your models here.
admin.site.register(Registration)
admin.site.register(item)
admin.site.register(Brands)
admin.site.register(Categories)
admin.site.register(User)

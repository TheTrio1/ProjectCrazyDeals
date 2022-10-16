from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Shirt)
admin.site.register(Pants)
admin.site.register(WomensWare)
admin.site.register(MenWare)
admin.site.register(KidsWare)
admin.site.register(Goggles)
admin.site.register(FootWare)

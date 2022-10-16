from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Shirt, ShirtAdmin)
admin.site.register(Pants)
admin.site.register(WomensWare)
admin.site.register(MenWare)
admin.site.register(KidsWare)
admin.site.register(Goggles)
admin.site.register(FootWare)

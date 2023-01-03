from django.contrib import admin

# Register your models here.
from .models import Lion, Feeding, Toy

admin.site.register(Lion)
admin.site.register(Feeding)
admin.site.register(Toy)
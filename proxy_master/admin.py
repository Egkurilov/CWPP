from django.contrib import admin
from .models import Project, Proxy, staticParam


admin.site.register(Project)
admin.site.register(Proxy)
admin.site.register(staticParam)
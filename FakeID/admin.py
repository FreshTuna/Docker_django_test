from django.contrib import admin
from .models import ID
# Register your models here.

class IDAdmin(admin.ModelAdmin):
    def queryset (self, request):
        qs = ID.objects.all()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

admin.site.register(ID, IDAdmin)

from django.contrib import admin
from insurance.models import Insurance, Client

# Register your models here.
# admin.site.register(Insurance)
# admin.site.register(Client)


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'name', 'price', 'period', ]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'bank_id', 'insurance', ]

from django.contrib import admin
from insurance.models import Insurance, Client, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.register(Insurance)
# admin.site.register(Client)

admin.site.register(User, UserAdmin)


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'name', 'price', 'period', ]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'bank_id', 'insurance', ]


# https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model

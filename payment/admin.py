from django.contrib import admin
from payment.models import Payement

# Register your models here.
@admin.register(Payement)

class PaymentAdmin(admin.ModelAdmin):
    list_display=('id','rid','pay')
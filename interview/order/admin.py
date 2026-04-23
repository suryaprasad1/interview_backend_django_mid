from django.contrib import admin
from interview.order.models import Order, OrderTag

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderTag)

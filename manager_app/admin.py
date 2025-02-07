from django.contrib import admin
from .models import userdata,Verification_otp

# Register your models here.
# class any_name(admin.ModelAdmin):
#     list_display =  ('id','name','email','mobile','password')

admin.site.register(userdata)
admin.site.register(Verification_otp)
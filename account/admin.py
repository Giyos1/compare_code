from django.contrib import admin
from account.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username')
    search_fields = ('email', 'username')


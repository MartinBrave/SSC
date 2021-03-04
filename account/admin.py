from django.contrib import admin

from account.models import Account


@admin.register(Account)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('username',)
    list_display = ('username', 'first_name', 'last_name')

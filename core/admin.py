from django.contrib import admin
from core.models import Expense, ExpenseParticipant, ExpenseGroup, GroupMember
# Register your models here.

admin.site.register(Expense)
admin.site.register(ExpenseGroup)
admin.site.register(GroupMember)


@admin.register(ExpenseParticipant)
class ExpenseParticipantAdmin(admin.ModelAdmin):
    list_display = ['expense', 'participant_amount', 'user', 'is_settled']
    list_per_page = 5
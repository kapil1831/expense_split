from django.db import models

# Create your models here.


class ExpenseGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_amount = models.DecimalField(null=True, blank=True, default=0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField()
    
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name
    

class GroupMember(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    group = models.ForeignKey('ExpenseGroup', related_name='group_members', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['user']
    
    def __str__(self):
        return self.user.username
    
class Expense(models.Model):
    name = models.CharField(max_length=100)
    expense_group = models.ForeignKey('ExpenseGroup', related_name='expense_group', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    payer = models.ForeignKey('auth.User', related_name='payer', on_delete=models.CASCADE)
    is_settled = models.BooleanField(default=False)    
    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name

class ExpenseParticipant(models.Model):
    expense = models.ForeignKey('Expense', related_name='expense_participants', on_delete=models.CASCADE)
    participant_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_settled = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    
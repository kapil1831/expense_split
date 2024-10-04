from django.db import models

# Create your models here.


class ExpenseGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField()

    def __str__(self):
        return self.name
    

class GroupMember(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    group = models.ForeignKey('ExpenseGroup', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
class Expense(models.Model):
    name = models.CharField(max_length=100)
    expense_group = models.ForeignKey('ExpenseGroup', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    payer = models.CharField(max_length=100)
    is_settled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ExpenseParticipant(models.Model):
    expense = models.ForeignKey('Expense', on_delete=models.CASCADE)
    participant_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    is_settled = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    
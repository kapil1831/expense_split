from rest_framework import serializers
from core.models import Expense, ExpenseParticipant, ExpenseGroup


class ExpenseGroupMemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    group = serializers.ReadOnlyField(source='group.name')
    is_admin = serializers.BooleanField()
    
    def create(self, validated_data):
        return ExpenseGroup.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.group = validated_data.get('group', instance.group)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.save()
        return instance


class ExpenseGroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    created_at = serializers.DateTimeField(read_only=True)
    image_url = serializers.URLField()
    group_members = ExpenseGroupMemberSerializer(many=True, read_only=True)  # For reverse relation

    
    def create(self, validated_data):
        return ExpenseGroup.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.save()
        return instance
     
class ExpenseParticipantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    expense = serializers.ReadOnlyField(source='expense.name')
    participant_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    user = serializers.ReadOnlyField(source='user.username')
    is_settled = serializers.BooleanField()
    
    def create(self, validated_data):
        return ExpenseParticipant.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.expense = validated_data.get('expense', instance.expense)
        instance.participant_amount = validated_data.get('participant_amount', instance.participant_amount)
        instance.user = validated_data.get('user', instance.user)
        instance.is_settled = validated_data.get('is_settled', instance.is_settled)
        instance.save()
        return instance

    
class ExpenseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    expense_group = serializers.ReadOnlyField(source='expense_group.name')
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    date = serializers.DateField()
    description = serializers.CharField()
    payer = serializers.ReadOnlyField(source='payer.username')
    is_settled = serializers.BooleanField()
    
    expense_participants = ExpenseParticipantSerializer(many=True, read_only=True)  # For reverse relation
    
    def create(self, validated_data):
        return Expense.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.expense_group = validated_data.get('expense_group', instance.expense_group)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)
        instance.payer = validated_data.get('payer', instance.payer)
        instance.is_settled = validated_data.get('is_settled', instance.is_settled)
        instance.save()
        return instance
    

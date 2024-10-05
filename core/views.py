from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import Expense, ExpenseParticipant, ExpenseGroup
from core.serializers import ExpenseSerializer, ExpenseGroupSerializer


# Create your views here.
@csrf_exempt
def index(request):

    if  request.method == 'GET':
        expense_groups = ExpenseGroup.objects.all()
        serializer = ExpenseGroupSerializer(expense_groups, many=True)
        
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExpenseGroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    return JsonResponse({'message': 'not supported method'}, status=405)


@csrf_exempt
def expense_list(request):
    if request.method == 'GET':
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    return JsonResponse({'message': 'not supported method'}, status=405)
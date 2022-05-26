from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from classifier import classifier
from django.http import JsonResponse

class Sub(APIView):
    def get(self,request):
        return render(request, "project_2022/index.html")

    def post(self,request):
        return render(request, "project_2022/index.html")

class Api(APIView):
    @csrf_exempt
    def post(self,request):
        input_text = request.POST['review']
        data = classifier(input_text)
        print(data)
        
        return JsonResponse(data)
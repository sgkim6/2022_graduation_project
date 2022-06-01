from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from classifier import classifier
from django.http import JsonResponse
import sqlite3 as sq3

class Sub(APIView):
    def get(self,request):
        return render(request, "project_2022/index.html")

    def post(self,request):
        return render(request, "project_2022/index.html")

class Api(APIView):
    @csrf_exempt
    def post(self,request):

        con = sq3.connect('./db.sqlite3', isolation_level= None)
        
        c = con.cursor()

        c.execute("SELECT dir FROM using_model")

        model_dir = c.fetchall()[0][0]
        print(model_dir)


        input_text = request.POST['review']
        data = classifier(input_text, model_dir)
        print(data)
        
        return JsonResponse(data)
    
class DB(APIView):
    def post(self, request):
        input_review = request.POST['review']
        input_result = request.POST['result']
        
        con = sq3.connect('./db.sqlite3', isolation_level= None)
        
        c = con.cursor()
        
        c.execute('INSERT INTO user_Data(REVIEW, RESULT) VALUES(?,?)',(input_review, input_result))
        
        con.close()
        
        return JsonResponse({'review' : input_review, 'reslut' : input_result})
        
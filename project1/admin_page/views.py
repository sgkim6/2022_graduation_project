from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from classifier import classifier
from django.http import JsonResponse
import sqlite3 as sq3

# Create your views here.

class Admin_page(APIView):
    def post(self,request):
        con = sq3.connect('./db.sqlite3', isolation_level= None)
        c = con.cursor()
        c.execute("SELECT * FROM model_list")
        data_list = c.fetchall()
        c.execute("DELETE FROM using_model")
        c.execute("INSERT INTO using_model VALUES('nsmc1','nsmc_model/bert-base',1)") #test
        con.close()
        
        return render(request, "project_2022/admin.html",{'data_list':data_list})

    def get(self,request):
        con = sq3.connect('./db.sqlite3', isolation_level= None)
        c = con.cursor()
        c.execute("SELECT * FROM model_list")
        data_list = c.fetchall()
        c.execute("DELETE FROM using_model")
        c.execute("INSERT INTO using_model VALUES('nsmc1','nsmc_model/bert-base',1)") #test
        con.close()
        
        return render(request, "project_2022/admin.html",{'data_list':data_list})

class Set_model(APIView):
    def post(self, request):
        model_name = request.POST.get('model_name')
        print(model_name)
        con = sq3.connect('./db.sqlite3', isolation_level= None)
        c = con.cursor()
        c.execute("SELECT dir FROM model_list WHERE name=?",(model_name,))
        model_dir = c.fetchall()[0][0]
        print(model_dir)
        c.execute("DELETE FROM using_model")
        c.execute("INSERT INTO using_model VALUES(?,?,1)",(model_name,model_dir,))

        con.close()
        return JsonResponse({'model_name':model_name})
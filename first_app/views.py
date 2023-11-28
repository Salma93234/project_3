from django.shortcuts import render
import datetime
def home(request):
    d={'author':'rahim','age':35,'list':[1,2,3],'lst':['phython','is','best'],'val':' ','birthday':datetime.datetime.now(),
       'courses':[
        {
            'id':1,
            'name':'django',
            'fee':5000,
        },
        {
            'id':2,
            'name':'c',
            'fee':6000,
        },
        {
            'id':3,
            'name':'js',
            'fee':8000,
        },
    ]}
    return render(request,'home.html',d)
from django.shortcuts import render
import datetime
def home(request):
    d={'author':'rahim','age':35,'list':[1,2,3],'lst':['phython','is','best'],'val':' ',
       
       'value':['Apple', 'Mango', 'Orange'] ,
       'my_data' : "cat\ndog\nhorse",
        'value3':'MY NAME SALMA',
        'value2':'you are wellcome in our programmin world',
        'value4':['Banana', 'Mango', 'Orange'],
         'some_list':['Father', 'Mother', 'Child'],
        'my_data2' : "It's a new day",
        
         'people' : [
        {'name': 'amy', 'age': 21},
        {'name': 'joe', 'age': 31},
        {'name': 'zed', 'age': 19},
    ],


        'value5':'Earthly',
       'birthday':datetime.datetime.now(),
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
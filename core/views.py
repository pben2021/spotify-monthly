from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import YearSerializer, JanuarySerializer, FebruarySerializer, MarchSerializer, AprilSerializer, MaySerializer, JuneSerializer, JulySerializer, AugustSerializer, SeptemberSerializer, OctoberSerializer, NovemberSerializer, DecemberSerializer
from .models import Year, January, February, March, April, May, June, July, August, September, October, November, December
from .monthspot import main
import time
from concurrent.futures import ThreadPoolExecutor


# Create your views here.
def front(request):
    context = { }
    return render(request, "index.html", context)

@api_view(['GET', 'POST'])
def year(request):

    if request.method == 'GET':
        year = Year.objects.all()
        serializer = YearSerializer(year, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        executor = ThreadPoolExecutor(max_workers=6)
        data=request.data

        #DELETE ALL CURRENT DATA SO IT DOESNT ADD EVERYTHING AGAIN WITH EACH RELOAD
        Year.objects.all().delete()
        January.objects.all().delete()
        February.objects.all().delete()
        March.objects.all().delete()
        April.objects.all().delete()
        May.objects.all().delete()
        June.objects.all().delete()
        July.objects.all().delete()
        August.objects.all().delete()
        September.objects.all().delete()
        October.objects.all().delete()
        November.objects.all().delete()
        December.objects.all().delete()

        #start getting individual month top and bottom songs. parallel for speed 😎. 
        f1 = executor.submit(jan, data)
        f2 = executor.submit(feb, data)
        f3 = executor.submit(mar, data)
        f4 = executor.submit(apr, data)
        f5 = executor.submit(my, data)
        f6 = executor.submit(jun, data)
        f7 = executor.submit(jul, data)
        f8 = executor.submit(aug, data)
        f9 = executor.submit(sep, data)
        f10 = executor.submit(oct, data)
        f11 = executor.submit(nov, data)
        f12 = executor.submit(dec, data)

        #save allmonths data
        allmonths = main(data, selection='allMonths', month=None)
        for month in allmonths:
            serializer = YearSerializer(data=month)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #sleep for 10 seconds after process done to allow parallel prgrams to complete. Should complete before 35 sec timeout
        time.sleep(10)
        return Response(status=status.HTTP_201_CREATED)
'''
Each month has 
-GET API view which returns serializd data
-normal function that gets top15 and bottom15 then serializes
'''

@api_view(['GET'])
def january(request):
    if request.method == 'GET':
        year = January.objects.all()
        serializer = JanuarySerializer(year, many=True)
        return Response(serializer.data)
def jan(DATA):
    entry = main(DATA, selection='perMonth', month='january')
    for song in entry:
        serializer = JanuarySerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])
def february(request):
    if request.method == 'GET':
        year = February.objects.all()
        serializer = FebruarySerializer(year, many=True)
        return Response(serializer.data)
def feb(DATA):
    entry = main(DATA, selection='perMonth', month='february')
    for song in entry:
        serializer = FebruarySerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])
def march(request):
    if request.method == 'GET':
        year = March.objects.all()
        serializer = MarchSerializer(year, many=True)
        return Response(serializer.data)
def mar(DATA):
    entry = main(DATA, selection='perMonth', month='march')
    for song in entry:
        serializer = MarchSerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])    
def april(request):
    if request.method == 'GET':
        year = April.objects.all()
        serializer = AprilSerializer(year, many=True)
        return Response(serializer.data)
def apr(DATA):
    entry = main(DATA, selection='perMonth', month='april')
    for song in entry:
        serializer = AprilSerializer(data=song)
        if serializer.is_valid():
            serializer.save()
            
@api_view(['GET'])
def may(request):
    if request.method == 'GET':
        year = May.objects.all()
        serializer = MaySerializer(year, many=True)
        return Response(serializer.data) 
def my(DATA):
    entry = main(DATA, selection='perMonth', month='may')
    for song in entry:
        serializer = MaySerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])
def june(request):
    if request.method == 'GET':
        year = June.objects.all()
        serializer = JuneSerializer(year, many=True)
        return Response(serializer.data) 
def jun(DATA):
    entry = main(DATA, selection='perMonth', month='june')
    print('done')
    for song in entry:
        serializer = JuneSerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])
def july(request):
    if request.method == 'GET':
        year = July.objects.all()
        serializer = JulySerializer(year, many=True)
        return Response(serializer.data)
def jul(DATA):
    entry = main(DATA, selection='perMonth', month='july')
    for song in entry:
        serializer = JulySerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])
def august(request):
    if request.method == 'GET':
        year = August.objects.all()
        serializer = AugustSerializer(year, many=True)
        return Response(serializer.data)
def aug(DATA):
    entry = main(DATA, selection='perMonth', month='august')
    for song in entry:
        serializer = AugustSerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])
def september(request):
    if request.method == 'GET':
        year = September.objects.all()
        serializer = SeptemberSerializer(year, many=True)
        return Response(serializer.data)
def sep(DATA):
    entry = main(DATA, selection='perMonth', month='september')
    for song in entry:
        serializer = SeptemberSerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])
def october(request):
    if request.method == 'GET':
        year = October.objects.all()
        serializer = OctoberSerializer(year, many=True)
        return Response(serializer.data)
def oct(DATA):
    entry = main(DATA, selection='perMonth', month='october')
    for song in entry:
        serializer = OctoberSerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])
def november(request):
    if request.method == 'GET':
        year = November.objects.all()
        serializer = NovemberSerializer(year, many=True)
        return Response(serializer.data)
def nov(DATA):
    entry = main(DATA, selection='perMonth', month='november')
    for song in entry:
        serializer = NovemberSerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])
def december(request):
    if request.method == 'GET':
        year = December.objects.all()
        serializer = DecemberSerializer(year, many=True)
        return Response(serializer.data)
def dec(DATA):
    entry = main(DATA, selection='perMonth', month='december')
    for song in entry:
        serializer = DecemberSerializer(data=song)
        if serializer.is_valid():
            serializer.save()

@api_view(['GET'])
def noview(request, month):
    return redirect(front)
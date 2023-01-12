from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')


def read_index_data(request):
    fnum = request.POST["tbfnum"]
    snum = request.POST["tbsnum"]
    print(type(fnum))
    print(type(snum))
    return  render(request,'home.html',{'fn':fnum,'sn':snum})
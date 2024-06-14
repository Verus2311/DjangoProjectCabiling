from django.shortcuts import render

# Create your views here.
def helloWorld (request):
    return render(request,'helloWorld.html')

def testpath (request):
    return render(request,'testPath.html')

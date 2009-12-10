# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from doodle.models import *


def helloWorld(theRequest):
    return HttpResponse("<h1>Hello World</h1>")

def helloPerson(theRequest, thePerson):
    return HttpResponse("<h1>Hello " + str(thePerson) + " !</h1>")

def listDoodleTypes(theRequest):
    myObjects = DoodleType.objects.all()
    # Optional - sort descending:
    #myObjects = DoodleType.objects.all().order_by("-name")
    myResult = "<h1>doodle types</h1>"
    for myObject in myObjects:
        myResult = myResult + str(myObject.id) + " : " + str(myObject.name) + "<br />"
    return HttpResponse(myResult)

def showDoodleType(theRequest, theId):
    # Old way :
    #myObject = DoodleType.objects.get(id=theId)
    # New way :
    myObject = get_object_or_404(DoodleType, id=theId)
    myResult = "<h1>Doodle Type Details</h1>"
    myResult = myResult + "Id: " + str(myObject.id) + "<br />"
    myResult = myResult + "Name: " + str(myObject.name) + "<br />"
    return HttpResponse(myResult)

def deleteDoodleType(theRequest, theId):
    myObject = get_object_or_404(DoodleType, id=theId)
    myResult = "<h1>Doodle Type Deleted:</h1>"
    myResult = myResult + "Id: " + str(myObject.id) + "<br />"
    myResult = myResult + "Name: " + str(myObject.name) + "<br />"
    myObject.delete()
    return HttpResponse(myResult)

def createDoodleType(theRequest, theName):
    myObject = DoodleType()
    myObject.name = theName
    myObject.save()
    myResult = "<h1>Doodle Type Created:</h1>"
    myResult = myResult + "Id: " + str(myObject.id) + "<br />"
    myResult = myResult + "Name: " + str(myObject.name) + "<br />"
    return HttpResponse(myResult)

def updateDoodleType(theRequest, theId, theName):
    myObject = get_object_or_404(DoodleType, id=theId)
    myObject.name = theName
    myObject.save()
    myResult = "<h1>Doodle Type Updated:</h1>"
    myResult = myResult + "Id: " + str(myObject.id) + "<br />"
    myResult = myResult + "Name: " + str(myObject.name) + "<br />"
    return HttpResponse(myResult)

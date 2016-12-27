from django.shortcuts import render, redirect
from . import models
import urllib
from django.contrib import messages
import bcrypt
import requests
import json

def index(request):
    return render(request, "project_app/index.html")

def school_list_process(request):
    school_name = request.POST["school_name"]
    # url = "https://api.data.gov/ed/collegescorecard/v1/schools?&api_key=BqnSd2SIBDqAoMR8Cv1hHNCQcKd4z9TzShqo4jTj"

    url = 'https://api.data.gov/ed/collegescorecard/v1/schools'

    #Format Try 1
    # api_key = {
    #           'api_key' : "BqnSd2SIBDqAoMR8Cv1hHNCQcKd4z9TzShqo4jTj"
    #          }
    # school = {
    #           'school.name' : school_name,
    #          }
    # api_key_encode = urllib.urlencode(api_key)
    # school_encode = urllib.urlencode(school)
    # full_url= url + "?" + school_encode + "&" + api_key_encode
    # response = urllib.urlopen(full_url)
    # result = response.read()

    #Format Try 2
    # values = {
    #           'school.name' : school_name,
    #           'api_key' : "BqnSd2SIBDqAoMR8Cv1hHNCQcKd4z9TzShqo4jTj",
    #          }
    #
    # data = urllib.urlencode(values)
    # full_url= url + "?" + data
    # response = urllib.urlopen(full_url)
    # result = response.read()
    # result = json.load(response)
    # tuition = result["results"][0]["2014"]["cost"]
    # school = result["results"][0]["school"]["name"]
    # location = result["results"][0]["school"]["city"] + ", " + result["results"][0]["school"]["state"]
    # num_undergrads = result["results"][0]["2014"]["student"]["size"]


    #Format Try 3


    r = requests.get('https://api.data.gov/ed/collegescorecard/v1/schools')
    r.encoding = 'UTF-8'
    print json.loads(r.text)
    #Name, Location, number of undergraduates, graduation, avg. annual cost,

    # context={
    #     "tuition" : tuition,
    #     "school" : school,
    #     "location" : location,
    #     "num_undergrads" : num_undergrads
    # }
    return render(request, "project_app/school_list.html")

    # if len(school_name)>0:
    #     # print "/school_profile_process/{school_name}"
    #     return redirect("/school_profile_process")
    # if request.POST["state"]>0 or len(zip_code)>0:
    #     return redirect("/school_list")

# def school_list(request):

    # arr =[""]
	# actors=[""]
	# url = "https://api.data.gov/ed/collegescorecard/v1/json&api_key=BqnSd2SIBDqAoMR8Cv1hHNCQcKd4z9TzShqo4jTj"
	# response = urllib.urlopen(url)
	# data = json.loads(response.read())
	# for i in data['data']:
	# 	if arr[len(arr)-1] != i[8]:
	# 		arr.append(i[8])
    #
	# for i in data['data']:
	# 	if actors[len(actors)-1] != i[14]:
	# 		actors.append(i[14])
    #
	# data = {"titles": arr, "actors":actors}
    # return render(request, "school_list.html")

# def school_profile_process(request):
#     print "Made it to school profile_process."


    # return render(request, "school_profile.html")

# def school_profile_process(request,school_name):
#     print "Made it to school profile process."
#
#     return redirect("/school_profile")

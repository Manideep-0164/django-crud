from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.contrib import messages
# Create your views here.

data = {
    "users":[
        {"id":1, "name":"john", "age":20, "city":'UK'},
        {"id":2, "name":"mariano", "age":25, "city":'New York'},
        {"id":3, "name":"doe", "age":30, "city":'London'},
    ]
}

def crud_home(request):
    return render(request, 'homepage/homepage.html')

def display_items(request):
    if len(data["users"]) == 0:
        messages.info(request, "No data present.")
        return redirect('homepage')
    return render(request, 'crud/display.html', context=data)

def get_userdata(request):
    if request.method == 'POST':
        total_data = request.POST.dict()
        id = len(data["users"]) + 1
        data["users"].append({"id":id, "name":total_data['username'], "age":total_data['age'], "city":total_data['city']})
        print(data)
        return redirect('display_items')
    return render(request, 'crud/userform.html')

def edit_user(request,item_id):
    itemIterater = filter(lambda user: user["id"] == item_id, data["users"])
    item = list(itemIterater)[0]
    if not item:
        return HttpResponseNotFound("User not found")
    if request.method == 'POST':
        name = request.POST.get('username')
        age = request.POST.get('age')
        city = request.POST.get('city')
        item['name'] = name
        item['age'] = age
        item['city'] = city
        return redirect("display_items")
    return render(request, 'crud/editform.html', {'item':item})

def delete_user(request,item_id):
    filteredData = filter(lambda user: user["id"] != item_id, data['users'])
    data['users'] = list(filteredData)
    return redirect("display_items")


        




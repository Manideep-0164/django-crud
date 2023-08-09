from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

data = {
    "users":[
        {"id":1, "name":"john", "age":20, "city":'UK'},
    ]
}

def crud_home(request):
    return render(request, 'homepage/homepage.html')

def display_items(request):
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
    item = None
    for user in data['users']:
        if user['id'] == item_id:
           item = user
        break
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
    data['users'] = filter(lambda user: user["id"] != item_id, data['users'])
    return redirect("display_items")


        




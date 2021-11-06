from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id':1, 'name': 'lets learn python!'},
#     {'id':2, 'name': 'Design with me!'},
#     {'id':3, 'name': 'frontend developers!'},
#
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, "colapp/home.html", context)



def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id = pk)
    context = {'room' : room}
    return render(request, "colapp/room.html", context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        #print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, "colapp/room_form.html", context)

def updateRoom(request, pk):                 # pass in request and also the pk(primary key) as we want to know which item we want to update
    room = Room.objects.get(id=pk)           # in this case we wanna update the room with Room.objects.get and the value we are going to get it by the id which is th pk
    form = RoomForm(instance=room)                        # when we click to edit a room we want to know wich room to edit, this line gives us an empty dictionary
    context = {'form':form}
    return render(request, 'colapp/room_form.html',context)
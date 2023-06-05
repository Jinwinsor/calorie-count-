from django.shortcuts import render, redirect
from .models import Food, Intake

# Create your views here.


def index(request):
    foods = Food.objects.all()
    user_intake = None
    if request.method == 'POST':
        my_selector = request.POST.get('calorie_selector')
        food_object = Food.objects.get(
            name=my_selector)

        user = request.user
        food_selector = Intake(user=user, food_intake=food_object)
        food_selector.save()
        foods = Food.objects.all()

    if request.user.is_authenticated:
        user_intake = Intake.objects.filter(user=request.user)

    return render(request, 'myapp/index.html', {'foods': foods, 'user_intake': user_intake})


def delete(request, id):
    my_delete = Intake.objects.get(id=id)
    # Bring each item's id.
    if request.method == 'POST':
        my_delete.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html', {'my_delete': my_delete})

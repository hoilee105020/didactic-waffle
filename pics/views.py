import random

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey, you're great!")

def random_int(request):
    upper_bound = request.GET.get('ub')
    lower_bound = request.GET.get('lb')

    num = random.randint(int(lower_bound), int(upper_bound))

    return HttpResponse('Your number is: ' + str(num))


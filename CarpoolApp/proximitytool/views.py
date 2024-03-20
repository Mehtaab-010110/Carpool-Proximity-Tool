from django.shortcuts import render
from .models import CarpoolGroup, Address, Person, Company

def index(request):
    """ View function for home page of site """

    # Get User's CarpoolGroup id
    carpool_group_id = 1 # NOTE: Stub value

    # Retrive the user's carpool group record
    carpool_group = CarpoolGroup.objects.filter(id__exact=carpool_group_id)[0]

    context = {"carpool_group" : carpool_group}

    # Render the HTML template index.html with the data in context variable
    return render(request, "index.html", context=context)

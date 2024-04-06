from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CarpoolGroup, Address, Person, Company

@login_required
def index(request):
    """ View function for home page of site """

    # Get User's CarpoolGroup id
    carpool_group_id = 1 # NOTE: Stub value

    # Retrive the user's carpool group record
    carpool_group = CarpoolGroup.objects.filter(id__exact=carpool_group_id)[0]

    # Visit Counter
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {"carpool_group" : carpool_group}

    # Render the HTML template index.html with the data in context variable
    return render(request, "index.html", context=context)

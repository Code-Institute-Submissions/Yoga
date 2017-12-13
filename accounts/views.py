from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from accounts.models import User
import datetime
import stripe
import arrow
import json

stripe.api_key = settings.STRIPE_SECRET

def register(request, e=None):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Customer.create(
                    email=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'],
                    plan='REG_MONTHLY',
                )

                if customer.paid:
                    form.save()
                    user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))

                    if user:
                        auth.login(request, user)
                        messages.success(request, "You have successfully registered")
                        return redirect(reverse('profile'))

                    else:
                        messages.error(request, "We are unable to log you in")

                else:
                    messages.error(request, "We were unable to take a payment with that card")

            except stripe.error.CardError as e:
                messages.error(request, "Your card was declined")

    else:
        today = datetime.date.today()
        form = UserRegistrationForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'Yoga/templates/register.html', args)

@login_required(login_url='Yoga/templates/login.html')
def profile(request):
     return render(request, 'Yoga/templates/profile.html')

@login_required(login_url='/accounts/login/')
def cancel_subscription(request):
   try:
       customer = stripe.Customer.retrieve(request.user.stripe_id)
       customer.cancel_subscription(at_period_end=True)
   except Exception as e:
       messages.error(request, e)
   return redirect('profile')



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'Yoga/templates/login.html', args)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

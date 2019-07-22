from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views import View
import datetime
from OWDR.forms import *
from OWDR.models import *
from OWDR.tokens import account_activation_token
from OWDR.utils import create_email_message


class LandingPageView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request):
        return render(request, 'OWDR/index.html')


class LoginView(View):
    def get(self, request, message=''):
        return render(request, 'OWDR/login.html', context={'form': LoginForm().as_p(), 'message': message})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_login')
            user_password = form.cleaned_data.get('user_password')
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    next_ = '/staff'
                else:
                    next_ = request.GET.get('next')
                print(next_)
                print(user.is_staff)
                if next_ is not None:
                    return redirect(next_)
                else:
                    return redirect(reverse_lazy('landing_page'))
            else:
                message = 'Niepoprawne dane logowania'
                return render(request, 'OWDR/login.html', context={'form': LoginForm(), 'message': message})


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm().as_p()
        context = {'form': form}
        return render(request, 'OWDR/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            email = create_email_message(get_current_site(request),
                                         "Aktywacja konta OWDR",
                                         'OWDR/acc_active_email.html',
                                         user,
                                         user.email)
            email.send()
            return redirect(reverse_lazy('login'))
        else:
            context = {'form': form}
            return render(request, 'OWDR/register.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and user.is_active != True and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'OWDR/activation.html')
    else:
        return HttpResponse('Nie poprawny link walidacyjny!')


class UserProfileView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request):
        return render(request, 'OWDR/user_profile.html', context={'user': request.user})


class EditProfileView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request):
        form = EditUserForm(instance=request.user).as_p()
        return render(request, 'OWDR/uni_form.html', context={'form': form, 'submit': 'Zapisz'})

    def post(self, request):
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('profile'))
        else:
            form = EditUserForm(instance=request.user).as_p()
            return render(request, 'OWDR/uni_form.html', context={'form': form, 'submit': 'Zapisz'})


class ChangePasswordView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, 'OWDR/uni_form.html', context={'form': form, 'submit': 'Zapisz'})

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse_lazy('profile'))
        else:
            message = "Hasło niepoprawne"
            form = PasswordChangeForm(user=request.user)
            return render(request, 'OWDR/uni_form.html', context={'form': form, 'submit': 'Zapisz', 'message': message})


class LogoutView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))


class FormView(LoginRequiredMixin, View):
    '''todo: check if date and time is not in the past'''
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request, error_message=''):
        items = Item.objects.filter(pk__lte=33)
        provinces = Province.objects.all()
        targets = Target.objects.all()
        institutions = Institution.objects.all()
        context = {'items': items, 'provinces': provinces, 'targets': targets, 'institutions': institutions, 'error_message': error_message}
        return render(request, 'OWDR/form.html', context)

    def post(self, request):
        items = request.POST.getlist('item')
        other_item = request.POST.get('others_text_field')
        quantity = request.POST.get('quantity')
        institution = request.POST.get('institution')
        street = request.POST.get('street')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        phone_number = request.POST.get('phone_number')
        date_ = request.POST.get('date')
        time_ = request.POST.get('time')
        message = request.POST.get('message')
        if (len(items) > 0 or other_item)\
                and None not in (quantity, institution, street, city, postal_code, phone_number, date_, time_, message):
            try:
                quantity = int(quantity)
                institution = int(institution)
                date_list = date_.split('-')
                date_ = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
                time_list = time_.split(':')
                time_ = datetime.time(int(time_list[0]), int(time_list[1]))
            except ValueError:
                return self.get(request, error_message="Coś poszło nie tak, uzupełnij formularz jeszcze raz")
            if other_item:
                catalogued_item = Item.objects.filter(name=other_item).first()
                if not catalogued_item:
                    other_item = Item.objects.create(name=other_item)
                    items.append(other_item.pk)
                else:
                    items.append(catalogued_item.pk)
            for i in range(len(items)):
                try:
                    items[i] = int(items[i])
                except ValueError:
                    return self.get(request, error_message="Coś poszło nie tak, uzupełnij formularz jeszcze raz")
            pick_up_address = PickUpAddress.objects.filter(street=street,
                                                           city=city,
                                                           postal_code=postal_code,
                                                           phone_number=phone_number).first()
            if not pick_up_address:
                pick_up_address = PickUpAddress.objects.create(street=street,
                                                               city=city,
                                                               postal_code=postal_code,
                                                               phone_number=phone_number)
            courier_information = CourierInformation.objects.filter(date=date_,
                                                                    time=time_,
                                                                    message=message).first()
            if not courier_information:
                courier_information = CourierInformation.objects.create(date=date_,
                                                                        time=time_,
                                                                        message=message)
            gift = Gift.objects.create(quantity=quantity,
                                       institution_id=institution,
                                       pick_up_address_id=pick_up_address.pk,
                                       courier_information_id=courier_information.pk,
                                       created_by=request.user)

            gift.items.add(*items)
        else:
            return self.get(request, error_message="Coś poszło nie tak, uzupełnij formularz jeszcze raz")
        return render(request, 'OWDR/thanks.html')


class MyDonationsView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request):
        my_active_donations = Gift.objects.filter(picked_up=False, created_by=request.user).order_by("created_date")
        my_past_donations = Gift.objects.filter(picked_up=True, created_by=request.user).order_by("-picked_up_date")
        context = {'active': my_active_donations, 'past': my_past_donations}
        return render(request, 'OWDR/my_donations.html', context)

    def post(self, request):
        donations = request.POST.getlist('donation')
        for i in range(len(donations)):
            try:
                donations[i] = int(donations[i])
                Gift.objects.filter(pk=donations[i]).update(picked_up=True, picked_up_date=datetime.date.today())
            except ValueError:
                return self.get(request)
        return self.get(request)


class DonationDetailsView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request, pk):
        donation = Gift.objects.get(pk=pk)
        return render(request, 'OWDR/donations_details.html', context={'donation': donation})

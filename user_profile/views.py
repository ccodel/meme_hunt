from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from users.models import CustomUser

class UserProfileListView(ListView):
    context_object_name = 'user_list'
    template_name = 'user_profile/user_list.html'

    def get(self, request):
        # If not admin, can't view the list
        if not request.user.is_staff:
            messages.add_message(request, messages.WARNING,
                    'Staff only page.')
            return HttpResponseRedirect(reverse(''))

        user_list = CustomUser.objects.all()
        return render(request, self.template_name, {'user_list': user_list})


class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'user_profile/user_profile.html'

    def get(self, request):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.WARNING,
                    'You must log in to view your profile.')
            return HttpResponseRedirect(reverse(''))
        elif request.GET.get('email', None) is not None:
            if not request.user.is_staff:
                messages.add_message(request, messages.WARNING,
                        'Staff only page.')
                return HttpResponseRedirect(reverse(''))

            # Otherwise, can view that user's page
            u = CustomUser.objects.get(email=request.GET.get('email'))
            return render(request, self.template_name, {'passed_user': u})
        else:
            return render(request, self.template_name, {'passed_user': request.user})

    def post(self, request):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.WARNING,
                    'You must log in to edit your profile.')
            return HttpResponseRedirect(reverse(''))

        # Update name information for the user
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if not request.user.is_staff and request.user.email != email:
            messages.add_message(request, messages.WARNING,
                    'You cannot edit another user\'s profile.')
            return HttpResponseRedirect(reverse(''))

        u = CustomUser.objects.get(email=email)
        u.first_name = first_name
        u.last_name = last_name
        u.save()

        # Let user know the profile has been updated
        messages.add_message(request, messages.SUCCESS, 'Profile updated')
        return render(request, self.template_name, {'passed_user': u})

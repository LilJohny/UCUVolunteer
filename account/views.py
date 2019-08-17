from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from account.models import Profile


# Create your views here.
class ProfileView(TemplateView):
    template_name = 'account/profile.html'

    def post(self, request, **kwargs):
        contex = self.get_context_data()
        username = request.POST["username"]
        user_profile = Profile.objects.filter(user__username=username)[0]
        contex["profile_image"] = user_profile.avatar
        return render_to_response(self.template_name, contex)

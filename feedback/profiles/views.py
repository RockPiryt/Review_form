from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.
################################Auto Form from model with CreateView
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile_createview.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name="profiles/user_info.html"
    context_object_name = "html_profiles"
#
################################DjangoForm+store file (path) in Database
# class CreateProfileView(View):
#     def get(self, request):
#         image_form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "html_image_form":image_form,
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             profile = UserProfile(zimage=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
        
#         return render(request, "profiles/create_profile.html", {
#             "html_image_form":submitted_form,
#         })

#################################html form with name="my_image"
# def store_file(file):
#     with open("temp/image.jpg", "wb+") as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)
# class CreateProfileView(View):
#     def get(self, request):
#         return render(request, "profiles/create_profile.html")

#     def post(self, request):
#         store_file(request.FILES["my_image"])
#         return HttpResponseRedirect("/profiles")

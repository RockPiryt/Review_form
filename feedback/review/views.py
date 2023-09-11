from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import AutoReviewForm, ReviewForm
from .models import Review

from django.views import View
# Create your views here.
class ReviewView(View):
    def get(self, request):
        first_form = AutoReviewForm()
        return render(request, "review/index.html", {"html_form": first_form,})
    
    def post(self,request):
        first_form = AutoReviewForm(request.POST)

        if first_form.is_valid():
            first_form.save()
            return HttpResponseRedirect("/thanks")
        
        return render(request, "review/index.html", {"html_form": first_form,})


# #--------------------MODELFORM------------#
# def index(request):
#     if request.method == "POST":
#         existing_data = Review.objects.get(pk=1)
#         first_form = AutoReviewForm(request.POST, instance=existing_data)

#         if first_form.is_valid():
#             first_form.save()
#             return HttpResponseRedirect("/thanks")

#     else:
#         first_form = AutoReviewForm()
#     return render(request, "review/index.html", {"html_form": first_form,})

def thank_you(request):
    return render(request, "review/thank.html")


# #-------------------------HANDY FORM------------------------#
# def index(request):
#     if request.method == "POST":
#         first_form = ReviewForm(request.POST)

#         if first_form.is_valid():
#             # print(first_form.cleaned_data)
#             my_review =  Review(user_name=first_form.cleaned_data['fuser_name'],
#                                 review_text=first_form.cleaned_data['freview_text'],
#                                 rating=first_form.cleaned_data['frating'])
#             my_review.save()

#             return HttpResponseRedirect("/thanks")

#     else:
#         first_form = ReviewForm()
#     return render(request, "review/index.html", {"html_form": first_form,})

# def thank_you(request):
#     return render(request, "review/thank.html")


#####################Handy Form###############################
# def index(request):
#     if request.method == "POST":
#         entered_username = request.POST['username_field']
        
#         if entered_username == "" and len(entered_username) >= 100:
#             return render(request, "review/index.html", {
#                 "has_error": True,
#             })
#         return HttpResponseRedirect("/thanks")
    
#     return render(request, "review/index.html", {
#         "has_error": False,
#     })
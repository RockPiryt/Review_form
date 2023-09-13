from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from .forms import AutoReviewForm, ReviewForm
from .models import Review

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView


# Create your views here.

#########################CLASS VIEWS OR DEF############################################
#----------------------------------------------------------------[CreateView] - super
class ReviewView4(CreateView):
    #GET method
    model = Review
    #Auto without custom labels/error messages
    # fields = "__all__" # which db fields in form 

    #My labels/error messages
    form_class = AutoReviewForm
    template_name = "review/index_formview.html"
    #POST method
    success_url = "/thank-you"

#----------------------------------------------------------------[FormView] - super
class ReviewView3(FormView):
    #GET method
    #Modelform
    form_class = AutoReviewForm
    template_name = "review/index_formview.html"
    #POST method
    success_url = "/thank-you"
    #Save form data
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



#----------------------------------------------------------------[View] -super (GET/POST)
class ReviewView(View):
    def get(self, request):
        first_form = AutoReviewForm()
        return render(request, "review/index.html", {"html_form": first_form,})
    
    def post(self,request):
        first_form = AutoReviewForm(request.POST)

        if first_form.is_valid():
            first_form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "review/index.html", {"html_form": first_form,})



######################Thank You 3 methods######################################
# --------------------------------------------------------------------[Def]  - super
def thank_you(request):
    return render(request, "review/thank.html", {
        "html_message": "This is passed context text!",
        })
#----------------------------------------------------------------[Template View] - long
class ThankYouView(TemplateView):
    template_name= "review/thank.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["html_message"] = "This is passed context text!"
        return context

#--------------------------------------------------------------------[Class View]
# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "review/thank.html")




######################List all reviews 2 methods######################################
#---------------------------------------------------------------------[ListView] -super
class ReviewListView2(ListView):
    template_name="review/review_list_listview.html"
    model = Review
    context_object_name = "html_all_reviews2"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=2)
        return data
# --------------------------------------------------------------------[TemplateView]
# class ReviewListView(TemplateView):
#     template_name="review/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         all_reviews = Review.objects.all()
#         context["html_all_reviews"] = all_reviews
#         return context

######################Single review 2 methods######################################
#--------------------------------------------------------------------[DetailView] -super
class SingleReviewView2(DetailView):
    template_name="review/single_review_detailview.html"
    model = Review# this DetailView get object (single_review)in context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # now in context we have Review object
        view_loaded_review = self.object 
        view_request = self.request
        eefavorite_id = view_request.session["zz_favorite_review"]
        #save way - don't make crash if not favorite id in session
        eefavorite_id = view_request.session.get("zz_favorite_review") # return None if key is not exist
        # if eefavorite_id == str(view_loaded_review.id):
        # # I add new info/data to my object
        #     context["tag_is_favorite"] = True
        #     return context
        # I add new info/data to my object if id are equal
        context["tag_is_favorite"] = eefavorite_id == str(view_loaded_review.id)
        return context

# --------------------------------------------------------------------[TemplateView]
# class SingleReviewView(TemplateView):
#     template_name="review/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["rev_id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["html_selected_review"] = selected_review
#         return context

class AddFavoriteView(View):
    def post(self, request):
        fav_review_id = request.POST["aareview_id"]
        # my_fav_review = Review.objects.get(pk=fav_review_id)# this object, can't be JSON
        # request.session["zz_favorite_review"] = my_fav_review
        request.session["zz_favorite_review"] = fav_review_id # correct for JSON format
        return HttpResponseRedirect("/reviews/"+ fav_review_id) # redirect to SingleReviewView2




#############################FORM 3 METHODS TO MAKE############################

# -----------------------------------[MODELFORM] - the best and fast way to create form
def index(request):
    if request.method == "POST":
        existing_data = Review.objects.get(pk=1)
        first_form = AutoReviewForm(request.POST, instance=existing_data)

        if first_form.is_valid():
            first_form.save()
            return HttpResponseRedirect("/thanks")

    else:
        first_form = AutoReviewForm()
    return render(request, "review/index.html", {"html_form": first_form,})

def thank_you(request):
    return render(request, "review/thank.html")


# #-------------------------[HANDY FORM with create DB object] - ok but slow
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


#---------------------------------------------------------[Handy HTML Form] - not good!!!
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
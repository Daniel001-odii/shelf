from re import template
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import post_form
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.


class HomeDetail(generic.ListView):
    queryset = False
    template_name = 'index.html'


'''class userProfile(generic.ListView):
    queryset = False
    template_name = 'profile.html'
''' 


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-uploaded_on')
    template_name = 'home.html'




class PostDetail(generic.DetailView):
    model = Post
    template_name = 'detail.html'



#----------update and make changes to a post ---------------------#
class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ["title", "description", "Book_author", "file", "thumbnail"]
    #template_name = 'pmaker/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("home")

    def get_queryset(self):
        return self.model.objects.filter(uploaded_by=self.request.user)




#---------------delete  POST -------------------------#
class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("home")

    def get_queryset(self):
        return self.model.objects.filter(uploaded_by=self.request.user)





BOOK_FILE_TYPES = ['pdf', 'doc', 'txt']

def create_post(request):
    form = post_form()
    if request.method == 'POST':
        form = post_form(request.POST, request.FILES)
        if form.is_valid():
            user_book = form.save(commit = False)
            user_book.user = request.user#------------#
            user_book.save()
            user_book.file = request.FILES['file']
            #---------------------#
            file_type = user_book.file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in BOOK_FILE_TYPES:
                return render(request, 'pmaker/error.html')
            user_book.save()
            return render(request, 'pmaker/success.html', 
                {'user_book': user_book})
    context = {"form": form,}
    return render(request, 'pmaker/create.html', context)


def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Post.objects.filter(Q(title__icontains=query) | Q(Book_author__icontains=query) | Q(level__icontains=query) )
    return render(request, 'search.html', {'query': query, 'results': results})
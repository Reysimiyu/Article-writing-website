from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from django.http import HttpResponseRedirect
from .forms import MemberForm,UpdateForm
# Create your views here.

def LikeView(request, pk):
    #like
    post = get_object_or_404(Member, id = request.POST.get('member_id'))

    #unlike
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('post_detail', args = [str(pk)]))

class HomePage(ListView):
    model=Member
    template_name='index.html'
    ordering=['-post_date']

    def get_context_data(self,*args,**kwargs):
        menu_list=Category.objects.all()
        context = super(HomePage,self).get_context_data(*args,**kwargs)
        context["menu_list"] = menu_list
        return context

def CategoryPosts(request, cats):
    category_posts=Member.objects.filter(category=cats)
    context={
        'cats':cats.title(),
        'category_posts':category_posts
    }
    return render(request, 'category.html',context)

class PostDetails(DetailView):
    model=Member
    template_name='post_detail.html'

    def get_context_data(self,*args,**kwargs):
        menu_list=Category.objects.all()
        context = super(PostDetails,self).get_context_data(*args,**kwargs)

        #liking the post
        NumberOfLikes=get_object_or_404(Member, id = self.kwargs['pk'])
        total_likes=NumberOfLikes.total_likes

        #unliking a post
        liked=False
        if NumberOfLikes.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["menu_list"] = menu_list
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPost(CreateView):
    model=Member
    form_class = MemberForm
    template_name='add_post.html'

class AddCategory(CreateView):
    model = Category
    fields='__all__'
    template_name = 'add_category.html'

class UpdateDetails(UpdateView):
    model=Member
    form_class = UpdateForm
    template_name='update_blog.html'

class DeleteBlog(DeleteView):
    model=Member
    template_name="delete_blog.html"
    success_url= reverse_lazy('home')



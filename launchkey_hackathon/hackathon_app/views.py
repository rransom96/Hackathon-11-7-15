from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response
from django.utils import timezone
from django.views.generic import View, ListView, CreateView
from hackathon_app.models import Post
from hackathon_app.forms import PostForm


class WelcomePage(View):

    def get(self, request):
        #return render_to_response('hackathon_app/homepage.html')
        return render(self.request, 'hackathon_app/homepage.html')


class ListPosts(ListView):
    model = Post
    queryset = Post.objects.order_by('-creation_time')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('list_bookmarks')
    template_name = 'hackathon_app/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)




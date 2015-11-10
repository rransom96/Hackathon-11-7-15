from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response
from django.utils import timezone
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView, DetailView
from hackathon_app.models import Post, Issue
from hackathon_app.forms import PostForm, IssueForm


class WelcomePage(View):
    def get(self, request):
        return render(self.request, 'hackathon_app/homepage.html')


###########  ISSUE VIEWS  ##############
class ListIssues(ListView):
    model = Issue
    queryset = Issue.objects.order_by('-creation_date_time')
    paginate_by = 5

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_load'] = timezone.now()
    #     return context


class IssueDetail(DetailView):
    model = Issue
    success_url = reverse_lazy('issue_detail')


class CreateIssue(CreateView):
    model = Issue
    form_class = IssueForm
    success_url = reverse_lazy('issues')
    template_name = 'hackathon_app/issue_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateIssue, self).form_valid(form)


class EditIssue(UpdateView):
    model = Issue
    form_class = IssueForm
    success_url = reverse_lazy('issues')
    template_name_suffix = '_update_form'


class DeleteIssue(DeleteView):
    model = Issue
    success_url = reverse_lazy('issues')








###########  POSTS VIEWS  ##############
class ListPosts(ListView):
    model = Post
    queryset = Post.objects.order_by('-creation_time')
    paginate_by = 5

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_load'] = timezone.now()
    #     return context


class PostDetail(DetailView):
    model = Post
    success_url = reverse_lazy('post_detail')


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')
    template_name = 'hackathon_app/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')
    template_name_suffix = '_update_form'


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')




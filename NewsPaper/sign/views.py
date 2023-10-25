from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

class UserInfoPage(LoginRequiredMixin, TemplateView):
    template_name = 'sign/user_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context

@login_required
def make_author(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    author_group.user_set.add(user)
    return redirect('/user_info')


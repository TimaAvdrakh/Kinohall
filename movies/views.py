from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .forms import RegisterUserForm, ChangeUserInfoForm
from django.shortcuts import render, redirect
from .models import Comment
from .models import movie
from .forms import UserCommentForm, GuestCommentForm, SeriesGuestCommentForm, SeriesUserCommentForm
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from .models import movie, Gender, series,seriesComment

class MPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
	template_name = 'movies/password_change.html'
	success_url = reverse_lazy('profile')
	success_message = 'Password of user changed'
	def get_context_data(self, **kwargs):
		context = super(MPasswordChangeView, self).get_context_data(**kwargs)
		context['genders'] = Gender.objects.all()
		return context


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = User
	template_name = 'movies/change_user_info.html'
	form_class = ChangeUserInfoForm
	success_url = reverse_lazy('profile')
	success_message = 'User personal data changed'

	def dispatch(self, request, *args, **kwargs):
		self.user_id = request.user.pk
		return super().dispatch(request, *args, **kwargs)

	def get_object(self, queryset=None):
		if not queryset:
			queryset = self.get_queryset()
		return get_object_or_404(queryset, pk = self.user_id)
	def get_context_data(self, **kwargs):
		context = super(ChangeUserInfoView, self).get_context_data(**kwargs)
		context['genders'] = Gender.objects.all()
		return context


class MLoginView(LoginView):
	template_name = 'registration/login.html'
	def get_context_data(self, **kwargs):
		context = super(MLoginView, self).get_context_data(**kwargs)
		context['genders'] = Gender.objects.all()
		return context

class SearchResultsView(ListView):
	model = movie
	template_name = 'movies/search_results.html'
	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = movie.objects.filter(title__contains=query)
		return object_list

	def get_context_data(self, **kwargs):
		context = super(SearchResultsView, self).get_context_data(**kwargs)
		context['genders'] = Gender.objects.all()
		context['mov'] = movie.objects.all()[:3]
		return context

class RegisterUserView(CreateView):
	model = User
	template_name = 'movies/register.html'
	form_class = RegisterUserForm
	success_url = reverse_lazy('register_done')
	def get_context_data(self, **kwargs):
		context = super(RegisterUserView, self).get_context_data(**kwargs)
		context['genders'] = Gender.objects.all()
		return context

class RegisterDoneView(TemplateView):
	template_name = 'movies/register_done.html'
	def get_context_data(self, **kwargs):
		context = super(RegisterDoneView, self).get_context_data(**kwargs)
		context['genders'] = Gender.objects.all()
		return context

def index(request):
	sser = series.objects.all()[:3]
	nns = movie.objects.all()[:3]
	mms = movie.objects.all()
	genders = Gender.objects.all()
	paginator = Paginator(mms, 12)
	if 'page' in request.GET:
		page_num = request.GET['page']
	else:
		page_num = 1
	page = paginator.get_page(page_num)
	context = {'mms': page.object_list, 'genders': genders, 'nns': nns, 'page': page, 'serials': sser}
	return render(request, 'movies/index.html', context)

def by_gender(request, gender_id):
	mov = movie.objects.all()[:3]
	mms = movie.objects.filter(gender=gender_id)
	genders = Gender.objects.all()
	current_gender = Gender.objects.get(pk=gender_id)
	context = {'mms': mms, 'genders': genders, 'current_gender': current_gender,'mov': mov}
	return render(request, 'movies/by_gender.html', context)

def series_by_gender(request, gender_id):
	ser = series.objects.all()[:2]
	mms = series.objects.filter(gender=gender_id)
	genders = Gender.objects.all()
	current_gender = Gender.objects.get(pk=gender_id)
	context = {'mms': mms, 'genders': genders, 'current_gender': current_gender, 'serials': ser}
	return render(request, 'movies/series_by_gender.html', context)
def contact(request):
	genders = Gender.objects.all()
	context = {'genders': genders}
	return render(request, 'movies/contact.html', context)

def moviepage(request, movie_id):
	mov = movie.objects.all()[:4]
	mms = movie.objects.get(pk=movie_id)
	genders = Gender.objects.all()
	current_movie = movie.objects.get(pk=movie_id)
	comments = Comment.objects.filter(Movie=movie_id, is_active=True)
	initial = {'Movie': mms.pk}
	if request.user.is_authenticated:
		initial['author'] = request.user.username
		form_class = UserCommentForm
	else:
		form_class = GuestCommentForm
	form = form_class(initial=initial)
	if request.method == 'POST':
		c_form = form_class(request.POST)
		if c_form.is_valid():
			c_form.save()
		else:
			form = c_form

	context = {'current_movie': current_movie, 'mms': mms, 'genders': genders, 'comments':comments, 'form':form, 'mov': mov}
	return render(request, 'movies/moviepage.html', context)

def serialspage(request, series_id):
	ser = series.objects.all()[:3]
	mms = series.objects.get(pk=series_id)
	genders = Gender.objects.all()
	current_series = series.objects.get(pk=series_id)
	comments = seriesComment.objects.filter(Series=series_id, is_active=True)
	initial = {'Series': mms.pk}
	if request.user.is_authenticated:
		initial['author'] = request.user.username
		form_class = SeriesUserCommentForm
	else:
		form_class = SeriesGuestCommentForm
	form = form_class(initial=initial)
	if request.method == 'POST':
		c_form = form_class(request.POST)
		if c_form.is_valid():
			c_form.save()
		else:
			form = c_form

	context = {'current_series': current_series, 'mms': mms, 'genders': genders, 'comments':comments, 'form':form, 'serials': ser}
	return render(request, 'movies/serialspage.html', context)

def signup(request):
	mms = movie.objects.all()
	genders = Gender.objects.all()
	context = {'mms': mms, 'genders': genders}
	return render(request, 'movies/signup.html', context)
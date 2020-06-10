from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404,redirect
from .forms import AddForm,ListForm,UpdateForm
from.models import Post,Category
from django.views.generic import ListView , DetailView,CreateView,UpdateView,DeleteView


def add(request):
	form = AddForm(request.POST)
	post_category = Category.objects.all()
	if request.method == 'POST':
		print(form.errors)
		if form.is_valid():
			post_saved = form.save(commit=False)
			post_saved.author = request.user.id
			form.save()
	return render(request, 'myaccount/add.html', {'form': form, 'post_category': post_category})


def all_posts(request):
	form = ListForm(request.POST)
	posts = Post.objects.all().order_by('-id')
	categoty_search = Category.objects.all()

	if request.method == 'POST':
		category_id = request.POST.get('category_id_f')
		posts = Post.objects.filter(category=category_id).order_by('-id')

	paginator = Paginator(posts, 10)
	page = request.GET.get('page')

	posts = paginator.get_page(page)

	context_posts = {
		'posts': posts,
		'categoty_search': categoty_search,
	}

	return render(request, 'myaccount/all_posts.html', context_posts)

# class PostListView(ListView):
# 	model = Post
# 	template_name = 'post_food/index.html'
# 	context_object_name = 'posts'
# 	ordering = ['-date_posted']



def show_post(request, pk):
	post = get_object_or_404(Post,pk=pk)
	brand = Category.objects.get(id=post.category)
	return render(request, 'myaccount/postdetail.html', {'post':post, 'brand':brand})


def list_category(request, pk: None):
	form = ListForm(request.POST)
	posts = Post.objects.filter(category=pk).order_by('-id')
	categoty_search = Category.objects.all()

	if request.method == 'POST':
		category_id = request.POST.get('brand_id_f')
		posts = Post.objects.filter(category=category_id_f).order_by('-id')

	paginator = Paginator(posts, 10)
	page = request.GET.get('page')

	posts = paginator.get_page(page)

	context_posts = {
		'posts': posts,
		'categoty_search': categoty_search,
	}

	return render(request, 'myaccount/all_posts.html', context_posts)


def Users_all_posts(request):
    user = request.user.id
    form = ListForm(request.POST)
    posts = Post.objects.filter(author=user).order_by('-id')
    category_search = Category.objects.all()

    if request.method == 'POST':
        category_id = request.POST.get('category_id_f')
        posts = Post.objects.filter(category=category_id, author=user).order_by('-id')

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')

    posts = paginator.get_page(page)

    context_posts = {
        'posts': posts,
        'category_search': category_search,
    }

    return render(request, 'myaccount/Users_all_posts.html', context_posts)

def update_post(request, pk):
	post = Post.objects.get(pk=pk)

	form = UpdateForm(request.POST, instance=post)
	all_category = Category.objects.all()
	if request.method == 'POST':
		print(form.errors)
		if form.is_valid():
			form.save()
	return render(request, 'myaccount/update_post.html', {'form': form, 'all_category': all_category, 'post': post})


def delete_post(request, pk):
	post = get_object_or_404(Post,pk=pk)
	if request.method == 'POST':
		post.delete()
		return redirect('mypost:list')
	context = {
		"object": post
	}
	return render(request, 'myaccount/delete_post.html', context)
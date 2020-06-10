from django.shortcuts import render
from .forms import AddForm
from.models import Post,Category


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

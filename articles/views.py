from django.shortcuts import render, redirect

from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, "create.html", {"form": form})
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article')
        else:
            form = ArticleForm()
            return render(request, "create.html", {"errors": form.errors, "form": form})


def article(request):
    posts = Article.objects.order_by('-vote_total')
    return render(request, 'profile.html', {'posts': posts})



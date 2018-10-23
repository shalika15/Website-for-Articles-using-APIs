from django.http.response import JsonResponse
from articles.models import *
from django.contrib.auth.models import User


def upvote(request):
    article = Article.objects.get(id=request.POST.get('id'))
    if request.POST.get('type') == "up":
        article.vote_total += 1
    else:
        article.vote_total -= 1
    article.save(update_fields=['vote_total'])
    return JsonResponse({'success': True})








from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from bookmark01 import models


# Create your views here.
@csrf_exempt
def addBookmark(request):
    if request.method == 'POST':
        user = UserProfile.objects.get(user=request.user)
        bookmark = json.loads(user.bookmark)
        bookmark.append(<id>)
        user.bookmark = json.dumps(bookmark)
        user.save()
        return HttpResponse("Bookmark added.")
    else:
        return HttpResponse("Invalid request method.")

@csrf_exempt
def like_recipe(request):
    if request.method == 'POST' and request.is_ajax():
        id = request.POST.get('id', None)
        is_liked = request.POST.get('is_liked', None)
        if id and is_liked:
            recipe = Recipe.objects.get(id=id)
            if is_liked == 'true':
                recipe.likes += 1
                recipe.save()
                status = 'ok'
            else:
                recipe.likes -= 1
                recipe.save()
                status = 'ok'
            return JsonResponse({'status': status})
    return JsonResponse({'status': 'error'})



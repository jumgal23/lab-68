# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from django.views.decorators.http import require_GET
# from django.contrib.auth.decorators import login_required
# from webapp.models import Article, Comment, Like, ArticleLikedItem, CommentLikedItem
#
# @login_required
# @require_GET
# def toggle_like(request, model_name, item_id):
#     user = request.user
#     liked_item_model = {'article': Article, 'comment': Comment}[model_name.lower()]
#     liked_item = get_object_or_404(liked_item_model, id=item_id)
#
#     liked_item_liked_model = {'article': ArticleLikedItem, 'comment': CommentLikedItem}[model_name.lower()]
#     liked_item_liked, created = liked_item_liked_model.objects.get_or_create(**{model_name.lower(): liked_item})
#
#     if user in liked_item_liked.likes.all():
#         liked_item_liked.likes.remove(user)
#     else:
#         like = Like.objects.create(user=user)
#         liked_item_liked.likes.add(like)
#
#     likes_count = liked_item_liked.get_likes_count()
#     return JsonResponse({'likes_count': likes_count})


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from webapp.models import Article, Comment, Like, ArticleLikedItem, CommentLikedItem

@login_required
@require_GET
def toggle_like(request, model_name, item_id):
    user = request.user
    liked_item_model = {'article': Article, 'comment': Comment}[model_name.lower()]
    liked_item = get_object_or_404(liked_item_model, id=item_id)

    liked_item_liked_model = {'article': ArticleLikedItem, 'comment': CommentLikedItem}[model_name.lower()]
    liked_item_liked, created = liked_item_liked_model.objects.get_or_create(**{model_name.lower(): liked_item})

    if user in liked_item_liked.likes.all():
        liked_item_liked.likes.remove(user)
    else:
        # Check if the user has already liked the item
        existing_like = Like.objects.filter(user=user, liked_items=liked_item_liked).first()

        if existing_like:
            # User already liked the item, so remove the like
            existing_like.delete()
        else:
            # User hasn't liked the item, so add the like
            like = Like.objects.create(user=user)
            liked_item_liked.likes.add(like)

    likes_count = liked_item_liked.get_likes_count()
    return JsonResponse({'likes_count': likes_count})








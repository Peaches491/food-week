from django.shortcuts import get_object_or_404, render
from recipes.models import Recipe


def index(request):
    latest_question_list = Recipe.objects.order_by('add_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'recipes/index.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    context = {"recipe": recipe}
    return render(request, 'recipes/detail.html', context)



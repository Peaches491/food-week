from django.shortcuts import get_object_or_404, render
from recipes.models import Recipe

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages


class MessageType:
    SUCCESS = "msg-success"
    INFO = "msg-info"
    WARNING = "msg-warning"
    ERROR = "msg-error"


def index(request):
    latest_question_list = Recipe.objects.order_by('add_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'recipes/index.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    context = {"recipe": recipe, }
    return render(request, 'recipes/detail.html', context)


def new(request, recipe_id=None):
    # TODO: Add user authentication
    context = {"messages": messages.get_messages(request)}

    if recipe_id is not None:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        context["recipe"] = recipe

    return render(request, 'recipes/edit.html', context)


def edit(request, recipe_id=None):
    if request.method == 'POST':
        print request.POST

        try:
            if recipe_id:
                recipe = Recipe.objects.get(pk=recipe_id)
            else:
                recipe = Recipe()
            recipe.name = request.POST["name"]
            recipe.short_description = request.POST["short"]
            recipe.details = request.POST["details"]
            # TODO Handle ingredients
        except Exception as ex:
            messages.error(request, ex.message)
            return HttpResponseRedirect(reverse('recipe:edit', args=(recipe_id,)))
        else:
            messages.success(request, "Your changes have been saved!")
            print recipe.save()
            return HttpResponseRedirect(reverse('recipe:detail', args=(recipe.pk,)))

    else:
        return new(request, recipe_id=recipe_id)
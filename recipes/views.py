from django.shortcuts import get_object_or_404, render
from django.utils.datastructures import MultiValueDictKeyError
from recipes.models import Recipe

from django.http import *
from django.core.urlresolvers import reverse
from django.contrib import messages


class MessageType:
    SUCCESS = "msg-success"
    INFO = "msg-info"
    WARNING = "msg-warning"
    ERROR = "msg-error"


def index(request):
    # latest_question_list = Recipe.objects.order_by('add_date')[:5]
    latest_question_list = Recipe.objects.order_by('add_date')
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
    is_enabled = False;

    if request.method == 'POST':
        print request.POST

        is_new_recipe = False

        try:
            if recipe_id:
                print "Attempting to edit recipe " + recipe_id + "...",
                recipe = Recipe.objects.get(pk=recipe_id)
                print "Loaded."

                if "delete-recipe" in request.POST:
                    print "Attempting to delete recipe...",
                    if is_enabled:
                        recipe.delete()
                        print "Deleted"
                        return HttpResponseRedirect(reverse('recipe:index'))
                    else:
                        messages.warning(request, "Edits are disabled.")
                        print "Failed. Edits disabled. "
                        return HttpResponseRedirect(reverse('recipe:detail', args=(recipe.pk,)))

            else:
                print "Building new recipe"
                recipe = Recipe()
                is_new_recipe = True
            recipe.name = request.POST["name"]
            recipe.short_description = request.POST["short"]
            recipe.details = request.POST["details"]

            # TODO Handle ingredients
        except Exception as ex:
            msg = str(type(ex)) + ": " + ex.message
            print "Exception: " + msg
            messages.error(request, msg)
            print "Referrer: " + request.META.get('HTTP_REFERER')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            if is_enabled:
                print recipe.save()
                messages.success(request, "Your changes have been saved!")
            else:
                messages.warning(request, "Edits are disabled.")
            return HttpResponseRedirect(reverse('recipe:detail', args=(recipe.pk,)))

    else:
        return new(request, recipe_id=recipe_id)


def test(request, recipe_id=None):
    print "TESTING"
    print request.POST
    return HttpResponse("Success")
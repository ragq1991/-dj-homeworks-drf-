from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet_view(request):
    return calc_serv(request, 'omlet')


def pasta_view(request):
    return calc_serv(request, 'pasta')


def buter_view(request):
    return calc_serv(request, 'buter')


def calc_serv(request, food):
    recipes = DATA.get(food)
    servings = int(request.GET.get('servings', 1))
    if servings <= 0:
        servings = 1
    composition = {}
    for ingridient in recipes:
        composition[ingridient] = round(recipes[ingridient] * servings, 1)
    context = {
        'name': food.capitalize(),
        'composition': composition
    }
    return render(request, 'recipes/recipes.html', context)

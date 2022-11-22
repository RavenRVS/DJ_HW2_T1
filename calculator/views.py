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


def servings_helper(request, recipe_name):
    number_of_servings = 1
    if request.GET.get("servings"):
        number_of_servings = int(request.GET.get("servings"))
    context = {}
    if recipe_name in DATA.keys():
        temp_dict = {}
        for key in DATA[recipe_name]:
            temp_dict[key] = DATA[recipe_name][key] * number_of_servings
        context['recipe'] = temp_dict

    return render(request, 'calculator/index.html', context)
from django.shortcuts import render
from django.http import Http404

DATA = {
    'cheesecake': {
        'печенье, г': 200,
        'сливочный сыр, г': 500,
        'сахар, г': 150,
        'яйца, шт': 3,
        'лимон, шт': 1,
        'мука, г': 50,
        'масло, г': 50,
    },

    'pork_shashlik': {
        'свинина, г': 500,
        'лук репчатый, г': 100,
        'перец болгарский, г': 100,
        'томаты, г': 100,
        'майонез, мл': 50,
        'соль, г': 10,
        'перец черный, г': 5,
    },
    'spaghetti_bolognese': {
        'спагетти, г': 300,
        'фарш мясной, г': 250,
        'томаты, г': 200,
        'лук репчатый, г': 50,
        'чеснок, зубчик': 2,
        'сыр пармезан, г': 50,
        'оливковое масло, мл': 50,
    }
    ,
    'caesar_salad': {
        'куриное филе, г': 200,
        'листья салата, г': 100,
        'сухарики, г': 50,
        'сыр пармезан, г': 50,
        'яйца, шт': 2,
        'чеснок, зубчик': 1,
        'майонез, мл': 50,
        'горчица, г': 10,
        'лимон, шт': 1,
        'оливковое масло, мл': 50,
    },

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


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def menu_view(request):
    return render(request, 'calculator/menu.html', {'dishes': DATA})


def recipe_view(request, recipe_name, number=None):
    recipe = DATA.get(recipe_name)
    if recipe is None:
        raise Http404('Рецепт не найден')

    servings = number if number is not None else 1
    context = {
        'recipe': {}
    }
    for ingredient, amount in recipe.items():
        context['recipe'][ingredient] = amount * servings
        print(context['recipe'][ingredient])
    return render(request, 'calculator/index.html', context)

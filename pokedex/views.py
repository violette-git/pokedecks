from django.shortcuts import get_object_or_404, render, redirect

from pokedex.models import PokemonType, Pokemon

from django.db.models import Q

# Create your views here.



def poke_deck(request):

    poke_ball = Pokemon.objects.all()
    poke_balls = ''

    search = request.POST.get('search') or ''

    poketype = request.POST.getlist('poketype')

    # print(f'poketype={poketype}')

    if poketype:

        for type in poketype:

            poke_ball = poke_ball.filter(

            types__name=type
            
            )

    if search:

        poke_ball = poke_ball.filter(

            Q(name__icontains=search)
        ) 
    # print(f"pokeball={poke_ball}")

    if search.isdigit():

        poke_balls = Pokemon.objects.get(number=search)
     

    context = {
        'poke_ball':poke_ball,
        'pokemon_types': PokemonType.objects.all(),
        'poke_balls':poke_balls
    }

    return render(request, 'pokedex/poke_deck.html', context)

def poke_info(request, id):
       
    
    # poke_info = request.POST.get('poke_info') or ''
    q = Pokemon.objects.filter(pk=id)
    poke = get_object_or_404(q)
    print(poke)
    context = {
        
        'poke':poke
    }

    return render(request, 'pokedex/poke_info.html', context)


   
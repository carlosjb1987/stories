from django.shortcuts import render, get_object_or_404, redirect
from .models import Story, Resultado
from django.http import HttpRequest


def story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    componentes = story.componentes.all()
    preguntas = story.preguntas.all()
    resultados = Resultado.objects.filter(story=story)

    if request.POST:
        for pregunta in preguntas:
            respuesta = request.POST.get(f'pregunta_{pregunta.id}')
            Resultado.objects.create(story=story, pregunta=pregunta, respuesta_elegida=respuesta)

    return render(request, 'story.html', {'story': story, 'componentes': componentes, 'preguntas': preguntas, 'resultados': resultados})


def list_stories(request):
    stories = Story.objects.all()
    return render(request, 'list_stories.html', {'stories': stories})


def detail_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    return render(request, 'detail_story.html', {'story': story})

def submit_answers(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    preguntas = story.preguntas.all()
    if request.POST:
        for pregunta in preguntas:
            respuesta_elegida = request.POST.get(f'pregunta_{pregunta.id}')
            Resultado.objects.create(story=story, pregunta=pregunta, respuesta_elegida=respuesta_elegida)
        return redirect('story', story_id=story.id)
    return render(request, 'submit_answers.html', {'story': story, 'preguntas': preguntas})

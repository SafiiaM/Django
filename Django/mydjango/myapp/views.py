# import logging

# from django.http import HttpResponse

# logger = logging.getLogger(__name__)


# def index(request):
#     logger.info('Index page accessed')
#     return HttpResponse("Hello, world!")


# def about(request):
#     try:
#         # some code that might raise an exception
#         result = 1 / 0
#     except Exception as e:
#         logger.exception(f'Error in about page: {e}')
#         return HttpResponse("Oops, something went wrong.")
#     else:
#         logger.debug('About page accessed')
#         return HttpResponse("This is the about page.")

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class MainPageView(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'Сафия'
        contex['email'] = 'sony10@yandex.ru'
        contex['phone'] = '+79885212067'
        logger.info(f'посещение страницы index в: {datetime.now()}')
        return contex


class AboutView(TemplateView):
    template_name = 'myapp/about.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'Сафия'
        contex['email'] = 'sony10@yandex.ru'
        contex['phone'] = '+79885212067'
        logger.info(f'посещение страницы about в: {datetime.now()}')
        return contex


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My first Django-site</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to my first Django-site!</h1>
    
        <h2>About site</h2>
        <p>This site is developed using Django, a powerful framework for creating web applications in Python. Here I can create and display various pages and data in a convenient format.</p>
    
        <h2>About me</h2>
        <p>Hi, I'm Safiia. I am an aspiring Data Engineer, also interested in web development and passionate about creating interactive and beautiful websites. My skills include HTML, CSS, JavaScript, as well as Python and Django.</p>
    
        <footer>
            <p>Please contact me: sony10@ynadex.ru | +79885212067</p>
        </footer>
    </body>
    </html>
    """
    logger.info(f'visit page "index" at: {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обо мне</title>
</head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;
            }
        </style>
<body>
    <header>
        <h1>Привет! Меня зовут Сафия!</h1>
    </header>

    <main>
        <section>
            <h2>Опыт работы</h2>
            <ul>
                <li>Место работы 1</li>
                <li>Место работы 2</li>
                <li>Место работы 3</li>
            </ul>
        </section>

        <section>
            <h2>Образование</h2>
            <ul>
                <li>Университет 1</li>
                <li>Университет 2</li>
            </ul>
        </section>

        <section>
            <h2>Навыки</h2>
            <ul>
                <li>Навык 1</li>
                <li>Навык 2</li>
                <li>Навык 3</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>Свяжитесь со мной: sony10@yandex.ru | +79885212067</p>
    </footer>
</body>
</html>
"""
    logger.info(f'посещение страницы about в: {datetime.now()}')
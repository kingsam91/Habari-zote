from flask import render_template, request
from ..requests import get_news, get_sources, get_news_by_custom_source
from . import home


@home.route('/')
def index():

    news = get_news()
    sources = get_sources()

    return render_template('home/index.html', mylist=news, mysources=sources)


@home.route('/search-source', methods=['GET', 'POST'])
def get_news_by_source():

    # news = get_news()
    sources = get_sources()

    if request.method == 'POST':
        name = request.form.get('search')

        news = get_news_by_custom_source(name)

    return render_template('home/index.html', mylist=news, source=name, mysources=sources)

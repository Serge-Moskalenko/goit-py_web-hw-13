from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from bson.objectid import ObjectId
from django.http import HttpResponseServerError
import traceback

from .forms import AuthorForm, QuoteForm
from .utils import get_mongodb

from collections import Counter

def main(request, page=1):
    print("main")
    try:
        db = get_mongodb()
        quotes = list(db.quotes.find())

        for quote in quotes:
            author = db.authors.find_one({'_id': quote['author']})
            quote['author_fullname'] = author['fullname'] if author else 'Невідомий'
            quote['author_id'] = str(quote['author'])

        paginator = Paginator(quotes, 5)
        quotes_on_page = paginator.page(page)

        all_tags = []
        for q in quotes:
            all_tags.extend(q.get('tags', []))

        tag_counter = Counter(all_tags)
        top_tags = tag_counter.most_common(10)

        return render(request, 'quotes/index.html', {
            'quotes': quotes_on_page,
            'top_tags': top_tags
        })
    except Exception:
        print("🔥 ПОМИЛКА:", traceback.format_exc())
        return HttpResponseServerError(f"<pre>{traceback.format_exc()}</pre>")

@login_required
def add_author(request):
    db = get_mongodb()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author_data = {
                'fullname': form.cleaned_data['fullname'],
                'born_date': form.cleaned_data['born_date'],
                'born_location': form.cleaned_data['born_location'],
                'description': form.cleaned_data['description']
            }
            db.authors.insert_one(author_data)
            return redirect('quotes:root')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    db = get_mongodb()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote_text = form.cleaned_data['quote']
            author_name = form.cleaned_data['author']
            tags = [tag.strip() for tag in form.cleaned_data['tags'].split(',')]

            author_doc = db.authors.find_one({'fullname': author_name})
            if not author_doc:
                form.add_error('author', 'Author not found in MongoDB')
            else:
                quote_doc = {
                    'quote': quote_text,
                    'author': ObjectId(author_doc['_id']),
                    'tags': tags
                }
                db.quotes.insert_one(quote_doc)
                return redirect('quotes:root')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def author_detail(request, author_id):
    db = get_mongodb()

    try:
        obj_id = ObjectId(author_id)
    except Exception:
        return render(request, '404.html', status=404)

    author = db.authors.find_one({'_id': obj_id})
    if not author:
        return render(request, '404.html', status=404)

    quotes = db.quotes.find({'author': obj_id})
    return render(request, 'quotes/author_detail.html', {
        'author': author,
        'quotes': quotes
    })

def quotes_by_tag(request, tag):
    db = get_mongodb()
    quotes = db.quotes.find({"tags": tag})
    return render(request, "quotes/quotes_by_tag.html", {"tag": tag, "quotes": quotes})

def search_by_tag(request):
    tag = request.GET.get('tag')
    quotes = []

    if tag:
        db = get_mongodb()
        
        quotes = db.quotes.find({
            "tags": {"$regex": tag, "$options": "i"}
        })

    return render(request, 'quotes/quotes_by_tag.html', {
        "tag": tag,
        "quotes": quotes
    })


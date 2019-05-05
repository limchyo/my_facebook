from django.shortcuts import render, redirect
from .models import Article, Page, Comment

# Create your views here.
def play(request):
    return render(request, 'play.html')

count = 0
def play2(request):
    my_name = "임채오"
    age = 30

    global count
    count = count + 1

    if age > 19:
        status = "성인"
    else:
        status = "청소년"

    diary = [
        '오늘은 날씨가 맑았다. - 4월 3일',
        '미세머지가 너무 심하다. (4월 2일)',
        '비가 온다. 4월 1일에 작성'
    ]

    ctx = {
        'name' : my_name,
        'cnt' : count,
        'age' : status,
        'diary' : diary,
    }
    return render(request, 'play2.html', ctx)

def profile(request):
    # ctx = {}
    return render(request, 'profile.html')

count = 0
def event(request):
    name = "임채오"
    age = 30

    if age >= 20:
        status = "성인"
    else:
        status = "청소년"

    global count
    count = count + 1

    if count is 7:
        result = "당첨!"
    else:
        result = "꽝..."

    ctx = {
        'name' : name,
        'age' : status,
        'cnt' : count,
        'result' : result,
    }
    return render(request, "event.html", ctx)

def fail(request):
    return render(request, "fail.html")

def help(request):
    return render(request, "help.html")

def warn(request):
    return render(request, "warn.html")

def newsfeed(request):
    articles = Article.objects.all()
    ctx = {
        'articles' : articles
    }
    return render(request, "newsfeed.html", ctx)

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        Comment.objects.create(
            article=article,
            author=request.POST.get('nickname'),
            text=request.POST.get('reply'),
            password=request.POST.get('password'),
        )
        return redirect(f'/feed/{ article.pk }')

    ctx = {'feed': article}
    return render(request, 'detail_feed.html', ctx)

def pages(request):
    pages = Page.objects.all()
    ctx = {'pages' : pages}
    return render(request, "pages.html", ctx)

def new_feed(request):
    if request.method == "POST":
        author=request.POST.get('author')
        title=request.POST.get('title')
        text=request.POST.get('text')
        password=request.POST.get('password')

        if request.POST.get('author') != '' and request.POST.get('title') != '' and request.POST.get('text') != '' and request.POST.get('password') != '':
            new_article = Article.objects.create(
                author=author,
                title=title,
                text=text,
                password=password,
            )


            return redirect(f'/feed/{ new_article.pk }')

    return render(request, "new_feed.html")

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/')
        else:
            return redirect('/fail/')

    ctx = {
        'article' : article,
    }
    return render(request, "remove_feed.html", ctx)

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        if request.POST['password'] == article.password:
            article.author = request.POST.get("author")
            article.title = request.POST.get("title")
            article.text = request.POST.get("text")
            article.save()
            return redirect(f'/feed/{ article.pk }')
        else:
            return redirect('/fail/')

    ctx = {
        'article' : article,
    }
    return render(request, "edit_feed.html", ctx)

def new_page(request):
    if request.method == "POST":
        master=request.POST.get("master")
        name=request.POST.get("name")
        category=request.POST.get("category")
        text=request.POST.get("text")

        if master != "" and name != "" and category != "" and text != "":
            new_page=Page.objects.create(
                master=master,
                name=name,
                category=category,
                text=text
            )

            return redirect("/pages/")

    return render(request, "new_page.html")

def edit_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == "POST":
        page.master=request.POST.get("master")
        page.name=request.POST.get("name")
        page.category=request.POST.get("category")
        page.text=request.POST.get("text")
        page.save()

        return redirect("/pages/")

    ctx = {'page' : page}
    return render(request, "edit_page.html", ctx)

def remove_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == "POST":
        page.remove()

        return redirect("/pages/")

    ctx = {'page' : page}
    return render(request, "remove_page.html", ctx)

def remove_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    article_pk = comment.article.pk

    if request.method == "POST":
        if request.POST.get("password") == comment.password:
            comment.delete()
            return redirect(f"/feed/{ article_pk }")
        else:
            return redirect("/fail/")

    ctx = {'comment' : comment}
    return render(request, "remove_comment.html", ctx)

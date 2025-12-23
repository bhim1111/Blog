from django.shortcuts import render

from blog_app.models import Post
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(published_at__isnull=False)
    return render(
        request,
        "post_list.html",
        {"posts": posts},
    )



def post_detail(request, pk):
    post = Post.objects.get(id=pk, published_at__isnull=False)
    return render(
        request,
        "post_detail.html",
        {"post":post},
    )


@login_required
def draft_list(request):
    posts = Post.objects.filter(published_at__isnull=True)
    return render(
        request,
        "draft_list.html",
        {"posts": posts},
    )


@login_required
def draft_detail(request, pk):
    post =Post.objects.get(pk=pk, published_at__isnull=True)
    return render(
        request,
        "draft_detail.html",
        {"post":post}

    )


@login_required
def post_create(request):
    if request.method == "GET":
        form = PostForm()
        return render(
            request,
            "post_create.html",
            {"form": form},
        )
    else:
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.User
            post.save()
            return redirect("draft-detail", pk=post.pk)

        else:
            return render(
                request,
                "post_create.html",
                {"form": form},
            )


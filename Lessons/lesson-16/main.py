from blog_app.managers import Blog

def find_category(blog: Blog, title: str) -> Category | None:
    for category in blog.categories:
        if category.title == title:
            pass
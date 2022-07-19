from django import templates
from blog.models import Post, Tag

register = Template.Library()

@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=3):
    post = Post.objects.order_by('-views')[:cnt]
    return {"post": posts}


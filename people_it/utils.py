from people_it.models import *

menu = [
    {"name":"about", 'url_name':"about"},
    {"name":"add post", 'url_name':"add_post"},
    {"name":"work", 'url_name':"work"},
    {"name":"login", 'url_name':"login"},
]

class DataMixin:
    
    def get_user_context(self, **kwargs):
        context = kwargs
        context["menu"] = menu
        if 'cat_selected' not in context:
            context['cat_selected'] = "all-categories"
        context["cats"] = Category.objects.all()
        return context


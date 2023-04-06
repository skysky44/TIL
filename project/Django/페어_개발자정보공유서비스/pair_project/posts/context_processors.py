from .forms import PostForm

def message_processor(request):
    form = PostForm()
    return {
        'categories': form
        # .fields.category.choices
    }
from django.views.generic.edit import FormView
from .forms import ExampleGeoMultipleChoiceForm

class ExampleView(FormView):
    template_name = 'sample_form.html'
    form_class = ExampleGeoMultipleChoiceForm
    success_url = '/'

    def form_valid(self, form):
        form.save(commit=True)
        return super().form_valid(form)

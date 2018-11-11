from allauth.account import views


class SigninView(views.LoginView):
    template_name = 'signin/index.html'

    def dispatch(self, request, *args, **kwargs):
        response = super(SigninView, self).dispatch(request, *args)
        return response

    def form_valid(self, form):
        return super(SigninView, self).form_valid(form)

signin_view = SigninView.as_view()


class SignupView(views.LoginView):
    template_name = 'signup/index.html'

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context

signup_view = SignupView.as_view()
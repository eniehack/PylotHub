from allauth.account import views
from django.shortcuts import redirect


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


class SignoutView(views.LogoutView):

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            self.logout()

        return redirect('/')


signout_view = SignoutView.as_view()

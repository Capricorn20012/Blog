from .forms import LoginForm, RegistrationFrom, EditAccountForm, EditProfileForm


def add_my_forms(request):
    return {
        'login_form': LoginForm(),
        'register_form': RegistrationFrom(),
        'edit_account': EditAccountForm(),
        'edit_profile': EditProfileForm()
    }
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# django User 객체에 대한 직접 참조 권장하지 않음!!!!!!
# 중간에 수정될 수 있어서 또는 순서상 User가 아직 활성화되지 않을 수도 있어서
# from .models import User

# 대신 다음과 같은 함수 제공
# get_user_model은 현재 프로젝트에 활성화 되어있는 User 객체를 반환해준다.
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # 상속 후 수정
        # 현재 우리가 사용하는 User class로 재정의
        model = get_user_model()
        # User 대신 간접 참조 필요(중간에 수정될 수 있어서).함수니까()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
        password = forms.CharField(
            widget=PasswordInput(attrs={'autocomplete': 'new-password'}),
            error_messages={
                'required': '비밀번호를 입력해주세요.',
                'min_length': '비밀번호는 8자 이상 입력해주세요.',
                'max_length': '비밀번호는 32자 이하로 입력해주세요.',
                'invalid': '비밀번호는 영문 대/소문자, 숫자, 특수문자를 포함해야 합니다.',
            }
        )

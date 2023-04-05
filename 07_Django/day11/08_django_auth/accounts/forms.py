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

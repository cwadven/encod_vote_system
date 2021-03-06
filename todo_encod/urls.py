from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path
import board.urls
import accounts.urls
from django.conf import settings
from django.conf.urls.static import static

from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

from django.views.generic import TemplateView

#jwt 토큰 사용
# from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
routes = getattr(settings, 'REACT_ROUTES', [])

urlpatterns = [
    # path('admin/', admin.site.urls),

    #REACT로 만든 index.html 게시글 접근
    # path('', TemplateView.as_view(template_name='index.html'),name='index'),
    #REACT ROUTER 역할 처럼 다시 들어올수 있도록 설정하기
    url(r'^(%s)?$' % '|'.join(routes), TemplateView.as_view(template_name="index.html"),name='index'),

    path('', include('board.urls')),
    path('accounts/', include('accounts.urls')),

    # path('api/token/', obtain_jwt_token),
    # path('api/token/verify/', verify_jwt_token),
    # path('api/token/refresh/', refresh_jwt_token),
    # path('api-auth/', include('rest_framework.urls')),

    #로그인
    # path("rest-auth/", include('rest_auth.urls')),

    path('rest-auth/login', LoginView.as_view(), name='rest_login'),
    path('rest-auth/logout', LogoutView.as_view(), name='rest_logout'),
    path('rest-auth/user', UserDetailsView.as_view(), name='rest_user_details'),
    path('rest-auth/password/change', PasswordChangeView.as_view(), name='rest_password_change'),
    
    #회원가입
    path("rest-auth/registration", include('rest_auth.registration.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
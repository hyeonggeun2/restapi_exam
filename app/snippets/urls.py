from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    # as_view는 클래스형 view에서 제공하는 클래스 진입 메소드이다.
    # 자동으로 request를 검사해서 맞는 함수에 요청을 보냄.
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
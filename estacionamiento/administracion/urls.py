from django.urls import path
from .views import RegistroView, LoginView, UsuarioView, UsuarioIdView, ObtenerSkillsPersona, ActualizarSkill, CrearSkill, ObtenerExpsPersona, ActualizarExp, CrearExp, ObtenerProysPersona, CrearProy, ActualizarProy, ObtenerSolsPersona, CrearSol, UsuarioCorreoView

urlpatterns= [
    path('login', LoginView.as_view()),
    path('register', RegistroView.as_view()),
    path('users', UsuarioView.as_view()),
    path('usuario/<int:usuId>', UsuarioIdView.as_view()),
    path('usuario/<str:usuCorreo>', UsuarioCorreoView.as_view()),
    path('skill/<int:usuId>', ObtenerSkillsPersona.as_view()),
    path('skilla/<int:skill_id>', ActualizarSkill.as_view()),
    path('skill', CrearSkill.as_view()),
    path('exp/<int:usuId>', ObtenerExpsPersona.as_view()),
    path('exp/<int:exp_id>', ActualizarExp.as_view()),
    path('exp', CrearExp.as_view()),
    path('proy/<int:usuId>', ObtenerProysPersona.as_view()),
    path('proy/<int:proy_id>', ActualizarProy.as_view()),
    path('proy', CrearProy.as_view()),
    path('sol/<int:usuId>', ObtenerSolsPersona.as_view()),
    path('sol', CrearSol.as_view()),
]
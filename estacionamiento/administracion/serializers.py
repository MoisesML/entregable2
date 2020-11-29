from .models import Usuario, SkillModel, ExperienciaModel, ProyectoModel, SolicitudModel
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth

# class InformacionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InformacionModel
#         fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillModel
        fields = '__all__'

    def update(self):
        self.instance.skill_nombre = self.validated_data.get('skill_nombre', self.instance.skill_nombre)
        self.instance.skill_valoracion = self.validated_data.get('skill_valoracion', self.instance.skill_valoracion)
        self.instance.skill_descripcion = self.validated_data.get('skill_descripcion', self.instance.skill_descripcion)
        self.instance.skill_url = self.validated_data.get('skill_url', self.instance.skill_url)
        self.instance.save()
        return self.instance
        
class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaModel
        fields = '__all__'

    def update(self):
        self.instance.exp_empresa = self.validated_data.get('exp_empresa', self.instance.exp_empresa)
        self.instance.exp_puesto = self.validated_data.get('exp_puesto', self.instance.exp_puesto)
        self.instance.exp_funciones = self.validated_data.get('exp_funciones', self.instance.exp_funciones)
        self.instance.exp_duracion = self.validated_data.get('exp_duracion', self.instance.exp_duracion)
        self.instance.save()
        return self.instance

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoModel
        fields = '__all__'

    def update(self):
        self.instance.proy_empresa = self.validated_data.get('proy_empresa', self.instance.proy_empresa)
        self.instance.proy_nombre = self.validated_data.get('proy_nombre', self.instance.proy_nombre)
        self.instance.proy_descripcion = self.validated_data.get('proy_descripcion', self.instance.proy_descripcion)
        self.instance.proy_duracion = self.validated_data.get('proy_duracion', self.instance.proy_duracion)
        self.instance.save()
        return self.instance

class SolicitudSerializar(serializers.ModelSerializer):
    class Meta:
        model = SolicitudModel
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(source='skillsInfo', read_only=True, many=True)
    class Meta:
        model = Usuario
        exclude = ['password']

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        exclude = ['last_login']
    def save(self):
        password = self.validated_data.get('password')
        usuCorreo = self.validated_data.get('usuCorreo')
        usuNombre = self.validated_data.get('usuNombre')
        usuFono = self.validated_data.get('usuFono')
        is_staff = self.validated_data.get('is_staff')
        is_superuser = self.validated_data.get('is_superuser')
        
        nuevoUsuario = Usuario(is_superuser=is_superuser, usuCorreo=usuCorreo, usuNombre=usuNombre, usuFono=usuFono,is_staff=is_staff)
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=5)
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)
    class Meta: 
        model = Usuario
        fields = ['email','password', 'tokens']
    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        usuario = auth.authenticate(usuCorreo=email, password=password)
        if not usuario:
            raise AuthenticationFailed('Credenciales invalidas, intentelo de nuevo')
        return {
            'email': usuario.usuCorreo,
            'tokens': usuario.tokens()
        }
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class ManejoUsuario(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, usuCorreo, usuNombre, usuFono, usuPass, **extra_fields):
        values = [usuCorreo, usuFono, usuNombre]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError("El valor de {} debe estar definido".format(field_name))
        usuCorreo = self.normalize_email(usuCorreo)
        user = self.model(
            usuCorreo = usuCorreo,
            usuNombre=usuNombre,
            usuFono=usuFono,
            **extra_fields
        )
        user.set_password(usuPass)
        user.save(using=self._db)  
        return user

    def create_user(self, usuCorreo, usuNombre, usuFono, usuPass=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(usuCorreo, usuNombre, usuFono, usuPass, **extra_fields)
    
    def create_superuser(self,  usuCorreo, usuNombre, usuFono, usuPass, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El super usuario debe de ser staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El super usuario debe de ser superusuario')
        return self._create_user( usuCorreo, usuNombre, usuFono, usuPass, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    usuId = models.AutoField(db_column='usu_id', primary_key=True)
    usuCorreo = models.EmailField(db_column='usu_correo', unique=True, verbose_name='Correo')
    usuNombre = models.CharField(db_column='usu_nombre', max_length=50)
    usuFono = models.CharField(db_column='usu_fono', max_length=15)
    # 
    usuDni = models.CharField(db_column='usuDni', null=True, max_length=11, default='pendiente')
    usuDirec = models.CharField(db_column='usuDirec', null=True, max_length=50, default='pendiente')
    usuPuesto = models.CharField(db_column='usuPuesto', null=True, max_length=20, default='pendiente')
    usuDesper = models.CharField(db_column='usuDesper', null=True, max_length=200, default='pendiente')
    usuDespro = models.CharField(db_column='usuDespro', null=True, max_length=200, default='pendiente')
    # 
    password = models.TextField(db_column='usu_pass', null=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_superuser = models.BooleanField(default=False, null=True)

    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = ManejoUsuario()

    USERNAME_FIELD = 'usuCorreo'
    REQUIRED_FIELDS = ['usuNombre','usuFono']
    
    def tokens(self):
        tokens = RefreshToken.for_user(self)
        return {
            'acceso': str(tokens.access_token),
            'refresh': str(tokens)
        }
    class Meta:
        db_table = 't_usuario'


    
    

# class InformacionModel(models.Model):
#     info_id =models.AutoField(db_column='info_id', primary_key=True, unique=True, null=False)
#     info_dni = models.CharField(db_column='info_dni', unique=True, null=True, max_length=11, default='pendiente')
#     info_direc = models.CharField(db_column='info_direc', null=True, max_length=50, default='pendiente')
#     info_puesto = models.CharField(db_column='info_puesto', null=True, max_length=20, default='pendiente')
#     info_desper = models.CharField(db_column='info_desper', null=True, max_length=200, default='pendiente')
#     info_despro = models.CharField(db_column='info_despro', null=True, max_length=200, default='pendiente')
#     createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
#     updatedAt = models.DateTimeField(db_column='update_at', auto_now=True)
#     estado = models.BooleanField(default=True, null=False)
#     class Meta:
#         db_table = 't_informacion'


class SkillModel(models.Model):
    skill_id = models.AutoField(db_column='skill_id', primary_key=True, unique=True, null=False)
    skill_nombre = models.CharField(db_column='skill_nombre', null=False, max_length=30)
    skill_valoracion = models.DecimalField(db_column='skill_valoracion', null=False, max_digits=3, decimal_places=2)
    skill_descripcion = models.CharField(db_column='skill_descripcion', null=False, max_length=100)
    skill_url = models.CharField(db_column='skill_url', null=False, max_length=1000)
    usuId = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usuId', related_name='skillsInfo')
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='update_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)
    class Meta:
        db_table = 't_skill'

class ExperienciaModel(models.Model):
    exp_id = models.AutoField(db_column='exp_id', primary_key=True, unique=True, null=False)
    exp_empresa = models.CharField(db_column='exp_empresa', null=False, max_length=20)
    exp_puesto = models.CharField(db_column='exp_puesto', null=False, max_length=20)
    exp_funciones = models.CharField(db_column='exp_funciones', null=False, max_length=150)
    exp_duracion = models.CharField(db_column='exp_duracion', null=False, max_length=10)
    usuId = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usuId', related_name='expesPersona')
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='update_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)
    class Meta:
        db_table = 't_experiencia'

class ProyectoModel(models.Model):
    proy_id = models.AutoField(db_column='proy_id', primary_key=True, unique=True, null=False)
    proy_empresa = models.CharField(db_column='proy_empresa', null=False, max_length=20)
    proy_nombre = models.CharField(db_column='proy_nombre', null=False, max_length=20)
    proy_descripcion = models.CharField(db_column='proy_descripcion', null=False, max_length=150)
    proy_duracion = models.CharField(db_column='proy_duracion', null=False, max_length=10)
    usuId = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usuId', related_name='proyectosPersona')
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='update_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)
    class Meta:
        db_table = 't_proyecto'

class SolicitudModel(models.Model):
    sol_id = models.AutoField(db_column='sol_id', primary_key=True, unique=True, null=False)
    sol_nombre = models.CharField(db_column='sol_nombre', max_length=30, null=False)
    sol_correo = models.CharField(db_column='sol_correo', max_length=40, null=False)
    sol_telefono = models.CharField(db_column='sol_telefono', max_length=12, null=False)
    sol_mensaje = models.CharField(db_column='sol_mensaje', max_length=200, null=False)
    sol_estado = models.BooleanField(default=True, null=False)
    usuId = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usuId', related_name='solicitudesPersona')
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='update_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)
    class Meta:
        db_table = 't_solicitud'
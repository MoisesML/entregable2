from .models import Usuario, ExperienciaModel, ProyectoModel, SolicitudModel, SkillModel
from .serializers import SkillSerializer, ExperienciaSerializer, ProyectoSerializer, RegistroUsuarioSerializer, LoginSerializer, UsuariosSerializer, SolicitudSerializar
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# Vista para llamar a todas las personas
class UsuarioView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer
    def get(self, request):
        respuesta = self.get_serializer(self.get_queryset(), many=True)
        if respuesta:
            return Response ({
                'Ok':True,
                'Content':respuesta.data,
                'Message':None
            }, status=status.HTTP_200_OK)
        else:
            return Response ({
                'Ok':False,
                'Content':None,
                'Message':'No hay usuarios en la DB'
            }, status=status.HTTP_204_NO_CONTENT)

class UsuarioIdView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer
    def get(self, request, usuId):
        respuesta = self.get_serializer(self.get_queryset().get(usuId=usuId))
        return Response({
            'ok':True,
            'content':respuesta.data,
            'message':None
        })

class UsuarioCorreoView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, usuCorreo):
        respuesta = self.get_serializer(self.get_queryset().get(usuCorreo=usuCorreo))
        if respuesta:
            return Response({
                'Ok':True,
                'Content':respuesta.data,
                'Message':None
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'Ok':False,
                'Content':None,
                'Message':'El usuario no existe'
            }, status=status.HTTP_404_NOT_FOUND)


# SkillsModel
class ObtenerSkillsPersona(ListAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer
    def get(self, request, usuId):
        respuesta = self.get_serializer(self.get_queryset().filter(usuId=usuId), many=True)
        return Response({
            'ok':True,
            'content':respuesta.data,
            'message':None
        })

class ActualizarSkill(UpdateAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer
    # permission_classes = (IsAuthenticated,)
    def put(self, request, skill_id):
        respuesta = self.get_serializer(self.get_queryset().get(skill_id=skill_id), data=request.data)
        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response({
                'ok':True,
                'content':self.serializer_class(resultado).data,
                'message': None
            })
        else:
            return Response({
                'ok':False,
                'content': 'Hubo un error al actualizar la skill'
            }, status=status.HTTP_400_BAD_REQUEST)

class CrearSkill(CreateAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        respuesta = self.get_serializer(data=request.data)
        if respuesta.is_valid(raise_exception=True):
            respuesta.save()
            return Response({
                'Ok':True,
                'Content':respuesta.data,
                'Message':None
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response({
                'Ok':False,
                'Content':None,
                'Message':'Hubo un error al crear la skill'
            },status=status.HTTP_400_BAD_REQUEST)

# Experiencia

class ObtenerExpsPersona(ListAPIView):
    queryset = ExperienciaModel.objects.all()
    serializer_class = ExperienciaSerializer
    def get(self, request, usuId):
        respuesta = self.get_serializer(self.get_queryset().filter(usuId=usuId), many=True)
        return Response({
            'ok':True,
            'content':respuesta.data,
            'message':None
        })

class ActualizarExp(UpdateAPIView):
    queryset = ExperienciaModel.objects.all()
    serializer_class = ExperienciaSerializer
    permission_classes = (IsAuthenticated,)
    def put(self, request, exp_id):
        respuesta = self.get_serializer(self.get_queryset().get(exp_id=exp_id), data=request.data)
        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response({
                'ok':True,
                'content':self.serializer_class(resultado).data,
                'message': None
            })
        else:
            return Response({
                'ok':False,
                'content': 'Hubo un error al actualizar la experiencia'
            }, status=status.HTTP_400_BAD_REQUEST)

class CrearExp(CreateAPIView):
    queryset = ExperienciaModel.objects.all()
    serializer_class = ExperienciaSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        respuesta = self.get_serializer(data=request.data)
        if respuesta.is_valid(raise_exception=False):
            respuesta.save()
            return Response({
                'Ok':True,
                'Content':respuesta.data,
                'Message':None
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response({
                'Ok':False,
                'Content':None,
                'Message':'Hubo un error al crear la experiencia'
            },status=status.HTTP_400_BAD_REQUEST)

# Proyecto

class ObtenerProysPersona(ListAPIView):
    queryset = ProyectoModel.objects.all()
    serializer_class = ProyectoSerializer
    def get(self, request, usuId):
        respuesta = self.get_serializer(self.get_queryset().filter(usuId=usuId), many=True)
        return Response({
            'ok':True,
            'content':respuesta.data,
            'message':None
        })

class ActualizarProy(UpdateAPIView):
    queryset = ProyectoModel.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = (IsAuthenticated,)
    def put(self, request, proy_id):
        respuesta = self.get_serializer(self.get_queryset().get(proy_id=proy_id), data=request.data)
        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response({
                'ok':True,
                'content':self.serializer_class(resultado).data,
                'message': None
            })
        else:
            return Response({
                'ok':False,
                'content': 'Hubo un error al actualizar el proyecto'
            }, status=status.HTTP_400_BAD_REQUEST)

class CrearProy(CreateAPIView):
    queryset = ProyectoModel.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        respuesta = self.get_serializer(data=request.data)
        if respuesta.is_valid(raise_exception=False):
            respuesta.save()
            return Response({
                'Ok':True,
                'Content':respuesta.data,
                'Message':None
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response({
                'Ok':False,
                'Content':None,
                'Message':'Hubo un error al crear el proyecto'
            },status=status.HTTP_400_BAD_REQUEST)

# Proyecto

class ObtenerSolsPersona(ListAPIView):
    queryset = SolicitudModel.objects.all()
    serializer_class = SolicitudSerializar
    permission_classes = (IsAuthenticated,)
    def get(self, request, usuId):
        respuesta = self.get_serializer(self.get_queryset().filter(usuId=usuId), many=True)
        return Response({
            'ok':True,
            'content':respuesta.data,
            'message':None
        })

class CrearSol(CreateAPIView):
    queryset = SolicitudModel.objects.all()
    serializer_class = SolicitudSerializar
    def post(self, request):
        respuesta = self.get_serializer(data=request.data)
        if respuesta.is_valid(raise_exception=False):
            respuesta.save()
            return Response({
                'Ok':True,
                'Content':respuesta.data,
                'Message':None
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response({
                'Ok':False,
                'Content':None,
                'Message':'Hubo un error al crear la solicitud'
            },status=status.HTTP_400_BAD_REQUEST)

class RegistroView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroUsuarioSerializer
    def post(self, request):
        # VALIDAR SI YA HAY UN USUARIO CON ESE EMAIL
        correo = request.data.get('usuCorreo')
        # el filter devuelve una LISTA de todas las coincidencias y el get si no hay indicara un error
        usuarios = self.get_queryset().filter(usuCorreo=correo).first()
        if usuarios:
            return Response({
                'ok': False,
                'message':'El usuario con correo {} ya existe'.format(correo,)
            },status = status.HTTP_400_BAD_REQUEST)
        else:
            respuesta = self.get_serializer(data=request.data)
            if respuesta.is_valid(raise_exception=True):
                resultado = respuesta.save()
                return Response({
                    'ok': True,
                    'content': self.get_serializer(resultado).data,
                    'message':'Usuario creado exitosamente'
                }, status=201)
            else:
                return Response({
                    'ok': False,
                    'message': 'Data Incorrecta'
                }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializador = self.get_serializer(data=request.data)
        serializador.is_valid(raise_exception=True)
        return Response({
            'ok':True,
            'content':serializador.data
        })
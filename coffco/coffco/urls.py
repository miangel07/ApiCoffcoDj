"""
URL configuration for coffco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from apps.documentos.api.Routers import routerDocumento
from apps.detalle.api.Routers import routerDetalle
from apps.finca.api.Routers import routerFinca
from apps.muestra.api.Routers import routerMuestra
from apps.municipio.api.Routers import routerMunicipio
from apps.servicio.api.Routers import routerServicio
from apps.variables.api.Routers import routerVariable
from apps.rol.api.Routers import routerRol
from apps.precios.api.Routers import routerPrecios
from apps.versiones.api.Routers import routerVersiones
from apps.ambiente.api.Routers import routerAmbiente
from apps.tipo_servicios.api.Routers import routerTipoServicio
from apps.tipo_documento.api.Routers import routerTipoDocumento
from apps.logos.api.Routers import routerLogo
from apps.logo_documento.api.Routers import routerLogoDocumento
from apps.valor.api.Routers import routerValor





from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.user.api.Routers')),
    path('api/',include(routerDocumento.urls)),
    path('api/',include(routerFinca.urls)),
    path('api/',include(routerDetalle.urls)),
    path('api/',include(routerMuestra.urls)),
    path('api/',include(routerMunicipio.urls)),
    path('api/',include(routerServicio.urls)),
    path('api/',include(routerVersiones.urls)),
    path('api/',include(routerPrecios.urls)),
    path('api/',include(routerVariable.urls)),
    path('api/',include(routerRol.urls)),
    path('api/',include(routerAmbiente.urls)),
    path('api/',include(routerTipoServicio.urls)),
    path('api/',include(routerTipoDocumento.urls)),
    path('api/',include(routerLogo.urls)),
    path('api/',include(routerLogoDocumento.urls)),
    path('api/',include(routerValor.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocS/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

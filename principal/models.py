from django.db import models

class Gallery(models.Model):
    nombre				= models.CharField(max_length=30)
    activo 				= models.BooleanField(default=True)
    default 			= models.BooleanField(default=False)

class Items(models.Model):
	gallery 			= models.ForeignKey(Gallery)
	ruta				= models.CharField(max_length=100,blank=False)	
	tipo				= models.CharField(max_length=1, blank=False, default="I")
	nombre 				= models.CharField(max_length=30, unique=True, blank=False)
	activo				= models.BooleanField(default=True, blank=False)
	title 				= models.CharField(max_length=100)
	orden				= models.IntegerField(blank=False)

class Pases(models.Model):
    langcode            = models.CharField(max_length=10,blank=False)
    enurl               = models.CharField(max_length=100,blank=True)
    esurl               = models.CharField(max_length=100,blank=True)
    activo              = models.BooleanField(default=True)
    default             = models.BooleanField(default=False)

    # user_id			= models.ForeignKey(User)
    # codigo_cliente	= models.CharField(max_length=10, blank=False, unique=True)	#Esta campo recuerdate de convertirlo en UNICO
    # propiedad			= models.CharField(max_length=45, blank=False)
    # propiedad_desc	= models.CharField(max_length=200, blank=False)
    # fecha_proceso 	= models.DateField()
    # saldo				= models.DecimalField(max_digits=17, decimal_places=2, blank=False)
    # activo			= models.BooleanField(default=True)

# [
# 	{
# 	"gallery":
# 		{"nombre":"Villas",
# 		 "items":
# 		 [
# 			{"ruta":"","tipo":"","nombre":""},
# 			{"ruta":"","tipo":"","nombre":""},
# 			{"ruta":"","tipo":"","nombre":""},
# 			{"ruta":"","tipo":"","nombre":""},
# 			{"ruta":"","tipo":"","nombre":""},
# 			{"ruta":"","tipo":"","nombre":""},
# 		 ]
# 		}
# 	},

# ]
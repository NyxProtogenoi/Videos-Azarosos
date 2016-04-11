#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
import os
import random

extensiones=[".FLV",".flv",".mpg",".mp4",".avi",".ogv",".mov",".mkv"]
archivos=os.listdir(os.getcwd())
#print "archivos" + str(archivos)	#DEBUG
azaroso=random.randint(0,len(archivos)-1)
elegido=archivos[azaroso]
#print "\nelegido " + elegido	#DEBUG

if " " in elegido:
	elegido = elegido.replace(" ","\ ")
	#print "ELEGIDO " + elegido	#DEBUG

especiales=("'","(",")","&")
for elemento in elegido:
	if elemento in especiales:
		elegido = elegido.replace(elemento,"\%s" %elemento)
		#print "ELEGIDO " + elegido	#DEBUG
		
(nombreFichero, extension) = os.path.splitext(elegido) #Extraer extension

#print "extension " + extension		#DEBUG

if extension.lower() not in extensiones:
	print "El archivo no es un video."
	#exit
else: 
	#print "os.path " + str(os.path.splitext(elegido))	#DEBUG
	elegidocompleto=os.getcwd()+"/"+elegido
	print "elegido completo " + elegidocompleto	#DEBUG
	pertenencia=extension in extensiones
	if pertenencia==True:
		print elegidocompleto
		os.system("vlc"+" "+str(elegido))
	if extension=="":
		print elegidocompleto
		comand="vlc "+str(elegidocompleto)
		os.system("dolphin"+" "+str(elegidocompleto))

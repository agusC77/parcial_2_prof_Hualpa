# 💻 Programación 1  
**Tecnicatura Universitaria en Programación**  
📍 *Universidad Tecnológica Nacional*  
📍 *Parcial 2 (Entrega Final Integradora)*  

## ✨ Estudiantes  
- **Nombre:** Allende Pablo, Contardi Agustín, Rojas Leonel 
- **Comisión:** 4  

## Docentes
- **Cinthia Rigoni**
- **Ramiro Hualpa**

## Estructura del programa:
- **Main:** menu_principal.py
- **Lista de paises en archivo csv:** paises.csv 
- **Funciones:** editar_archivo.py, filtrar_los_paises.py, ver_informacion_de_paises.py, validar.py

## 📂 Descripción del Repositorio  
El sistema utiliza una estructura jerárquica de carpetas para organizar la información de los países de forma clara y ordenada. Dentro 
de una carpeta principal llamada “datos” se crean subcarpetas para cada continente, y dentro de estas, otras carpetas para cada país. En
cada carpeta de país se guarda un archivo csv que contiene los datos básicos de ese país, como su nombre, continente, población y 
superficie. Por ejemplo, la ruta de acceso a la información de Argentina sería algo como “datos/América/Argentina/info.csv”. Esta forma
de organizar los archivos imita una base de datos jerárquica, donde cada nivel representa una categoría más específica.

Para leer toda la información almacenada, el programa utiliza recursividad. Esto significa que una función recorre todas las carpetas 
dentro de “datos” y sus subcarpetas de manera automática, buscando archivos “info.csv” sin necesidad de indicar manualmente las rutas. 
Así, si se agregan nuevos continentes o países, el sistema los detecta de forma automática y los incluye al mostrar los datos. Este 
diseño jerárquico y recursivo permite mantener los archivos organizados, facilitar la búsqueda y modificación de la información, y hacer
que el sistema pueda crecer fácilmente sin cambiar la lógica del programa.

-**Link de video explicativo:** https://youtu.be/QNVEO9-3jhk

-**Link de Git HuB:** https://github.com/agusC77/parcial_2_prof_Hualpa.git
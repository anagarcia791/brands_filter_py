# Buscador de similitud fonética y sintáctica de marcas

## Dependencias
   Instalación de [python](https://www.python.org/)

   IDE (Integrated Development Environment) de preferencia, recomendado [visual studio](https://code.visualstudio.com/)


## Uso
1. Descargar el proyecto

   ![descarga](https://raw.githubusercontent.com/anagarcia791/brands_filter_py/refs/heads/main/assets/images/descarga.png)

2. Ambientar python y descargar el IDE
3. Dentro de la carpeta descargada agregar un archivo con nombre descriptivo, ej:

   img antes de agregar archivo:

   ![archivos por defecto](https://raw.githubusercontent.com/anagarcia791/brands_filter_py/refs/heads/main/assets/images/files.png)

   img después de agregar archivo:

   ![excel agregado](https://raw.githubusercontent.com/anagarcia791/brands_filter_py/refs/heads/main/assets/images/excel_added.png)

4. Abrir el folder del proyecto en el IDE de preferencia

   ![visual](https://raw.githubusercontent.com/anagarcia791/brands_filter_py/refs/heads/main/assets/images/visual.png)

5. Abrir el archivo main
   - cambiar la linea 5 y 6 con la informacion respectiva, ej:
   
     brand_to_compare = 'CLASTOZ'
   
     original_file = 'CLASTOZ.xlsx'
   
     ![main](https://raw.githubusercontent.com/anagarcia791/brands_filter_py/refs/heads/main/assets/images/main.png)
   
   - para cambiar de empresa se sigue el mismo formato, ej:
   
     brand_to_compare = 'EMPRESA_X'
   
     original_file = 'EMPRESA_X.xlsx'

6. Ejecutar el archivo main, una vez la información de linea 5 y 6 coinciden dar click en el botón de ejcución de python

     ![ejecucion](https://raw.githubusercontent.com/anagarcia791/brands_filter_py/refs/heads/main/assets/images/ejecucion.png)

7. Una vez termine la ejecución, verá un archivo excel generado en el folder del proyecto

     ![resultado](https://raw.githubusercontent.com/anagarcia791/brands_filter_py/refs/heads/main/assets/images/resultado.png)

8. Recuerde hacer limpieza del folder. Siempre que termine una ejecución elimine los archivos excel agregados/generados
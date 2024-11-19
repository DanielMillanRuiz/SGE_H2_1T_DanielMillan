# Proyecto: Gestión de Encuestas con Tkinter y MySQL

Este proyecto combina una interfaz gráfica construida con **Tkinter** y el manejo de datos mediante una base de datos **MySQL**, proporcionando un sistema para analizar datos relacionados con el consumo de alcohol y sus efectos en la salud.


## Autor

- [@DanielMillan](https://github.com/DanielMillanRuiz)

## Requisitos previos

Antes de comenzar, asegúrate de contar con lo siguiente instalado en tu sistema:
1. **Python 3.9 o superior**: Descarga desde [python.org](https://www.python.org/).
2. **MySQL Server**: Descarga desde [MySQL Community Downloads](https://dev.mysql.com/downloads/).
3. Las siguientes librerías de Python, que se pueden instalar con `pip`:
   - `pymysql`
   - `pandas`
   - `openpyxl`
   - `matplotlib`

## Instalación y configuración
Antes de nada la carpeta con el proyecto debe estar en la ruta designada por defecto de pycharm la cual suele estar dentro del a carpeta de **usuarios\nombredeusuario\PycharmProjects.**

Dentro de esta se debe pegar la carpeta para luego dentro de la aplicacion ir a los 3 puntos arriba a la izquierda y luego a **open** y dentro de **PycharmProjects** seleccionar la carpeta del proyecto.

Ademas hay que importar dentro de **Workbench** el sql del progrma y ejecutarlo para que todo funcione correctamente

### Instalar dependencias
En la terminal integrada del IDE o del sistema, ejecuta el siguiente comando para instalar las dependencias necesarias:

pip install pymysql pandas openpyxl matplotlib
## Guia de uso

### Ejecución del programa

- Iniciar el programa
En PyCharm, abre el archivo principal Hito2DanielMillan.py.
Haz clic en el botón verde de Run en la parte superior derecha o presiona Shift + F10.

- Usar la aplicación
La interfaz gráfica de Tkinter te permitirá realizar las siguientes operaciones:

- Operaciones CRUD:
- Exportar a Excel
- Visualización de gráficos


## Funcionalidades principales
### Operaciones CRUD
- Crear registro: Ingresa todos los datos requeridos en los campos y presiona Crear registro.
- Editar registro: Selecciona un registro en la tabla, modifica los campos y presiona Editar registro.
- Eliminar registro: Selecciona un registro y presiona Eliminar registro, confirmando en la ventana emergente.
- Consultar registros: Presiona Consultar para ver todos los registros o usa filtros para búsquedas específicas.
### Generación de gráficos
- Usa los botones de Gráfico de Barras o Gráfico Circular para visualizar los datos filtrados en la tabla.
### Exportación a Excel
- Presiona Exportar a Excel para guardar los datos mostrados en un archivo .xlsx.

## FAQ

#### Error de conexión con MySQL:

Verifica que el servidor esté ejecutándose y los detalles de conexión sean correctos.

#### Librerías no encontradas:

Asegúrate de haber instalado todas las dependencias usando pip.

#### Errores en PyCharm:

- Verifica que el intérprete de Python esté configurado correctamente.
- Asegúrate de estar en el entorno virtual correcto.

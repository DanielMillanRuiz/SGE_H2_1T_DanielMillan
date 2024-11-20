Proyecto: Gestión de Encuestas con Tkinter y MySQL
==================================================

Este proyecto combina una interfaz gráfica construida con **Tkinter** y el manejo de datos mediante una base de datos **MySQL**, proporcionando un sistema para analizar datos relacionados con el consumo de alcohol y sus efectos en la salud.

Autor
-----

-   [@DanielMillan](https://github.com/DanielMillanRuiz)

* * * * *

Requisitos previos
------------------

Antes de comenzar, asegúrate de contar con lo siguiente instalado en tu sistema:

1.  **Python 3.9 o superior**\
    Descárgalo desde [python.org](https://www.python.org/).

2.  **MySQL Server**\
    Descárgalo desde [MySQL Community Downloads](https://dev.mysql.com/downloads/).

3.  **Librerías de Python necesarias**\
    Se instalan con el comando `pip`:

    -   `pymysql`
    -   `pandas`
    -   `openpyxl`
    -   `matplotlib`

* * * * *

Instalación y configuración
---------------------------

### 1\. **Importar el proyecto en PyCharm**

-   Copia la carpeta completa del proyecto en la ruta predeterminada de PyCharm:\
    `C:\Usuarios\TuNombreUsuario\PycharmProjects`.

-   Abre PyCharm y selecciona la opción **File > Open**. Navega a la carpeta **PycharmProjects** y selecciona la carpeta del proyecto.

### 2\. **Configurar la base de datos en MySQL Workbench**

-   Abre **MySQL Workbench**.
-   Importa el archivo SQL proporcionado y ejecútalo para crear la estructura de la base de datos necesaria.

### 3\. **Instalar las dependencias**

Abre la terminal integrada en PyCharm (o cualquier terminal) y ejecuta el siguiente comando:

`pip install pymysql pandas openpyxl matplotlib`  

* * * * *

Guía de uso
-----------

### 1\. **Ejecutar el programa**

-   En PyCharm, abre el archivo principal `Hito2DanielMillan.py`.
-   Ejecuta el programa haciendo clic en el botón verde **Run** en la esquina superior derecha o presionando `Shift + F10`.

### 2\. **Usar la aplicación**

La interfaz gráfica te permitirá realizar las siguientes operaciones:

#### Operaciones CRUD

-   **Crear registro**: Llena los campos requeridos y presiona **Crear registro**.
-   **Editar registro**: Selecciona un registro en la tabla, edita los campos y presiona **Editar registro**.
-   **Eliminar registro**: Selecciona un registro, presiona **Eliminar registro** y confirma.
-   **Consultar registros**: Presiona **Consultar** para ver todos los registros o usa los filtros disponibles.

#### Generación de gráficos

-   Usa los botones **Gráfico de Barras** o **Gráfico Circular** para visualizar los datos filtrados.

#### Exportación a Excel

-   Presiona el botón **Exportar a Excel** para guardar los datos visibles en un archivo `.xlsx`.

* * * * *

Solución de problemas
---------------------

#### **Error de conexión con MySQL**

-   Verifica que el servidor de MySQL esté ejecutándose.
-   Asegúrate de que las credenciales de conexión en el código sean correctas.

#### **Librerías no encontradas**

-   Ejecuta nuevamente el comando `pip install pymysql pandas openpyxl matplotlib` para instalar las dependencias faltantes.

#### **Errores en PyCharm**

-   Verifica que el intérprete de Python esté configurado correctamente en **File > Settings > Project > Python Interpreter**.
-   Asegúrate de estar trabajando en el entorno virtual correcto.

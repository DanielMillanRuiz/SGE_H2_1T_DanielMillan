# Imports

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

conexion = None

columnas = [
    "ID", "Sexo", "Edad", "BebidasSemana", "CervezasSemana", "BebidasFinSemana",
    "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl",
    "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"
]


# Funciones de utilidad

# Funcion para mostrar mensajes de error
def mensajeError(mensaje):
    messagebox.showerror("Error", mensaje)


# Funcion para generar un grafico de barras tomando como datos las bebidas a la semana
def generarGraficoBarras(tree):
    data = [tree.item(item)["values"] for item in tree.get_children()]  # Extrae los datos del Treeview
    if not data:
        mensajeError("No hay se han seleccionado datos para generar el grafico")
        return
    df = pd.DataFrame(data, columns=[columnas])
    try:
        valores = df["BebidasSemana"].value_counts()
        if valores.empty:
            mensajeError("La columna esta vacia")
            return

        # Genera el grafico de barras
        valores.plot(kind='bar', color='skyblue', edgecolor='black')

        plt.xlabel("Cantidad de Bebidas por Semana")
        plt.ylabel("Frecuencia")
        plt.title("Frecuencia de Bebidas por Semana")

        plt.xticks(rotation=45, ha="right", fontsize=8)  # Rotar las etiquetas si hay muchas
        plt.tight_layout()
        plt.show()
    except KeyError:
        mensajeError("No se ha encontrado la columna para el grafico")


# Funcion para generar un grafico circular tomando como datos si se sufre de dolor de cabeza
def generar_grafico_circular(tree):
    data = [tree.item(item)["values"] for item in tree.get_children()]  # Extrae los datos del Treeview
    if not data:
        mensajeError("No hay se han seleccionado datos para generar el grafico")
        return

    df = pd.DataFrame(data, columns=[columnas])

    try:
        valores = df["DolorCabeza"].value_counts()

        if valores.empty:
            mensajeError("La columna esta vacia")
            return
        # Genera el grafico circular
        valores.plot(kind='pie', autopct='%1.1f%%', startangle=90)

        plt.title("Distribucion por Dolor de cabeza")
        plt.ylabel("")
        plt.tight_layout()

        plt.show()
    except KeyError:
        mensajeError("No se ha encontrado la columna para el grafico")


# Funcion para exportar los datos seleccionados a excel
def exportarExcel(tree):
    data = [tree.item(item)["values"] for item in tree.get_children()]  # Extrae los valores de cada fila en el treeview

    # Crea el DataFrame usando las columnas ajustadas
    df = pd.DataFrame(data, columns=columnas)

    # Exporta el DataFrame a un archivo Excel
    df.to_excel("datosEncuesta.xlsx", index=False)
    messagebox.showinfo("Exito", "Datos exportados a Excel correctamente")


#  Limpia el contenido de todos los campos pasados como argumentos.
def limpiar_campos(*args):
    for campo in args:
        campo.delete(0, 'end')  # Limpia el contenido del campo


def verificar_campos(sexo, edad, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                     bebidas_destiladas_semana, vinos_semana, perdidas_control,
                     diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza):
    valores = [sexo, edad, bebidas_semana, cervezas_semana, bebidas_fin_semana,
               bebidas_destiladas_semana, vinos_semana, perdidas_control,
               diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza]

    # Verificar que los valores no esten vacios o sean None
    if any(not valor for valor in valores):
        mensajeError("Todos los campos deben estar completos")
        return False

    # Validaciones de los campos
    if sexo.strip() not in ["Hombre", "Mujer"]:
        mensajeError("El campo 'Sexo' solo puede ser 'Hombre' o 'Mujer'")
        return False

    if diversion_dependencia_alcohol not in ["Si", "No"]:
        mensajeError("El campo 'Diversion Dependencia Alcohol' solo puede ser 'Si' o 'No'")
        return False

    if problemas_digestivos not in ["Si", "No"]:
        mensajeError("El campo 'Problemas Digestivos' solo puede ser 'Si' o 'No'")
        return False

    if tension_alta not in ["Si", "No", "No lo se"]:
        mensajeError("El campo 'Tension Alta' solo puede ser 'Si', 'No' o 'No lo se'")
        return False

    if dolor_cabeza not in ["Nunca", "Alguna vez", "Muy a menudo"]:
        mensajeError("El campo 'Dolor de Cabeza' solo puede ser 'Nunca', 'Alguna vez' o 'Muy a menudo'")
        return False

    return True


# Funcion para conectarse a la base de datos
def conectar_bd(ventana):
    global conexion
    try:
        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='campusfp',
            database='ENCUESTAS'
        )
        return True
    except pymysql.Error as e:
        conexion = None  # Reinicia la conexion en caso de fallo
        mensajeError(f"No se pudo conectar a la base de datos: {e}")
        return False


# Funcion para iniciar el programa
def iniciar_programa():
    if conectar_bd(ventana):
        ventana.mainloop()
    else:
        ventana.quit()


# Funcion para consultar la poblacion tomando como datos los inputs
def consultarPoblacion(inputSexo, inputEdad, inputBebidasSemana, inputCervezasSemana, inputBebidasFinSemana,
                       inputBebidasDestiladasSemana, inputVinosSemana, inputPerdidasControl,
                       inputDiversionDependenciaAlcohol, inputProblemasDigestivos, inputTensionAlta, inputDolorCabeza,
                       tree):
    if conexion is None:  # Verifica si la conexion es None
        mensajeError("No se ha establecido una conexion con la base de datos")
        return

    # Se toman los datos de los inputs
    sexo = inputSexo.get()
    edad = inputEdad.get()
    bebidas_semana = inputBebidasSemana.get()
    cervezas_semana = inputCervezasSemana.get()
    bebidas_fin_semana = inputBebidasFinSemana.get()
    bebidas_destiladas_semana = inputBebidasDestiladasSemana.get()
    vinos_semana = inputVinosSemana.get()
    perdidas_control = inputPerdidasControl.get()
    diversion_dependencia_alcohol = inputDiversionDependenciaAlcohol.get()
    problemas_digestivos = inputProblemasDigestivos.get()
    tension_alta = inputTensionAlta.get()
    dolor_cabeza = inputDolorCabeza.get()

    # Iniciar la consulta base
    query = "SELECT * FROM ENCUESTA WHERE 1=1"
    params = []

    # Agregar condiciones de filtro
    if sexo:
        query += " AND Sexo = %s"
        params.append(sexo)
    if edad:
        query += " AND edad = %s"
        params.append(edad)
    if bebidas_semana:
        query += " AND BebidasSemana = %s"
        params.append(bebidas_semana)
    if cervezas_semana:
        query += " AND CervezasSemana = %s"
        params.append(cervezas_semana)
    if bebidas_fin_semana:
        query += " AND BebidasFinSemana = %s"
        params.append(bebidas_fin_semana)
    if bebidas_destiladas_semana:
        query += " AND BebidasDestiladasSemana = %s"
        params.append(bebidas_destiladas_semana)
    if vinos_semana:
        query += " AND VinosSemana = %s"
        params.append(vinos_semana)
    if perdidas_control:
        query += " AND PerdidasControl = %s"
        params.append(perdidas_control)
    if diversion_dependencia_alcohol:
        query += " AND DiversionDependenciaAlcohol = %s"
        params.append(diversion_dependencia_alcohol)
    if problemas_digestivos:
        query += " AND ProblemasDigestivos = %s"
        params.append(problemas_digestivos)
    if tension_alta:
        query += " AND TensionAlta = %s"
        params.append(tension_alta)
    if dolor_cabeza:
        query += " AND DolorCabeza = %s"
        params.append(dolor_cabeza)

    try:
        cursor = conexion.cursor()
        cursor.execute(query, tuple(params))  # Ejecutamos la consulta con los parametros
        results = cursor.fetchall()
        cursor.close()
        # Limpiar el Treeview antes de mostrar los nuevos resultados
        for item in tree.get_children():
            tree.delete(item)

        # Insertar los resultados en el Treeview
        for row in results:
            tree.insert("", "end", values=row)

    except pymysql.Error as e:
        mensajeError(f"Error al consultar la base de datos: {e}")


# Funcion crear un nuevo registro
def crear_registro(sexo, edad, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                   bebidas_destiladas_semana, vinos_semana, perdidas_control,
                   diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza):
    if conexion is None:  # Verifica si la conexion es None
        mensajeError("No se ha establecido una conexion con la base de datos")
        return

        # Verificar que todos los campos esten completos
    if not verificar_campos(sexo, edad, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                            bebidas_destiladas_semana, vinos_semana, perdidas_control,
                            diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza):
        return

    # Validar y convertir los valores a enteros si es necesario, asignar None si estan vacios
    def validar_entero(valor):
        try:
            # Si el valor no es vacio, convertirlo a entero
            return int(valor) if valor.strip() != "" else None
        except ValueError:
            return None  # si no es entero devuelve none

    # Validamos los valores y mostramos el resultado despues de la validacion
    edad = validar_entero(edad)
    bebidas_semana = validar_entero(bebidas_semana)
    cervezas_semana = validar_entero(cervezas_semana)
    bebidas_fin_semana = validar_entero(bebidas_fin_semana)
    bebidas_destiladas_semana = validar_entero(bebidas_destiladas_semana)
    vinos_semana = validar_entero(vinos_semana)
    perdidas_control = validar_entero(perdidas_control)

    try:
        cursor = conexion.cursor()
        query = """
            INSERT INTO ENCUESTA (Sexo, edad, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, 
            VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query,
                       (sexo, edad, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana,
                        vinos_semana, perdidas_control, diversion_dependencia_alcohol, problemas_digestivos,
                        tension_alta, dolor_cabeza))
        conexion.commit()

        messagebox.showinfo("Registro creado", "El registro se ha creado correctamente.")

        limpiar_campos(inputSexo, inputEdad, inputBebidasSemana, inputCervezasSemana, inputBebidasFinSemana,
                       inputBebidasDestiladasSemana, inputVinosSemana, inputPerdidasControl,
                       inputDiversionDependenciaAlcohol, inputProblemasDigestivos, inputTensionAlta, inputDolorCabeza)
    except pymysql.Error as e:
        mensajeError(f"No se pudo crear el registro: {e}")


# Funcion para editar registro
def editar_registro(tree, sexo, edad, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                    bebidas_destiladas_semana, vinos_semana, perdidas_control,
                    diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza):
    # Verificar que todos los campos esten completos
    if not verificar_campos(sexo, edad, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                            bebidas_destiladas_semana, vinos_semana, perdidas_control,
                            diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza):
        return

    # Obtener el ID del registro seleccionado
    selected_item = tree.selection()
    if not selected_item:
        mensajeError("Debes seleccionar un registro en la tabla para editar")
        return

    item_id = tree.item(selected_item)['values'][0]  # ID del registro seleccionado

    try:
        # Establecer la conexion a la base de datos y crear un cursor
        cursor = conexion.cursor()

        # Consulta SQL para actualizar el registro
        query = """
            UPDATE ENCUESTA SET Sexo = %s, edad = %s, BebidasSemana = %s, CervezasSemana = %s, BebidasFinSemana = %s, 
            BebidasDestiladasSemana = %s, VinosSemana = %s, PerdidasControl = %s, DiversionDependenciaAlcohol = %s, 
            ProblemasDigestivos = %s, TensionAlta = %s, DolorCabeza = %s WHERE idencuesta = %s
        """

        # Ejecutar la consulta
        cursor.execute(query, (sexo, edad, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                               bebidas_destiladas_semana, vinos_semana, perdidas_control,
                               diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza,
                               item_id))
        conexion.commit()

        # Mostrar mensaje de exito
        messagebox.showinfo("Registro actualizado", "El registro ha sido actualizado correctamente.")

        # Actualizar la tabla con los nuevos valores
        tree.item(selected_item, values=(item_id, sexo, edad, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                                         bebidas_destiladas_semana, vinos_semana, perdidas_control,
                                         diversion_dependencia_alcohol, problemas_digestivos, tension_alta,
                                         dolor_cabeza))

        # Limpiar los campos después de la actualización
        limpiar_campos(inputSexo, inputEdad, inputBebidasSemana, inputCervezasSemana, inputBebidasFinSemana,
                       inputBebidasDestiladasSemana, inputVinosSemana, inputPerdidasControl,
                       inputDiversionDependenciaAlcohol, inputProblemasDigestivos, inputTensionAlta, inputDolorCabeza)

    except pymysql.Error as e:
        # Manejo de errores en caso de fallo en la actualización
        mensajeError(f"No se pudo actualizar el registro: {e}")


# Funcion para eliminar registro
def eliminar_registro(tree):
    selected_item = tree.selection()
    if not selected_item:
        mensajeError("Debes seleccionar un registro en la tabla para eliminar")
        return

    item_id = tree.item(selected_item)['values'][0]

    if messagebox.askyesno("Confirmacion de eliminacion", f"Se va a eliminar el registro con ID {item_id}"):
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM ENCUESTA WHERE idencuesta = %s"
            cursor.execute(query, (item_id,))
            conexion.commit()
            messagebox.showinfo("Registro eliminado", "El registro ha sido eliminado correctamente.")
            tree.delete(selected_item)
        except pymysql.Error as e:
            mensajeError(f"No se pudo eliminar el registro: {e}")


# Ventana principal
ventana = tk.Tk()
ventana.title("Consulta Encuesta")
ventana.geometry("1350x600")  # Puedes ajustar el tamaño según necesites
ventana.resizable(True, True)  # Permite redimensionar la ventana

# Crear un Frame principal para organizar los componentes
framePrincipal = tk.Frame(ventana, padx=10, pady=10, bg="lightblue")
framePrincipal.pack(fill=tk.BOTH, expand=True)

# Crear un Frame para el formulario
frameFormulario = tk.Frame(framePrincipal, bg="white", padx=10, pady=10, bd=2, relief="groove")
frameFormulario.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Titulo de la encuesta
tk.Label(frameFormulario, text="ENCUESTA DE BEBIDAS").grid(row=0, column=0, columnspan=8, padx=2, pady=2, sticky='ew')

# Campos del formulario
tk.Label(frameFormulario, text="Edad").grid(row=1, column=0, pady=10, sticky='e')
inputEdad = tk.Entry(frameFormulario)
inputEdad.grid(row=1, column=1, padx=6, pady=10, sticky='w')

tk.Label(frameFormulario, text="Sexo").grid(row=1, column=2, padx=6, pady=10, sticky='e')
inputSexo = ttk.Combobox(frameFormulario, values=["Hombre", "Mujer"])
inputSexo.grid(row=1, column=3, padx=6, pady=10, sticky='w')

tk.Label(frameFormulario, text="Bebidas Semana").grid(row=1, column=4, padx=6, pady=10, sticky='e')
inputBebidasSemana = tk.Entry(frameFormulario)
inputBebidasSemana.grid(row=1, column=5, padx=6, pady=10, sticky='w')

tk.Label(frameFormulario, text="Cervezas Semana").grid(row=1, column=6, padx=6, pady=10, sticky='e')
inputCervezasSemana = tk.Entry(frameFormulario)
inputCervezasSemana.grid(row=1, column=7, padx=6, pady=10, sticky='w')

tk.Label(frameFormulario, text="Bebidas Fin Semana").grid(row=2, column=0, padx=6, pady=4, sticky='e')
inputBebidasFinSemana = tk.Entry(frameFormulario)
inputBebidasFinSemana.grid(row=2, column=1, padx=6, pady=4, sticky='w')

tk.Label(frameFormulario, text="Bebidas Destiladas Semana").grid(row=2, column=2, padx=6, pady=4, sticky='e')
inputBebidasDestiladasSemana = tk.Entry(frameFormulario)
inputBebidasDestiladasSemana.grid(row=2, column=3, padx=6, pady=4, sticky='w')

tk.Label(frameFormulario, text="Vinos Semana").grid(row=2, column=4, padx=2, pady=4, sticky='e')
inputVinosSemana = tk.Entry(frameFormulario)
inputVinosSemana.grid(row=2, column=5, padx=2, pady=4, sticky='w')

tk.Label(frameFormulario, text="Perdidas de Control").grid(row=2, column=6, padx=6, pady=2, sticky='e')
inputPerdidasControl = tk.Entry(frameFormulario)
inputPerdidasControl.grid(row=2, column=7, padx=6, pady=2, sticky='w')

tk.Label(frameFormulario, text="Diversion Dependencia Alcohol").grid(row=3, column=0, padx=6, pady=10, sticky='e')
inputDiversionDependenciaAlcohol = ttk.Combobox(frameFormulario, values=["Si", "No"])
inputDiversionDependenciaAlcohol.grid(row=3, column=1, padx=6, pady=10, sticky='w')

tk.Label(frameFormulario, text="Problemas Digestivos").grid(row=3, column=2, padx=6, pady=10, sticky='e')
inputProblemasDigestivos = ttk.Combobox(frameFormulario, values=["Si", "No"])
inputProblemasDigestivos.grid(row=3, column=3, padx=6, pady=10, sticky='w')

tk.Label(frameFormulario, text="Tension Alta").grid(row=3, column=4, padx=6, pady=10, sticky='e')
inputTensionAlta = ttk.Combobox(frameFormulario, values=["Si", "No", "No lo se"])
inputTensionAlta.grid(row=3, column=5, padx=6, pady=10, sticky='w')

tk.Label(frameFormulario, text="Dolor de Cabeza").grid(row=3, column=6, padx=6, pady=10, sticky='e')
inputDolorCabeza = ttk.Combobox(frameFormulario, values=["Nunca", "Alguna vez", "Muy a menudo"])
inputDolorCabeza.grid(row=3, column=7, padx=6, pady=10, sticky='w')

# Crear un Frame para los botones
frameBotones = tk.Frame(framePrincipal, bg="DarkCyan", padx=10, pady=10)
frameBotones.pack(side=tk.TOP, fill=tk.X, padx=268, pady=10)

# Botones para las acciones

# Boton para crear un registro
btnCrear = tk.Button(frameBotones, text="Crear Registro", command=lambda: crear_registro(
    inputSexo.get(), inputEdad.get(), inputBebidasSemana.get(), inputCervezasSemana.get(),
    inputBebidasFinSemana.get(), inputBebidasDestiladasSemana.get(), inputVinosSemana.get(),
    inputPerdidasControl.get(), inputDiversionDependenciaAlcohol.get(),
    inputProblemasDigestivos.get(), inputTensionAlta.get(), inputDolorCabeza.get()
))
btnCrear.grid(row=0, column=3, padx=5, pady=10)

# Boton para editar un registro
btnEditar = tk.Button(frameBotones, text="Editar Registro", command=lambda: editar_registro(
    tree,  # Pasa la tabla tree como primer argumento
    inputSexo.get(), inputEdad.get(), inputBebidasSemana.get(), inputCervezasSemana.get(),
    inputBebidasFinSemana.get(), inputBebidasDestiladasSemana.get(), inputVinosSemana.get(),
    inputPerdidasControl.get(), inputDiversionDependenciaAlcohol.get(),
    inputProblemasDigestivos.get(), inputTensionAlta.get(), inputDolorCabeza.get()  # Pasa todos los valores
))
btnEditar.grid(row=0, column=4, padx=5, pady=10)

# Boton para eliminar un registro
btnEliminar = tk.Button(frameBotones, text="Eliminar Registro", command=lambda: eliminar_registro(tree))
btnEliminar.grid(row=0, column=5, padx=5, pady=10)

# Boton para consultar los registros usando los filtros
btnConsultar = tk.Button(frameBotones, text="Consultar",
                         command=lambda: consultarPoblacion(inputSexo, inputEdad, inputBebidasSemana,
                                                            inputCervezasSemana, inputBebidasFinSemana,
                                                            inputBebidasDestiladasSemana, inputVinosSemana,
                                                            inputPerdidasControl, inputDiversionDependenciaAlcohol,
                                                            inputProblemasDigestivos, inputTensionAlta,
                                                            inputDolorCabeza, tree))
btnConsultar.grid(row=0, column=6, padx=5, pady=10)

# Boton para exportar a Excel
buttonExportar = tk.Button(frameBotones, text="Exportar a Excel", command=lambda: exportarExcel(tree))
buttonExportar.grid(row=0, column=7, padx=5, pady=10)

# Boton para generar el grafico de barras
btn_grafico_barras = tk.Button(frameBotones, text="Generar Grafico de Barras",
                               command=lambda: generarGraficoBarras(tree))
btn_grafico_barras.grid(row=0, column=8, padx=5, pady=10)

# Boton para generar el grafico circular
btn_grafico_circular = tk.Button(frameBotones, text="Generar Grafico Circular",
                                 command=lambda: generar_grafico_circular(tree))
btn_grafico_circular.grid(row=0, column=9, padx=5, pady=10)

# Creando un marco para el arbol de valores
frameTree = tk.Frame(framePrincipal, bg="white", padx=10, pady=10, bd=2, relief="groove")
frameTree.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# arbol para mostrar los resultados de la consulta
tree = ttk.Treeview(frameTree, columns=("ID", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana",
                                        "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl",
                                        "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta",
                                        "DolorCabeza"), show="headings")

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configurar las columnas del Treeview
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=90, stretch=tk.YES)

# Crear barras de desplazamiento
scrollbarY = tk.Scrollbar(frameTree, orient="vertical", command=tree.yview)
scrollbarY.pack(side=tk.RIGHT, fill=tk.Y)

# Asociar los Scrollbars al Treeview
tree.config(yscrollcommand=scrollbarY.set)

# Iniciar el programa
iniciar_programa()
ventana.mainloop()

"""
Sistema Aurelion - Análisis de Kiosko
Programa para navegar interactivamente por la documentación del proyecto
"""

import os
import sys


def leer_documentacion():
    """Lee el archivo Documentación.md y retorna su contenido"""
    try:
        with open('Documentación.md', 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'Documentación.md'")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


def mostrar_menu():
    """Muestra el menú principal de opciones"""
    print("\n" + "="*50)
    print("    SISTEMA AURELION - ANÁLISIS DE KIOSKO")
    print("="*50)
    print("1. Ver Tema")
    print("2. Ver Problema")
    print("3. Ver Solución")
    print("4. Ver Base de Datos")
    print("5. Ver Pseudocódigo")
    print("6. Ver Diagrama")
    print("7. Ver Todo")
    print("0. Salir")
    print("-"*50)


def extraer_seccion(contenido, titulo_seccion):
    """Extrae una sección específica del contenido markdown"""
    if not contenido:
        return "No se pudo cargar el contenido"
    
    lineas = contenido.split('\n')
    seccion_encontrada = []
    capturando = False
    
    for linea in lineas:
        # Buscar el inicio de la sección
        if titulo_seccion.lower() in linea.lower() and linea.startswith('#'):
            capturando = True
            seccion_encontrada.append(linea)
            continue
        
        # Si encontramos otra sección principal, parar
        if capturando and linea.startswith('##') and titulo_seccion.lower() not in linea.lower():
            break
            
        # Si estamos capturando, agregar la línea
        if capturando:
            seccion_encontrada.append(linea)
    
    if seccion_encontrada:
        return '\n'.join(seccion_encontrada)
    else:
        return f"No se encontró la sección '{titulo_seccion}'"


def mostrar_tema():
    """Muestra la sección Tema del proyecto"""
    contenido = leer_documentacion()
    seccion = extraer_seccion(contenido, "Tema")
    
    print("\n" + "="*50)
    print("           TEMA DEL PROYECTO")
    print("="*50)
    print(seccion)
    print("-"*50)


def mostrar_problema():
    """Muestra la sección Problema"""
    contenido = leer_documentacion()
    seccion = extraer_seccion(contenido, "Problema")
    
    print("\n" + "="*50)
    print("         PROBLEMAS IDENTIFICADOS")
    print("="*50)
    print(seccion)
    print("-"*50)


def mostrar_solucion():
    """Muestra la sección Solución Propuesta"""
    contenido = leer_documentacion()
    seccion = extraer_seccion(contenido, "Solución Propuesta")
    
    print("\n" + "="*50)
    print("         SOLUCIÓN PROPUESTA")
    print("="*50)
    print(seccion)
    print("-"*50)


def mostrar_base_datos():
    """Muestra la sección Base de Datos Actual"""
    contenido = leer_documentacion()
    seccion = extraer_seccion(contenido, "Base de Datos Actual")
    
    print("\n" + "="*50)
    print("       BASE DE DATOS ACTUAL")
    print("="*50)
    print(seccion)
    print("-"*50)


def mostrar_pseudocodigo():
    """Muestra la sección Pseudocódigo"""
    contenido = leer_documentacion()
    seccion = extraer_seccion(contenido, "Pseudocódigo")
    
    print("\n" + "="*50)
    print("           PSEUDOCÓDIGO")
    print("="*50)
    print(seccion)
    print("-"*50)


def mostrar_diagrama():
    """Muestra la sección Diagrama del flujo"""
    contenido = leer_documentacion()
    seccion = extraer_seccion(contenido, "Diagrama del flujo")
    
    print("\n" + "="*50)
    print("         DIAGRAMA DE FLUJO")
    print("="*50)
    print(seccion)
    print("-"*50)


def mostrar_documentacion_completa():
    """Muestra toda la documentación"""
    contenido = leer_documentacion()
    
    if contenido:
        print("\n" + "="*50)
        print("       DOCUMENTACIÓN COMPLETA")
        print("="*50)
        print(contenido)
        print("-"*50)
    else:
        print("No se pudo cargar la documentación completa")


def validar_opcion():
    """Valida la entrada del usuario"""
    while True:
        try:
            opcion = input("Seleccione una opción (0-7): ").strip()
            if opcion in ['0', '1', '2', '3', '4', '5', '6', '7']:
                return int(opcion)
            else:
                print("Error: Ingrese un número del 0 al 7")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario")
            sys.exit(0)
        except Exception:
            print("Error: Ingrese un número válido")


def main():
    """Función principal del programa"""
    print("Bienvenido al Sistema Aurelion")
    print("Cargando documentación...")
    
    # Verificar que existe el archivo de documentación
    if not os.path.exists('Documentación.md'):
        print("Error: No se encontró el archivo 'Documentación.md' en el directorio actual")
        print("Asegúrese de ejecutar el programa desde el directorio correcto")
        return
    
    while True:
        mostrar_menu()
        opcion = validar_opcion()
        
        if opcion == 1:
            mostrar_tema()
        elif opcion == 2:
            mostrar_problema()
        elif opcion == 3:
            mostrar_solucion()
        elif opcion == 4:
            mostrar_base_datos()
        elif opcion == 5:
            mostrar_pseudocodigo()
        elif opcion == 6:
            mostrar_diagrama()
        elif opcion == 7:
            mostrar_documentacion_completa()
        elif opcion == 0:
            print("\n¡Gracias por usar el Sistema Aurelion!")
            print("Programa finalizado.")
            break
        
        # Pausa para que el usuario pueda leer
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()

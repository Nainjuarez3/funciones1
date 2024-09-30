import streamlit as st

def saludar(nombre):
    return f"hola {nombre}"

def sumar(n1:float, n2:float)->float:
    return n1 + n2

def calcular_area_triangulo(altura, base):
    return altura * base * 0.5

def calcular_precio_final(precio_or):
    descuento_20 = precio_or * 0.20
    imp_16 = (precio_or-descuento_20) * 0.16
    return (precio_or - descuento_20) + imp_16

def sumar_lista(numeros):
    return sum(numeros)

def producto(name_prod, cantidad, precio_u):
    return f"El monto a pagar por {cantidad} {name_prod} es {precio_u * cantidad}"

def numeros_pares_e_impares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def informacion_personal(**kwargs):
    return "\n".join([f"{clave}: {valor}" for clave, valor in kwargs.items()])

def calculadora_flexible(a, b, operacion="suma"):
    match operacion:
        case "suma":
            return a + b
        case "resta":
            return a - b
        case "multiplicacion":
            return a * b
        case "division":
            return a / b if b != 0 else "no se puede dividir por 0"
        case _:
            return "operacion no valida"

def main():
    st.title("TABLERO INTERACTIVO")

    opcion = st.sidebar.selectbox("SELECCIONA UNA FUNCION", [
        "saludo", "suma", "area de un triangulo", "calculadora de descuento",
        "suma de lista", "costo de un producto", "numeros pares e impares", 
        "multiplicacion con *args", "informacion personal con **kwargs", "calculadora flexible"
    ])

    match opcion:
        case "saludo":
            nombre = st.text_input("INTRODUCE TU NOMBRE:")
            if st.button("Saludar"):
                st.write(saludar(nombre))

        case "suma":
            n1 = st.number_input("NUMERO 1:", step=1.0)
            n2 = st.number_input("NUMERO 2:", step=1.0)
            if st.button("Sumar"):
                st.write(f"la suma es: {sumar(n1, n2)}")

        case "area de un triangulo":
            base = st.number_input("base del triangulo:", step=1.0)
            altura = st.number_input("altura del triangulo:", step=1.0)
            if st.button("calcular area"):
                st.write(f"el area del triangulo es: {calcular_area_triangulo(altura, base)}")

        case "calculadora de descuento":
            precio_or = st.number_input("Precio Original:", step=1.0)
            if st.button("calcular precio final"):
                st.write(f"el precio final es: {calcular_precio_final(precio_or)}")

        case "suma de lista":
            numeros = st.text_input("introduce los numeros separados por comas:")
            lista_numeros = [int(num) for num in numeros.split(",") if num.isdigit()]
            if st.button("sumar lista"):
                st.write(f"la suma es: {sumar_lista(lista_numeros)}")

        case "costo de un producto":
            name_prod = st.text_input("nombre del producto:")
            cantidad = st.number_input("cantidad:", step=1)
            precio_u = st.number_input("precio por unidad:", step=1.0)
            if st.button("Calcular Total"):
                st.write(producto(name_prod, cantidad, precio_u))

        case "numeros pares e impares":
            numeros = st.text_input("Introduce los numeros separados por comas:")
            lista_numeros = [int(num) for num in numeros.split(",") if num.isdigit()]
            if st.button("SEPARAR"):
                pares, impares = numeros_pares_e_impares(lista_numeros)
                st.write(f"PARES: {pares}")
                st.write(f"IMPARES: {impares}")

        case "Multiplicacion con *args":
            numeros = st.text_input("introduce los numeros separados por comas:")
            lista_numeros = [int(num) for num in numeros.split(",") if num.isdigit()]
            if st.button("MULTIPLICAR"):
                st.write(f"RESULTADO: {multiplicar_todos(*lista_numeros)}")

        case "informacion personal con **kwargs":
            nombre = st.text_input("NOMBRE:")
            edad = st.number_input("EDAD:", step=1)
            direccion = st.text_input("DIRECCION:")
            if st.button("MOSTRAR INFORMACION"):
                st.write(informacion_personal(nombre=nombre, edad=edad, direccion=direccion))

        case "calculadora flexible":
            num1 = st.number_input("NUMERO 1:", step=1.0)
            num2 = st.number_input("NUMERO 2:", step=1.0)
            operacion = st.selectbox("OPERACION", ["suma", "resta", "multiplicacion", "division"])
            if st.button("CALCULAR"):
                st.write(f"resultado: {calculadora_flexible(num1, num2, operacion)}")

if __name__ == "__main__":
    main()

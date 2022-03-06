from db import obtenerVacunados
from pathlib import Path
import webbrowser

def exportarAHTML():
    vacunados = obtenerVacunados()

    html = open("./vacunados.html", "w", encoding="utf-8")
    cuerpo_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vacunados</title>
    <style>
        table {
            border: 1px solid black;
        }
        td {
            padding: 20px;
            text-align: center;
            border: 1px solid gray;
        }
    </style>
</head>
<body>

    <h1>Informe de personas vacunadas</h1>
    
    <table>
        <thead>
            <th>Cedula</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Telefono</th>
            <th>Fecha de nacimiento</th>
            <th>Dosis</th>
            <th>Provincia</th>
            <th>Registro</th>
        </thead>
        <tbody>"""

    for vacunado in vacunados:
        cuerpo_html += f"""
        <tr>
            <td>{ vacunado["cedula"] }</td>
            <td>{ vacunado["nombre"] }</td>
            <td>{ vacunado["apellido"] }</td>
            <td>{ vacunado["telefono"] }</td>
            <td>{ vacunado["fechaNacimiento"] }</td>
            <td>"""

        for dosis in vacunado["dosis"]:
            cuerpo_html += f"""
            <ul>
                <li>{ dosis["tipoVacuna"] } - { dosis["fecha"] }</li>
            </ul>
            """

        cuerpo_html += f"""</td>
            <td>{ vacunado["provincia"] }</td>
            <td>{ vacunado["fechaRegistro"] }</td>
        </tr>
        """

    cuerpo_html += """</tbody>
    </table>
</body>
</html>
    """

    html.write(cuerpo_html)
    html.close()

    archivo_html = f"file:///{ Path().resolve() }/vacunados.html"
    webbrowser.open(archivo_html)
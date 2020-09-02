import json
import webbrowser

with open('Datos.json') as f:
    data = json.load(f)


html = open('ReportedeInformación.html', 'w')
html.write('<html>')
html.write('    <head>')
html.write('        <title>Reporte de Empleados</title>')
html.write('        <style>')
html.write('            *{')
html.write('                background-color: #02AC66;')
html.write('                color: #ececec;')
html.write('              }')
html.write('        </style>')
html.write('    </head>')
html.write('    <body>')
html.write('        <center>')
html.write('            <h1>Reporte de Empleados</h1>')

for i in range(len(data)):
    html.write('            <h2><b>Nombre: '+data[i].get("nombre")+" Edad: "+data[i].get("edad")+" Activo: "+data[i].get("activo")+" Saldo: "+data[i].get("saldo")+'</b></h2>')

html.write('        </center>')
html.write('    </body>')
html.write('</html>')
html.close()

webbrowser.open_new_tab('ReportedeInformación.html')
import requests
from bs4 import BeautifulSoup
URL = "http://rpu.edu.pe/miembros-rpu/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="listado-miembros")
ListaMiembros = results.find_all("div", class_="listaMiembros-popupCoordinador")
for Miembro in ListaMiembros:
    universidad = Miembro.find("h3", class_="listaMiembros-popupText")
    titulo = Miembro.find(class_="listaMiembros-popupSubTitulo")
    nombre = Miembro.find("p")
    correo = Miembro.find(class_="listaMiembros-popupInfo listaMiembros-popupCorreo")
    #print(universidad.text.strip())
    print(titulo.text.strip())
    print(nombre.text.strip())
    print(correo.text.strip())
    print()

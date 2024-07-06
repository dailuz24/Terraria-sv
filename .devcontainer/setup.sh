#!/bin/bash

# Actualizar y instalar dependencias
sudo apt-get update
sudo apt-get install -y wget unzip

# Descargar la última versión de TShock
wget $(curl -s https://api.github.com/repos/Pryaxis/TShock/releases/latest | grep browser_download_url | grep linux | cut -d '"' -f 4) -O tshock.zip
unzip tshock.zip -d tshock
rm tshock.zip

# Hacer que los archivos del servidor sean ejecutables
chmod +x tshock/TerrariaServer*

# Imprimir mensaje de finalización
echo "TShock se ha descargado e instalado en el directorio 'tshock'."

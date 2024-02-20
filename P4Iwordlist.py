
#!Creador de WORDLISTS - P4Iwordlist.py -  By P4IM0N

#?----------------------------------------------------------------------------------------------------------
#REQUERIMIENTOS DE INSTALACION

#pip install random-word
#pip install mtranslate
#pip install tqdm 
#pip install requests
#pip install beautifulsoup4

#?----------------------------------------------------------------------------------------------------------
#IMPORTAMOS LIBRERIAS

import random

from random_word import RandomWords

from mtranslate import translate

from tqdm import tqdm

import requests

from bs4 import BeautifulSoup

import re 


#?----------------------------------------------------------------------------------------------------------                    
#COLORES ANSI WORDLIST

color_rojo = '\033[31m'
color_amarillo = '\033[33m'
color_azul = '\033[34m'
color_magenta = '\033[35m'
reset_formato = '\033[0m'

#COLORES ANSI EXTRACTOR WEB
color_purpura = '\033[95m'  
color_rojoso = '\033[91m'  
color_rosa_electrico = '\033[95m' 
reset = '\033[0m'

#?----------------------------------------------------------------------------------------------------------                    
#BANNER:

banner = f'''

__________  _____ .___                        .___.__  .__          __   
{color_magenta}\______   \/  |  ||   |_  _  _____________  __| _/|  | |__| _______/  |_ 
 |     ___/   |  ||   \ \/ \/ /  _ \_  __ \/ __ | |  | |  |/  ___/\   __|
 |    |  /    ^   /   |\     (  <_> )  | \/ /_/ | |  |_|  |\___ \  |  |  
 |____|  \____   ||___| \/\_/ \____/|__|  \____ | |____/__/____  > |__|  
              |__|                             \/              \/ {reset_formato}       
{color_rojo}By P4IM0N{reset_formato}'''

print(banner)


#?---------------------------------------------------------------------------------------------
#FUNCION PRINCIPAL QUE MANEJA EL PROGRAMA DE EXTRACCION DE PALABRAS CLAVES DE LAS URL APORTADAS
def main():
    
    #---------------------------------------------------------------------------------------------
    #?BANNER
    banner= f'''{color_rosa_electrico}

    __________  _____ .___                 __                                    ___.                                     .__                
    \______   \/  |  ||   | ____   _______/  |_____________    ______  _  __ ____\_ |__   ______ ________________  ______ |__| ____    ____  
    |     ___/   |  ||   |/ __ \ /  ___/\   __\_  __ \__  \ _/ ___\ \/ \/ // __ \| __ \ /  ___// ___\_  __ \__  \ \____ \|  |/    \  / ___\ 
    |    |  /    ^   /   \  ___/ \___ \  |  |  |  | \// __ \  \___\     /\  ___/| \_\ \___  \  \___|  | \// __ \|  |_> >  |   |  \/ /_/  >
    |____|  \____   ||___|\___  >____  > |__|  |__|  (____  /\___  >\/\_/  \___  >___  /____  >\___  >__|  (____  /   __/|__|___|  /\___  / 
                |__|         \/     \/                   \/     \/            \/    \/     \/     \/           \/|__|           \//_____/  
    {reset}{color_rojoso}By P4IM0N{reset}'''
    print(banner)
    
    print(f'{color_purpura}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{reset}')
    urls = input('Manito ingresa una o varias url de sitios objetivos para obtener posibles palbras claves para la generacion de la WORDLIST (si desas podes pasar varias url EJ:url,url,url):').split(',')
    
    for url in urls:
        
        palabras = extraer_palabras(url)   
        
        print(f'{color_purpura}*************************************************************************************************************{reset}')
        print(f'{color_rosa_electrico}SE AGREGARON A LA LISTA PARA LA WORDLIST, Y ESTAS SON LAS PALABRAS EXTRAIDAS MANITO de LA URL:{reset} \n {color_purpura}{url}{reset}')  
        print(palabras)
        print(f'{color_purpura}*************************************************************************************************************{reset}')
    
    return palabras


#---------------------------------------------------------------------------------------------
#FUNCION QUE EXTRAE LAS POSIBLES PALABRAS CLAVES DE LA WEB PARA LA WORDLIST
def extraer_palabras(url):
    
    palabras_no_deseadas = {
    'result', 'false', 'hash', 'null', 'areas', 'static', 'type', 'Filtros', 
    'center', 'keyframes', 'http', 'https', 'busca', 'busqueda', 'blog', 
    'arrow', 'default', 'format', 'filter', 'div', 'span', ' static ', ' type ', 
    'class_type', 'subtype', 'truetype', 'opentype', 'class', 'truetype', 'true',  
    'html', 'head', 'title', 'meta', 'link', 'body', 'script', 'style', 'div', 
    'span', 'form', 'input', 'button', 'select', 'option', 'textarea', 'label', 
    'img', 'a', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'table', 
    'tr', 'td', 'th', 'thead', 'tbody', 'tfoot', 'iframe', 'nav', 'header', 'footer', 
    'section', 'article', 'aside', 'main', 'video', 'audio', 'canvas', 'svg', 'map', 
    'fieldset', 'legend', 'caption', 'abbr', 'address', 'b', 'bdi', 'bdo', 'cite', 
    'code', 'data', 'dfn', 'em', 'i', 'kbd', 'mark', 'q', 'rp', 'rt', 'rtc', 'ruby', 
    's', 'samp', 'small', 'strong', 'sub', 'sup', 'time', 'u', 'var', 'wbr', 'area', 
    'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 
    'track', 'wbr', 'abbr', 'accept', 'accept-charset', 'accesskey', 'action', 'align', 
    'alt', 'async', 'autocomplete', 'autofocus', 'autoplay', 'autosave', 'bgcolor', 'border', 
    'buffered', 'challenge', 'charset', 'checked', 'cite', 'class', 'codebase', 'color', 
    'cols', 'colspan', 'content', 'contenteditable', 'contextmenu', 'controls', 'coords', 
    'data', 'datetime', 'default', 'defer', 'dir', 'dirname', 'disabled', 'download', 
    'draggable', 'dropzone', 'enctype', 'for', 'form', 'formaction', 'headers', 'height', 
    'hidden', 'high', 'href', 'hreflang', 'http-equiv', 'icon', 'id', 'ismap', 'itemprop', 
    'keytype', 'kind', 'label', 'lang', 'language', 'list', 'loop', 'low', 'manifest', 
    'max', 'maxlength', 'media', 'method', 'min', 'multiple', 'muted', 'name', 'novalidate', 
    'open', 'optimum', 'pattern', 'ping', 'placeholder', 'poster', 'preload', 'radiogroup', 
    'readonly', 'rel', 'required', 'reversed', 'rows', 'rowspan', 'sandbox', 'scope', 
    'scoped', 'seamless', 'selected', 'shape', 'size', 'sizes', 'span', 'spellcheck', 
    'src', 'srcdoc', 'srclang', 'srcset', 'start', 'step', 'style', 'summary', 'tabindex', 
    'target', 'title', 'type', 'usemap', 'value', 'width', 'wrap',
    'doctype', 'xmlns:xlink', 'xmlns:xhtml', 'xmlns:math', 'xmlns:x',

    }
    
    patron_px = re.compile(r'\d+px$', re.IGNORECASE)
    
    palabras = set()
    
    encabezado_user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=encabezado_user_agent)
    
    if response.status_code == 200:
        
        html = response.content
        
        soup = BeautifulSoup(html, 'html5lib')
        
        #? Eliminamos las etiquetas de script y estilo 
        for script in soup(["script", "style"]):
            script.extract()

        #? Extraemos solo el texto visible
        textos = soup.stripped_strings
        
        for texto in textos:
            
            palabras.update(re.findall(r'\b[a-zA-Z]{4,10}\b', texto))
            
            palabras.update(re.findall(r'\b\d{1,4}\b', texto))
    
    palabras_filtradas = [palabra for palabra in palabras if palabra not in palabras_no_deseadas and not patron_px.match(palabra)]        
            
    return palabras_filtradas



#?----------------------------------------------------------------------------------------------------------                    
#FUNCION QUE COMBINA TODAS LOS ELEMENTOS Y GUARDA EN EL ARCHIVO WORDLISTS

lista_de_palabras_ya_combinadas = []
lista_de_palabras_ya_combinadas_de_forma_aleatoria = []


def combinar_palabras_para_passwd(lista_palabras_principaless,lista_palabras_secundariass,lista_numeros_sospechososs,lista_de_palabras_randomm,lista_de_numeros_radomm,cantidad_de_palabras_combinadass):
    
    contador = 0
    llave_cantidad_de_combinaciones = True
    
    #?INICIO DE CONTEO DE BARRA DE PROGRESO
    with tqdm(total=cantidad_de_palabras_combinadass) as barra_progreso:
        
        while llave_cantidad_de_combinaciones:
            contador += 1  
            try:
                
                #?MANEJO DE PALABRAS AL AZAR PARA UNA COMBINACION BASICA ESTRUCTURADA DE LAS PALABRAS PASWORD
                
                palabra_principal_azar = random.choice(lista_palabras_principaless)if lista_palabras_principaless else ''
                palabras_secundarias_azar = random.choice(lista_palabras_secundariass)if lista_palabras_secundariass else ''
                numeros_sospechosos_azar = random.choice(lista_numeros_sospechososs)if lista_numeros_sospechososs else ''
                palabras_random_azar = random.choice(lista_de_palabras_randomm)if lista_de_palabras_randomm else ''
                numeros_random_azar = random.choice(lista_de_numeros_radomm)if lista_de_numeros_radomm else ''
                
                #?PALABRA PASSWORD COMBINADA DE FORMA ESTRUCTURADA
                
                palabra_ya_combinada = palabra_principal_azar+palabras_secundarias_azar+numeros_sospechosos_azar+palabras_random_azar+str(numeros_random_azar)
                
                #?MANEJO DE LISTAS AL AZAR Y PALABRAS AL AZAR PARA UNA COMBINACION DE PALABRA PASSWORD ALEATORIA
                
                lista_para_combinar_al_azar_1 = random.choice([lista_palabras_principaless,lista_palabras_secundariass,lista_numeros_sospechososs,lista_de_palabras_randomm,lista_de_numeros_radomm]) if lista_palabras_principaless or lista_palabras_secundariass or lista_numeros_sospechososs or lista_de_palabras_randomm or lista_de_numeros_radomm else ''
                lista_para_combinar_al_azar_2 = random.choice([lista_palabras_principaless,lista_palabras_secundariass,lista_numeros_sospechososs,lista_de_palabras_randomm,lista_de_numeros_radomm]) if lista_palabras_principaless or lista_palabras_secundariass or lista_numeros_sospechososs or lista_de_palabras_randomm or lista_de_numeros_radomm else ''
                lista_para_combinar_al_azar_3 = random.choice([lista_palabras_principaless,lista_palabras_secundariass,lista_numeros_sospechososs,lista_de_palabras_randomm,lista_de_numeros_radomm]) if lista_palabras_principaless or lista_palabras_secundariass or lista_numeros_sospechososs or lista_de_palabras_randomm or lista_de_numeros_radomm else ''
                lista_para_combinar_al_azar_4 = random.choice([lista_palabras_principaless,lista_palabras_secundariass,lista_numeros_sospechososs,lista_de_palabras_randomm,lista_de_numeros_radomm]) if lista_palabras_principaless or lista_palabras_secundariass or lista_numeros_sospechososs or lista_de_palabras_randomm or lista_de_numeros_radomm else ''
                lista_para_combinar_al_azar_5 = random.choice([lista_palabras_principaless,lista_palabras_secundariass,lista_numeros_sospechososs,lista_de_palabras_randomm,lista_de_numeros_radomm]) if lista_palabras_principaless or lista_palabras_secundariass or lista_numeros_sospechososs or lista_de_palabras_randomm or lista_de_numeros_radomm else ''
                
                palabra_para_combinar_al_azar_1 = random.choice(lista_para_combinar_al_azar_1) if lista_para_combinar_al_azar_1 else ''
                palabra_para_combinar_al_azar_2 = random.choice(lista_para_combinar_al_azar_2) if lista_para_combinar_al_azar_2 else ''
                palabra_para_combinar_al_azar_3 = random.choice(lista_para_combinar_al_azar_3) if lista_para_combinar_al_azar_3 else ''
                palabra_para_combinar_al_azar_4 = random.choice(lista_para_combinar_al_azar_4) if lista_para_combinar_al_azar_4 else ''
                palabra_para_combinar_al_azar_5 = random.choice(lista_para_combinar_al_azar_5) if lista_para_combinar_al_azar_5 else ''
                
                #?PALABRA PASSWORD COMBINADA DE FORMA ALEATORIA
                
                palabra_ya_combinada_al_azar = str(palabra_para_combinar_al_azar_1)+str(palabra_para_combinar_al_azar_2)+str(palabra_para_combinar_al_azar_3)+str(palabra_para_combinar_al_azar_4)+str(palabra_para_combinar_al_azar_5)
                
                #?AGREGAMOS CADA PALABRA PASSWD DE COMBINACION ESTRUCTURADA Y LAS ALEATORIAS A SUS RESPECTIVAS LISTAS
                
                lista_de_palabras_ya_combinadas.extend(palabra_ya_combinada.split(','))
                lista_de_palabras_ya_combinadas_de_forma_aleatoria.extend(palabra_ya_combinada_al_azar.split(','))
                
                #?ACTUALIZANDO LA BARRA DE PROGRESO
                barra_progreso.update(6)
                
                #?CONDICIONAL PARA EL CONTADOR DE PASSWORD SOLICITADOS Y DETENER EL LOOP
                
                if contador == int(cantidad_de_palabras_combinadass/6):
                    llave_cantidad_de_combinaciones = False
            
            except IndexError:
                continue       
    
    with open(opcion_nombre_de_archivo, 'w') as archivo_passwd:
                for passwd_1, passwd_2 in zip(lista_de_palabras_ya_combinadas,lista_de_palabras_ya_combinadas_de_forma_aleatoria):
                    
                    #?AGREGAMOS AL ARCHIVO LAS COMBINACIONES ESTRUCTURADAS CON SUS DISTINTAS MODIFICACIONES
                    archivo_passwd.write(passwd_1+'\n')
                    archivo_passwd.write(passwd_1.replace('a', '4').replace('o', '0').replace('e', '3').replace('i', '1').replace('s', '$').replace('&', '&').replace('l', '!').replace('x', '*') + '\n')                
                    archivo_passwd.write(passwd_1.capitalize()+'\n')
                    
                    #?AGREGAMOS AL ARCHIVO LAS COMBINACIONES ALEATORIAS CON SUS DISTINTAS MODIFICACIONES
                    archivo_passwd.write(passwd_2+'\n')
                    archivo_passwd.write(passwd_2.replace('a', '4').replace('o', '0').replace('e', '3').replace('i', '1').replace('s', '$').replace('&', '&').replace('l', '!').replace('x', '*') + '\n')                
                    archivo_passwd.write(passwd_2.capitalize()+'\n')
                
                archivo_passwd.close()
    
    print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
    print(f'{color_azul}---------------------FINALIZADO Y GUARDADO MANITO-------------------------------------{reset_formato}')
    print(f'''{color_magenta}
                                                          _nnnn_                      
                                                         dGGGGMMb     ,"""""""""""""""""""".
                                                        @p~qp~~qMb    | {reset_formato}{color_azul}TERMINAMOS MANITO!{reset_formato}{color_magenta} |
                                                        M|{reset_formato}{color_rojo}@{reset_formato}{color_magenta}||{reset_formato}{color_rojo}@{reset_formato}{color_magenta}) M|   _;....................'
                                                        @,----.JM| -'
                                                       JS^{reset_formato}{color_rojo}\__/{reset_formato}{color_magenta}  qKL
                                                      dZP        qKRb
                                                     dZP          qKKb
                                                    fZP            SMMb
                                                    HZM            MMMM
                                                    FqM            MMMM
                                                  __| ".        |\dS"qML
                                                  |    `.       | `' \Zq
                                                 _)      \.___.,|     .'
                                                 \____   )XXXXXX|   .'
                                                      `-'       `--' {reset_formato}{color_rojo}By P4IM0N{reset_formato}''')       
        



#?----------------------------------------------------------------------------------------------------------
#INICIO DE INSTANCIA PARA PALABRAS RANDOM

generador_de_palabras_random = RandomWords()


#?----------------------------------------------------------------------------------------------------------
#MAYORIA DE LISTAS DE CADA ELEMENTO A COMBINAR

lista_palabras_principales = []

lista_palabras_secundarias = []

lista_numeros_sospechosos = []

lista_de_palabras_random = []

lista_de_numeros_radom = []


#?----------------------------------------------------------------------------------------------------------
#AGREGADO DE ELEMENTOS A LAS LISTAS SIN COMA

print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')

palabras_principales = input(f'{color_azul}Dame las palabras principales que sospechas tenga tu objetivo manito: (puedes pasar varias solo separadas por coma Ej: perro,gato,loro){reset_formato}')

lista_palabras_principales.extend(palabras_principales.split(','))


print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')

palabras_secundaria = input(f'{color_azul}Dame las palabras secundarias que sospechas tenga tu objetivo manito: (puedes pasar varias solo separadas por coma Ej: perro,gato,loro){reset_formato}')

lista_palabras_secundarias.extend(palabras_secundaria.split(','))


print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')

numeros_sospechoso = input(f'{color_azul}Dame los numeros sospechosos que deseas agregar manito (puedes pasar varias solo separadas por coma Ej: 2019,1234,2030){reset_formato}')

lista_numeros_sospechosos.extend(numeros_sospechoso.split(','))

print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')


#?----------------------------------------------------------------------------------------------------------
#LOOP PARA EL MENU DE OPCIONES Y GESTION DEL SCRIPT


finalizar = True

if palabras_principales or palabras_secundaria or numeros_sospechoso:
    while finalizar:
        print(f'''{color_azul}--------------------------------------------------------------------------------------------
            //////////////////{reset_formato}{color_rojo}SELECCIONA UNA OPCION{reset_formato}{color_azul}//////////////////////////////////////////////////////////
            -------------------------------------------------------------------------------------------------
            | {reset_formato}{color_rojo}1{reset_formato}{color_azul} - Queres que agreguemos palabras aleatorias?:                                               |
            | {reset_formato}{color_rojo}2{reset_formato}{color_azul} - Quieres que creemos numeros random para agregar a la union de tus primeras palabras?      |
            | {reset_formato}{color_rojo}3{reset_formato}{color_azul} - Darme el nombre de como quieres nombrar a tu archivo.txt?                                |
            | {reset_formato}{color_rojo}4{reset_formato}{color_azul} - generar WORDLISTS YA...!!!                                                                |
            | {reset_formato}{color_rojo}5{reset_formato}{color_azul} - Manito queres extraer posibles palabras de url objetivo para agregarla a la WORDLISTS ?   |
            | {reset_formato}{color_rojo}6{reset_formato}{color_azul} - SALIR :(                                                                                  |--> {reset_formato}''') 
        print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
        
        opcion_elejida = input(f'{color_azul}Eleji una opcion manito?:{reset_formato}')
        
        print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')

#?----------------------------------------------------------------------------------------------------------
#CREA LAS PALABRAS RANDOM
        
        if opcion_elejida == '1':
            opcion_idioma = input(f'''{color_azul}
            | En que idiomas quieres estas palabras aleatorias agregadas?:                                  |
            |     +INGLES= por defecto en blanco , +ESPAÑOL= es , +Italiano= it ,  +frances= fr             |
            |     +PORTUGUES-BRASIL= pt-BR , +ALEMAN= de                                                    |-->{reset_formato} ''')
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            opcion_cantidad_palabras_random = int(input(f'''{color_azul}
            | Cuantas de estas palabras quieres que agreguemos? (resp. cantidad en numero)                  |-->{reset_formato} '''))
            
            contador = 0
            llave_loop_genera_palabras_aleatorias = True
            
            
            while llave_loop_genera_palabras_aleatorias:
                 
                if opcion_idioma:
                    contador += 1
                    palabra_random = generador_de_palabras_random.get_random_word()
                    palabra_traducida = translate(palabra_random, opcion_idioma)
                    lista_de_palabras_random.append(palabra_traducida)
                    
                    if contador == opcion_cantidad_palabras_random:
                        llave_loop_genera_palabras_aleatorias = False
            
                
                else:
                    contador += 1
                    palabra_random = generador_de_palabras_random.get_random_word()
                    lista_de_palabras_random.append(palabra_random)
                    
                    if contador == opcion_cantidad_palabras_random:
                        llave_loop_genera_palabras_aleatorias = False
        
                    

#?----------------------------------------------------------------------------------------------------------          
#CREA LOS NUMEROS RANDOM

        if opcion_elejida == '2':
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            opcion_cantidad_numeros_random = int(input(f'''{color_azul}
            | Cuantos numeros random queres que agreguemos a la lista?: (resp. cantidad en numero)       |--> {reset_formato}'''))
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            
            
            contador = 0
            llave_loop_genera_numeros_aleatorias = True
            
            
            while llave_loop_genera_numeros_aleatorias:
                contador += 1
                numero_aleatorio = random.randint(1,9999)
                lista_de_numeros_radom.append(numero_aleatorio)
                
                if contador == opcion_cantidad_numeros_random:
                    llave_loop_genera_numeros_aleatorias = False 
                
                        
                    
#?----------------------------------------------------------------------------------------------------------                    
#ASIGNA EL NOMBRE DE ARCHIVO
        
        if opcion_elejida == '3':
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            opcion_nombre_de_archivo = input(f'{color_azul}Ahora dame el nombre del archivo manito: (Ej: tuhermana.txt){reset_formato}')
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            
                    
                        
#?----------------------------------------------------------------------------------------------------------                    
#EJECUTA LA CREACION DE LA WORDLISTS
        
        if opcion_elejida == '4':
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            cantidad_de_palabras_combinadas = int(input(f'{color_azul}Manito por ultimo decime cuantas palabras APROX queres que tenga la lista de combinaciones de PASSWORD?: {reset_formato}'))
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            print(f'{color_azul}Manito estamos agregando la misma cantidad de combinaciones, pero con caracteres especiales(EJ:0,4,$,@), un momento...{reset_formato}')
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            print(f'{color_azul}Manito estamos agregando la misma cantidad de combinaciones, pero ahora con mayuscula la primer letra (EJ:Perro), un momento...{reset_formato}')
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            combinar_palabras_para_passwd(lista_palabras_principales,lista_palabras_secundarias,lista_numeros_sospechosos,lista_de_palabras_random,lista_de_numeros_radom,cantidad_de_palabras_combinadas)
            
            
#?----------------------------------------------------------------------------------------------------------                    
#EJECUTA LA FUNCION MAIN PARA EXTRACCION DE PALABRAS WEB
        
        if opcion_elejida == '5':
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            palabras_extraidas_para_wordlists = main()
            
            # Eliminar comillas simples y espacios en blanco de cada palabra
            palabras_limpiadas = [palabra.replace("'", "").replace(" ", "") for palabra in palabras_extraidas_para_wordlists]
            
            lista_palabras_secundarias.extend(palabras_limpiadas)
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            
            

#?----------------------------------------------------------------------------------------------------------                    
#FINALIZA SCRIPT
        
        if opcion_elejida == '6':
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            print(f'{color_azul}Gracias manito sera hasta la proxima  :D {reset_formato}')
            print(f'{color_amarillo}-------------------------------------------------------------------------------------{reset_formato}')
            finalizar = False
            


#?----------------------------------------------------------------------------------------------------------                    

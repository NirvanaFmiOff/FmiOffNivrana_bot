Conversation with Gemini
No tengo ese es el del IMEI..ahora quiero preparar para el otro dónde voy

¡Ah, perfecto! Menos mal que lo revisamos a tiempo para no tocar el del IMEI.

Para preparar el repositorio del otro bot (el de Nirvana Infinito) y conectarlo correctamente en Render, hagamos esto paso a paso:

Crea un repositorio nuevo en GitHub:

Entra a tu cuenta de GitHub y crea un nuevo repositorio (por ejemplo, ponle de nombre nirvana-infinito-bot). Déjalo público o privado, como prefieras, pero asegúrate de que esté vacío (sin archivos previos para evitar confusiones).

Sube los dos archivos clave:

Sube el archivo main.py (con todo el código del menú, los botones de soporte para ti y para Fernando, y el detector de IMEI).

Sube el archivo requirements.txt con estas dos líneas adentro:

Plaintext
python-telegram-bot
flask
Vuelve a Render y conéctalo:

Regresa a la pantalla de Render que tienes abierta en tu captura (la de New Web Service).   
PNG

Como ya vinculaste tu GitHub, ahora debería aparecerte el nuevo repositorio que acabas de crear (nirvana-infinito-bot).

Selecciónalo y haz clic en el botón de conectar.

¿Me avisas cuando hayas creado el repositorio en GitHub y te aparezca en la lista de Render para dar el último empujón con la configuración?

Le di newweb y me envió ahí

¡Exacto! Justamente ahí estás en la pantalla para conectar tu repositorio (como se ve en la segunda captura, dice New Web Service y te muestra el buscador de GitHub).   
PNG

Como te comentaba recién, en este momento solo te aparece el repositorio del IMEI (bot-ifree). Para que aparezca el bot de Nirvana Infinito:   
PNG

Ve a tu cuenta de GitHub y crea un nuevo repositorio vacío (por ejemplo, llámalo nirvana-infinito-bot).

Sube ahí tus dos archivos: el main.py con el código actualizado de los soportes y el requirements.txt.

Vuelve a esta misma pantalla de Render, actualiza la página o usa la barra de búsqueda que dice Search para encontrar tu nuevo repositorio y seleccionarlo.   
PNG

¡Avísame en cuanto lo subas a GitHub para guiarte con los últimos botoncitos de configuración en Render!

Dónde voy o que presionó es es el codigo del que está funcionando perfecto

¡Ah, ya entiendo perfecto! Estás viendo el repositorio de GitHub de tu bot de IMEI (bot-ifree) y ahí tienes el código funcionando con telebot.   
JPG

Como este es el repositorio del otro bot, no toques este código para no alterar el del IMEI. Lo que vamos a hacer es crear un nuevo repositorio en GitHub para tu bot de Nirvana Infinito.

Sigue estos pasos rápidos en GitHub:

Crea el nuevo repositorio:

Toca el ícono del gatito de GitHub arriba a la izquierda o ve al inicio de tu perfil para crear un New repository (Repositorio nuevo).

Ponle de nombre nirvana-infinito (o el que prefieras), déjalo en modo público o privado y dale a Create repository.

Sube los archivos del bot principal:

Una vez creado el repositorio nuevo, sube los dos archivos que Render necesita:

El archivo requirements.txt

El archivo main.py (con el código completo del menú y los botones de soporte que te pasé antes).

Vuelve a Render:

Regresa a la pestaña de Render donde estabas creando el Web Service. Ahora sí te aparecerá este nuevo repositorio en la lista, lo seleccionas y terminamos de configurarlo en un minuto.

¿Me avisas en cuanto crees el repositorio nuevo en GitHub? ¡Ya casi lo tienes listo!

Ahí donde voy

¡Perfecto! Ya estás en el Dashboard principal de tu GitHub.   
JPG

Para crear el repositorio nuevo para este bot, haz lo siguiente:

Toca el botón de las tres rayitas horizontales (menú) que está arriba a la izquierda (al lado del logo de GitHub).

En el menú que se despliega, busca y selecciona la opción que dice "New repository" (o un botón con el signo +).

Ponle un nombre (por ejemplo, nirvana-infinito), déjalo público o privado y dale abajo al botón verde para crearlo.

¡Avísame en cuanto estés dentro de ese nuevo repositorio vacío para decirte cómo subir los dos archivos!

No me sale nada

¡Ya veo por qué no te aparece! Estás en la aplicación móvil de GitHub o en su versión de interfaz reducida, la cual oculta el botón directo de crear repositorios desde el menú lateral.

Para solucionarlo súper fácil sin dar tantas vueltas, haz lo siguiente:

Toca los tres puntos verticales de la esquina superior derecha de tu navegador (Google Chrome).

Marca la casilla que dice "Sitio para computador" (o Desktop site). Esto recargará la página de GitHub tal como se ve en una computadora y te mostrará el botón verde de "New" o "+" para crear el repositorio al instante.

Prueba activar esa opción de escritorio y dime si ya te deja ver el botón para crear el nuevo repositorio.

Pero antes lo hicimos con versión móvil

¡Tienes toda la razón y te pido disculpas! Si antes pudiste moverte bien sin cambiar a modo escritorio, hagámoslo directo desde ahí mismo.

Para no enredarnos con los menús de GitHub, haz esto en un segundo:

Toca en la opción "All repositories" que te sale ahí mismo en el menú desplegable que abriste en la captura.   
PNG

Una vez que estés en tu lista de repositorios, arriba a la derecha te aparecerá un botón con un signo de más (+) o un botón verde que dice New. ¡Dale clic ahí para crear tu repositorio nuevo (nirvana-infinito) y avísame cuando estés adentro!

Ahí que hago y que pongo

¡Excelente! Ya estás exactamente en la pantalla correcta para crear el nuevo repositorio.

Llena estos dos datos sencillos y déjalo como está abajo:

*Repository name : Escribe un nombre corto sin espacios, por ejemplo: nirvana-bot

Configuration: Déjalo en Public (o Private, como prefieras) y no marques ninguna de las opciones de abajo (ni README, ni gitignore, ni license).

Baja la página hasta el final, presiona el botón verde de crear y avísame para indicarte cómo subir los archivos rápidamente.

De ahí que sigo

¡Perfecto! Ya tienes creado tu nuevo repositorio llamado FmiOffNivrana_bot.   
PNG

Ahora lo único que falta es subir los dos archivos que necesitamos para que Render lo levante. Haz esto:

En la pantalla que estás viendo (la de tu repositorio vacío), busca en el cuadro azul de abajo el texto que dice "uploading an existing file" y presiónalo.   
PNG

Sube los dos archivos que tenemos listos:

El archivo main.py (con el código completo que te pasé del bot).

El archivo requirements.txt (con python-telegram-bot y flask).

Baja hasta el final de la página y presiona el botón verde que dice Commit changes para guardarlos.

¡Avísame en cuanto le des a guardar los cambios en GitHub y nos vamos directo a Render a conectarlo!

Dónde presionó y como los subo

¡Estás en el lugar exacto!

Ahí mismo donde dice en azul "choose your files" (dentro del recuadro grande con el dibujo de una hoja), presiona y selecciona los dos archivos desde tu teléfono:   
PNG

El archivo main.py (con el código del bot).

El archivo requirements.txt (con las dependencias).

Una vez que se carguen y los veas listados, baja hasta el botón verde de abajo que dice Commit changes y presiónalo para guardarlos definitivamente.   
PNG

Avísame cuando le des a ese botón verde y nos vamos directo a Render a echar a andar el bot.

Me sale para poner fotos no tengo ningún script descargado ni nada

¡Ah, entiendo perfectamente! No te preocupes por eso. Como estamos creando el código desde cero y lo tienes en nuestra conversación, lo creamos directamente aquí en GitHub de forma súper fácil sin tener que descargar archivos.

Haz lo siguiente en esa misma pantalla:

1
Cambiar a creación manual
GitHub
Arriba de ese recuadro negro, busca y toca el texto que dice "create a new file" (crear un archivo nuevo) para escribir el código aquí mismo.

2
Crear requirements.txt
Paso 1
En el espacio para el nombre del archivo, escribe exactamente: requirements.txt

3
Pegar dependencias
Contenido
En el cuadro grande de texto pega estas dos líneas:

Plaintext
python-telegram-bot
flask
4
Guardar cambios
Commit
Baja la página y presiona el botón verde Commit changes.

Haz ese primer archivo y dime cuando esté listo para pasarte el código del main.py y crearlo de la misma manera en un minuto.

Volví a la parte anterior de los textos azules y le di a create a new file

¡Excelente! Estás justo en el blanco. Veo que ya pusiste el nombre requirements.txt arriba.   
PNG

Haz esto ahora mismo:

En el cuadro grande de texto que dice "Enter file contents here", escribe exactamente estas dos líneas:   
PNG

Plaintext
python-telegram-bot
flask
Toca el botón verde de arriba que dice Commit changes... para guardarlo.   
PNG

Avísame en cuanto le des a guardar para pasarte de inmediato el código del main.py y crearlo igual de rápido.

Pero a la par de txt dice mayn.py

¡Perfecto! Si dice main.py o te da la opción para crear el siguiente archivo, vamos a crear ese mismo main.py con todo el código que tiene la estructura de los botones, el menú de bienvenida, los dos administradores (Nirvana y Fernando) y el sistema de IMEI.

Copia y pega este código completo en el cuadro de texto de GitHub:

Python
import os
import telebot
from telebot import types
import requests
from flask import Flask
from threading import Thread

# Configuración del Bot y Token desde las variables de entorno de Render
TOKEN = os.getenv('NIRVANA_BOT_TOKEN')
IFREE_API_KEY = "SYE-VKS-E4U-9CR-TZB-X68-7YH-ID"  # Tu API Key de IMEI
bot = telebot.TeleBot(TOKEN)

# Servidor Flask para mantener el bot despierto en Render 24/7
app = Flask('')

@app.route('/')
def home():
    return "Bot de Nirvana Infinito activo 24/7"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Menú Principal con botones interactivos
def main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_imei = types.KeyboardButton("🔍 Consultar IMEI")
    btn_soporte = types.KeyboardButton("📞 Soporte Admins")
    btn_info = types.KeyboardButton("ℹ️ Información")
    markup.add(btn_imei, btn_soporte, btn_info)
    bot.send_message(chat_id, "✨ **Bienvenido a Nirvana Infinito Services** ✨\n\nElige una opción del menú:", parse_mode="Markdown", reply_markup=markup)

# Comando /start y /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    main_menu(message.chat.id)

# Manejo de los botones del menú
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "🔍 Consultar IMEI":
        bot.reply_to(message, "📱 Envía el número de IMEI que deseas consultar (15 dígitos).")
    
    elif message.text == "📞 Soporte Admins":
        texto_soporte = (
            "📞 **Administradores Oficiales de Soporte:**\n\n"
            "• Nirvana: @NirvanaFmiOff\n"
            "• Fernando: @Fernando5656\n\n"
            "Escríbele a cualquiera de los dos para pagos, dudas o contrataciones."
        )
        bot.reply_to(message, texto_soporte, parse_mode="Markdown")
        
    elif message.text == "ℹ️ Información":
        texto_info = (
            "🚀 **Nirvana Infinito Services**\n"
            "Sistema automatizado para consultas y servicios exclusivos.\n"
            "Administradores: @NirvanaFmiOff y @Fernando5656"
        )
        bot.reply_to(message, texto_info, parse_mode="Markdown")
        
    elif len(message.text) == 15 and message.text.isdigit():
        # Lógica automática de consulta de IMEI
        msg = bot.reply_to(message, "⏳ Consultando IMEI, por favor espera...")
        url = f"https://api.ifreeicloud.co.uk/api/v1/check?imei={message.text}&key={IFREE_API_KEY}"
        
        try:
            response = requests.get(url, timeout=20)
            data = response.json()
            
            if data.get("status") or data.get("success") or "result" in data:
                resultado_texto = f"✅ **Resultado de IMEI:**\n\n```json\n{data}\n```"
            else:
                resultado_texto = f"⚠️ Respuesta de la API:\n{data}"
                
            bot.edit_message_text(resultado_texto, chat_id=message.chat.id, message_id=msg.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.edit_message_text(f"❌ Error al conectar con el servidor de consultas: {e}", chat_id=message.chat.id, message_id=msg.message_id)
    else:
        bot.reply_to(message, "⚠️ No reconozco ese comando. Usa el menú inferior para navegar.")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
Una vez que lo pegues, dale al botón verde de Commit changes para guardarlo. ¡Avísame cuando esté listo y pasamos a configurar las credenciales en Render!

No me estás dando el código mal el del check de IMEI no el que tiene el menu con los botones

¡Tienes toda la razón, discúlpame por el desliz! El otro bot tiene los menús desplegables avanzados con los botones internos para servicios, verificación y todo lo demás.

Aquí tienes el código completo correcto con todo el menú y los botones que diseñamos para este bot:

Python
import os
import telebot
from telebot import types
import requests
from flask import Flask
from threading import Thread

TOKEN = os.getenv('NIRVANA_BOT_TOKEN')
IFREE_API_KEY = "SYE-VKS-E4U-9CR-TZB-X68-7YH-ID"
bot = telebot.TeleBot(TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Bot Nirvana Infinito activo 24/7"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Menú principal con botones interactivos
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_servicios = types.InlineKeyboardButton("🛠️ Ver Servicios y Precios", callback_data="servicios")
    btn_soporte = types.InlineKeyboardButton("📞 Soporte Admins", callback_data="soporte")
    btn_imei = types.InlineKeyboardButton("📱 Consultar IMEI", callback_data="imei_info")
    markup.add(btn_servicios, btn_soporte, btn_imei)
    
    welcome_text = (
        "✨ **Bienvenido a Nirvana Infinito Services** ✨\n\n"
        "Selecciona una de las opciones del menú para continuar:"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=markup)

# Manejador de los botones interactivos (Inline)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "servicios":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_regresar = types.InlineKeyboardButton("⬅️ Volver al Menú", callback_data="volver")
        markup.add(btn_regresar)
        
        texto_servicios = (
            "🛠️ **Servicios Disponibles:**\n\n"
            "• Verificación de IMEI (Clean / Lost / Stolen)\n"
            "• Liberaciones y servicios de software\n\n"
            "Para contrataciones o dudas, contacta a nuestros administradores oficiales:"
        )
        bot.edit_message_text(texto_servicios, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        
    elif call.data == "soporte":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_regresar = types.InlineKeyboardButton("⬅️ Volver al Menú", callback_data="volver")
        markup.add(btn_regresar)
        
        texto_soporte = (
            "📞 **Administradores Oficiales de Soporte:**\n\n"
            "• Nirvana: @NirvanaFmiOff\n"
            "• Fernando: @Fernando5656\n\n"
            "Escríbele directamente a cualquiera de los dos para atención personalizada."
        )
        bot.edit_message_text(texto_soporte, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        
    elif call.data == "imei_info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_regresar = types.InlineKeyboardButton("⬅️ Volver al Menú", callback_data="volver")
        markup.add(btn_regresar)
        
        texto_imei = (
            "📱 **Consulta de IMEI:**\n\n"
            "Simplemente envía directamente tu número de IMEI (15 dígitos) en el chat para realizar la consulta automática."
        )
        bot.edit_message_text(texto_imei, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        
    elif call.data == "volver":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_servicios = types.InlineKeyboardButton("🛠️ Ver Servicios y Precios", callback_data="servicios")
        btn_soporte = types.InlineKeyboardButton("📞 Soporte Admins", callback_data="soporte")
        btn_imei = types.InlineKeyboardButton("📱 Consultar IMEI", callback_data="imei_info")
        markup.add(btn_servicios, btn_soporte, btn_imei)
        
        welcome_text = (
            "✨ **Bienvenido a Nirvana Infinito Services** ✨\n\n"
            "Selecciona una de las opciones del menú para continuar:"
        )
        bot.edit_message_text(welcome_text, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)

# Procesamiento de mensajes de texto (para recibir el IMEI de 15 dígitos)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if len(message.text) == 15 and message.text.isdigit():
        msg = bot.reply_to(message, "⏳ Consultando IMEI, por favor espera...")
        url = f"https://api.ifreeicloud.co.uk/api/v1/check?imei={message.text}&key={IFREE_API_KEY}"
        
        try:
            response = requests.get(url, timeout=20)
            data = response.json()
            
            if data.get("status") or data.get("success") or "result" in data:
                resultado_texto = f"✅ **Resultado de IMEI:**\n\n```json\n{data}\n```"
            else:
                resultado_texto = f"⚠️ Respuesta de la API:\n{data}"
                
            bot.edit_message_text(resultado_texto, chat_id=message.chat.id, message_id=msg.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.edit_message_text(f"❌ Error al conectar con el servidor: {e}", chat_id=message.chat.id, message_id=msg.message_id)
    else:
        bot.reply_to(message, "⚠️ Por favor, usa los botones del menú /start o envía un número de IMEI válido de 15 dígitos.")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
Pega este código en tu archivo main.py de GitHub, guárdalo con el botón verde de Commit changes, ¡y me avisas para configurar de una vez la variable del Token en Render!

Sigues dándome el mismo ya te paso el script del que tenemos que poner pero antes dime esto en la pantalla está ..ahí dice reerimwint.twx in mayn

¡Ah, ya te entendí perfecto! Lo que ves ahí que dice in main (en azul a la par del nombre del archivo) solo significa que estás guardando el archivo dentro de la rama principal de tu repositorio (que por defecto se llama main). Es totalmente normal y correcto.

Haz lo siguiente en esa misma pantalla:

Borra lo que dice requirements.txt en el recuadro de arriba y escribe main.py (para crear primero el código que me vas a pasar).

En el cuadro grande de abajo, pega tu script completo.

Toca el botón verde Commit changes... para guardarlo.

Pásame tu código o pégalo aquí mismo cuando estés listo y te guío con el requirements.txt que falta en un segundo.

import logging

import os

import re

import time

from threading import Thread

from flask import Flask

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import (

ApplicationBuilder,

CallbackQueryHandler,

CommandHandler,

ContextTypes,

MessageHandler,

filters,

)



# Configuración de logs

logging.basicConfig(

format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",

level=logging.INFO,

)

logger = logging.getLogger(__name__)



# --- SERVIDOR WEB FLASK PARA MANTENER ACTIVO ---

app_web = Flask(__name__)





@app_web.route("/")

def home():

return "¡El Bot Nirvana Infinito está activo y funcionando 24/7!"





def run_web():

app_web.run(host="0.0.0.0", port=8080)





def keep_alive():

t = Thread(target=run_web)

t.start()





# --- MENÚ PRINCIPAL ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

keyboard = [

[

InlineKeyboardButton(

"📋 Catálogo Ilimitado", callback_data="menu_catalogo"

)

],

[

InlineKeyboardButton(

"📱 Android & Xiaomi (FRP/Mi)", callback_data="serv_android"

)

],

[

InlineKeyboardButton(

"💳 Métodos de Pago", callback_data="menu_pagos"

)

],

[

InlineKeyboardButton("👑 Soporte Nirvana", url="https://t.me/NirvanaFmiOff"),

InlineKeyboardButton("🛠️ Soporte Fernando", url="https://t.me/Fernando5656")

],

[

InlineKeyboardButton(

"📢 Unirse al Canal Privado", callback_data="enlace_canal"

)

],

]

reply_markup = InlineKeyboardMarkup(keyboard)



bienvenida_texto = (

"♾️ **BIENVENIDO A NIRVANA INFINITO SERVICES** ♾️\n\n"

"Soluciones profesionales, herramientas y servicios sin límites.\n"

"Selecciona una opción del menú para continuar o envía un IMEI para consulta:"

)



if update.message:

await update.message.reply_text(

bienvenida_texto, reply_markup=reply_markup, parse_mode="Markdown"

)

elif update.callback_query:

query = update.callback_query

await query.answer()

await query.edit_message_text(

bienvenida_texto, reply_markup=reply_markup, parse_mode="Markdown"

)





# --- MENÚ DE CATÁLOGO ---

async def menu_catalogo(

update: Update, context: ContextTypes.DEFAULT_TYPE

) -> None:

query = update.callback_query

await query.answer()



keyboard = [

[

InlineKeyboardButton(

"LIMPIEZA IMEI 🍎", callback_data="serv_fmi"

),

InlineKeyboardButton(

"📱 Open Menu Ilimitado", callback_data="serv_open"

),

],

[

InlineKeyboardButton(

"Phishing Mensual", callback_data="serv_phishing"

),

InlineKeyboardButton(

"🌍 Clean FMI OFF Worldwide", callback_data="serv_clean"

),

],

[

InlineKeyboardButton(

"⭐ Check Premium Ilimitado", callback_data="serv_check"

),

InlineKeyboardButton(

"🍏 Bypass A12 Ilimitado", callback_data="serv_bypass"

),

],

[

InlineKeyboardButton(

"📺 TV Digital Premium", callback_data="serv_tv"

),

InlineKeyboardButton(

"💳 Comprar Info Países", callback_data="serv_info"

),

],

[InlineKeyboardButton("⬅️ Volver al Menú", callback_data="menu_principal")],

]

reply_markup = InlineKeyboardMarkup(keyboard)



texto = (

"📋 **CATÁLOGO DE SERVICIOS ILIMITADOS**\n\n"

"Elige la categoría que deseas consultar:"

)

await query.edit_message_text(

texto, reply_markup=reply_markup, parse_mode="Markdown"

)





# --- MENÚ DE PAGOS ---

async def menu_pagos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

query = update.callback_query

await query.answer()



keyboard = [

[

InlineKeyboardButton("👑 Soporte Nirvana", url="https://t.me/NirvanaFmiOff"),

InlineKeyboardButton("🛠️ Soporte Fernando", url="https://t.me/Fernando5656")

],

[InlineKeyboardButton("⬅️ Volver", callback_data="menu_principal")]

]

reply_markup = InlineKeyboardMarkup(keyboard)



texto = (

"💳 **MÉTODOS DE PAGO Y SOPORTE**\n\n"

"• **💵 Medios aceptados:** Mercado Pago / Cripto (USDT)\n\n"

"⚠️ *Recuerda enviar siempre tu comprobante directamente al soporte una vez realizado el pago.*\n\n"

"👑 **Administradores Oficiales:**\n"

"• Soporte Principal: @NirvanaFmiOff\n"

"• Soporte Técnico: @Fernando5656"

)

await query.edit_message_text(

texto, reply_markup=reply_markup, parse_mode="Markdown"

)





# --- DETALLE DE SERVICIOS ---

async def mostrar_servicio(

update: Update, context: ContextTypes.DEFAULT_TYPE

) -> None:

query = update.callback_query

await query.answer()



data = query.data

detalle = ""

boton_volver_destino = "menu_catalogo"



if data == "serv_android":

detalle = (

"📱 **SERVICIOS ANDROID & XIAOMI PRO** 📱\n\n"

"Soluciones profesionales, seguras y definitivas para liberar tu dispositivo al instante.\n\n"

"⚡ **¿Qué podemos hacer por ti?**\n"

"• 🔓 **FRP Google:** Eliminación de cuentas Google (todos los modelos).\n"

"• 🛠️ **MDM:** Bypass y remoción de bloqueos corporativos.\n"

"• ☁️ **Cuentas Mi:** Limpieza de cuentas Xiaomi 100% de raíz (servidor oficial).\n"

"• 🔒 **Lost FRP:** Soluciones especializadas para equipos bloqueados.\n\n"

"💬 **¿Cómo avanzamos?**\n"

"Los precios varían según el modelo y la seguridad actual de tu equipo. ¡Consúltanos indicando tu modelo exacto para darte el mejor presupuesto!"

)

boton_volver_destino = "menu_principal"

elif data == "serv_fmi":

detalle = (

"🍎 **Limpieza de IMEI**\n\n"

"Servicio especializado para remover reportes en equipos que no levantan señal.\n\n"

"⚠️ *Nota:* Los países soportados varían constantemente. Consulta directamente con soporte para verificar la disponibilidad para el país de tu equipo."

)

elif data == "serv_open":

detalle = (

"📱 **Open Menu Ilimitado**\n\n"

"**Requisitos indispensables:**\n"

"• El equipo **no** debe tener la contraseña cambiada.\n"

"• **No** se debe desactivar el Apple ID.\n"

"• Debe ingresar a **iCloud.com** desde Safari en el propio dispositivo y dejarlo con la sesión iniciada mediante el código PIN del equipo a desbloquear."

)

elif data == "serv_phishing":

detalle = (

"🔐 **Phishing / Acceso Exclusivo Semanal**\n\n"

"Herramienta avanzada con altísima tasa de éxito orientada a la obtención de información clave (mensaje de propietario, chip original, ficha médica, etc.).\n\n"

"💵 **Inversión:** Por solo **30 USDT** obtienes acceso completo para procesar todos los equipos que desees durante **una semana**.\n\n"

"🔒 **Privacidad Total:** Interactúas de forma 100% directa en el chat privado con tu propio bot, garantizando que nadie más vea tus procesos ni tus movimientos."

)

elif data == "serv_clean":

detalle = (

"🌍 **Clean FMI OFF Worldwide**\n\n"

"**Requisitos del servicio:**\n"

"• El dispositivo **no** debe poseer ningún tipo de reporte ni encontrarse en modo perdido.\n"

"• Es obligatorio realizar un **Check GSX Full Report** previo para validar que todas las condiciones se cumplan.\n\n"

"⏱️ *Tiempo estimado del proceso:* Entre 15 y 25 días hábiles."

)

elif data == "serv_check":

detalle = (

"⭐ **Check Premium Ilimitado (Planes Mensuales / Semanales)**\n\n"

"Realiza cualquier tipo de consulta y check de forma completamente ilimitada según el plan que elijas (ideal para técnicos de alto flujo).\n\n"

"🔒 **Privacidad Exclusiva:** Interactúas de manera 100% directa y privada con el bot. Ninguna otra persona podrá ver los checks ni los resultados que realices."

)

elif data == "serv_bypass":

detalle = (

"🍏 **Bypass A12 Ilimitado**\n\n"

"• **iPhone XR al 11 Pro Max:** Soporta cualquier versión de iOS, tanto en modo *passcode* como en *iPhone desactivado*.\n"

" - Con IMEI limpio: Sale con **señal full**.\n"

" - En pantalla Hola: Sale **sin señal**.\n"

" - *Requisito físico:* Necesita herramienta física **Raspberry Pi Pico 2 (modelo 2350)** y un cable USB.\n\n"

"• **iPhone 12 al 17 Pro Max:** Funciona exclusivamente en **iOS 26.1** y únicamente estando en **pantalla Hola**."

)

elif data == "serv_tv":

detalle = (

"📺 **TV Digital Premium**\n\n"

"El servicio más completo del mercado para dispositivos Android (Celulares, Tablets, Smart TV o TV Box).\n\n"

"✨ Disfruta de todos los canales en alta definición, series, películas y deportes premium.\n"

"💼 **Planes disponibles:** Renta mensual, anual y adquisición de **paneles oficiales para revendedores**."

)

elif data == "serv_info":

detalle = (

"💳 **Comprar Info de Países**\n\n"

"Acceso a reportes de información internacional.\n\n"

"⚖️ **Aviso Legal Importante:** Este servicio está destinado exclusivamente a usos legítimos (como localización por deudas legítimas o procesos de desbloqueo autorizados). Queda terminantemente prohibido su uso con fines maliciosos o que violen las leyes vigentes.\n\n"

"⚠️ *Nirvana Infinito Services no se hace responsable por el mal uso o la manipulación indebida de la información obtenida a través de esta herramienta.*"

)



texto_boton_volver = "⬅️ Volver al Menú" if boton_volver_destino == "menu_principal" else "⬅️ Volver al Catálogo"



keyboard = [

[

InlineKeyboardButton(

"🛒 Contratar Nirvana", url="https://t.me/NirvanaFmiOff"

),

InlineKeyboardButton(

"🛒 Contratar Fernando", url="https://t.me/Fernando5656"

)

],

[

InlineKeyboardButton(

texto_boton_volver, callback_data=boton_volver_destino

)

],

]

reply_markup = InlineKeyboardMarkup(keyboard)



await query.edit_message_text(

detalle, reply_markup=reply_markup, parse_mode="Markdown"

)





# --- DETECTOR AUTOMÁTICO DE IMEI ---

async def handle_imei_message(

update: Update, context: ContextTypes.DEFAULT_TYPE

) -> None:

if not update.message or not update.message.text:

return


texto_usuario = update.message.text.strip()



if re.match(r"^\d{15}$", texto_usuario):

respuesta = (

f"🔍 **IMEI Recibido:** `{texto_usuario}`\n\n"

"⏳ Procesando consulta automática...\n"

"*(Para finalizar contratación o verificar estado detallado, contacta a soporte)*"

)

keyboard = [

[

InlineKeyboardButton(

"👑 Consultar Nirvana", url="https://t.me/NirvanaFmiOff"

),

InlineKeyboardButton(

"🛠️ Consultar Fernando", url="https://t.me/Fernando5656"

)

]

]

reply_markup = InlineKeyboardMarkup(keyboard)

await update.message.reply_text(

respuesta, reply_markup=reply_markup, parse_mode="Markdown"

)

else:

await update.message.reply_text(

"👋 ¡Hola! Usa el menú principal con /start o envía un número de IMEI válido de 15 dígitos para consultar."

)





# --- MANEJADOR DE BOTONES ---

async def button_handler(

update: Update, context: ContextTypes.DEFAULT_TYPE

) -> None:

query = update.callback_query

data = query.data



if data == "menu_principal":

await start(update, context)

elif data == "menu_catalogo":

await menu_catalogo(update, context)

elif data == "menu_pagos":

await menu_pagos(update, context)

elif data == "enlace_canal":

await query.answer()

texto_canal = (

"🔐 **COMUNIDAD PRIVADA - NIRVANA INFINITO** 🔐\n\n"

"💻 ¡Hola, querido colega unlocker! 📱\n\n"

"Al ser un canal privado de alta seguridad y exclusividad, te compartimos el enlace directo para que tus compañeros y colegas de todo el mundo puedan ingresar, sumarse y formar parte de esta gran comunidad de trabajo:\n\n"

"🔗 **Link de Acceso Exclusivo:**\n"

"https://t.me/+U99kMTOYIGYxNGQ5\n\n"

"⚡ *¡Te esperamos adentro para seguir destrabando límites sin escalas!* 🚀🛠️"

)

keyboard_volver = [[InlineKeyboardButton("⬅️ Volver al Menú", callback_data="menu_principal")]]

reply_markup_volver = InlineKeyboardMarkup(keyboard_volver)

await query.edit_message_text(

texto_canal, reply_markup=reply_markup_volver, parse_mode="Markdown"

)

elif data.startswith("serv_"):

await mostrar_servicio(update, context)





def main() -> None:

# Arrancamos el servidor web Flask en segundo plano

keep_alive()



TOKEN = os.getenv("NIRVANA_BOT_TOKEN")



if not TOKEN:

logger.error("No se encontró el token NIRVANA_BOT_TOKEN en los Secrets.")

return



application = ApplicationBuilder().token(TOKEN).build()



application.add_handler(CommandHandler("start", start))

application.add_handler(CallbackQueryHandler(button_handler))

application.add_handler(

MessageHandler(filters.TEXT & ~filters.COMMAND, handle_imei_message)

)



logger.info("Iniciando Bot Nirvana Infinito con bucle de seguridad 24/7...")



# Bucle try/except para autoreconexión y mantenimiento 24/7

while True:

try:

application.run_polling(drop_pending_updates=True)

except Exception as e:

logger.error(f"Error en la conexión del bot: {e}. Reconectando en 5 segundos...")

time.sleep(5)





if __name__ == "__main__":

main() 


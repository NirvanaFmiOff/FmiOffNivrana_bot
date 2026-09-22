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
        [InlineKeyboardButton("📋 Catálogo Ilimitado", callback_data="menu_catalogo")],
        [InlineKeyboardButton("📱 Android & Xiaomi (FRP/Mi)", callback_data="serv_android")],
        [InlineKeyboardButton("💳 Métodos de Pago", callback_data="menu_pagos")],
        [
            InlineKeyboardButton("👑 Soporte Nirvana", url="https://t.me/NirvanaFmiOff"),
            InlineKeyboardButton("🛠️ Soporte Fernando", url="https://t.me/Fernando5656")
        ],
        [InlineKeyboardButton("📢 Unirse al Canal Privado", callback_data="enlace_canal")],
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
async def menu_catalogo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton("LIMPIEZA IMEI 🍎", callback_data="serv_fmi"),
            InlineKeyboardButton("📱 Open Menu Ilimitado", callback_data="serv_open"),
        ],
        [
            InlineKeyboardButton("Phishing Mensual", callback_data="serv_phishing"),
            InlineKeyboardButton("🌍 Clean FMI OFF Worldwide", callback_data="serv_clean"),
        ],
        [
            InlineKeyboardButton("⭐ Check Premium Ilimitado", callback_data="serv_check"),
            InlineKeyboardButton("🍏 Bypass A12 Ilimitado", callback_data="serv_bypass"),
        ],
        [
            InlineKeyboardButton("📺 TV Digital Premium", callback_data="serv_tv"),
            InlineKeyboardButton("💳 Comprar Info Países", callback_data="serv_info"),
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
async def mostrar_servicio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
            "  - Con IMEI limpio: Sale con **señal full**.\n"
            "  - En pantalla Hola: Sale **sin señal**.\n"
            "  - *Requisito físico:* Necesita herramienta física **Raspberry Pi Pico 2 (modelo 2350)** y un cable USB.\n\n"
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
            InlineKeyboardButton("🛒 Contratar Nirvana", url="https://t.me/NirvanaFmiOff"),
            InlineKeyboardButton("🛒 Contratar Fernando", url="https://t.me/Fernando5656")
        ],
        [InlineKeyboardButton(texto_boton_volver, callback_data=boton_volver_destino)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        detalle, reply_markup=reply_markup, parse_mode="Markdown"
    )

# --- DETECTOR AUTOMÁTICO DE IMEI ---
async def handle_imei_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
                InlineKeyboardButton("👑 Consultar Nirvana", url="https://t.me/NirvanaFmiOff"),
                InlineKeyboardButton("🛠️ Consultar Fernando", url="https://t.me/Fernando5656")
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
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
            "https://t.me/+oGhtE4RKVyE5MzVh\n\n"
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
    keep_alive()

    TOKEN = os.getenv("NIRVANA_BOT_TOKEN")
    if not TOKEN:
        logger.error("No se encontró el token NIRVANA_BOT_TOKEN en los Secrets.")
        return

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_imei_message))

    logger.info("Iniciando Bot Nirvana Infinito con bucle de seguridad 24/7...")

    while True:
        try:
            application.run_polling(drop_pending_updates=True)
        except Exception as e:
            logger.error(f"Error en la conexión del bot: {e}. Reconectando en 5 segundos...")
            time.sleep(5)

if __name__ == "__main__":
    main()

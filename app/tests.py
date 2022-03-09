from ecommerce.wsgi import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.template.loader import render_to_string

from ecommerce import settings
from app.user.models import User

#FUNCION DE ENVIO DE CORREO DE PRUEBA
def send_email():
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado..')

        email_to = 'zachafe@gmail.com'
        # Construimos el mensaje simple
        #mensaje = MIMEText("""Este es el mensaje de prueba Django APP afquintero""")
        #MENAJES COMPUESTO
        mensaje = MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = "Tienes un correo"

        #CONTENIDO CUANDO EL MENSAJE ES COMPUESTO 
        content = render_to_string('send_email.html', {'user': User.objects.get(pk=1)})
        mensaje.attach(MIMEText(content, 'html'))

        mailServer.sendmail(settings.EMAIL_HOST_USER,
                            email_to,
                            mensaje.as_string())

        print('Correo enviado correctamente')
    except Exception as e:
        print(e)

send_email()

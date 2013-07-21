import smtplib
import csv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from htmlentitydefs import codepoint2name 

def unicode2htmlentities(u): 
   htmlentities = list() 
   for c in u: 
      if ord(c) < 128: 
         htmlentities.append(c) 
      else: 
         htmlentities.append('&%s;' % codepoint2name[ord(c)]) 
   return ''.join(htmlentities)

me = 'devday@devisland.com'  
  
# Credentials (if needed)  
username = 'devday@devisland.com'  
password = ''  
  
# Create the body of the message (a plain-text and an HTML version).
text = """\
Ola <NOME>,

Gostariamos de agradecer por sua inscricao no #DEVDAY2013, maior evento de Desenvolvedores de Minas Gerais.

O #DEVDAY e um evento que esta na sua quarta edicao e prezamos muito por sermos ainda um evento feito pela comunidade.
Neste caso, isto nos possibilita fazer um evento onde voce pode participar, escolher e definir o que quer ver no evento.
Alem disto e um evento que a base e ter DEV falando para DEV, com isto, o evento e o que falamos sem MIMIMI.

Continue acompanhando o evento pelo site devday.devisland.com alem de site do DEVISLAND.

Prepare-se tambem assistindo as palestras do ano passado no canal do youtube: youtube.com/devisland
Obrigado novamente e nos vemos no DEVDAY.

Organizacao do #DEVDAY2013.
"""

html = """\
<html>
	<head>
		<title>Confirma&ccedil;&atilde;o de Inscri&ccedil;&atilde;o</title>
	    <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet">
	</head>
	<body>
	   	<img src="http://devday.devisland.com/assets/img/logo/devday2013.png" width="200" />
	   	<img src="http://devday.devisland.com/assets/img/logo/DevIsland_logo.png" width="100"/>
		<br />
		<br />
		<br />
		
		<div class="alert alert-info">
			Ol&aacute; <strong><NOME></strong>,
			
			<p>
				Gostar&iacute;amos de agradecer por sua inscri&ccedil;&atilde;o no <a href="http://devday.devisland.com">#DEVDAY2013</a>, maior evento de Desenvolvedores de Minas Gerais.
			</p>
			<p>
				O #DEVDAY &eacute; um evento que est&aacute; na sua quarta edi&ccedil;&atilde;o e prezamos muito por sermos ainda um evento feito pela comunidade. 
				<br />Neste caso, isto nos possibilita fazer um evento onde voc&ecirc; pode participar, escolher e definir o que quer ver no evento. 
				<br />Al&eacute;m disto &eacute; um evento que a base &eacute; ter <strong>DEV</strong> falando para <strong>DEV</strong>, com isto, o evento &eacute; o que falamos sem <strong>MIMIMI</strong>.
			</p>
			<p>
				Continue acompanhando o evento pelo site <a href="http://devday.devisland.com">devday.devisland.com</a> al&eacute;m de site do <a href="http://devisland.com">DEVISLAND</a>.
			</p>
			<p>
				Prepare-se tamb&eacute;m assistindo as palestras do ano passado no canal do youtube: <a href="http://youtube.com/devisland">youtube.com/devisland</a>
			</p>
			<strong>Obrigado novamente e nos vemos no DEVDAY.</strong>
			<p><strong>Organiza&ccedil;&atilde;o do #DEVDAY2013.</strong></p>
		</div>
	</body>
</html>
"""

fileInscritos = csv.reader(open('inscritos.csv', 'rU'), delimiter=';')
for [nome,email] in fileInscritos:
	print 'nome=%s | email=%s' % (nome.decode('utf-8', 'ignore'), email)
  	htmlUsuario = html.replace('<NOME>', unicode2htmlentities(nome.decode('utf-8', 'ignore')))
	textUsuario = text.replace('<NOME>', nome.decode('ascii', 'ignore'))
	
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "CONFIRMACAO DE INSCRICAO DEVDAY2013"
	msg['From'] = me
	msg['To'] = email
	you = email

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(textUsuario, 'plain')
	part2 = MIMEText(htmlUsuario, 'html')

	msg.attach(part1)
	msg.attach(part2)

	# Send the message via local SMTP server.
	server = smtplib.SMTP('smtp.gmail.com:587') 
	server.starttls()  
	server.login(username,password)  
	server.sendmail(me, you, msg.as_string())
	server.quit()

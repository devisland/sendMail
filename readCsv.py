""" Le um arquivo delimitado e mostra os campos na tela. """
import csv
from htmlentitydefs import codepoint2name 
 
def unicode2htmlentities(u): 
   htmlentities = list() 
   for c in u: 
      if ord(c) < 128: 
         htmlentities.append(c) 
      else: 
         htmlentities.append('&%s;' % codepoint2name[ord(c)]) 
   return ''.join(htmlentities)

print __doc__
f = csv.reader(open('inscritos.csv', 'rU'), delimiter=';')
for [nome,email] in f:
    print 'nome=%s | email=%s | nome=%s' % (nome.decode('utf-8', 'ignore'),email, unicode2htmlentities(nome.decode('utf-8', 'ignore')))
	
print f.line_num, 'linhas lidas'
print '--- fim'
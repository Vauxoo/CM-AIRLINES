# -*- coding: utf-8 -*-

import time
from datetime import datetime
from dateutil import tz
from pytz import timezone
from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError
from itertools import ifilter

class company_inherit(models.Model):
	_inherit='res.company'
	
	@api.model
	def setDate(self,date):
		if not self.env.context.get('tz'):
			raise UserError(_('Please Define the TimeZone for the User'))
		UTC = tz.gettz('UTC')
		gmt = datetime.strptime(date,'%Y-%m-%d %H:%M:%S').replace(tzinfo=UTC)
		return gmt.astimezone(timezone(self.env.context['tz'])).strftime("%Y-%m-%d %H:%M:%S")
	@api.model
	def resetDate(self,date):
		if not self.env.context.get('tz'):
			raise UserError(_('Please Define the TimeZone for the User'))
		UTC = tz.gettz('UTC')
		gmt = datetime.strptime(date,'%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone(self.env.context['tz']))
		return gmt.astimezone(UTC).strftime("%Y-%m-%d %H:%M:%S")
	def validate_centavos(numero):
		if numero > 0 and numero < 9:
			return True
	@api.model
	def to_word(self,number, mi_moneda):
	    valor= number
	    number=abs(int(number))
	    n = (round(valor-number,2))*100
	    centavos = int(round(n,0))
	    
	    UNIDADES = (
	    '',
	    'UN ',
	    'DOS ',
	    'TRES ',
	    'CUATRO ',
	    'CINCO ',
	    'SEIS ',
	    'SIETE ',
	    'OCHO ',
	    'NUEVE ',
	    'DIEZ ',
	    'ONCE ',
	    'DOCE ',
	    'TRECE ',
	    'CATORCE ',
	    'QUINCE ',
	    'DIECISEIS ',
	    'DIECISIETE ',
	    'DIECIOCHO ',
	    'DIECINUEVE ',
	    'VEINTE '
	)

	    DECENAS = (
	    'VEINTI',
	    'TREINTA ',
	    'CUARENTA ',
	    'CINCUENTA ',
	    'SESENTA ',
	    'SETENTA ',
	    'OCHENTA ',
	    'NOVENTA ',
	    'CIEN '
	)

	    CENTENAS = (
	    'CIENTO ',
	    'DOSCIENTOS ',
	    'TRESCIENTOS ',
	    'CUATROCIENTOS ',
	    'QUINIENTOS ',
	    'SEISCIENTOS ',
	    'SETECIENTOS ',
	    'OCHOCIENTOS ',
	    'NOVECIENTOS '
	)
	    MONEDAS = (
		    {'country': u'Colombia', 'currency': 'COP', 'singular': u'PESO COLOMBIANO', 'plural': u'PESOS COLOMBIANOS', 'symbol': u'$'},
		    {'country': u'Honduras', 'currency': 'HNL', 'singular': u'Lempira', 'plural': u'Lempiras', 'symbol': u'L'},
		    {'country': u'Estados Unidos', 'currency': 'USD', 'singular': u'DÓLAR', 'plural': u'DÓLARES', 'symbol': u'US$'},
		    {'country': u'Europa', 'currency': 'EUR', 'singular': u'EURO', 'plural': u'EUROS', 'symbol': u'€'},
		    {'country': u'México', 'currency': 'MXN', 'singular': u'PESO MEXICANO', 'plural': u'PESOS MEXICANOS', 'symbol': u'$'},
		    {'country': u'Perú', 'currency': 'PEN', 'singular': u'NUEVO SOL', 'plural': u'NUEVOS SOLES', 'symbol': u'S/.'},
		    {'country': u'Reino Unido', 'currency': 'GBP', 'singular': u'LIBRA', 'plural': u'LIBRAS', 'symbol': u'£'}
		)
	    if mi_moneda != None:
                print number,mi_moneda
		try:
		    moneda = ifilter(lambda x: x['currency'] == mi_moneda, MONEDAS).next()
		    print moneda,number
		    if number < 2:
		        moneda = moneda['singular']
		    else:
		        moneda = moneda['plural']
		except:
		    return "Tipo de moneda inválida"
	    else:
		moneda = ""
	    moneda = ""
	    """Converts a number into string representation"""
	    converted = ''

	    if not (0 < number < 999999999):
		return 'No es posible convertir el numero a letras'

	    number_str = str(number).zfill(9)
	    millones = number_str[:3]
	    miles = number_str[3:6]
	    cientos = number_str[6:]

	    if(millones):
		if(millones == '001'):
		    converted += 'UN MILLON '
		elif(int(millones) > 0):
		    converted += '%sMILLONES ' % self.convert_group(millones)

	    if(miles):
		if(miles == '001'):
		    converted += 'MIL '
		elif(int(miles) > 0):
		    converted += '%sMIL ' % self.convert_group(miles)

	    if(cientos):
		if(cientos == '001'):
		    converted += 'UN '
		elif(int(cientos) > 0):
		    converted += '%s ' % self.convert_group(cientos)
	    exactos = "Exactos"
	    if(centavos)>0:
		exactos = ""
		if centavos < 9:
			converted+= "con 0%i/100 "%centavos
		else:
			converted+= "con %2i/100 "%centavos
	    moneda=""
	    #converted += moneda
	    converted += (moneda + exactos)

	    return converted.title()


	def convert_group(self,n):
	    UNIDADES = (
	    '',
	    'UN ',
	    'DOS ',
	    'TRES ',
	    'CUATRO ',
	    'CINCO ',
	    'SEIS ',
	    'SIETE ',
	    'OCHO ',
	    'NUEVE ',
	    'DIEZ ',
	    'ONCE ',
	    'DOCE ',
	    'TRECE ',
	    'CATORCE ',
	    'QUINCE ',
	    'DIECISEIS ',
	    'DIECISIETE ',
	    'DIECIOCHO ',
	    'DIECINUEVE ',
	    'VEINTE '
	)

	    DECENAS = (
	    'VEINTI',
	    'TREINTA ',
	    'CUARENTA ',
	    'CINCUENTA ',
	    'SESENTA ',
	    'SETENTA ',
	    'OCHENTA ',
	    'NOVENTA ',
	    'CIEN '
	)

	    CENTENAS = (
	    'CIENTO ',
	    'DOSCIENTOS ',
	    'TRESCIENTOS ',
	    'CUATROCIENTOS ',
	    'QUINIENTOS ',
	    'SEISCIENTOS ',
	    'SETECIENTOS ',
	    'OCHOCIENTOS ',
	    'NOVECIENTOS '
	)
	    MONEDAS = (
		    {'country': u'Colombia', 'currency': 'COP', 'singular': u'PESO COLOMBIANO', 'plural': u'PESOS COLOMBIANOS', 'symbol': u'$'},
		    {'country': u'Honduras', 'currency': 'HNL', 'singular': u'Lempira', 'plural': u'Lempiras', 'symbol': u'L'},
		    {'country': u'Estados Unidos', 'currency': 'USD', 'singular': u'DÓLAR', 'plural': u'DÓLARES', 'symbol': u'US$'},
		    {'country': u'Europa', 'currency': 'EUR', 'singular': u'EURO', 'plural': u'EUROS', 'symbol': u'€'},
		    {'country': u'México', 'currency': 'MXN', 'singular': u'PESO MEXICANO', 'plural': u'PESOS MEXICANOS', 'symbol': u'$'},
		    
{'country': u'Perú', 'currency': 'PEN', 'singular': u'NUEVO SOL', 'plural': u'NUEVOS SOLES', 'symbol': u'S/.'},
		    {'country': u'Reino Unido', 'currency': 'GBP', 'singular': u'LIBRA', 'plural': u'LIBRAS', 'symbol': u'£'}
		)
	    """Turn each group of numbers into letters"""
	    output = ''

	    if(n == '100'):
		output = "CIEN "
	    elif(n[0] != '0'):
		output = CENTENAS[int(n[0]) - 1]

	    k = int(n[1:])
	    if(k <= 20):
		output += UNIDADES[k]
	    else:
		if((k > 30) & (n[2] != '0')):
		    output += '%sY %s' % (DECENAS[int(n[1]) - 2], UNIDADES[int(n[2])])
		else:
		    output += '%s%s' % (DECENAS[int(n[1]) - 2], UNIDADES[int(n[2])])
	    return output

	def addComa(self, snum ):
		s = snum;
		i = s.index('.') # Se busca la posición del punto decimal
		while i > 3:
			i = i - 3
			s = s[:i] +  ',' + s[i:]
		return s

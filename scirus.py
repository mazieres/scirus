import os, sys
import urllib2
from mechanize import *
from random import choice


user_agents = [u'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1', u'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2', u'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0', u'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00', ]


def scirus(query):
	
	# Setting Mechanize's Browser
	br = Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(False)
	br.addheaders = [('User-agent', choice(user_agents))]

	# Displaying results
	response = br.open("http://www.scirus.com/")
	br.select_form("search")
	br["q"] = query
	response = br.submit()
	response = br.open(br.geturl())

	f = open('./scirus.ris', 'w')
	new_idx = 10

	while True:

		# Listing results of the page
		br.select_form("results")
		controls = br.form.controls
		idz = br.find_control('r').possible_items()

		# Grabbin data
		data_to_post = 'res='
		for each in idz:
			data_to_post += '#SEP#%s' % each
		data_to_post += '&pagefrom=export&submitted=submitted&exporttype=abs&fileformat=ris&displaytype=save'
		d = urllib2.urlopen('http://www.scirus.com/srsapp/exportresults', data_to_post).read()

		# Writtin data
		f.write(d)
		print d

		if new_idx > 999:
			print "Reached the Scirus 1000 results limit, quitting..."
			break

		# Update url
		try:
			br.select_form("navresult")
			controls = br.form.controls
			for each in controls:
				print each
			new_idx += 10
			new_url = 'http://www.scirus.com/srsapp/search?' + br['qs'] + '&sort=0&p=%s' % new_idx
			print new_url
		except:
			print "no more Next Page..."
			break

	f.close()


# Example
# scirus('Reverse engineering')

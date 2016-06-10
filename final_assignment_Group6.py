#!/usr/bin/env python3

# Final Assignment Taaltechnologie
# Gerben Timmerman s2769670
# Stan Snijders s2760002
# Robert Veenhoven s2770199
# Stan Korenromp s

import socket
import sys
from lxml import etree
from SPARQLWrapper import SPARQLWrapper, JSON
import wikipedia

def alpino_parse(sent, host='zardoz.service.rug.nl', port=42424):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	sent = sent + "\n\n"
	sentbytes= sent.encode('utf-8')
	s.sendall(sentbytes)
	bytes_received= b''
	while True:
		byte = s.recv(8192)
		if not byte:
			break
		bytes_received += byte
		#print(bytes_received.decode(’utf-8’), file=sys.stderr)
	xml = etree.fromstring(bytes_received)
	return xml

def print_example_queries():
	print("Wanneer begonnen de Olympische Zomerspelen 2012?")
	print("Wat is de lengte van Usain Bolt?")
	print("Hoe lang is Usain Bolt?")
	print("Hoe zwaar is Marleen Veldhuis?")
	print("Op welke datum sloten de Olympische Zomerspelen 2012?")
	print("Wie is de trainer van Epke Zonderland?")
	print("Welk gewicht heeft Henk Grol?")
	print("Aan welk onderdeel neemt Henk Grol deel?")
	print("Door wie wordt Usain Bolt getraind?")
	print("Wat is de geboorteplaats van Marleen Veldhuis?")
	print("In welke plaats is Epke Zonderland geboren?\n")
	
def leesbestand():
	f= open("test.txt", "r")
	filedata = f.read()	
	newdata = filedata.replace(" spelen"," Spelen")
	newdata2 = newdata.replace(" olympisch"," Olympisch")
	newdata3 = newdata2.replace(" zomerspelen"," Zomerspelen")
	newdata4 = newdata3.replace(" winterspelen"," Winterspelen")
	ff = open("beteretest.txt",'w')
	ff.write(newdata4)
	ff.close()
	
	
def main(argv):
	#leesbestand()
	#f=open("beteretest.txt", "r")
	print_example_queries()
	for line in sys.stdin:
		#zin=line.split("\t")
		#print(zin[1])
		stringY=returnName(line) #zin[1]
		Proplist=returnProp(line) #zin[1]
		Keuzewoord = returnKeuzewoord(line)
		answer = create_and_fire_query(stringY,Proplist)
		print(answer)

#def kiesfuncties():
	#soortvraag= xml.xpath('//node[ @rel="whd"] ')
	#if soortvraag =="Wanneer" or soortvraag == "Sinds wanneer":
		
	#if soortvraag =="Wie" or soortvraag =="Wat":
			
	#//node[ @postag="BW()" and @word="Hoe"] hoe zinnen
			
def returnName(line): #wie/wat vragen
	Ylist, Ylist2, Ylist3, Ylist4=[],[],[],[]
	line = line.rstrip()
	xml = alpino_parse(line)
	names = xml.xpath('//node[@spectype="deeleigen"] ')
	names2= xml.xpath('//node[@neclass="year"]')
	if names==[]:
		names3=xml.xpath('//node[ @cat="np" and @rel="obj1" and node[@rel="det"]]')
		for name in names3:	
			Ylist3.append(tree_yield(name))
		stringY3= ' '.join(Ylist3)
		if names3==[]:
			names4=xml.xpath('//node[ @rel="su"]')
			for name in names4:	
				Ylist4.append(tree_yield(name))
			stringY3= ' '.join(Ylist4)
	else:			
		for name in names:
			Ylist.append(tree_yield(name))
		for name in names2:
			Ylist2.append(tree_yield(name))	
		stringY= ' '.join(Ylist)
		stringY2= ' '.join(Ylist2)
		stringY3= stringY+" "+stringY2
	stringY4=stringY3.rstrip()
	stringY5=stringY4.replace("het ","")
	stringY6=stringY5.replace("de ","")
	print(stringY6)
	return stringY6
	
	
	
def returnName2(line): #Wanneer of sindswanneer
	Ylist=[]
	Ylist2=[]
	Ylist3=[]
	line = line.rstrip()
	xml = alpino_parse(line)
	names = xml.xpath('//node[@word="Worstelen" or @word="hoogspringen" or @word="basketbal" or @word="taekwondo" or @word="kogelstoten" or @word="korfbal" or @word="judo" or @word="boogschieten"]')
	if names==[]:
		names2=xml.xpath('//node[@spectype="deeleigen"]')
		names3= xml.xpath('//node[@neclass="year"]')
		for name in names2:
			Ylist2.append(tree_yield(name))
		for name in names3:	
			Ylist3.append(tree_yield(name))
		stringY= ' '.join(Ylist2)
		stringY2= ' '.join(Ylist3)
		stringY3= stringY+" "+stringY2	
	else:			
		for name in names:
			Ylist.append(tree_yield(name))
		stringY3= ' '.join(Ylist)		
	stringY4=stringY3.rstrip()
	stringY5=stringY4.replace("het ","")
	stringY6=stringY4.replace("de ","")
	print(stringY6)
	return stringY6	
	
def returnProp(line):
	Proplist=[]
	line = line.rstrip()
	xml = alpino_parse(line)
	names = xml.xpath('//node[@rel="hd"]')
	for name in names :
		Proplist.append(tree_yield(name))
	return Proplist
	
def returnKeuzewoord(line):
	line = line.rstrip()
	xml = alpino_parse(line)
	names = xml.xpath('//node[@rel="whd"]')
	for name in names :
		Keuzewoordlist = tree_yield(name).split()
	print('Dit is de keuzewoordlist',Keuzewoordlist)
	if 'Wanneer' in Keuzewoordlist or 'wanneer' in Keuzewoordlist:
		Keuzewoord = 'wanneer'
	elif 'Wat' in Keuzewoordlist or 'wat' in Keuzewoordlist:
		Keuzewoord = 'wat'
	elif 'Wie' in Keuzewoordlist or 'wie' in Keuzewoordlist:
		Keuzewoord = 'wie'
	elif 'Welk' in Keuzewoordlist or 'welk' in Keuzewoordlist or 'Welke' in Keuzewoordlist or 'welke' in Keuzewoordlist:
		Keuzewoord = 'welke'
	elif 'Waar' in Keuzewoordlist or 'waar' in Keuzewoordlist:
		Keuzewoord = 'waar'
	elif 'Hoe' in Keuzewoordlist or 'hoe' in Keuzewoordlist:
		Keuzewoord = 'hoe' 
	print('Het keuzewoord is',Keuzewoord)
	return Keuzewoord
	
def tree_yield(xml):
	leaves = xml.xpath('descendant-or-self::node[@word]')
	words = []
	for l in leaves :
		words.append(l.attrib["word"])
	return " ".join(words)	
	

def findproperty(searchwordlist):
	wie_wat_dictionary = {
        'prop-nl:volgende': ["aankomende","volgende","komende","eerstvolgende","na"],
        'prop-nl:vorige': ["vorige","voorgaand","laatste"],
        'prop-nl:locatie': ["baan", "locatie"],
        'prop-nl:debuut': ["debuut", "eerste professionele wedstrijd"],
        'prop-nl:bijnaam': ["bijnaam", "nickname", "bijnamen"],
        'prop-nl:onderdeel': ["stok","onderdeel", "specialisatie","sport"],
        'prop-nl:naam': ["naam", "volledige naam", "namen"],
        'prop-nl:motto': ["motto",""],
        'prop-nl:wrman': ["wereldrecord"],
        'prop-nl:landen': ["aantal"],
        'foaf:homepage': ["website"],
        'prop-nl:geboortestad': ["geboorteplaats"],
        'prop-nl:rang': ["rang"],
        'prop-nl:bijnamen': ["bijnamen"],
        'prop-nl:vorigenamen': ["voormalige naam", "naam"],
        'rdfs:comment': ["bekend"],
        'prop-nl:sport': ["sporten", "aantal sporten"],
        'prop-nl:lengte': ["lengte"],
        'prop-nl:discipline':["sport","soort","discipline", "olympische-sportdiscipline"],
        'prop-nl:olympischKampioen': ["olympische spelen", "Olympische Spelen","snelste"],
        'prop-nl:opening': ["startdatum"],
        'prop-nl:organisator': ["organisator","georganiseerd","organiseren","organiseert"],
        'prop-nl:eerste': ["eerste", "moderne"],
        'prop-nl:atleten': ["atleten","deelnemende atleten", "deelnemers"],
        'prop-nl:soort': ["soort"],
        'prop-nl:vlaggendrager': ["vlaggendrager","vlagdragers", "vlaggendragers","vlag"],
        'prop-nl:opener': ["geopend", "opening","opende"],
        'prop-nl:coach': ["trainer","coach"],
        'prop-nl:bondscoach': ["bondscoach","coach"],
        'prop-nl:vlam': ["vlam","vlamdragers","fakkel","droegen", "vuur","fakkeldragers","toorts"],
        'dcterms:subject': ["kampioen"],
        'prop-nl:voorzitter': ["voorzitter","topman","president"],
        'prop-nl:topscorer': ["topscorer"],
        'prop-nl:goudNaam': ["gewonnen","goud","gouden"],
        'dbpedia-owl:currentWorldChampion': ["wereldrecordhouders","wereldkampioenen","wereldkampioen","huidige","huidig"],
        'prop-nl:eed': ["eed"],
        'prop-nl:presentatie': ["presentatoren"],
        'prop-nl:architect': ["ontwierp "],
        'prop-nl:zilverNaam': ["zilver", "zilveren"],
        'prop-nl:referee': ["scheidsrechters","scheidsrechter"]
    }
	for searchword in searchwordlist:
		for property,words in wie_wat_dictionary.items():
			for word in wie_wat_dictionary[property]:
				if searchword == word:
					propertylist = []
					propertylist.append(property)
	print('Dit is de propertylist:',propertylist)
	return propertylist		
		
def create_and_fire_query(stringY,Proplist):
	propertieslist = findproperty(Proplist)
	sparql = SPARQLWrapper("http://nl.dbpedia.org/sparql")	
	File=open('pairCounts')
	maxlist, answerlist,urllist=[], [], []
	for line in File:
		elements=line.split("\t")
		if stringY == elements[0]:
			maxlist.append([elements[0],elements[1],elements[2].rstrip("\n")])
	maxlist.sort(key=lambda x: int(x[2]), reverse=True)
	if maxlist == []:
		try:
			wikipedia.set_lang("nl")
			wikisearch=wikipedia.search(stringY)
			for item in range(0,2):
				wikipage = wikipedia.page(wikisearch[item])
				url = wikipage.url
				answer = wikipage.title
				dblink= url.replace("https://nl.wikipedia.org/wiki/","http://nl.dbpedia.org/page/")
				urllist.append(dblink)

		#except wikipedia.exceptions.DisambiguationError as error:
			#link=url[0]
			#urllist.append(link)	
		except wikipedia.exceptions.WikipediaException as error:
			urlstring=stringY6.replace(" ","_")
			link="http://nl.dbpedia.org/page/"+urlstring
			urllist.append(link)			
		except IndexError:
			wikipage = wikipedia.page(stringY)
			url = wikipage.url
			dblink= url.replace("https://nl.wikipedia.org/wiki/","http://nl.dbpedia.org/page/")
			urllist.append(dblink)
		except:
			urlstring=stringY6.replace(" ","_")
			link="http://nl.dbpedia.org/page/"+urlstring
			urllist.append(link)					
				
	else:	
		link=maxlist[0][1]
		urllist.append(link)
	
	for link in urllist:
		print(link)
		for item in propertieslist:					
			sparql.setQuery("""
			SELECT ?antwoord
			WHERE {
			<"""+link+"""> """+ item + """ ?antwoord.
			} """)
		
			sparql.setReturnFormat(JSON)
			results = sparql.query().convert()
			for result in results["results"]["bindings"]:
				for arg in result :
					answer = arg + " : " + result[arg]["value"]
					answerlist.append(answer)
		
	return answerlist
					
if __name__ == "__main__":
	main(sys.argv)

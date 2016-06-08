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
		stringY=returnName2(line) #zin[1]
		Proplist=returnProp(line) #zin[1]
		answer = create_and_fire_query(stringY,Proplist)
		print(answer)

#def kiesfuncties():
	#soortvraag= xml.xpath('//node[ @rel="whd"] ')
	#if soortvraag =="Wanneer" or soortvraag == "Sinds wanneer":
		
	#if soortvraag =="Wie" or soortvraag =="Wat":
			
	#//node[ @postag="BW()" and @word="Hoe"] hoe zinnen
			
def returnName(line): #wie/wat vragen
	Ylist=[]
	Ylist2=[]
	Ylist3=[]
	line = line.rstrip()
	xml = alpino_parse(line)
	names = xml.xpath('//node[@spectype="deeleigen"] ')
	names2= xml.xpath('//node[@neclass="year"]')
	if names==[]:
		names3=xml.xpath('//node[ @cat="np" and @rel="obj1" and node[@rel="det"]]')
		for name in names3:	
			Ylist3.append(tree_yield(name))
		stringY3= ' '.join(Ylist3)
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
	
def tree_yield(xml):
	leaves = xml.xpath('descendant-or-self::node[@word]')
	words = []
	for l in leaves :
		words.append(l.attrib["word"])
	return " ".join(words)	
			
		
def create_and_fire_query(stringY,Proplist):
	sparql = SPARQLWrapper("http://nl.dbpedia.org/sparql")	
	File=open('pairCounts')
	maxlist=[]
	for line in File:
		elements=line.split("\t")
		if stringY == elements[0]:
			maxlist.append([elements[0],elements[1],elements[2].rstrip("\n")])
	maxlist.sort(key=lambda x: int(x[2]), reverse=True)
	if maxlist == []:
		sys.exit("Error!, "+stringY+" wordt niet herkend door DBpedia")
	else:	
		link=maxlist[0][1]
		
	for X in Proplist:
	
		if X == "startdatum" or X=="begindatum" or X=="begonnen" or X=="beginnen":
			prop="dbpedia-owl:startDate"
			
		elif X == "plaats" or X=="locatie" or X=="plek" or X=="Waar":
			prop="dbpedia-owl:location"
			
		elif X == "lengte" or X=="hoogte" or X=="grootte" or X=="lang":
			prop="prop-nl:lengte"
			
		elif X == "coach":
			prop="prop-nl:bondscoach"	
			
		elif X == "trainer" or X=="oefenmeester" or X=="leermeester" or X=="getraind":
			prop="prop-nl:trainer"
			
		elif X == "coach":
			prop="prop-nl:bondscoach"
   		
		elif X == "motto" or X=="spreuk" or X=="slogan" or X=="slagzin" or X=="leus" or X=="leuze" or X=="kernspreuk":
			prop="prop-nl:motto"

		elif X == "sluiting" or X=="einddatum" or X=="sluitdatum" or X=="eind" or X=="sloten":
			prop="dbpedia-owl:endDate"		
			
		elif X == "gewicht" or X=="massa" or X=="zwaarte" or X=="zwaar":
			prop="prop-nl:gewicht"
			
		elif X == "bijnaam" or X=="alias" or X=="nickname":
			prop="prop-nl:bijnaam"
			
		elif X == "onderdeel" or X=="discipline" or X=="gebied" or X=="sectie" or X=="domein" or X=="vakgebied":
			prop="prop-nl:onderdeel"
			
		elif X == "geboorteplaats" or X == "bakermat" or X == "geboren" or X == "Waar":
			prop="prop-nl:geboorteplaats"						
									
	sparql.setQuery("""
	SELECT ?antwoord
	WHERE {
	<"""+link+""">"""+ prop + """ ?antwoord.
	} """)
	
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	for result in results["results"]["bindings"]:
		for arg in result :
			answer = arg + " : " + result[arg]["value"]
			return answer
					
if __name__ == "__main__":
	main(sys.argv)

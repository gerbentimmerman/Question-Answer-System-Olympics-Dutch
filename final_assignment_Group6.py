#!/usr/bin/env python3

# Final Assignment Taaltechnologie
# Gerben Timmerman s2769670
# Stan Snijders s2760002
# Robert Veenhoven s2770199
# Stan Korenromp s2717557

import socket
import sys
from lxml import etree
from SPARQLWrapper import SPARQLWrapper, JSON
import wikipedia
import propertiesdict

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
	
def leesbestand(argv):
	f= open(argv[1], "r")
	filedata = f.read()	
	newdata = filedata.replace(" spelen"," Spelen")
	newdata2 = newdata.replace(" olympisch"," Olympisch")
	newdata3 = newdata2.replace(" zomerspelen"," Zomerspelen")
	newdata4 = newdata3.replace(" winterspelen"," Winterspelen")
	ff = open("verbeter.txt",'w')
	ff.write(newdata4)
	ff.close()
	
	
def main(argv):
	leesbestand(argv)
	f=open("verbeter.txt", "r")
	schrijf= open("output.txt", "w")
	for line in f:
		zin=line.split("\t")
		ID=zin[0]
		print(ID)
		stringY=returnName(zin[1])
		Proplist=returnProp(zin[1])
		Keuzewoord = returnKeuzewoord(zin[1])
		answer = create_and_fire_query(stringY,Proplist,Keuzewoord)
		antwoordstring="\t".join(answer)
		Write=ID+"\t"+antwoordstring+"\n"
		schrijf.write(Write)
	schrijf.close()	
			
			
def returnName(line):
	Ylist, Ylist2, Ylist3, Ylist4, sportlist, landlist, NLlist=[],[],[],[],[],[],[]
	line = line.rstrip()
	xml = alpino_parse(line)
	sporten = xml.xpath('//node[@word="Worstelen" or @word="hoogspringen" or @word="basketbal" or @word="taekwondo" or @word="kogelstoten" or @word="korfbal" or @word="judo" or @word="boogschieten"]')
	for sport in sporten:
		sportlist.append(tree_yield(sport))
	stringsport=' '.join(sportlist)
	landen = xml.xpath('//node[@word="Hongarije" or @word="Nederland" or @word="denemarken" or @word="Oostenrijk" or @word="Canada" or @word="Sovjet-Unie" or @word="indonesie" or @word="China" or @word="jamaica" or @word="Griekenland"]')
	NL = xml.xpath('//node[@word="Nederlandse" or @word="Nederlands" or @word="Nederlanders"]')
	for land in NL:
		NLlist.append(tree_yield(land))
	stringNL=' '.join(NLlist)
	for land in landen:
		landlist.append(tree_yield(land))
	stringLand=' '.join(landlist)
	if stringNL != "":
		stringLand="Nederland"
	names = xml.xpath('//node[@spectype="deeleigen"] ')
	names2= xml.xpath('//node[@neclass="year"]')
	if names==[]:
		names3=xml.xpath('//node[ @cat="np" and @rel="obj1" and node[@rel="det"]]')
		for name in names3:	
			Ylist3.append(tree_yield(name))
		stringY3= ' '.join(Ylist3)
		stringY4=stringY3.rstrip()
		stringY5=stringY4.replace("het ","")
		stringY6=stringY5.replace("de ","")
		if stringLand != "":
			stringY3=stringLand+" op de "+stringY3
			stringY6=stringY3.rstrip()
		if stringsport != "":
			stringY6=stringsport
		if names3==[]:
			names4=xml.xpath('//node[ @rel="su"]')
			for name in names4:	
				Ylist4.append(tree_yield(name))
			stringY3= ' '.join(Ylist4)
			stringY4=stringY3.rstrip()
			stringY5=stringY4.replace("het ","")
			stringY6=stringY5.replace("de ","")
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
		if stringsport != "":
			stringY6=stringsport
		if stringLand != "":
			stringY3=stringLand+" op de "+stringY+" van "+stringY2
			stringY6=stringY3.rstrip()			
	return stringY6
	
			
def returnProp(line):
	Proplist=[]
	line = line.rstrip()
	xml = alpino_parse(line)
	names = xml.xpath('//node[@rel="hd" or @pos="adj" or @pos="noun" or @rel="mod" or @pt="tw" or @rel="svp"]')
	for name in names :
		Proplist.append(tree_yield(name))
	return Proplist
	
def returnKeuzewoord(line):
	line = line.rstrip()
	xml = alpino_parse(line)
	names = xml.xpath('//node[@rel="whd" or @pt="vnw"]')
	Keuzewoordlist=[]
	for name in names:
		Keuzewoordlist = tree_yield(name).split()
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
	elif 'Hoeveel' in Keuzewoordlist or 'hoeveel' in Keuzewoordlist:
		Keuzewoord = 'hoeveel'
	else:
		Keuzewoord= 'wie'
	return Keuzewoord
	
def tree_yield(xml):
	leaves = xml.xpath('descendant-or-self::node[@word]')
	words = []
	for l in leaves :
		words.append(l.attrib["word"])
	return " ".join(words)	
	
def findproperty(searchwordlist,Keuzewoord):
	propertylist = []
	rightdict = propertiesdict.dictfinder(Keuzewoord)
	for searchword in searchwordlist:
		for property,words in rightdict.items():
			for word in rightdict[property]:
				if searchword == word:
					propertylist.append(property)
	return propertylist		
		
def create_and_fire_query(stringY,Proplist,Keuzewoord):
	propertieslist = findproperty(Proplist,Keuzewoord)
	sparql = SPARQLWrapper("http://nl.dbpedia.org/sparql")	
	File=open('pairCounts')
	maxlist,urllist=[], []
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
				dblink= url.replace("https://nl.wikipedia.org/wiki/","http://nl.dbpedia.org/resource/")
				urllist.append(dblink)
		except wikipedia.exceptions.WikipediaException as error:
			urlstring=stringY.replace(" ","_")
			link="http://nl.dbpedia.org/page/"+urlstring
			urllist.append(link)			
		except:
			urlstring=stringY.replace(" ","_")
			link="http://nl.dbpedia.org/page/"+urlstring
			urllist.append(link)
						
				
	else:	
		link=maxlist[0][1]
		urllist.append(link)
	answerlist1 = []
	for link in urllist:
		answerlist = []
		for item in propertieslist:
			sparql = SPARQLWrapper("http://nl.dbpedia.org/sparql")
			sparql.setQuery("""
			SELECT ?antwoord
			WHERE {
			<"""+link+"""> """+ item + """ ?antwoord .
			} """)
			
			sparql.setReturnFormat(JSON)
			results = sparql.query().convert()
			for result in results["results"]["bindings"]:
				for arg in result :
					answer = result[arg]["value"]
					answerlist.append(answer)
					answerlist1 += answerlist
	return list(set(answerlist1))




if __name__ == "__main__":
	main(sys.argv)

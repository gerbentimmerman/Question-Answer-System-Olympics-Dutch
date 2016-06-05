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

def print_example_queries():
    questions = ["Wanneer begonnen de Olympische Winterspelen 2014?",
              "In welke stad werden de Olympische Zomerspelen 2008 gehouden?",
              "Hoe lang is Usain Bolt?",
              "Wat is de naam van de trainer van Usain Bolt?",
              "Welk motto had de Olympische Zomerspelen 2008?",
              "Op welke datum was de afsluiting van de Olympische Zomerspelen 2008?",
              "Wat is de bijnaam van Epke Zonderland?",
              "Hoe heet de fakkeldrager op de Olympische Winterspelen 2010?",
              "Wie heeft de Olympische Winterspelen 2014 geopend?",
              "Wat is de naam van de ploeg van Sven Kramer?"]
    for question in questions:
        print(question)

def main(argv):
    print_example_queries()
    print()
    for line in sys.stdin:
        line = line.rstrip()
        answer = create_and_fire_query(line)
        print(answer + "\n")

def create_and_fire_query(question):
    if question == "":
        sys.exit("Vul alsjeblieft een vraag in aan de hand van de voorbeeldzinnen.")
    getname = getName(question)
    getprop = getProp(question)
    sparql = SPARQLWrapper("http://nl.dbpedia.org/sparql")
    pairCounts = open('pairCounts')
    sortlijst = []
    for line in pairCounts:
        items = line.split("\t")
        if getname == items[0]:
            sortlijst.append([items[0], items[1], items[2].rstrip("\n")])
    sortlijst.sort(key=lambda x: int(x[2]))
    sortlijst.reverse()

    if sortlijst == []:
        sys.exit("Helaas kan deze zoekopdracht niet gevonden worden")
    else:
        Y = sortlijst[0][1]

    X = get_property(getprop)

    query = """ select ?antwoord
            WHERE {
            <""" + Y + """>""" + X +""" ?antwoord
            }"""
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        for arg in result:
            answer = arg + " : " + result[arg]["value"]
        return answer

def getName(question):
    deeleigenlist = []
    xml = alpino_parse(question)
    names = xml.xpath('//node[@spectype = "deeleigen"]')
    for name in names:
        deeleigenlist.append(tree_yield(name))
    deeleigen = " ".join(deeleigenlist)
    return deeleigen

def getProp(question):
    propertylist = []
    xml = alpino_parse(question)
    properties = xml.xpath('//node[@rel = "hd"]')
    for property in properties:
        propertylist.append(tree_yield(property))
    return propertylist

def get_property(proplist):
    for prop in proplist:
        if prop == "startdatum" or prop == "begindatum" or prop == "start" or prop == "begint" or prop =="startte" or prop == "begon" or prop == "startten" or prop == "begonnen":
            uri = "prop-nl:opening"
        elif prop == "plaats" or prop == "stad" or prop == "locatie" or prop == "plek":
            uri = "prop-nl:plaats"
        elif prop == "lengte" or prop == "grootte" or prop == "hoogte" or prop == "lang":
            uri = "prop-nl:lengte"
        elif prop == "trainer" or prop == "coach" or prop == "oefenmeester" or prop == "getraind":
            uri = "prop-nl:trainer"
        elif prop == "motto" or prop == "leus" or prop == "slogan":
            uri = "prop-nl:motto"
        elif prop == "sluitingsdatum" or prop == "einddatum" or prop == "afsluiting" or prop == "sloot" or prop == "sloten" or prop == "eindigden":
            uri = "prop-nl:sluiting"
        elif prop == "bijnaam" or prop == "nickname" or prop == "alias":
            uri = "prop-nl:bijnaam"
        elif prop == "fakkeldrager" or prop == "vlamdrager" or prop == "vuurdrager" or prop == "vuur":
            uri = "prop-nl:vlam"
        elif prop == "opener" or prop == "ziener" or prop == "geopend" or prop == "opende":
            uri = "prop-nl:opener"
        elif prop == "ploeg" or prop == "team" or prop == "squad" or prop == "groep":
            uri = "dbpedia-owl:team"
        elif prop =="deelnemers" or prop == "atleten" or prop == "sporters":
            uri = "prop-nl:atleten"
    return uri

def tree_yield(xml):
    leaves = xml.xpath('descendant-or-self::node[@word]')
    words = []
    for l in leaves:
        words.append(l.attrib["word"])
    return " ".join(words)

# parse input sentence and return alpino output as an xml element tree
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
    # print(bytes_received.decode('utf-8'), file=sys.stderr)
    xml = etree.fromstring(bytes_received)
    return xml

if __name__ == '__main__':
    main(sys.argv)
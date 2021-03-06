#!/usr/bin/env python3

import sys

def dictfinder(Keuzewoord):
	
	wie_wat_dictionary = {
		'prop-nl:volgende': ["aankomende","volgende","komende","eerstvolgende","na"],
		'prop-nl:vorige': ["vorige","voorgaand","laatste","laatst"],
		'prop-nl:locatie': ["baan", "locatie"],
		'prop-nl:debuut': ["debuut", "eerste", "wedstrijd"],
		'prop-nl:bijnaam': ["bijnaam", "nickname", "bijnamen"],
		'prop-nl:onderdeel': ["stok","onderdeel", "specialisatie","sport"],
		'prop-nl:naam': ["naam", "volledige", "namen"],
		'prop-nl:motto': ["motto"],
		'prop-nl:wrman': ["wereldrecord"],
		'prop-nl:landen': ["aantal","landen"],
		'foaf:homepage': ["website","site"],
		'prop-nl:geboorteplaats': ["geboorteplaats","geboortestad"],
		'prop-nl:rang': ["rang"],
		'prop-nl:bijnamen': ["bijnamen"],
		'prop-nl:vorigenamen': ["voormalige"],
		'rdfs:comment': ["bekend"],
		'prop-nl:sport': ["sporten", "aantal"],
		'prop-nl:lengte': ["lengte"],
		'prop-nl:discipline':["sport","soort","discipline", "olympische-sportdiscipline"],
		'prop-nl:olympischKampioen': ["kampioen","snelste","beste"],
		'prop-nl:opening': ["startdatum", "start","opening","begin"],
		'prop-nl:sluiting': ["sloten","gesloten","sloot","afgesloten"],
		'prop-nl:organisator': ["organisator","georganiseerd","organiseren","organiseert"],
		'prop-nl:eerste': ["eerste", "moderne","allereerste"],
		'prop-nl:atleten': ["atleten","deelnemende", "deelnemers"],
		'prop-nl:soort': ["soort","type"],
		'prop-nl:vlaggendrager': ["vlaggendrager","vlagdragers", "vlaggendragers","vlag"],
		'prop-nl:opener': ["geopend", "opening","opende","openden","opent"],
		'prop-nl:coach': ["coach","trainer","begeleider"],
		'prop-nl:trainer': ["trainer", "getraind","coach"],
		'prop-nl:bondscoach': ["bondscoach","coach","trainer"],
		'prop-nl:vlam': ["vlam","vlamdragers","fakkel","droegen", "vuur","fakkeldragers","toorts"],
		'dcterms:subject': ["kampioen","beste"],
		'prop-nl:voorzitter': ["voorzitter","topman","president","leider","voorman"],
		'prop-nl:topscorer': ["topscorer"],
		'prop-nl:goudNaam': ["gewonnen","goud","gouden"],
		'dbpedia-owl:currentWorldChampion': ["wereldrecordhouders","wereldkampioenen","wereldkampioen","huidige","huidig"],
		'prop-nl:eed': ["eed"],
		'prop-nl:presentatie': ["presentatoren","presentator","presentatrice","presenteerde","presenteerden"],
		'prop-nl:architect': ["ontwierp","designde","vorm","ontworpen","vormgegeven"],
		'prop-nl:zilverNaam': ["zilver", "zilveren"],
		'prop-nl:referee': ["scheidsrechters","scheidsrechter","scheids"],
		'prop-nl:gewicht': ["gewicht"]
	}
	
	wanneer_dictionary = {
		'prop-nl:eerste': ["eerste","eerst"],
		'prop-nl:geboortedatum': ["geboren"],
		'prop-nl:vorige': ["vorige","laatste","voor","laatst","voorgaand","voorgaande"],
		'prop-nl:volgende': ["volgende","eerstvolgende","aankomende","komende","na"],
		'prop-nl:sluiting': ["sluiting","afsluiting","eindceremonie","einde","eind","eindigden","beeindigd","afgesloten"],
		'prop-nl:opening': ["start","begin","begonnen","opening","beginnen","geopend"],
		'prop-nl:olympisch': ["Olympisch","olympisch","olympische"],
		'prop-nl:paralympisch': ["paralympisch","paralympische","onderdeel"],
		'prop-nl:overleden': ["overleden","overleed"],
		'prop-nl:gesticht': ["gesticht"]
	}

	waar_dictionary = {
		'prop-nl:eerste': ["eerste","eerst"],
		'prop-nl:geboortestad': ["geboren"],
		'prop-nl:vorige': ["vorige","laatste","voor","laatst","voorgaand","voorgaande"],
		'prop-nl:volgende': ["volgende","eerstvolgende","aankomende","komende","na"],
		'prop-nl:olympisch': ["olympisch","paralympisch","olympische","paralympische"],
		'dbpedia-owl:flagBearer': ["vlaggendrager","vlaggendragers","dragers","droegen","droeg"],
		'prop-nl:zilverNaam': ["zilver","tweede","zilveren"],
		'prop-nl:goudNaam': ["goud","eerste","gouden"],
		'prop-nl:soort': ["seizoen"],
		'prop-nl:jaar': ["jaar","jaartal","jaren","jaartallen"],
		'prop-nl:discipline': ["sport","discipline","disciplines","onderdeel","onderdelen"],
		'prop-nl:plaats': ["stad","stadje","plaats","locatie","steden","locaties","plek","gehouden"],
		'dbpedia-owl:location': ["land"],
		'prop-nl:area': ["regio","gebied"],
		'prop-nl:coach': ["coach","trainer","begeleider"],
		'prop-nl:motto': ["motto","slagzin","slogan"]
	}

	hoe_dictionary = {
		'prop-nl:lengte' : ["lang","groot"],
		'prop-nl:organisator' : ["organiseert"],
		'prop-nl:naam' : ["genoemd", "heet"],
		'prop-nl:gewicht' : ["zwaar","weegt"]
	}
	
	hoeveel_dictionary = {
		'prop-nl:brons' : ["bronzen","bronze","brons"],
		'prop-nl:zilver' : ["zilver","zilveren"],
		'prop-nl:goud' : ["goud","gouden"],
		'prop-nl:totaal': ["medailles"],
		'prop-nl:landen': ["landen"],
		'prop-nl:capaciteit':["zitplaatsen","bank","bankjes","plaatsen"],
		'prop-nl:sport':["zomersporten","sporten","sport","wintersporten"],
		'prop-nl:atleten':["deelnemers","mee","sporters","spelers","atleten"],
		'prop-nl:vlam':["fakkeldragers"],
		'prop-nl:leden':["leden"],
		'prop-nl:evenementen':["sportevenementen","evenementen","evenement", "activiteit", "activiteiten"],
		'prop-nl:spelen':["Olympiade"],
		'prop-nl:inwoners':["inwoners","bewoners","mensen"],
		'prop-nl:kampioenschappen':["onderdelen"],
		'prop-nl:totaalDeelnemers':["deelnemers","deel","atleten","landen"],
		'prop-nl:gewicht':["weegt","gewicht"]
	}
		
	welke_dictionary = {
		'prop-nl:slagen' : ["zwemstijlen"],
		'prop-nl:geboortestad' : ["stad", "dorp","plaats"],
		'prop-nl:geboorteplaats' : ["stad", "dorp","plaats"],
		'prop-nl:bijnaam' : ["bijnamen","nickname","alias", "bijnaam"],
		'prop-nl:discipline' : ["discipline", "sport","disciplines","varianten","onderdeel"],
		'prop-nl:positie' : ["positie"],
		'prop-nl:plaats' : ["land","gehouden","spelen af", "locatie(s)","plek","stad","locaties","steden","plaats","stadje","dorp"],
		'prop-nl:opening' : ["beginnen","begonnen", "geopend", "opening","gestart", "begon", "opende"],
		'prop-nl:eerste' : ["eerste", "eerst"],
		'prop-nl:sluiting' : ["sloten","afsluiting","afsluiten"],
		'prop-nl:organisator' : ["georganiseerd", "organisatie","organiseert"],
		'prop-nl:evenementen':["sportevenementen","evenementen","evenement", "activiteit", "activiteiten"],
		'prop-nl:geboortedatum' : ["geboren"],
		'prop-nl:specialisatie' : ["gespecialiseerd","specialisatie"],
		'prop-nl:soort' : ["seizoen","categorie","type"],
		'prop-nl:jaar' : ["jaar"],
		'prop-nl:vlaggendrager' : ["vlaggendrager","vlaggendragers"],
		'prop-nl:rugnummer' : ["rugnummer"],
		'prop-nl:motto' : ["motto","leus"],
		'prop-nl:jury' : ["rol"],
		'dbpedia-owl:torchBearer' : ["rol","flame","vlam"],
		'prop-nl:olympischKampioen' : ["Kampioen","kampioen"],
		'prop-nl:accommodatie' : ["stadions","accomodatie"],
		'prop-nl:olympischespelen' : ["nam","deel"],
		'prop-nl:debuut' : ["debuut"],
		'prop-nl:coach' : ["coached","coach","trainer"],
		'prop-nl:volgende' : ["volgende","eerstvolgende"],
		'dbpedia-owl:goldMedalist' : ["gouden","goud"],
		'prop-nl:categorie' : ["sportcategorien","categorie"],
		'prop-nl:vlam' : ["vuur"],
		'prop-nl:gewicht' : ["gewicht"]
	}

	if Keuzewoord == 'wat' or Keuzewoord == 'wie':
		return wie_wat_dictionary
	elif Keuzewoord == 'wanneer':
		return wanneer_dictionary
	elif Keuzewoord == 'hoe':
		return hoe_dictionary
	elif Keuzewoord == 'hoeveel':
		return hoeveel_dictionary
	elif Keuzewoord == 'welke':
		return welke_dictionary
	elif Keuzewoord == 'waar':
		return waar_dictionary

if __name__ == '__main__':
	main(sys.argv)

#!/usr/bin/env python3

import sys

def dictfinder(Keuzewoord):
	
	wie_wat_dictionary = {
		'prop-nl:volgende': ["aankomende","volgende","komende","eerstvolgende","na"],
		'prop-nl:vorige': ["vorige","voorgaand","laatste"],
		'prop-nl:locatie': ["baan", "locatie"],
		'prop-nl:debuut': ["debuut", "eerste", "wedstrijd"],
		'prop-nl:bijnaam': ["bijnaam", "nickname", "bijnamen"],
		'prop-nl:onderdeel': ["stok","onderdeel", "specialisatie","sport"],
		'prop-nl:naam': ["naam", "volledige", "namen"],
		'prop-nl:motto': ["motto"],
		'prop-nl:wrman': ["wereldrecord"],
		'prop-nl:landen': ["aantal","landen"],
		'foaf:homepage': ["website"],
		'prop-nl:geboorteplaats': ["geboorteplaats"],
		'prop-nl:rang': ["rang"],
		'prop-nl:bijnamen': ["bijnamen"],
		'prop-nl:vorigenamen': ["voormalige", "naam"],
		'rdfs:comment': ["bekend"],
		'prop-nl:sport': ["sporten", "aantal"],
		'prop-nl:lengte': ["lengte"],
		'prop-nl:discipline':["sport","soort","discipline", "olympische-sportdiscipline"],
		'prop-nl:olympischKampioen': ["kampioen","snelste"],
		'prop-nl:opening': ["startdatum", "start"],
		'prop-nl:sluiting': ["sloten"],
		'prop-nl:organisator': ["organisator","georganiseerd","organiseren","organiseert"],
		'prop-nl:eerste': ["eerste", "moderne"],
		'prop-nl:atleten': ["atleten","deelnemende", "deelnemers"],
		'prop-nl:soort': ["soort"],
		'prop-nl:vlaggendrager': ["vlaggendrager","vlagdragers", "vlaggendragers","vlag"],
		'prop-nl:opener': ["geopend", "opening","opende"],
		'prop-nl:coach': ["coach","trainer"],
		'prop-nl:trainer': ["trainer", "getraind","coach"],
		'prop-nl:bondscoach': ["bondscoach","coach","trainer"],
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
	
	wanneer_dictionary = {
		'prop-nl:eerste': ["eerste"],
		'prop-nl:geboortedatum': ["geboren"],
		'prop-nl:vorige': ["vorige","laatste","voor"],
		'prop-nl:volgende': ["volgende","eerstvolgende","aankomende","komende","na"],
		'prop-nl:sluiting': ["sluiting","afsluiting","eindceremonie","einde","eind","eindigden"],
		'prop-nl:opening': ["start","begin","begonnen","opening","beginnen"],
		'prop-nl:olympisch': ["Olympisch","olympisch","olympische"],
		'prop-nl:paralympisch': ["paralympisch","paralympische","onderdeel"],
		'prop-nl:overleden': ["overleden","overleden"],
		'prop-nl:gesticht': ["gesticht"]
	}

	waar_dictionary = {
		'prop-nl:eerste': ["eerste","eerst"],
		'prop-nl:geboortestad': ["geboren"],
		'prop-nl:vorige': ["vorige","laatste","voor","laatst","voorgaand"],
		'prop-nl:volgende': ["volgende","eerstvolgende","aankomende","komende","na"],
		'prop-nl:olympisch': ["olympisch","paralympisch","olympische","paralympische"],
		'dbpedia-owl:flagBearer of': ["vlaggendrager"],
		'prop-nl:zilverNaam of': ["zilver","tweede"],
		'prop-nl:goudNaam of': ["goud","eerste"],
		'prop-nl:soort': ["seizoen"],
		'prop-nl:jaar': ["jaar","jaartal","jaren","jaartallen"],
		'prop-nl:discipline': ["sport","discipline","disciplines"],
		'prop-nl:plaats': ["stad","stadje","plaats","locatie","steden","locaties"],
		'dbpedia-owl:location': ["land"],
		'prop-nl:area': ["regio","gebied"],
		'prop-nl:coach': ["coach","trainer"],
		'prop-nl:motto': ["motto"]
	}

	hoe_dictionary = {
		'prop-nl:lengte' : ["lang"],
		'prop-nl:organisator' : ["organiseert"],
		'prop-nl:naam' : ["genoemd", "heet"],
		'prop-nl:gewicht' : ["zwaar"]
	}
	
	hoeveel_dictionary = {
		'prop-nl:brons' : ["bronzen","bronze"],
		'prop-nl:zilver' : ["zilver","zilveren"],
		'prop-nl:goud' : ["goud","gouden"],
		'prop-nl:totaal': ["medailles"],
		'prop-nl:landen': ["landen"],
		'prop-nl:capaciteit':["zitplaatsen"],
		'prop-nl:sport':["zomersporten","sporten","sport","wintersporten"],
		'prop-nl:atleten':["deelnemers","mee","sporters","spelers","atleten"],
		'prop-nl:vlam':["fakkeldragers"],
		'prop-nl:leden':["leden"],
		'prop-nl:evenementen':["sportevenementen","evenementen"],
		'prop-nl:spelen':["Olympiade"],
		'prop-nl:inwoners':["inwoners"],
		'prop-nl:kampioenschappen of':["onderdelen"],
		'prop-nl:totaalDeelnemers':["deelnemers"],
		'prop-nl:gewicht':["weegt","gewicht"]
	}
		
	welke_dictionary = {
		'prop-nl:slagen' : ["zwemstijlen"],
		'prop-nl:geboortestad' : ["stad", "dorp","plaats"],
		'prop-nl:geboorteplaats' : ["stad", "dorp","plaats"],
		'prop-nl:bijnaam' : ["bijnamen"],
		'prop-nl:discipline' : ["discipline", "sport","disciplines","varianten","onderdeel"],
		'prop-nl:positie' : ["positie"],
		'prop-nl:plaats' : ["land","gehouden","spelen af", "locatie(s)","plek","stad","locaties","steden","plaats","stadje"],
		'prop-nl:opening' : ["beginnen", "geopend", "opening","gestart", "begon", "opende"],
		'prop-nl:eerste' : ["eerste", "eerst"],
		'prop-nl:sluiting' : ["sloten"],
		'prop-nl:slagen' : ["zwemstijlen"],
		'prop-nl:organisator' : ["georganiseerd", "organisatie"],
		'prop-nl:evenementen' : ["evenement"],
		'prop-nl:geboortedatum' : ["geboren"],
		'prop-nl:specialisatie' : ["gespecialiseerd","specialisatie"],
		'prop-nl:soort' : ["seizoen"],
		'prop-nl:jaar' : ["jaar"],
		'prop-nl:vlaggendrager' : ["vlaggendrager","vlaggendragers"],
		'is dbpedia-owl:goldMedalist of' : ["gouden"],
		'prop-nl:rugnummer' : ["rugnummer"],
		'prop-nl:motto' : ["motto"],
		'is prop-nl:jury of' : ["rol"],
		'is dbpedia-owl:torchBearer of' : ["rol"],
		'is dbpedia-owl:torchBearer of' : ["flame"],
		'is prop-nl:olympischKampioen of' : ["Kampioen"],
		'prop-nl:accommodatie' : ["stadions","accomodatie"],
		'prop-nl:olympischespelen' : ["nam deel"],
		'prop-nl:debuut' : ["debuut"],
		'is prop-nl:coach of' : ["coached"],
		'prop-nl:volgende' : ["volgende"],
		'is dbpedia-owl:goldMedalist of' : ["gouden"],
		'prop-nl:categorie' : ["sportcategorien"],
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
	else:
		return wie_wat_dictionary	

if __name__ == '__main__':
    main(sys.argv)

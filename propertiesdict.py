#!/usr/bin/env python3

import sys



def wie_wat_dictionary(eigenschap):
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
        'prop-nl:referee': ["scheidsrechters","scheidsrechter"],

    }
	

def wanneer_dictionary(eigenschap):
    wanneer_dictionary = {
		'prop-nl:eerste': ["eerste"],
		'prop-nl:geboortedatum': ["geboren"],
		'prop-nl:vorige': ["vorige","laatste","voor"],
		'prop-nl:volgende': ["volgende","eerstvolgende","aankomende","komende","na"],
		'prop-nl:sluiting': ["sluiting","afsluiting","eindceremonie","einde","eind","eindigden"],
		'prop-nl:opening': ["start","begin","begonnen","opening","beginnen"],
		'prop-nl:olympisch': ["olympisch","paralympisch","olympische","paralympische"],
		'prop-nl:overleden': ["overleden","overleden"],
		'prop-nl:gesticht': ["gesticht"]

    }
    
def waar_in_dictionary(eigenschap):
    waar_in_dictionary = {
        'prop-nl:eerste': ["eerste","eerst"],
        'prop-nl:geboortedatum': ["geboren"],
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

def findproperty(searchwordlist):
	for searchword in searchwordlist:
		for property,words in wie_wat_dictionary.items():
			for word in wie_wat_dictionary[property]:
				if searchword == word:
					propertylist = []
					propertylist.append(property)
	return propertylist

if __name__ == '__main__':
    main(sys.argv)

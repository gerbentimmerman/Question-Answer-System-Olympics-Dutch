#!/usr/bin/env python3

import sys



def wie_wat_dictionary(eigenschap):
    dictionary = {
        'prop-nl:volgende': ["aankomende","volgende","komende","eerstvolgende"],
        'prop-nl:vorige': ["vorige","voorgaand"],
        'prop-nl:locatie': ["baan"],
        'prop-nl:debuut': ["debuut", "eerste professionele wedstrijd"],
        'prop-nl:bijnaam': ["bijnaam", "nickname"],
        'prop-nl:onderdeel': ["stok","onderdeel"],
        'prop-nl:naam': ["naam"],
        'prop-nl:motto': ["motto",""],
        'prop-nl:wrman': ["wereldrecord"],
        'prop-nl:landen': ["aantal"],
        'dbpedia-owl:wikiPageExternalLink': ["website"],
        'prop-nl:geboortestad': ["geboorteplaats"]
    }
	dictionary[eigenschap]

    wanneer= {
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
    
    waar_in_dicationary = {
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
                    print(property)


if __name__ == '__main__':
    main(sys.argv)
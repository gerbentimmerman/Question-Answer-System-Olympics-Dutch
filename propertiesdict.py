#!/usr/bin/env python3

import sys



def main(wie_wat_dictionary):
    wie_wat_dictionary = {
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
    
    property = "bijnaam"
    for key,lists in wie_wat_dictionary.items():
        for word in wie_wat_dictionary[key]:
            if property == word:
                print(key)


if __name__ == '__main__':
    main(sys.argv)
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDFS
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD

import json
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

catalogo = Element('catalogo')
with open('SoilDB.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)


g = Graph()
result = g.parse("C:\\Users\\inesd\\OneDrive\\Escritorio\\4º Ingeniería Bioinformática\\Primer Cuatrimestre\\Estándares de Datos Abiertos e Integración de Datos\\Final Course Project\\json-rdf\\soilDB.owl")
base = 'http://www.semanticweb.org/inma/ontologies/2021/09/untitled-ontology-6'
#type = g.value(semweb, RDFS.label)


for row in obj:
    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#CODE"),
        Literal(str(row['CODE']), datatype=XSD.string)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#PHOTOGRAPHS"),
        Literal(str(row['PHOTOGRAPHS']), datatype=XSD.string)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#DESCRIPTION"),
        Literal(str(row['DESCRIPTION']), datatype=XSD.string)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#COORDINATES_X"),
        Literal(str(row['COORDINATES X']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#COORDINATES_Y"),
        Literal(str(row['COORDINATES Y']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#ALTITUDE"),
        Literal(str(row['ALTITUDE']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#INCLINE"),
        Literal(str(row['INCLINE']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#GRAVES"),
        Literal(str(row['GRAVES']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#VERY_THICK_SAND"),
        Literal(str(row['VERY THICK SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#THICK_SAND"),
        Literal(str(row['THICK SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#MEDIUM_SAND"),
        Literal(str(row['MEDIUM SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#FINE_SAND"),
        Literal(str(row['FINE SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#VERY_FINE_SAND"),
        Literal(str(row['VERY FINE SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#TOTAL_SAND"),
        Literal(str(row['TOTAL SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#THICK_LIMES"),
        Literal(str(row['THICK LIMES']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#FINE_LIMES"),
        Literal(str(row['FINE LIMES']), datatype=XSD.int)
    ))
    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#TOTAL_LIMES"),
        Literal(str(row['TOTAL LIMES']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#CLAY"),
        Literal(str(row['CLAY']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#K_FACTOR"),
        Literal(str(row['K FACTOR']), datatype=XSD.double)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#APPARENT_DENSITY"),
        Literal(str(row['APPARENT DENSITY']), datatype=XSD.double)
    ))
    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#AGGREGATE_STABILITY"),
        Literal(str(row['AGGREGATE STABILITY']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#PERMEABILITY"),
        Literal(str(row['PERMEABILITY']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#DESCRIPTION"),
        Literal(str(row['DESCRIPTION']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#FIELD_CAPACITY"),
        Literal(str(row['FIELD CAPACITY']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#PERMANENT_WILTING_POINT"),
        Literal(str(row['PERMANENT WILTING POINT']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#HYDROPHOBICITY"),
        Literal(str(row['HYDROPHOBICITY']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#ORGANIC_CARBON"),
        Literal(str(row['ORGANIC CARBON']), datatype=XSD.string)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#C_FACTOR"),
        Literal(str(row['C FACTOR']), datatype=XSD.double)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#ELECTRIC_CONDUCTIVITY"),
        Literal(str(row['ELECTRIC CONDUCTIVITY']), datatype=XSD.string)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id']['$oid'])),
        URIRef(base + "#SPECTRAL_RESPONSE"),
        Literal(str(row['SPECTRAL RESPONSE ']), datatype=XSD.string)
    ))


f = open("PySoilDB.owl", "w")
f.write(result.serialize(format="xml"))
f.close()
#tostring(catalogo, encoding='unicode')

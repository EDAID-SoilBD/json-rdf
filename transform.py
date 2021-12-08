from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDFS
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD

import json
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

catalogo = Element('catalogo')
with open('SoildDB.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)


g = Graph()
result = g.parse(
    "K:\\Mi unidad\\Trabajo\\Docencia\\2021-2022\\Estándares de Datos e Integración de Datos\\esquemapersonas.owl")
base = 'http://www.semanticweb.org/ismaelnavas/ontologies/2021/10/untitled-ontology-72'
#type = g.value(semweb, RDFS.label)


for row in obj:
    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#CODE"),
        Literal(str(row['CODE']), datatype=XSD.string)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#PHOTOGRAPHS"),
        Literal(str(row['PHOTOGRAPHS']), datatype=XSD.string)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#DESCRIPTION"),
        Literal(str(row['DESCRIPTION']), datatype=XSD.string)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#COORDINATES X"),
        Literal(str(row['COORDINATES X']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#COORDINATES Y"),
        Literal(str(row['COORDINATES Y']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#ALTITUDE"),
        Literal(str(row['ALTITUDE']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#INCLINE"),
        Literal(str(row['INCLINE']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#GRAVES"),
        Literal(str(row['GRAVES']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#VERY THICK SAND"),
        Literal(str(row['VERY THICK SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#THICK SAND"),
        Literal(str(row['THICK SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#MEDIUM SAND"),
        Literal(str(row['MEDIUM SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#FINE SAND"),
        Literal(str(row['FINE SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#VERY FINE SAND"),
        Literal(str(row['VERY FINE SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#TOTAL SAND"),
        Literal(str(row['TOTAL SAND']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#THICK LIMES"),
        Literal(str(row['THICK LIMES']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#FINE LIMES"),
        Literal(str(row['FINE LIMES']), datatype=XSD.int)
    ))
    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#TOTAL LIMES"),
        Literal(str(row['TOTAL LIMES']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#CLAY"),
        Literal(str(row['CLAY']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#K FACTOR"),
        Literal(str(row['K FACTOR']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#APPARENT DENSITY"),
        Literal(str(row['APPARENT DENSITY']), datatype=XSD.int)
    ))
    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#AGGREGATE STABILITY"),
        Literal(str(row['AGGREGATE STABILITY']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#PERMEABILITY"),
        Literal(str(row['PERMEABILITY']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#DESCRIPTION"),
        Literal(str(row['DESCRIPTION']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#FIELD CAPACITY"),
        Literal(str(row['FIELD CAPACITY']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#PERMANENT WILTING POINT"),
        Literal(str(row['PERMANENT WILTING POINT']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#HYDROPHOBICITY"),
        Literal(str(row['HYDROPHOBICITY']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#ORGANIC CARBON"),
        Literal(str(row['ORGANIC CARBON']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#C FACTOR"),
        Literal(str(row['C FACTOR']), datatype=XSD.int)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#ELECTRIC CONDUCTIVITY"),
        Literal(str(row['ELECTRIC CONDUCTIVITY']), datatype=XSD.string)
    ))

    result.add((
        URIRef(base + "#" + str(row['_id'])),
        URIRef(base + "#SPECTRAL RESPONSE "),
        Literal(str(row['SPECTRAL RESPONSE ']), datatype=XSD.string)
    ))


f = open("PyFauna.owl", "w")
f.write(result.serialize(format="xml").decode())
f.close()
#tostring(catalogo, encoding='unicode')

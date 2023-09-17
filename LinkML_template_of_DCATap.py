# Auto generated from None by pythongen.py version: 0.9.0
# Generation date: 2023-09-06T17:25:01
# Schema: DCATap_LinkML_Template
#
# id: https://ndfi4cat.de/linkml/tests/DCATap
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DCATAP_LINKML_TEMPLATE_FROM_NFDI4CAT = CurieNamespace('DCATap_LinkML_Template_from_NFDI4Cat', 'https://ndfi4cat.de/linkml/tests/DCATap')
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms')
CC = CurieNamespace('cc', 'http://creativecommons.org/ns')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCATAP = CurieNamespace('dcatap', 'http://data.europa.eu/r5r/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LCON = CurieNamespace('lcon', 'http://www.w3.org/ns/locn')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ODRL = CurieNamespace('odrl', 'http://www.w3.org/ns/odrl/2/')
ORG = CurieNamespace('org', 'http://www.w3.org/ns/org')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SH = CurieNamespace('sh', 'http://www.w3.org/ns/shacl')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SPDX = CurieNamespace('spdx', 'http://spdx.org/rdf/terms')
TIME = CurieNamespace('time', 'http://www.w3.org/2006/time')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SH


# Types

# Class references



@dataclass
class Catalog(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Catalog
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "Catalog"
    class_model_uri: ClassVar[URIRef] = SH.Catalog

    dct_description_mm: Union[Union[dict, "Literal"], List[Union[dict, "Literal"]]] = None
    dct_title_mm: Union[Union[dict, "Literal"], List[Union[dict, "Literal"]]] = None
    dcat_themeTaxonomy_rm: Optional[Union[Union[dict, "SkosConceptScheme"], List[Union[dict, "SkosConceptScheme"]]]] = empty_list()
    dct_issued_rs: Optional[Union[dict, "TemporalLiteral"]] = None
    dct_language_rm: Optional[Union[Union[dict, "DctLinguisticSystem"], List[Union[dict, "DctLinguisticSystem"]]]] = empty_list()
    dct_modified_rs: Optional[Union[dict, "TemporalLiteral"]] = None
    foaf_homepage_rs: Optional[Union[dict, "Document"]] = None
    dct_rights_os: Optional[Union[dict, "RightsStatement"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dct_description_mm):
            self.MissingRequiredField("dct_description_mm")
        if not isinstance(self.dct_description_mm, list):
            self.dct_description_mm = [self.dct_description_mm] if self.dct_description_mm is not None else []
        self.dct_description_mm = [v if isinstance(v, Literal) else Literal(**as_dict(v)) for v in self.dct_description_mm]

        if self._is_empty(self.dct_title_mm):
            self.MissingRequiredField("dct_title_mm")
        if not isinstance(self.dct_title_mm, list):
            self.dct_title_mm = [self.dct_title_mm] if self.dct_title_mm is not None else []
        self.dct_title_mm = [v if isinstance(v, Literal) else Literal(**as_dict(v)) for v in self.dct_title_mm]

        if not isinstance(self.dcat_themeTaxonomy_rm, list):
            self.dcat_themeTaxonomy_rm = [self.dcat_themeTaxonomy_rm] if self.dcat_themeTaxonomy_rm is not None else []
        self.dcat_themeTaxonomy_rm = [v if isinstance(v, SkosConceptScheme) else SkosConceptScheme(**as_dict(v)) for v in self.dcat_themeTaxonomy_rm]

        if self.dct_issued_rs is not None and not isinstance(self.dct_issued_rs, TemporalLiteral):
            self.dct_issued_rs = TemporalLiteral()

        if not isinstance(self.dct_language_rm, list):
            self.dct_language_rm = [self.dct_language_rm] if self.dct_language_rm is not None else []
        self.dct_language_rm = [v if isinstance(v, DctLinguisticSystem) else DctLinguisticSystem(**as_dict(v)) for v in self.dct_language_rm]

        if self.dct_modified_rs is not None and not isinstance(self.dct_modified_rs, TemporalLiteral):
            self.dct_modified_rs = TemporalLiteral()

        if self.foaf_homepage_rs is not None and not isinstance(self.foaf_homepage_rs, Document):
            self.foaf_homepage_rs = Document()

        if self.dct_rights_os is not None and not isinstance(self.dct_rights_os, RightsStatement):
            self.dct_rights_os = RightsStatement()

        super().__post_init__(**kwargs)


@dataclass
class LicenseDocument(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT.LicenseDocument
    class_class_curie: ClassVar[str] = "dct:LicenseDocument"
    class_name: ClassVar[str] = "LicenseDocument"
    class_model_uri: ClassVar[URIRef] = SH.LicenseDocument

    dct_type_rm: Optional[Union[Union[dict, "SkosConcept"], List[Union[dict, "SkosConcept"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.dct_type_rm, list):
            self.dct_type_rm = [self.dct_type_rm] if self.dct_type_rm is not None else []
        self.dct_type_rm = [v if isinstance(v, SkosConcept) else SkosConcept(**as_dict(v)) for v in self.dct_type_rm]

        super().__post_init__(**kwargs)


@dataclass
class DataService(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.DataService
    class_class_curie: ClassVar[str] = "dcat:DataService"
    class_name: ClassVar[str] = "DataService"
    class_model_uri: ClassVar[URIRef] = SH.DataService

    dct_modified_ms: Union[dict, "SkosConcept"] = None
    adms_status_rs: Optional[Union[dict, "SkosConcept"]] = None
    dct_conformsTo_rs: Optional[Union[dict, "DctStandard"]] = None
    dct_issued_rs: Optional[Union[dict, "TemporalLiteral"]] = None
    dct_description_om: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()
    dct_language_om: Optional[Union[Union[dict, "DctLinguisticSystem"], List[Union[dict, "DctLinguisticSystem"]]]] = empty_list()
    dct_title_om: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dct_modified_ms):
            self.MissingRequiredField("dct_modified_ms")
        if not isinstance(self.dct_modified_ms, SkosConcept):
            self.dct_modified_ms = SkosConcept()

        if self.adms_status_rs is not None and not isinstance(self.adms_status_rs, SkosConcept):
            self.adms_status_rs = SkosConcept()

        if self.dct_conformsTo_rs is not None and not isinstance(self.dct_conformsTo_rs, DctStandard):
            self.dct_conformsTo_rs = DctStandard()

        if self.dct_issued_rs is not None and not isinstance(self.dct_issued_rs, TemporalLiteral):
            self.dct_issued_rs = TemporalLiteral()

        if not isinstance(self.dct_description_om, list):
            self.dct_description_om = [self.dct_description_om] if self.dct_description_om is not None else []
        self.dct_description_om = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_description_om]

        if not isinstance(self.dct_language_om, list):
            self.dct_language_om = [self.dct_language_om] if self.dct_language_om is not None else []
        self.dct_language_om = [v if isinstance(v, DctLinguisticSystem) else DctLinguisticSystem(**as_dict(v)) for v in self.dct_language_om]

        if not isinstance(self.dct_title_om, list):
            self.dct_title_om = [self.dct_title_om] if self.dct_title_om is not None else []
        self.dct_title_om = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_title_om]

        super().__post_init__(**kwargs)


class CatalogRecord(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.CatalogRecord
    class_class_curie: ClassVar[str] = "dcat:CatalogRecord"
    class_name: ClassVar[str] = "CatalogRecord"
    class_model_uri: ClassVar[URIRef] = SH.CatalogRecord


class Location(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT.Location
    class_class_curie: ClassVar[str] = "dct:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = SH.Location


class PeriodOfTime(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT.PeriodOfTime
    class_class_curie: ClassVar[str] = "dct:PeriodOfTime"
    class_name: ClassVar[str] = "PeriodOfTime"
    class_model_uri: ClassVar[URIRef] = SH.PeriodOfTime


class Dataset(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Dataset
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = SH.Dataset


class Distribution(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Distribution
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "Distribution"
    class_model_uri: ClassVar[URIRef] = SH.Distribution


class DatasetSeries(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.DatasetSeries
    class_class_curie: ClassVar[str] = "dcat:DatasetSeries"
    class_name: ClassVar[str] = "DatasetSeries"
    class_model_uri: ClassVar[URIRef] = SH.DatasetSeries


@dataclass
class Agent(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF.Agent
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = SH.Agent

    name: str = None
    dct_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.dct_type is not None and not isinstance(self.dct_type, str):
            self.dct_type = str(self.dct_type)

        super().__post_init__(**kwargs)


class SkosConceptScheme(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS.ConceptScheme
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "skos_ConceptScheme"
    class_model_uri: ClassVar[URIRef] = SH.SkosConceptScheme


class TemporalLiteral(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SH.TemporalLiteral
    class_class_curie: ClassVar[str] = "sh:TemporalLiteral"
    class_name: ClassVar[str] = "TemporalLiteral"
    class_model_uri: ClassVar[URIRef] = SH.TemporalLiteral


class DctLinguisticSystem(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT.LinguisticSystem
    class_class_curie: ClassVar[str] = "dct:LinguisticSystem"
    class_name: ClassVar[str] = "dct_LinguisticSystem"
    class_model_uri: ClassVar[URIRef] = SH.DctLinguisticSystem


class Document(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF.Document
    class_class_curie: ClassVar[str] = "foaf:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = SH.Document


class Literal(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS.Literal
    class_class_curie: ClassVar[str] = "rdfs:Literal"
    class_name: ClassVar[str] = "Literal"
    class_model_uri: ClassVar[URIRef] = SH.Literal


class RightsStatement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT.RightsStatement
    class_class_curie: ClassVar[str] = "dct:RightsStatement"
    class_name: ClassVar[str] = "RightsStatement"
    class_model_uri: ClassVar[URIRef] = SH.RightsStatement


class SkosConcept(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS.Concept
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "skos_Concept"
    class_model_uri: ClassVar[URIRef] = SH.SkosConcept


class DctStandard(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT.Standrad
    class_class_curie: ClassVar[str] = "dct:Standrad"
    class_name: ClassVar[str] = "dct_Standard"
    class_model_uri: ClassVar[URIRef] = SH.DctStandard


class RdfsLiteral(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS.Literal
    class_class_curie: ClassVar[str] = "rdfs:Literal"
    class_name: ClassVar[str] = "rdfs_Literal"
    class_model_uri: ClassVar[URIRef] = SH.RdfsLiteral


# Enumerations


# Slots
class slots:
    pass

slots.dct_description_mm = Slot(uri=DCT.description, name="dct_description_mm", curie=DCT.curie('description'),
                   model_uri=SH.dct_description_mm, domain=None, range=Union[Union[dict, Literal], List[Union[dict, Literal]]])

slots.dct_title_mm = Slot(uri=DCT.title, name="dct_title_mm", curie=DCT.curie('title'),
                   model_uri=SH.dct_title_mm, domain=None, range=Union[Union[dict, Literal], List[Union[dict, Literal]]])

slots.dcat_themeTaxonomy_rm = Slot(uri=DCAT.themeTaxonomy, name="dcat_themeTaxonomy_rm", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=SH.dcat_themeTaxonomy_rm, domain=None, range=Optional[Union[Union[dict, SkosConceptScheme], List[Union[dict, SkosConceptScheme]]]])

slots.dct_issued_rs = Slot(uri=DCAT.themeTaxonomy, name="dct_issued_rs", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=SH.dct_issued_rs, domain=None, range=Optional[Union[dict, TemporalLiteral]])

slots.dct_language_rm = Slot(uri=DCT.language, name="dct_language_rm", curie=DCT.curie('language'),
                   model_uri=SH.dct_language_rm, domain=None, range=Optional[Union[Union[dict, DctLinguisticSystem], List[Union[dict, DctLinguisticSystem]]]])

slots.dct_modified_rs = Slot(uri=DCT.modified, name="dct_modified_rs", curie=DCT.curie('modified'),
                   model_uri=SH.dct_modified_rs, domain=None, range=Optional[Union[dict, TemporalLiteral]])

slots.foaf_homepage_rs = Slot(uri=FOAF.homepage, name="foaf_homepage_rs", curie=FOAF.curie('homepage'),
                   model_uri=SH.foaf_homepage_rs, domain=None, range=Optional[Union[dict, Document]])

slots.dct_rights_os = Slot(uri=DCT.rights, name="dct_rights_os", curie=DCT.curie('rights'),
                   model_uri=SH.dct_rights_os, domain=None, range=Optional[Union[dict, RightsStatement]])

slots.dct_type_rm = Slot(uri=DCT.type, name="dct_type_rm", curie=DCT.curie('type'),
                   model_uri=SH.dct_type_rm, domain=None, range=Optional[Union[Union[dict, SkosConcept], List[Union[dict, SkosConcept]]]])

slots.dct_modified_ms = Slot(uri=ADMS.status, name="dct_modified_ms", curie=ADMS.curie('status'),
                   model_uri=SH.dct_modified_ms, domain=None, range=Union[dict, SkosConcept])

slots.adms_status_rs = Slot(uri=ADMS.status, name="adms_status_rs", curie=ADMS.curie('status'),
                   model_uri=SH.adms_status_rs, domain=None, range=Optional[Union[dict, SkosConcept]])

slots.dct_conformsTo_rs = Slot(uri=DCT.conformsTo, name="dct_conformsTo_rs", curie=DCT.curie('conformsTo'),
                   model_uri=SH.dct_conformsTo_rs, domain=None, range=Optional[Union[dict, DctStandard]])

slots.dct_description_om = Slot(uri=DCT.description, name="dct_description_om", curie=DCT.curie('description'),
                   model_uri=SH.dct_description_om, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.dct_language_om = Slot(uri=DCT.language, name="dct_language_om", curie=DCT.curie('language'),
                   model_uri=SH.dct_language_om, domain=None, range=Optional[Union[Union[dict, DctLinguisticSystem], List[Union[dict, DctLinguisticSystem]]]])

slots.dct_title_om = Slot(uri=DCT.title, name="dct_title_om", curie=DCT.curie('title'),
                   model_uri=SH.dct_title_om, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.service = Slot(uri=SH.service, name="service", curie=SH.curie('service'),
                   model_uri=SH.service, domain=None, range=Optional[str])

slots.name = Slot(uri=FOAF.name, name="name", curie=FOAF.curie('name'),
                   model_uri=SH.name, domain=None, range=str)

slots.dct_type = Slot(uri=SKOS.Concept, name="dct_type", curie=SKOS.curie('Concept'),
                   model_uri=SH.dct_type, domain=None, range=Optional[str])

slots.theme = Slot(uri=SKOS.Concept, name="theme", curie=SKOS.curie('Concept'),
                   model_uri=SH.theme, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DCT.publisher, name="publisher", curie=DCT.curie('publisher'),
                   model_uri=SH.publisher, domain=None, range=Union[dict, Agent])
from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "0.0.2"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_curi_maps': ['semweb_context'],
     'default_prefix': 'bertron',
     'default_range': 'string',
     'description': 'Schema for BERtron common data model.',
     'id': 'https://w3id.org/ber-data/bertron-schema',
     'imports': ['linkml:types', 'bertron_types'],
     'license': 'BSD-3',
     'name': 'bertron-schema',
     'prefixes': {'MIXS': {'prefix_prefix': 'MIXS',
                           'prefix_reference': 'https://w3id.org/mixs/'},
                  'UO': {'prefix_prefix': 'UO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/UO_'},
                  'WGS84': {'prefix_prefix': 'WGS84',
                            'prefix_reference': 'http://www.w3.org/2003/01/geo/wgs84_pos#'},
                  'bertron': {'prefix_prefix': 'bertron',
                              'prefix_reference': 'https://w3id.org/ber-data/bertron-schema/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://ber-data.github.io/bertron-schema'],
     'source_file': 'src/schema/linkml/bertron_schema.yaml',
     'title': 'BERtron schema'} )

class BERSourceType(str, Enum):
    """
    The BER data source from whence the entity originated.
    """
    EMSL = "EMSL"
    ESS_DIVE = "ESS-DIVE"
    JGI = "JGI"
    MONET = "MONET"
    NMDC = "NMDC"


class EntityType(str, Enum):
    """
    The type of entity captured in this record.
    """
    biodata = "biodata"
    jgi_biosample = "jgi_biosample"
    sample = "sample"
    sequence = "sequence"
    taxon = "taxon"
    unspecified = "unspecified"
    project = "project"
    """
    An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.
    """
    site = "site"
    """
    An entity that describes a location of experimentation or sample collection
    """
    dataset = "dataset"
    """
    A single or collection or data generated from an experimental entity
    """


class NameType(str, Enum):
    """
    The relationship between a name and a synonym of that name.
    """
    broad_synonym = "broad_synonym"
    """
    The synonym refers to a broader group of entities than the name.
    """
    exact_synonym = "exact_synonym"
    """
    String with exactly the same meaning and connotations as the original name.
    """
    narrow_synonym = "narrow_synonym"
    """
    The synonym refers to a narrower group of entities than the name.
    """
    related_synonym = "related_synonym"
    """
    The synonym has overlap with the name but the precise relationship is not defined.
    """
    acronym = "acronym"
    """
    An acronym or abbreviation for the name.
    """



class AttributeValue(ConfiguredBaseModel):
    """
    The value for any value of attribute for an entity. This object can hold both the un-normalized atomic value and the structured value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nmdc:AttributeValue',
         'from_schema': 'https://w3id.org/ber-data/bertron_types'})

    attribute: Attribute = Field(default=..., description="""The attribute being represented.""", json_schema_extra = { "linkml_meta": {'alias': 'attribute', 'domain_of': ['AttributeValue']} })
    raw_value: Optional[str] = Field(default=None, description="""The value that was specified for an annotation in raw form, i.e. a string. E.g. \"2 cm\" or \"2-4 cm\"""", json_schema_extra = { "linkml_meta": {'alias': 'raw_value',
         'domain_of': ['AttributeValue'],
         'mappings': ['nmdc:raw_value']} })


class Attribute(ConfiguredBaseModel):
    """
    A domain, measurement, attribute, property, or any descriptor for additional properties to be added to an entity. Where available, please use OBO Foundry ontologies or other controlled vocabularies for attributes; the label should be the term name from the ontology and the id should be the fully-qualified CURIE.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ber-data/bertron_types'})

    id: Optional[str] = Field(default=None, description="""A CURIE for the attribute, should one exist. Where available, please use OBO Foundry ontologies or other controlled vocabularies for labelling attributes; the id should be the term ID from the ontology.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Attribute', 'Entity', 'DataCollection'],
         'recommended': True} })
    label: str = Field(default=..., description="""Text string to describe the attribute. Where available, please use OBO Foundry ontologies or other controlled vocabularies for labelling attributes; the label should be the term name from the ontology.""", json_schema_extra = { "linkml_meta": {'alias': 'label', 'aliases': ['name', 'title'], 'domain_of': ['Attribute']} })


class QuantityValue(AttributeValue):
    """
    A simple quantity, e.g. 2cm.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nmdc:QuantityValue',
         'from_schema': 'https://w3id.org/ber-data/bertron_types',
         'mappings': ['schema:QuantityValue'],
         'slot_usage': {'raw_value': {'description': 'Unnormalized atomic string '
                                                     'representation, suggested syntax '
                                                     '{number} {unit}',
                                      'name': 'raw_value'}}})

    maximum_numeric_value: Optional[float] = Field(default=None, description="""The maximum value part, expressed as number, of the quantity value when the value covers a range.""", json_schema_extra = { "linkml_meta": {'alias': 'maximum_numeric_value',
         'domain_of': ['QuantityValue'],
         'is_a': 'numeric_value',
         'mappings': ['nmdc:maximum_numeric_value']} })
    minimum_numeric_value: Optional[float] = Field(default=None, description="""The minimum value part, expressed as number, of the quantity value when the value covers a range.""", json_schema_extra = { "linkml_meta": {'alias': 'minimum_numeric_value',
         'domain_of': ['QuantityValue'],
         'is_a': 'numeric_value',
         'mappings': ['nmdc:minimum_numeric_value']} })
    numeric_value: Optional[float] = Field(default=None, description="""The numerical part of a quantity value.""", json_schema_extra = { "linkml_meta": {'alias': 'numeric_value',
         'domain_of': ['QuantityValue'],
         'mappings': ['nmdc:numeric_value', 'qud:quantityValue', 'schema:value']} })
    unit: Optional[str] = Field(default=None, description="""Links a QuantityValue to a unit. Units should be taken from the UCUM unit collection or the Unit Ontology.""", json_schema_extra = { "linkml_meta": {'alias': 'unit',
         'aliases': ['scale'],
         'domain_of': ['QuantityValue'],
         'mappings': ['nmdc:unit', 'qud:unit', 'schema:unitCode', 'UO:0000000']} })
    unit_cv_id: Optional[str] = Field(default=None, description="""The unit of the quantity, expressed as a CURIE from the Unit Ontology.""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cv_id', 'domain_of': ['QuantityValue']} })
    attribute: Attribute = Field(default=..., description="""The attribute being represented.""", json_schema_extra = { "linkml_meta": {'alias': 'attribute', 'domain_of': ['AttributeValue']} })
    raw_value: Optional[str] = Field(default=None, description="""Unnormalized atomic string representation, suggested syntax {number} {unit}""", json_schema_extra = { "linkml_meta": {'alias': 'raw_value',
         'domain_of': ['AttributeValue'],
         'mappings': ['nmdc:raw_value']} })


class TextValue(AttributeValue):
    """
    A quality, described using a text string.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nmdc:TextValue',
         'from_schema': 'https://w3id.org/ber-data/bertron_types'})

    value: Optional[str] = Field(default=None, description="""The value, as a text string.""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['TextValue', 'DateTimeValue']} })
    value_cv_id: Optional[str] = Field(default=None, description="""For values that are in a controlled vocabulary (CV), this attribute should capture the controlled vocabulary ID for the value.""", json_schema_extra = { "linkml_meta": {'alias': 'value_cv_id', 'domain_of': ['TextValue']} })
    attribute: Attribute = Field(default=..., description="""The attribute being represented.""", json_schema_extra = { "linkml_meta": {'alias': 'attribute', 'domain_of': ['AttributeValue']} })
    raw_value: Optional[str] = Field(default=None, description="""The value that was specified for an annotation in raw form, i.e. a string. E.g. \"2 cm\" or \"2-4 cm\"""", json_schema_extra = { "linkml_meta": {'alias': 'raw_value',
         'domain_of': ['AttributeValue'],
         'mappings': ['nmdc:raw_value']} })


class DateTimeValue(AttributeValue):
    """
    A date or date and time value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nmdc:DateTimeValue',
         'from_schema': 'https://w3id.org/ber-data/bertron_types',
         'slot_usage': {'value': {'description': 'The date or date/time value, '
                                                 'expressed in ISO 8601-compatible '
                                                 'form. Dates should be expressed as '
                                                 'YYYY-MM-DD; times should be '
                                                 'expressed as HH:MM:SS with optional '
                                                 'milliseconds and an indication of '
                                                 'the timezone.',
                                  'examples': [{'value': '2025-11-09'},
                                               {'value': '2025-09-16T22:48:54Z'}],
                                  'name': 'value'}}})

    value: Optional[str] = Field(default=None, description="""The date or date/time value, expressed in ISO 8601-compatible form. Dates should be expressed as YYYY-MM-DD; times should be expressed as HH:MM:SS with optional milliseconds and an indication of the timezone.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['TextValue', 'DateTimeValue'],
         'examples': [{'value': '2025-11-09'}, {'value': '2025-09-16T22:48:54Z'}]} })
    attribute: Attribute = Field(default=..., description="""The attribute being represented.""", json_schema_extra = { "linkml_meta": {'alias': 'attribute', 'domain_of': ['AttributeValue']} })
    raw_value: Optional[str] = Field(default=None, description="""The value that was specified for an annotation in raw form, i.e. a string. E.g. \"2 cm\" or \"2-4 cm\"""", json_schema_extra = { "linkml_meta": {'alias': 'raw_value',
         'domain_of': ['AttributeValue'],
         'mappings': ['nmdc:raw_value']} })


class Entity(ConfiguredBaseModel):
    """
    An object retrieved by BERtron from a BER data API.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/ber-data/bertron-schema',
         'tree_root': True})

    ber_data_source: BERSourceType = Field(default=..., description="""The BER member from whence the entity originated.""", json_schema_extra = { "linkml_meta": {'alias': 'ber_data_source', 'domain_of': ['Entity']} })
    coordinates: Optional[Coordinates] = Field(default=None, description="""The geographic coordinates associated with an entity. For entities with a bounding box, the centroid is used as the geographic reference.""", json_schema_extra = { "linkml_meta": {'alias': 'coordinates', 'domain_of': ['Entity']} })
    entity_type: list[EntityType] = Field(default=..., description="""What kind of entity is this -- e.g. sequence data; a soil core; a well; field site; sample; etc.""", json_schema_extra = { "linkml_meta": {'alias': 'entity_type', 'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Textual description of the entity.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity', 'DataCollection'],
         'examples': [{'value': 'River water sample taken by AquaTROLL 9000.'},
                      {'value': 'Genome sequence of P. aeruginosa strain IDDQD'}],
         'slot_uri': 'schema:description'} })
    id: Optional[str] = Field(default=None, description="""The unique ID used for the entity within the BER resource. It may not necessarily be resolvable outside the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'aliases': ['BER data source internal identifier', 'CURIE'],
         'comments': ['If the data source does not use CURIEs, we cannot guarantee '
                      'that IDs will be unique between all the BER sources.'],
         'domain_of': ['Attribute', 'Entity', 'DataCollection'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable string representing an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'Name'],
         'examples': [{'value': 'Pseudomonas aeruginosa strain IDDQD'},
                      {'value': 'Soil core FW-106'}],
         'slot_uri': 'schema:name'} })
    alt_ids: Optional[list[str]] = Field(default=None, description="""Fully-qualified URI or CURIE used as an identifier for an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'alt_ids',
         'aliases': ['CURIEs',
                     'database cross-references',
                     'dbxrefs',
                     'IDs',
                     'alternative identifiers',
                     'alternative IDs',
                     'alternative PIDs',
                     'PIDs'],
         'comments': ['The entity `id` should not appear in this list.'],
         'domain_of': ['Entity', 'DataCollection'],
         'examples': [{'value': 'NCBItaxon:172684329'}, {'value': 'ISGN:1986497'}]} })
    alt_names: Optional[list[Name]] = Field(default=None, description="""Textual identifiers for an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'alt_names',
         'aliases': ['alternative names', 'synonyms'],
         'comments': ['The entity `name` should not appear in this list.'],
         'domain_of': ['Entity']} })
    part_of_collection: Optional[list[DataCollection]] = Field(default=None, description="""Administrative collection (e.g. project, campaign, whatever) that the entity was generated as part of. May also be called a project.""", json_schema_extra = { "linkml_meta": {'alias': 'part_of_collection', 'domain_of': ['Entity']} })
    uri: str = Field(default=..., description="""Permanent resolvable URI for the entity at the data source.""", json_schema_extra = { "linkml_meta": {'alias': 'uri', 'aliases': ['url'], 'domain_of': ['Entity']} })
    properties: Optional[list[Union[QuantityValue, TextValue]]] = Field(default=None, description="""Provide extended context that may be relevant and applicable to the entity you're describing.""", json_schema_extra = { "linkml_meta": {'alias': 'properties',
         'any_of': [{'range': 'TextValue'}, {'range': 'QuantityValue'}],
         'domain_of': ['Entity'],
         'examples': [{'object': {'attribute': {'id': 'MIXS:0000117',
                                                'label': 'total phosphorus'},
                                  'numeric_value': 2.2,
                                  'raw_value': '2.2 ppm',
                                  'unit': 'ppm'}},
                      {'object': {'attribute': {'id': 'MIXS:0000011',
                                                'label': 'collection date'},
                                  'raw_value': '2025-06-12'}},
                      {'object': {'attribute': {'id': 'MIXS:0000012',
                                                'label': 'env_broad_scale'},
                                  'value': 'terrestrial biome',
                                  'value_cv_id': 'ENVO:00000446'}},
                      {'object': {'attribute': {'id': 'PATO:0001687',
                                                'label': 'elevation'},
                                  'numeric_value': 2.2,
                                  'raw_value': '2.2 m',
                                  'unit': 'UO:0000008'}}],
         'mappings': ['MIXS:0000008']} })


class Coordinates(ConfiguredBaseModel):
    """
    The coordinates defining the position associated with the entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ber-data/bertron-schema'})

    latitude: float = Field(default=..., description="""latitude""", json_schema_extra = { "linkml_meta": {'alias': 'latitude',
         'broad_mappings': ['MIXS:0000009'],
         'domain_of': ['Coordinates'],
         'examples': [{'value': '-33.460524'}],
         'mappings': ['schema:latitude'],
         'slot_uri': 'WGS84:lat'} })
    longitude: float = Field(default=..., description="""longitude""", json_schema_extra = { "linkml_meta": {'alias': 'longitude',
         'broad_mappings': ['MIXS:0000009'],
         'domain_of': ['Coordinates'],
         'examples': [{'value': '150.168149'}],
         'mappings': ['schema:longitude'],
         'slot_uri': 'WGS84:long'} })


class Name(ConfiguredBaseModel):
    """
    The name or label for an entity. This may be a primary name, alternative name, synonym, acronym, or any other label used to refer to an entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ber-data/bertron-schema'})

    name_type: Optional[NameType] = Field(default=None, description="""Brief description of the name and/or its relationship to the entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name_type', 'domain_of': ['Name']} })
    name: str = Field(default=..., description="""The string used as a name.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'Name'],
         'examples': [{'value': 'Heat-inducible transcription repressor HrcA'},
                      {'value': 'FW106 groundwater metagenome'}],
         'slot_uri': 'schema:name'} })


class DataCollection(ConfiguredBaseModel):
    """
    Administrative unit (e.g. project, proposal, etc.) in which one or more entities is collected.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['May be equivalent to FundingReference in the CreditMetadata '
                      'schema.'],
         'from_schema': 'https://w3id.org/ber-data/bertron-schema'})

    id: Optional[str] = Field(default=None, description="""The unique ID used for the grouped set of data within the BER resource. It may not necessarily be resolvable outside the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'aliases': ['proposal ID', 'project ID'],
         'comments': ['If the data source does not use CURIEs, we cannot guarantee '
                      'that IDs will be unique between all the BER sources.'],
         'domain_of': ['Attribute', 'Entity', 'DataCollection'],
         'slot_uri': 'schema:identifier'} })
    title: Optional[str] = Field(default=None, description="""Human-readable string representing the grouped set of data.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'aliases': ['name'],
         'domain_of': ['DataCollection'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Textual description of the grouped set of data.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity', 'DataCollection'],
         'slot_uri': 'schema:description'} })
    alt_ids: Optional[list[str]] = Field(default=None, description="""Fully-qualified URI or CURIE used as an identifier for a grouped set of data.""", json_schema_extra = { "linkml_meta": {'alias': 'alt_ids',
         'aliases': ['CURIEs',
                     'database cross-references',
                     'dbxrefs',
                     'IDs',
                     'alternative identifiers',
                     'alternative IDs',
                     'alternative PIDs',
                     'PIDs'],
         'comments': ['The project `id` should not appear in this list.'],
         'domain_of': ['Entity', 'DataCollection']} })
    alt_titles: Optional[list[Name]] = Field(default=None, description="""Alternative versions of the title/name of a grouped set of data.""", json_schema_extra = { "linkml_meta": {'alias': 'alt_titles',
         'aliases': ['alternative titles'],
         'comments': ['The project `title` should not appear in this list.'],
         'domain_of': ['DataCollection']} })
    url: str = Field(default=..., description="""Permanent resolvable URI for the collection at the data source.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['DataCollection']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AttributeValue.model_rebuild()
Attribute.model_rebuild()
QuantityValue.model_rebuild()
TextValue.model_rebuild()
DateTimeValue.model_rebuild()
Entity.model_rebuild()
Coordinates.model_rebuild()
Name.model_rebuild()
DataCollection.model_rebuild()


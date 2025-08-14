# Auto generated from bertron_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-05-05T09:28:13
# Schema: bertron-schema
#
# id: https://w3id.org/ber-data/bertron-schema
# description: Schema for BERtron common data model.
# license: BSD-3

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Datetime, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "0.0.2"

# Namespaces
DATACITE = CurieNamespace('DataCite', 'https://purl.org/datacite/v4.4/')
MIXS = CurieNamespace('MIXS', 'http://example.org/UNKNOWN/MIXS/')
BERTRON = CurieNamespace('bertron', 'https://w3id.org/ber-data/bertron-schema/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCM = CurieNamespace('dcm', 'https://kbase.github.io/credit_engine/linkml/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
WGS84 = CurieNamespace('wgs84', 'http://example.org/UNKNOWN/wgs84/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BERTRON


# Types
class DecimalDegree(float):
    """ A decimal degree expresses latitude or longitude as decimal fractions. """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "decimal degree"
    type_model_uri = BERTRON.DecimalDegree


class Unit(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "unit"
    type_model_uri = BERTRON.Unit


# Class references
class CreditMetadataIdentifier(URIorCURIE):
    pass


@dataclass(repr=False)
class Entity(YAMLRoot):
    """
    An object retrieved by BERtron from a BER data API.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = BERTRON.Entity

    ber_data_source: Union[str, "BERSourceType"] = None
    credit_metadata: Union[str, CreditMetadataIdentifier] = None
    coordinates: Union[dict, "Coordinates"] = None
    data_type: Union[Union[str, "DataTypeTagType"], list[Union[str, "DataTypeTagType"]]] = None
    uri: Union[str, URIorCURIE] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    alt_ids: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    alt_names: Optional[Union[Union[dict, "Name"], list[Union[dict, "Name"]]]] = empty_list()
    part_of_collection: Optional[Union[Union[dict, "DataCollection"], list[Union[dict, "DataCollection"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ber_data_source):
            self.MissingRequiredField("ber_data_source")
        if not isinstance(self.ber_data_source, BERSourceType):
            self.ber_data_source = BERSourceType(self.ber_data_source)

        if self._is_empty(self.credit_metadata):
            self.MissingRequiredField("credit_metadata")
        if not isinstance(self.credit_metadata, CreditMetadataIdentifier):
            self.credit_metadata = CreditMetadataIdentifier(self.credit_metadata)

        if self._is_empty(self.coordinates):
            self.MissingRequiredField("coordinates")
        if not isinstance(self.coordinates, Coordinates):
            self.coordinates = Coordinates(**as_dict(self.coordinates))

        if self._is_empty(self.data_type):
            self.MissingRequiredField("data_type")
        if not isinstance(self.data_type, list):
            self.data_type = [self.data_type] if self.data_type is not None else []
        self.data_type = [v if isinstance(v, DataTypeTagType) else DataTypeTagType(v) for v in self.data_type]

        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URIorCURIE):
            self.uri = URIorCURIE(self.uri)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.alt_ids, list):
            self.alt_ids = [self.alt_ids] if self.alt_ids is not None else []
        self.alt_ids = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alt_ids]

        self._normalize_inlined_as_dict(slot_name="alt_names", slot_type=Name, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="part_of_collection", slot_type=DataCollection, key_name="url", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Coordinates(YAMLRoot):
    """
    The coordinates defining the position associated with the entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BERTRON["Coordinates"]
    class_class_curie: ClassVar[str] = "bertron:Coordinates"
    class_name: ClassVar[str] = "Coordinates"
    class_model_uri: ClassVar[URIRef] = BERTRON.Coordinates

    latitude: float = None
    longitude: float = None
    altitude: Optional[Union[dict, "QuantityValue"]] = None
    depth: Optional[Union[dict, "QuantityValue"]] = None
    elevation: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.altitude is not None and not isinstance(self.altitude, QuantityValue):
            self.altitude = QuantityValue(**as_dict(self.altitude))

        if self.depth is not None and not isinstance(self.depth, QuantityValue):
            self.depth = QuantityValue(**as_dict(self.depth))

        if self.elevation is not None and not isinstance(self.elevation, QuantityValue):
            self.elevation = QuantityValue(**as_dict(self.elevation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Name(YAMLRoot):
    """
    The name or label for an entity. This may be a primary name, alternative name, synonym, acronym, or any other
    label used to refer to an entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BERTRON["Name"]
    class_class_curie: ClassVar[str] = "bertron:Name"
    class_name: ClassVar[str] = "Name"
    class_model_uri: ClassVar[URIRef] = BERTRON.Name

    name: str = None
    name_type: Optional[Union[str, "NameType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.name_type is not None and not isinstance(self.name_type, NameType):
            self.name_type = NameType(self.name_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataCollection(YAMLRoot):
    """
    Administrative unit (e.g. project, proposal, etc.) in which one or more entities is collected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BERTRON["DataCollection"]
    class_class_curie: ClassVar[str] = "bertron:DataCollection"
    class_name: ClassVar[str] = "DataCollection"
    class_model_uri: ClassVar[URIRef] = BERTRON.DataCollection

    url: Union[str, URIorCURIE] = None
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    alt_ids: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    alt_titles: Optional[Union[Union[dict, Name], list[Union[dict, Name]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.alt_ids, list):
            self.alt_ids = [self.alt_ids] if self.alt_ids is not None else []
        self.alt_ids = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alt_ids]

        self._normalize_inlined_as_dict(slot_name="alt_titles", slot_type=Name, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttributeValue(YAMLRoot):
    """
    The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and
    the structured value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["AttributeValue"]
    class_class_curie: ClassVar[str] = "nmdc:AttributeValue"
    class_name: ClassVar[str] = "AttributeValue"
    class_model_uri: ClassVar[URIRef] = BERTRON.AttributeValue

    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(AttributeValue):
    """
    A simple quantity, e.g. 2cm
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["QuantityValue"]
    class_class_curie: ClassVar[str] = "nmdc:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = BERTRON.QuantityValue

    has_maximum_numeric_value: Optional[float] = None
    has_minimum_numeric_value: Optional[float] = None
    has_numeric_value: Optional[float] = None
    has_raw_value: Optional[str] = None
    has_unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_maximum_numeric_value is not None and not isinstance(self.has_maximum_numeric_value, float):
            self.has_maximum_numeric_value = float(self.has_maximum_numeric_value)

        if self.has_minimum_numeric_value is not None and not isinstance(self.has_minimum_numeric_value, float):
            self.has_minimum_numeric_value = float(self.has_minimum_numeric_value)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreditMetadata(YAMLRoot):
    """
    Represents the credit metadata associated with an object.

    In the following documentation, 'resource' is used to refer to the object
    that the CM pertains to, for example, a KBase Workspace object; a
    sample from NMDC or ESS-DIVE; sequence data from IMG.

    The 'resource_type' field should be filled using values from the [DataCite
    resourceTypeGeneral
    field](https://support.datacite.org/docs/datacite-metadata-schema-v44-mandatory-properties#10a-resourcetypegeneral).

    Currently this schema only supports credit metadata for objects of type
    'dataset'; anything else will return an error.

    The license may be supplied either as an URL pointing to licensing information for
    the resource, or using an SPDX license identifier from the list maintained at https://spdx.org/licenses/.

    Required fields are:
    - identifier
    - resource_type
    - versioning information: if the resource does not have an explicit version number,
    one or more dates should be supplied: ideally the date of resource publication and
    the last update (if applicable).
    - contributors (one or more required)
    - titles (one or more required)
    - meta

    The resource_type field is required, but as there is currently only a single valid
    value, 'dataset', it is automatically populated if no value is supplied.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCM["CreditMetadata"]
    class_class_curie: ClassVar[str] = "dcm:CreditMetadata"
    class_name: ClassVar[str] = "CreditMetadata"
    class_model_uri: ClassVar[URIRef] = BERTRON.CreditMetadata

    identifier: Union[str, CreditMetadataIdentifier] = None
    contributors: Union[Union[dict, "Contributor"], list[Union[dict, "Contributor"]]] = None
    meta: Union[dict, "Metadata"] = None
    resource_type: Union[str, "ResourceType"] = None
    titles: Union[Union[dict, "Title"], list[Union[dict, "Title"]]] = None
    comment: Optional[Union[str, list[str]]] = empty_list()
    content_url: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    dates: Optional[Union[Union[dict, "EventDate"], list[Union[dict, "EventDate"]]]] = empty_list()
    descriptions: Optional[Union[Union[dict, "Description"], list[Union[dict, "Description"]]]] = empty_list()
    funding: Optional[Union[Union[dict, "FundingReference"], list[Union[dict, "FundingReference"]]]] = empty_list()
    license: Optional[Union[dict, "License"]] = None
    publisher: Optional[Union[dict, "Organization"]] = None
    related_identifiers: Optional[Union[Union[dict, "PermanentID"], list[Union[dict, "PermanentID"]]]] = empty_list()
    url: Optional[Union[str, URI]] = None
    version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, CreditMetadataIdentifier):
            self.identifier = CreditMetadataIdentifier(self.identifier)

        if self._is_empty(self.contributors):
            self.MissingRequiredField("contributors")
        if not isinstance(self.contributors, list):
            self.contributors = [self.contributors] if self.contributors is not None else []
        self.contributors = [v if isinstance(v, Contributor) else Contributor(**as_dict(v)) for v in self.contributors]

        if self._is_empty(self.meta):
            self.MissingRequiredField("meta")
        if not isinstance(self.meta, Metadata):
            self.meta = Metadata(**as_dict(self.meta))

        if self._is_empty(self.resource_type):
            self.MissingRequiredField("resource_type")
        if not isinstance(self.resource_type, ResourceType):
            self.resource_type = ResourceType(self.resource_type)

        if self._is_empty(self.titles):
            self.MissingRequiredField("titles")
        if not isinstance(self.titles, list):
            self.titles = [self.titles] if self.titles is not None else []
        self.titles = [v if isinstance(v, Title) else Title(**as_dict(v)) for v in self.titles]

        if not isinstance(self.comment, list):
            self.comment = [self.comment] if self.comment is not None else []
        self.comment = [v if isinstance(v, str) else str(v) for v in self.comment]

        if not isinstance(self.content_url, list):
            self.content_url = [self.content_url] if self.content_url is not None else []
        self.content_url = [v if isinstance(v, URI) else URI(v) for v in self.content_url]

        if not isinstance(self.dates, list):
            self.dates = [self.dates] if self.dates is not None else []
        self.dates = [v if isinstance(v, EventDate) else EventDate(**as_dict(v)) for v in self.dates]

        if not isinstance(self.descriptions, list):
            self.descriptions = [self.descriptions] if self.descriptions is not None else []
        self.descriptions = [v if isinstance(v, Description) else Description(**as_dict(v)) for v in self.descriptions]

        if not isinstance(self.funding, list):
            self.funding = [self.funding] if self.funding is not None else []
        self.funding = [v if isinstance(v, FundingReference) else FundingReference(**as_dict(v)) for v in self.funding]

        if self.license is not None and not isinstance(self.license, License):
            self.license = License(**as_dict(self.license))

        if self.publisher is not None and not isinstance(self.publisher, Organization):
            self.publisher = Organization(**as_dict(self.publisher))

        if not isinstance(self.related_identifiers, list):
            self.related_identifiers = [self.related_identifiers] if self.related_identifiers is not None else []
        self.related_identifiers = [v if isinstance(v, PermanentID) else PermanentID(**as_dict(v)) for v in self.related_identifiers]

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Contributor(YAMLRoot):
    """
    Represents a contributor to the resource.

    Contributors must have a 'contributor_type', either 'Person' or 'Organization', and
    one of the 'name' fields: either 'given_name' and 'family_name' (for a person), or 'name' (for an organization or
    a person).

    The 'contributor_role' field takes values from the DataCite and CRediT contributor
    roles vocabularies. For more information on these resources and choosing
    appropriate roles, please see the following links:

    DataCite contributor roles:
    https://support.datacite.org/docs/datacite-metadata-schema-v44-recommended-and-optional-properties#7a-contributortype

    CRediT contributor role taxonomy: https://credit.niso.org.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCM["Contributor"]
    class_class_curie: ClassVar[str] = "dcm:Contributor"
    class_name: ClassVar[str] = "Contributor"
    class_model_uri: ClassVar[URIRef] = BERTRON.Contributor

    contributor_type: Optional[Union[str, "ContributorType"]] = None
    contributor_id: Optional[Union[str, URIorCURIE]] = None
    name: Optional[str] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    affiliations: Optional[Union[Union[dict, "Organization"], list[Union[dict, "Organization"]]]] = empty_list()
    contributor_roles: Optional[Union[Union[str, "ContributorRole"], list[Union[str, "ContributorRole"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contributor_type is not None and not isinstance(self.contributor_type, ContributorType):
            self.contributor_type = ContributorType(self.contributor_type)

        if self.contributor_id is not None and not isinstance(self.contributor_id, URIorCURIE):
            self.contributor_id = URIorCURIE(self.contributor_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.given_name is not None and not isinstance(self.given_name, str):
            self.given_name = str(self.given_name)

        if self.family_name is not None and not isinstance(self.family_name, str):
            self.family_name = str(self.family_name)

        self._normalize_inlined_as_dict(slot_name="affiliations", slot_type=Organization, key_name="organization_name", keyed=False)

        if not isinstance(self.contributor_roles, list):
            self.contributor_roles = [self.contributor_roles] if self.contributor_roles is not None else []
        self.contributor_roles = [v if isinstance(v, ContributorRole) else ContributorRole(v) for v in self.contributor_roles]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSource(YAMLRoot):
    """
    Source of any kind of data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCM["DataSource"]
    class_class_curie: ClassVar[str] = "dcm:DataSource"
    class_name: ClassVar[str] = "DataSource"
    class_model_uri: ClassVar[URIRef] = BERTRON.DataSource

    access_timestamp: int = None
    source_data_updated: Optional[Union[str, XSDDateTime]] = None
    source_name: Optional[str] = None
    source_url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.access_timestamp):
            self.MissingRequiredField("access_timestamp")
        if not isinstance(self.access_timestamp, int):
            self.access_timestamp = int(self.access_timestamp)

        if self.source_data_updated is not None and not isinstance(self.source_data_updated, XSDDateTime):
            self.source_data_updated = XSDDateTime(self.source_data_updated)

        if self.source_name is not None and not isinstance(self.source_name, str):
            self.source_name = str(self.source_name)

        if self.source_url is not None and not isinstance(self.source_url, URIorCURIE):
            self.source_url = URIorCURIE(self.source_url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Description(YAMLRoot):
    """
    Textual information about the resource being represented.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCM["Description"]
    class_class_curie: ClassVar[str] = "dcm:Description"
    class_name: ClassVar[str] = "Description"
    class_model_uri: ClassVar[URIRef] = BERTRON.Description

    description_text: str = None
    description_type: Optional[Union[str, "DescriptionType"]] = None
    language: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description_text):
            self.MissingRequiredField("description_text")
        if not isinstance(self.description_text, str):
            self.description_text = str(self.description_text)

        if self.description_type is not None and not isinstance(self.description_type, DescriptionType):
            self.description_type = DescriptionType(self.description_type)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EventDate(YAMLRoot):
    """
    Represents an event in the lifecycle of a resource and the date it occurred on.

    See https://support.datacite.org/docs/datacite-metadata-schema-v44-recommended-and-optional-properties#8-date for
    more information on the events.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCM["EventDate"]
    class_class_curie: ClassVar[str] = "dcm:EventDate"
    class_name: ClassVar[str] = "EventDate"
    class_model_uri: ClassVar[URIRef] = BERTRON.EventDate

    date: str = None
    event: Union[str, "EventType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.date):
            self.MissingRequiredField("date")
        if not isinstance(self.date, str):
            self.date = str(self.date)

        if self._is_empty(self.event):
            self.MissingRequiredField("event")
        if not isinstance(self.event, EventType):
            self.event = EventType(self.event)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FundingReference(YAMLRoot):
    """
    Represents a funding source for a resource, including the funding body and the grant awarded.

    One (or more) of the fields 'grant_id', 'grant_url', or 'funder.organization_name' is required; others are
    optional.

    Recommended resources for organization identifiers include:
    - Research Organization Registry, http://ror.org
    - International Standard Name Identifier, https://isni.org
    - Crossref Funder Registry, https://www.crossref.org/services/funder-registry/ (to be subsumed into ROR)

    Some organizations may have a digital object identifier (DOI).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["MonetaryGrant"]
    class_class_curie: ClassVar[str] = "schema:MonetaryGrant"
    class_name: ClassVar[str] = "FundingReference"
    class_model_uri: ClassVar[URIRef] = BERTRON.FundingReference

    funder: Optional[Union[dict, "Organization"]] = None
    grant_id: Optional[str] = None
    grant_title: Optional[str] = None
    grant_url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.funder is not None and not isinstance(self.funder, Organization):
            self.funder = Organization(**as_dict(self.funder))

        if self.grant_id is not None and not isinstance(self.grant_id, str):
            self.grant_id = str(self.grant_id)

        if self.grant_title is not None and not isinstance(self.grant_title, str):
            self.grant_title = str(self.grant_title)

        if self.grant_url is not None and not isinstance(self.grant_url, URIorCURIE):
            self.grant_url = URIorCURIE(self.grant_url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class License(YAMLRoot):
    """
    License information for the resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCM["License"]
    class_class_curie: ClassVar[str] = "dcm:License"
    class_name: ClassVar[str] = "License"
    class_model_uri: ClassVar[URIRef] = BERTRON.License

    id: Optional[str] = None
    url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Metadata(YAMLRoot):
    """
    Metadata for the credit metadata, including the schema version used, who submitted it, and the date of submission.
    When the credit metadata for a resource is added or updated, this additional metadata must be provided along with
    the credit information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCM["Metadata"]
    class_class_curie: ClassVar[str] = "dcm:Metadata"
    class_name: ClassVar[str] = "Metadata"
    class_model_uri: ClassVar[URIRef] = BERTRON.Metadata

    credit_metadata_schema_version: str = None
    saved_by: str = None
    timestamp: int = None
    credit_metadata_source: Optional[Union[Union[dict, DataSource], list[Union[dict, DataSource]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.credit_metadata_schema_version):
            self.MissingRequiredField("credit_metadata_schema_version")
        if not isinstance(self.credit_metadata_schema_version, str):
            self.credit_metadata_schema_version = str(self.credit_metadata_schema_version)

        if self._is_empty(self.saved_by):
            self.MissingRequiredField("saved_by")
        if not isinstance(self.saved_by, str):
            self.saved_by = str(self.saved_by)

        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, int):
            self.timestamp = int(self.timestamp)

        self._normalize_inlined_as_dict(slot_name="credit_metadata_source", slot_type=DataSource, key_name="access_timestamp", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(YAMLRoot):
    """
    Represents an organization.

    Recommended resources for organization identifiers and canonical organization names include:
    - Research Organization Registry, http://ror.org
    - International Standard Name Identifier, https://isni.org
    - Crossref Funder Registry, https://www.crossref.org/services/funder-registry/

    For example, the US DOE would be entered as:
    organization_name: United States Department of Energy
    organization_id:   ROR:01bj3aw27
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Organization"]
    class_class_curie: ClassVar[str] = "schema:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = BERTRON.Organization

    organization_name: str = None
    organization_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.organization_name):
            self.MissingRequiredField("organization_name")
        if not isinstance(self.organization_name, str):
            self.organization_name = str(self.organization_name)

        if self.organization_id is not None and not isinstance(self.organization_id, URIorCURIE):
            self.organization_id = URIorCURIE(self.organization_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PermanentID(YAMLRoot):
    """
    Represents a persistent unique identifier for an entity and its relationship to some other entity.

    The 'id' field and 'relationship_type' fields are required.

    The values in the 'relationship_type' field come from controlled vocabularies maintained by DataCite and Crossref.
    See the documentation links below for more details.

    DataCite relation types:
    https://support.datacite.org/docs/datacite-metadata-schema-v44-recommended-and-optional-properties#12b-relationtype

    Crossref relation types:
    https://www.crossref.org/documentation/schema-library/markup-guide-metadata-segments/relationships/
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCM["PermanentID"]
    class_class_curie: ClassVar[str] = "dcm:PermanentID"
    class_name: ClassVar[str] = "PermanentID"
    class_model_uri: ClassVar[URIRef] = BERTRON.PermanentID

    id: Union[str, URIorCURIE] = None
    description: Optional[str] = None
    relationship_type: Optional[Union[str, "RelationshipType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, URIorCURIE):
            self.id = URIorCURIE(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.relationship_type is not None and not isinstance(self.relationship_type, RelationshipType):
            self.relationship_type = RelationshipType(self.relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Title(YAMLRoot):
    """
    Represents the title or name of a resource, the type of that title, and the language used (if appropriate).

    The 'title' field is required; 'title_type' is only necessary if the text is not the primary title.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCM["Title"]
    class_class_curie: ClassVar[str] = "dcm:Title"
    class_name: ClassVar[str] = "Title"
    class_model_uri: ClassVar[URIRef] = BERTRON.Title

    title: str = None
    language: Optional[str] = None
    title_type: Optional[Union[str, "TitleType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.title_type is not None and not isinstance(self.title_type, TitleType):
            self.title_type = TitleType(self.title_type)

        super().__post_init__(**kwargs)


# Enumerations
class BERSourceType(EnumDefinitionImpl):
    """
    The BER data source from whence the entity originated.
    """
    EMSL = PermissibleValue(text="EMSL")
    JGI = PermissibleValue(text="JGI")
    MONET = PermissibleValue(text="MONET")
    NMDC = PermissibleValue(text="NMDC")

    _defn = EnumDefinition(
        name="BERSourceType",
        description="The BER data source from whence the entity originated.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ESS-DIVE",
            PermissibleValue(text="ESS-DIVE"))

class DataTypeTagType(EnumDefinitionImpl):
    """
    Tags used to describe an entity.
    """
    biodata = PermissibleValue(text="biodata")
    jgi_biosample = PermissibleValue(text="jgi_biosample")
    sample = PermissibleValue(text="sample")
    sequence = PermissibleValue(text="sequence")
    taxon = PermissibleValue(text="taxon")

    _defn = EnumDefinition(
        name="DataTypeTagType",
        description="Tags used to describe an entity.",
    )

class NameType(EnumDefinitionImpl):
    """
    The relationship between a name and a synonym of that name.
    """
    broad_synonym = PermissibleValue(
        text="broad_synonym",
        description="The synonym refers to a broader group of entities than the name.")
    exact_synonym = PermissibleValue(
        text="exact_synonym",
        description="String with exactly the same meaning and connotations as the original name.")
    narrow_synonym = PermissibleValue(
        text="narrow_synonym",
        description="The synonym refers to a narrower group of entities than the name.")
    related_synonym = PermissibleValue(
        text="related_synonym",
        description="The synonym has overlap with the name but the precise relationship is not defined.")
    acronym = PermissibleValue(
        text="acronym",
        description="An acronym or abbreviation for the name.")

    _defn = EnumDefinition(
        name="NameType",
        description="The relationship between a name and a synonym of that name.",
    )

class ContributorRole(EnumDefinitionImpl):
    """
    The type of contribution made by a contributor.
    """
    contact_person = PermissibleValue(
        text="contact_person",
        description="""Person with knowledge of how to access, troubleshoot, or otherwise field issues related to the resource. May also be \"Point of Contact\" in organisation that controls access to the resource, if that organisation is different from Publisher, Distributor, Data Manager.""",
        meaning=DATACITE["ContactPerson"])
    data_collector = PermissibleValue(
        text="data_collector",
        description="""Person/institution responsible for finding, gathering/collecting data under the guidelines of the author(s) or Principal Investigator (PI). May also use when crediting survey conductors, interviewers, event or condition observers, person responsible for monitoring key instrument data.""",
        meaning=DATACITE["DataCollector"])
    data_curator = PermissibleValue(
        text="data_curator",
        description="""Person tasked with reviewing, enhancing, cleaning, or standardizing metadata and the associated data submitted for storage, use, and maintenance within a data centre or repository. While the \"DataManager\" is concerned with digital maintenance, the DataCurator's role encompasses quality assurance focused on content and metadata. This includes checking whether the submitted dataset is complete, with all files and components as described by submitter, whether the metadata is standardized to appropriate systems and schema, whether specialized metadata is needed to add value and ensure access across disciplines, and determining how the metadata might map to search engines, database products, and automated feeds.""",
        meaning=DATACITE["DataCurator"])
    data_manager = PermissibleValue(
        text="data_manager",
        description="""Person (or organisation with a staff of data managers, such as a data centre) responsible for maintaining the finished resource. The work done by this person or organisation ensures that the resource is periodically \"refreshed\" in terms of software/hardware support, is kept available or is protected from unauthorized access, is stored in accordance with industry standards, and is handled in accordance with the records management requirements applicable to it.""",
        meaning=DATACITE["DataManager"])
    distributor = PermissibleValue(
        text="distributor",
        description="""Institution tasked with responsibility to generate/disseminate copies of the resource in either electronic or print form. Works stored in more than one archive/repository may credit each as a distributor.""",
        meaning=DATACITE["Distributor"])
    editor = PermissibleValue(
        text="editor",
        description="""A person who oversees the details related to the publication format of the resource. N.b. if the Editor is to be credited in place of multiple creators, the Editor's name may be supplied as Creator, with \"(Ed.)\" appended to the name.""",
        meaning=DATACITE["Editor"])
    hosting_institution = PermissibleValue(
        text="hosting_institution",
        description="""Typically, the organisation allowing the resource to be available on the internet through the provision of its hardware/software/operating support. May also be used for an organisation that stores the data offline. Often a data centre (if that data centre is not the \"publisher\" of the resource).""",
        meaning=DATACITE["HostingInstitution"])
    producer = PermissibleValue(
        text="producer",
        description="""Typically a person or organisation responsible for the artistry and form of a media product. In the data industry, this may be a company \"producing\" DVDs that package data for future dissemination by a distributor.""",
        meaning=DATACITE["Producer"])
    project_leader = PermissibleValue(
        text="project_leader",
        description="""Person officially designated as head of project team or sub- project team instrumental in the work necessary to development of the resource. The Project Leader is not \"removed\" from the work that resulted in the resource; he or she remains intimately involved throughout the life of the particular project team.""",
        meaning=DATACITE["ProjectLeader"])
    project_manager = PermissibleValue(
        text="project_manager",
        description="""Person officially designated as manager of a project. Project may consist of one or many project teams and sub-teams. The manager of a project normally has more administrative responsibility than actual work involvement.""",
        meaning=DATACITE["ProjectManager"])
    project_member = PermissibleValue(
        text="project_member",
        description="""Person on the membership list of a designated project/project team. This vocabulary may or may not indicate the quality, quantity, or substance of the person's involvement.""",
        meaning=DATACITE["ProjectMember"])
    registration_agency = PermissibleValue(
        text="registration_agency",
        description="""Institution/organisation officially appointed by a Registration Authority to handle specific tasks within a defined area of responsibility. DataCite is a Registration Agency for the International DOI Foundation (IDF). One of DataCite's tasks is to assign DOI prefixes to the allocating agents who then assign the full, specific character string to data clients, provide metadata back to the DataCite registry, etc.""",
        meaning=DATACITE["RegistrationAgency"])
    registration_authority = PermissibleValue(
        text="registration_authority",
        description="""A standards-setting body from which Registration Agencies obtain official recognition and guidance. The IDF serves as the Registration Authority for the International Standards Organisation (ISO) in the area/domain of Digital Object Identifiers.""",
        meaning=DATACITE["RegistrationAuthority"])
    related_person = PermissibleValue(
        text="related_person",
        description="""A person without a specifically defined role in the development of the resource, but who is someone the author wishes to recognize. This person could be an author's intellectual mentor, a person providing intellectual leadership in the discipline or subject domain, etc.""",
        meaning=DATACITE["RelatedPerson"])
    researcher = PermissibleValue(
        text="researcher",
        description="""A person involved in analyzing data or the results of an experiment or formal study. May indicate an intern or assistant to one of the authors who helped with research but who was not so \"key\" as to be listed as an author. Should be a person, not an institution. Note that a person involved in the gathering of data would fall under the contributorType \"data_collector.\" The researcher may find additional data online and correlate it to the data collected for the experiment or study, for example.""",
        meaning=DATACITE["Researcher"])
    research_group = PermissibleValue(
        text="research_group",
        description="""Typically refers to a group of individuals with a lab, department, or division; the group has a particular, defined focus of activity. May operate at a narrower level of scope; may or may not hold less administrative responsibility than a project team.""",
        meaning=DATACITE["ResearchGroup"])
    rights_holder = PermissibleValue(
        text="rights_holder",
        description="""Person or institution owning or managing property rights, including intellectual property rights over the resource.""",
        meaning=DATACITE["RightsHolder"])
    sponsor = PermissibleValue(
        text="sponsor",
        description="""Person or organisation that issued a contract or under the auspices of which a work has been written, printed, published, developed, etc. Includes organisations that provide in-kind support, through donation, provision of people or a facility or instrumentation necessary for the development of the resource, etc.""",
        meaning=DATACITE["Sponsor"])
    supervisor = PermissibleValue(
        text="supervisor",
        description="""Designated administrator over one or more groups/teams working to produce a resource or over one or more steps of a development process.""",
        meaning=DATACITE["Supervisor"])
    work_package_leader = PermissibleValue(
        text="work_package_leader",
        description="""A Work Package is a recognized data product, not all of which is included in publication. The package, instead, may include notes, discarded documents, etc. The Work Package Leader is responsible for ensuring the comprehensive contents, versioning, and availability of the Work Package during the development of the resource.""",
        meaning=DATACITE["WorkPackageLeader"])
    other = PermissibleValue(
        text="other",
        description="""Any person or institution making a significant contribution to the development and/or maintenance of the resource, but whose contribution does not \"fit\" other controlled vocabulary for contributorType. Could be a photographer, artist, or writer whose contribution helped to publicize the resource (as opposed to creating it), a reviewer of the resource, someone providing administrative services to the author (such as depositing updates into an online repository, analysing usage, etc.), or one of many other roles.""",
        meaning=DATACITE["Other"])
    conceptualization = PermissibleValue(
        text="conceptualization",
        description="Ideas; formulation or evolution of overarching research goals and aims.",
        meaning=CRCR["conceptualization"])
    data_curation = PermissibleValue(
        text="data_curation",
        description="""Management activities to annotate (produce metadata), scrub data and maintain research data (including software code, where it is necessary for interpreting the data itself) for initial use and later re-use.""",
        meaning=CRCR["data-curation"])
    formal_analysis = PermissibleValue(
        text="formal_analysis",
        description="""Application of statistical, mathematical, computational, or other formal techniques to analyze or synthesize study data.""",
        meaning=CRCR["formal-analysis"])
    funding_acquisition = PermissibleValue(
        text="funding_acquisition",
        description="Acquisition of the financial support for the project leading to this publication.",
        meaning=CRCR["funding-acquisition"])
    investigation = PermissibleValue(
        text="investigation",
        description="""Conducting a research and investigation process, specifically performing the experiments, or data/evidence collection.""",
        meaning=CRCR["investigation"])
    methodology = PermissibleValue(
        text="methodology",
        description="Development or design of methodology; creation of models.",
        meaning=CRCR["methodology"])
    project_administration = PermissibleValue(
        text="project_administration",
        description="Management and coordination responsibility for the research activity planning and execution.",
        meaning=CRCR["project-administration"])
    resources = PermissibleValue(
        text="resources",
        description="""Provision of study materials, reagents, materials, patients, laboratory samples, animals, instrumentation, computing resources, or other analysis tools.""",
        meaning=CRCR["resources"])
    software = PermissibleValue(
        text="software",
        description="""Programming, software development; designing computer programs; implementation of the computer code and supporting algorithms; testing of existing code components.""",
        meaning=CRCR["software"])
    supervision = PermissibleValue(
        text="supervision",
        description="""Oversight and leadership responsibility for the research activity planning and execution, including mentorship external to the core team.""",
        meaning=CRCR["supervision"])
    validation = PermissibleValue(
        text="validation",
        description="""Verification, whether as a part of the activity or separate, of the overall replication/reproducibility of results/experiments and other research outputs.""",
        meaning=CRCR["validation"])
    visualization = PermissibleValue(
        text="visualization",
        description="""Preparation, creation and/or presentation of the published work, specifically visualization/data presentation.""",
        meaning=CRCR["visualization"])
    writing_original_draft = PermissibleValue(
        text="writing_original_draft",
        description="""Preparation, creation and/or presentation of the published work, specifically writing the initial draft (including substantive translation).""",
        meaning=CRCR["writing-original-draft"])
    writing_review_editing = PermissibleValue(
        text="writing_review_editing",
        description="""Preparation, creation and/or presentation of the published work by those from the original research group, specifically critical review, commentary or revision -- including pre- or post-publication stages.""",
        meaning=CRCR["writing-review-editing"])

    _defn = EnumDefinition(
        name="ContributorRole",
        description="The type of contribution made by a contributor.",
    )

class ContributorType(EnumDefinitionImpl):
    """
    The type of contributor being represented.
    """
    Person = PermissibleValue(
        text="Person",
        description="A person.",
        meaning=SCHEMA["Person"])
    Organization = PermissibleValue(
        text="Organization",
        description="An organization.",
        meaning=SCHEMA["Organization"])

    _defn = EnumDefinition(
        name="ContributorType",
        description="The type of contributor being represented.",
    )

class DescriptionType(EnumDefinitionImpl):
    """
    The type of text being represented.
    """
    abstract = PermissibleValue(
        text="abstract",
        description="A brief description of the resource and the context in which the resource was created.",
        meaning=DATACITE["abstract"])
    description = PermissibleValue(
        text="description",
        meaning=DATACITE["descriptions.description.descriptionType"])
    summary = PermissibleValue(
        text="summary",
        meaning=DATACITE["summary"])

    _defn = EnumDefinition(
        name="DescriptionType",
        description="The type of text being represented.",
    )

class EventType(EnumDefinitionImpl):
    """
    The type of date being represented.
    """
    accepted = PermissibleValue(
        text="accepted",
        description="""The date that the publisher accepted the resource into their system. To indicate the start of an embargo period, use Submitted or Accepted, as appropriate.""",
        meaning=DATACITE["accepted"])
    available = PermissibleValue(
        text="available",
        description="""The date the resource is made publicly available. To indicate the end of an embargo period, use Available.""",
        meaning=DATACITE["available"])
    copyrighted = PermissibleValue(
        text="copyrighted",
        description="""The specific, documented date at which the resource receives a copyrighted status, if applicable.""",
        meaning=DATACITE["copyrighted"])
    collected = PermissibleValue(
        text="collected",
        description="""The date or date range in which the resource content was collected. To indicate precise or particular timeframes in which research was conducted.""",
        meaning=DATACITE["collected"])
    created = PermissibleValue(
        text="created",
        description="""The date the resource itself was put together; this could refer to a timeframe in ancient history, be a date range or a single date for a final component, e.g., the finalized file with all of the data.""",
        meaning=DATACITE["created"])
    issued = PermissibleValue(
        text="issued",
        description="""The date that the resource is published or distributed e.g. to a data centre""",
        meaning=DATACITE["issued"])
    submitted = PermissibleValue(
        text="submitted",
        description="""The date the creator submits the resource to the publisher. This could be different from Accepted if the publisher then applies a selection process. To indicate the start of an embargo period, use Submitted or Accepted, as appropriate.""",
        meaning=DATACITE["submitted"])
    updated = PermissibleValue(
        text="updated",
        description="""The date of the last update to the resource, when the resource is being added to.""",
        meaning=DATACITE["updated"])
    valid = PermissibleValue(
        text="valid",
        description="""The date (or date range) during which the dataset or resource is accurate.""",
        meaning=DATACITE["valid"])
    withdrawn = PermissibleValue(
        text="withdrawn",
        description="""The date the resource is removed.""",
        meaning=DATACITE["withdrawn"])
    other = PermissibleValue(
        text="other",
        meaning=DATACITE["other"])

    _defn = EnumDefinition(
        name="EventType",
        description="The type of date being represented.",
    )

class RelationshipType(EnumDefinitionImpl):
    """
    The relationship between two entities. For example, when a PermanentID class is used to represent objects in the
    CreditMetadata field 'related_identifiers', the 'relationship_type' field captures the relationship between the
    resource being registered (A) and this ID (B).
    """
    based_on_data = PermissibleValue(
        text="based_on_data",
        meaning=CROSSREF["BasedOnData"])
    cites = PermissibleValue(
        text="cites",
        description="Indicates that A includes B in a citation.",
        meaning=DATACITE["Cites"])
    compiles = PermissibleValue(
        text="compiles",
        description="""Indicates B is the result of a compile or creation event using A. May be used for software and text, as a compiler can be a computer program or a person.""",
        meaning=DATACITE["Compiles"])
    continues = PermissibleValue(
        text="continues",
        description="Indicates A is a continuation of the work B.",
        meaning=DATACITE["Continues"])
    describes = PermissibleValue(
        text="describes",
        description="Indicates A describes B.",
        meaning=DATACITE["Describes"])
    documents = PermissibleValue(
        text="documents",
        description="Indicates A is documentation about B; e.g. points to software documentation.",
        meaning=DATACITE["Documents"])
    finances = PermissibleValue(
        text="finances",
        meaning=CROSSREF["Finances"])
    has_comment = PermissibleValue(
        text="has_comment",
        meaning=CROSSREF["HasComment"])
    has_derivation = PermissibleValue(
        text="has_derivation",
        meaning=CROSSREF["HasDerivation"])
    has_expression = PermissibleValue(
        text="has_expression",
        meaning=CROSSREF["HasExpression"])
    has_format = PermissibleValue(
        text="has_format",
        meaning=CROSSREF["HasFormat"])
    has_manifestation = PermissibleValue(
        text="has_manifestation",
        meaning=CROSSREF["HasManifestation"])
    has_manuscript = PermissibleValue(
        text="has_manuscript",
        meaning=CROSSREF["HasManuscript"])
    has_metadata = PermissibleValue(
        text="has_metadata",
        description="Indicates resource A has additional metadata B.",
        meaning=DATACITE["HasMetadata"])
    has_part = PermissibleValue(
        text="has_part",
        description="""Indicates A includes the part B. Primarily this relation is applied to container-contained type relationships. May be used for individual software modules; note that code repository-to-version relationships should be modeled using IsVersionOf and HasVersion.""",
        meaning=DATACITE["HasPart"])
    has_preprint = PermissibleValue(
        text="has_preprint",
        meaning=CROSSREF["HasPreprint"])
    has_related_material = PermissibleValue(
        text="has_related_material",
        meaning=CROSSREF["HasRelatedMaterial"])
    has_reply = PermissibleValue(
        text="has_reply",
        meaning=CROSSREF["HasReply"])
    has_review = PermissibleValue(
        text="has_review",
        meaning=CROSSREF["HasReview"])
    has_translation = PermissibleValue(
        text="has_translation",
        meaning=CROSSREF["HasTranslation"])
    has_version = PermissibleValue(
        text="has_version",
        description="""Indicates A has a version (B). The registered resource such as a software package or code repository has a versioned instance (indicates A has the instance B) e.g. it may be used to relate an un-versioned code repository to one of its specific software versions.""",
        meaning=DATACITE["HasVersion"])
    is_based_on = PermissibleValue(
        text="is_based_on",
        meaning=CROSSREF["IsBasedOn"])
    is_basis_for = PermissibleValue(
        text="is_basis_for",
        meaning=CROSSREF["IsBasisFor"])
    is_cited_by = PermissibleValue(
        text="is_cited_by",
        description="Indicates that B includes A in a citation.",
        meaning=DATACITE["IsCitedBy"])
    is_comment_on = PermissibleValue(
        text="is_comment_on",
        meaning=CROSSREF["IsCommentOn"])
    is_compiled_by = PermissibleValue(
        text="is_compiled_by",
        description="""Indicates B is used to compile or create A. May be used for software and text, as a compiler can be a computer program or a person.""",
        meaning=DATACITE["IsCompiledBy"])
    is_continued_by = PermissibleValue(
        text="is_continued_by",
        description="Indicates A is continued by the work B.",
        meaning=DATACITE["IsContinuedBy"])
    is_data_basis_for = PermissibleValue(
        text="is_data_basis_for",
        meaning=CROSSREF["IsDataBasisFor"])
    is_derived_from = PermissibleValue(
        text="is_derived_from",
        description="""Indicates B is a source upon which A is based. IsDerivedFrom should be used for a resource that is a derivative of an original resource. For example, 'A isDerivedFrom B' could describe a dataset (A) derived from a larger dataset (B) where data values have been manipulated from their original state.""",
        meaning=DATACITE["IsDerivedFrom"])
    is_described_by = PermissibleValue(
        text="is_described_by",
        description="Indicates A is described by B.",
        meaning=DATACITE["IsDescribedBy"])
    is_documented_by = PermissibleValue(
        text="is_documented_by",
        description="Indicates B is documentation about/explaining A; e.g. points to software documentation.",
        meaning=DATACITE["IsDocumentedBy"])
    is_expression_of = PermissibleValue(
        text="is_expression_of",
        meaning=CROSSREF["IsExpressionOf"])
    is_financed_by = PermissibleValue(
        text="is_financed_by",
        meaning=CROSSREF["IsFinancedBy"])
    is_format_of = PermissibleValue(
        text="is_format_of",
        meaning=CROSSREF["IsFormatOf"])
    is_identical_to = PermissibleValue(
        text="is_identical_to",
        description="""Indicates that A is identical to B, for use when there is a need to register two separate instances of the same resource. Should be used for a resource that is the same as the registered resource but is saved in another location, e.g. another institution.""",
        meaning=DATACITE["IsIdenticalTo"])
    is_manifestation_of = PermissibleValue(
        text="is_manifestation_of",
        meaning=CROSSREF["IsManifestationOf"])
    is_manuscript_of = PermissibleValue(
        text="is_manuscript_of",
        meaning=CROSSREF["IsManuscriptOf"])
    is_metadata_for = PermissibleValue(
        text="is_metadata_for",
        description="Indicates additional metadata A for a resource B.",
        meaning=DATACITE["IsMetadataFor"])
    is_new_version_of = PermissibleValue(
        text="is_new_version_of",
        description="Indicates A is a new edition of B, where the new edition has been modified or updated.",
        meaning=DATACITE["IsNewVersionOf"])
    is_obsoleted_by = PermissibleValue(
        text="is_obsoleted_by",
        description="Indicates A is replaced by B.",
        meaning=DATACITE["IsObsoletedBy"])
    is_original_form_of = PermissibleValue(
        text="is_original_form_of",
        description="""Indicates A is the original form of B. May be used for different software operating systems or compiler formats, for example.""",
        meaning=DATACITE["IsOriginalFormOf"])
    is_part_of = PermissibleValue(
        text="is_part_of",
        description="""Indicates A is a portion of B; may be used for elements of a series. Primarily this relation is applied to container-contained type relationships. May be used for individual software modules; note that code repository-to-version relationships should be modeled using IsVersionOf and HasVersion.""",
        meaning=DATACITE["IsPartOf"])
    is_preprint_of = PermissibleValue(
        text="is_preprint_of",
        meaning=CROSSREF["IsPreprintOf"])
    is_previous_version_of = PermissibleValue(
        text="is_previous_version_of",
        description="Indicates A is a previous edition of B.",
        meaning=DATACITE["IsPreviousVersionOf"])
    is_published_in = PermissibleValue(
        text="is_published_in",
        description="Indicates A is published inside B, but is independent of other things published inside of B.",
        meaning=DATACITE["IsPublishedIn"])
    is_referenced_by = PermissibleValue(
        text="is_referenced_by",
        description="Indicates A is used as a source of information by B.",
        meaning=DATACITE["IsReferencedBy"])
    is_related_material = PermissibleValue(
        text="is_related_material",
        meaning=CROSSREF["IsRelatedMaterial"])
    is_replaced_by = PermissibleValue(
        text="is_replaced_by",
        meaning=CROSSREF["IsReplacedBy"])
    is_reply_to = PermissibleValue(
        text="is_reply_to",
        meaning=CROSSREF["IsReplyTo"])
    is_required_by = PermissibleValue(
        text="is_required_by",
        description="Indicates A is required by B. May be used to indicate software dependencies.",
        meaning=DATACITE["IsRequiredBy"])
    is_review_of = PermissibleValue(
        text="is_review_of",
        meaning=CROSSREF["IsReviewOf"])
    is_reviewed_by = PermissibleValue(
        text="is_reviewed_by",
        description="Indicates that A is reviewed by B.",
        meaning=DATACITE["IsReviewedBy"])
    is_same_as = PermissibleValue(
        text="is_same_as",
        meaning=CROSSREF["IsSameAs"])
    is_source_of = PermissibleValue(
        text="is_source_of",
        description="""Indicates A is a source upon which B is based. IsSourceOf is the original resource from which a derivative resource was created. For example, 'A isSourceOf B' could describe a dataset (A) which acts as the source of a derived dataset (B) where the values have been manipulated.""",
        meaning=DATACITE["IsSourceOf"])
    is_supplement_to = PermissibleValue(
        text="is_supplement_to",
        description="Indicates that A is a supplement to B.",
        meaning=DATACITE["IsSupplementTo"])
    is_supplemented_by = PermissibleValue(
        text="is_supplemented_by",
        description="Indicates that B is a supplement to A.",
        meaning=DATACITE["IsSupplementedBy"])
    is_translation_of = PermissibleValue(
        text="is_translation_of",
        meaning=CROSSREF["IsTranslationOf"])
    is_variant_form_of = PermissibleValue(
        text="is_variant_form_of",
        description="""Indicates A is a variant or different form of B. Use for a different form of one thing. May be used for different software operating systems or compiler formats, for example.""",
        meaning=DATACITE["IsVariantFormOf"])
    is_version_of = PermissibleValue(
        text="is_version_of",
        description="""Indicates A is a version of B. The registered resource is an instance of a target resource (indicates that A is an instance of B) e.g. it may be used to relate a specific version of a software package to its software code repository.""",
        meaning=DATACITE["IsVersionOf"])
    obsoletes = PermissibleValue(
        text="obsoletes",
        description="Indicates A replaces B.",
        meaning=DATACITE["Obsoletes"])
    references = PermissibleValue(
        text="references",
        description="Indicates B is used as a source of information for A.",
        meaning=DATACITE["References"])
    replaces = PermissibleValue(
        text="replaces",
        meaning=CROSSREF["Replaces"])
    requires = PermissibleValue(
        text="requires",
        description="Indicates A requires B. May be used to indicate software dependencies.",
        meaning=DATACITE["Requires"])
    reviews = PermissibleValue(
        text="reviews",
        description="Indicates that A is a review of B.",
        meaning=DATACITE["Reviews"])
    unknown = PermissibleValue(
        text="unknown",
        description="The relationship between subject and object is unknown.")

    _defn = EnumDefinition(
        name="RelationshipType",
        description="""The relationship between two entities. For example, when a PermanentID class is used to represent objects in the CreditMetadata field 'related_identifiers', the 'relationship_type' field captures the relationship between the resource being registered (A) and this ID (B).""",
    )

class ResourceType(EnumDefinitionImpl):
    """
    The type of resource being represented.
    """
    dataset = PermissibleValue(
        text="dataset",
        description="A dataset.",
        meaning=SCHEMA["Dataset"])

    _defn = EnumDefinition(
        name="ResourceType",
        description="The type of resource being represented.",
    )

class TitleType(EnumDefinitionImpl):
    """
    The type of title being represented.
    """
    subtitle = PermissibleValue(
        text="subtitle",
        description="Any subtitle for the resource.")
    alternative_title = PermissibleValue(
        text="alternative_title",
        description="Other title(s) or names for the resource.")
    translated_title = PermissibleValue(
        text="translated_title",
        description="Translation of the title into another language.")
    other = PermissibleValue(
        text="other",
        description="Anything that doesn't fit into the above categories.")

    _defn = EnumDefinition(
        name="TitleType",
        description="The type of title being represented.",
    )

# Slots
class slots:
    pass

slots.has_numeric_value = Slot(uri=BERTRON.has_numeric_value, name="has_numeric_value", curie=BERTRON.curie('has_numeric_value'),
                   model_uri=BERTRON.has_numeric_value, domain=None, range=Optional[float], mappings = [NMDC["has_numeric_value"], QUD["quantityValue"], SCHEMA["value"]])

slots.has_minimum_numeric_value = Slot(uri=BERTRON.has_minimum_numeric_value, name="has_minimum_numeric_value", curie=BERTRON.curie('has_minimum_numeric_value'),
                   model_uri=BERTRON.has_minimum_numeric_value, domain=None, range=Optional[float], mappings = [NMDC["has_minimum_numeric_value"]])

slots.has_maximum_numeric_value = Slot(uri=BERTRON.has_maximum_numeric_value, name="has_maximum_numeric_value", curie=BERTRON.curie('has_maximum_numeric_value'),
                   model_uri=BERTRON.has_maximum_numeric_value, domain=None, range=Optional[float], mappings = [NMDC["has_maximum_numeric_value"]])

slots.has_raw_value = Slot(uri=BERTRON.has_raw_value, name="has_raw_value", curie=BERTRON.curie('has_raw_value'),
                   model_uri=BERTRON.has_raw_value, domain=None, range=Optional[str], mappings = [NMDC["has_raw_value"]])

slots.has_unit = Slot(uri=BERTRON.has_unit, name="has_unit", curie=BERTRON.curie('has_unit'),
                   model_uri=BERTRON.has_unit, domain=None, range=Optional[str], mappings = [NMDC["has_unit"], QUD["unit"], SCHEMA["unitCode"]])

slots.entity__ber_data_source = Slot(uri=BERTRON.ber_data_source, name="entity__ber_data_source", curie=BERTRON.curie('ber_data_source'),
                   model_uri=BERTRON.entity__ber_data_source, domain=None, range=Union[str, "BERSourceType"])

slots.entity__credit_metadata = Slot(uri=BERTRON.credit_metadata, name="entity__credit_metadata", curie=BERTRON.curie('credit_metadata'),
                   model_uri=BERTRON.entity__credit_metadata, domain=None, range=Union[str, CreditMetadataIdentifier])

slots.entity__coordinates = Slot(uri=BERTRON.coordinates, name="entity__coordinates", curie=BERTRON.curie('coordinates'),
                   model_uri=BERTRON.entity__coordinates, domain=None, range=Union[dict, Coordinates])

slots.entity__data_type = Slot(uri=BERTRON.data_type, name="entity__data_type", curie=BERTRON.curie('data_type'),
                   model_uri=BERTRON.entity__data_type, domain=None, range=Union[Union[str, "DataTypeTagType"], list[Union[str, "DataTypeTagType"]]])

slots.entity__description = Slot(uri=SCHEMA.description, name="entity__description", curie=SCHEMA.curie('description'),
                   model_uri=BERTRON.entity__description, domain=None, range=Optional[str])

slots.entity__id = Slot(uri=SCHEMA.identifier, name="entity__id", curie=SCHEMA.curie('identifier'),
                   model_uri=BERTRON.entity__id, domain=None, range=Optional[str])

slots.entity__name = Slot(uri=SCHEMA.name, name="entity__name", curie=SCHEMA.curie('name'),
                   model_uri=BERTRON.entity__name, domain=None, range=Optional[str])

slots.entity__alt_ids = Slot(uri=BERTRON.alt_ids, name="entity__alt_ids", curie=BERTRON.curie('alt_ids'),
                   model_uri=BERTRON.entity__alt_ids, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.entity__alt_names = Slot(uri=BERTRON.alt_names, name="entity__alt_names", curie=BERTRON.curie('alt_names'),
                   model_uri=BERTRON.entity__alt_names, domain=None, range=Optional[Union[Union[dict, Name], list[Union[dict, Name]]]])

slots.entity__part_of_collection = Slot(uri=BERTRON.part_of_collection, name="entity__part_of_collection", curie=BERTRON.curie('part_of_collection'),
                   model_uri=BERTRON.entity__part_of_collection, domain=None, range=Optional[Union[Union[dict, DataCollection], list[Union[dict, DataCollection]]]])

slots.entity__uri = Slot(uri=BERTRON.uri, name="entity__uri", curie=BERTRON.curie('uri'),
                   model_uri=BERTRON.entity__uri, domain=None, range=Union[str, URIorCURIE])

slots.coordinates__altitude = Slot(uri=MIXS['0000094'], name="coordinates__altitude", curie=MIXS.curie('0000094'),
                   model_uri=BERTRON.coordinates__altitude, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.coordinates__depth = Slot(uri=MIXS['0000018'], name="coordinates__depth", curie=MIXS.curie('0000018'),
                   model_uri=BERTRON.coordinates__depth, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.coordinates__elevation = Slot(uri=MIXS['0000093'], name="coordinates__elevation", curie=MIXS.curie('0000093'),
                   model_uri=BERTRON.coordinates__elevation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.coordinates__latitude = Slot(uri=WGS84.lat, name="coordinates__latitude", curie=WGS84.curie('lat'),
                   model_uri=BERTRON.coordinates__latitude, domain=None, range=float, mappings = [SCHEMA["latitude"]])

slots.coordinates__longitude = Slot(uri=WGS84.long, name="coordinates__longitude", curie=WGS84.curie('long'),
                   model_uri=BERTRON.coordinates__longitude, domain=None, range=float, mappings = [SCHEMA["longitude"]])

slots.name__name_type = Slot(uri=BERTRON.name_type, name="name__name_type", curie=BERTRON.curie('name_type'),
                   model_uri=BERTRON.name__name_type, domain=None, range=Optional[Union[str, "NameType"]])

slots.name__name = Slot(uri=SCHEMA.name, name="name__name", curie=SCHEMA.curie('name'),
                   model_uri=BERTRON.name__name, domain=None, range=str)

slots.dataCollection__id = Slot(uri=SCHEMA.identifier, name="dataCollection__id", curie=SCHEMA.curie('identifier'),
                   model_uri=BERTRON.dataCollection__id, domain=None, range=Optional[str])

slots.dataCollection__title = Slot(uri=SCHEMA.name, name="dataCollection__title", curie=SCHEMA.curie('name'),
                   model_uri=BERTRON.dataCollection__title, domain=None, range=Optional[str])

slots.dataCollection__description = Slot(uri=SCHEMA.description, name="dataCollection__description", curie=SCHEMA.curie('description'),
                   model_uri=BERTRON.dataCollection__description, domain=None, range=Optional[str])

slots.dataCollection__alt_ids = Slot(uri=BERTRON.alt_ids, name="dataCollection__alt_ids", curie=BERTRON.curie('alt_ids'),
                   model_uri=BERTRON.dataCollection__alt_ids, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.dataCollection__alt_titles = Slot(uri=BERTRON.alt_titles, name="dataCollection__alt_titles", curie=BERTRON.curie('alt_titles'),
                   model_uri=BERTRON.dataCollection__alt_titles, domain=None, range=Optional[Union[Union[dict, Name], list[Union[dict, Name]]]])

slots.dataCollection__url = Slot(uri=BERTRON.url, name="dataCollection__url", curie=BERTRON.curie('url'),
                   model_uri=BERTRON.dataCollection__url, domain=None, range=Union[str, URIorCURIE])

slots.creditMetadata__comment = Slot(uri=SCHEMA.comment, name="creditMetadata__comment", curie=SCHEMA.curie('comment'),
                   model_uri=BERTRON.creditMetadata__comment, domain=None, range=Optional[Union[str, list[str]]])

slots.creditMetadata__content_url = Slot(uri=DCM.content_url, name="creditMetadata__content_url", curie=DCM.curie('content_url'),
                   model_uri=BERTRON.creditMetadata__content_url, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.creditMetadata__contributors = Slot(uri=SCHEMA.creator, name="creditMetadata__contributors", curie=SCHEMA.curie('creator'),
                   model_uri=BERTRON.creditMetadata__contributors, domain=None, range=Union[Union[dict, Contributor], list[Union[dict, Contributor]]])

slots.creditMetadata__dates = Slot(uri=DCM.dates, name="creditMetadata__dates", curie=DCM.curie('dates'),
                   model_uri=BERTRON.creditMetadata__dates, domain=None, range=Optional[Union[Union[dict, EventDate], list[Union[dict, EventDate]]]])

slots.creditMetadata__descriptions = Slot(uri=SCHEMA.description, name="creditMetadata__descriptions", curie=SCHEMA.curie('description'),
                   model_uri=BERTRON.creditMetadata__descriptions, domain=None, range=Optional[Union[Union[dict, Description], list[Union[dict, Description]]]])

slots.creditMetadata__funding = Slot(uri=SCHEMA.funding, name="creditMetadata__funding", curie=SCHEMA.curie('funding'),
                   model_uri=BERTRON.creditMetadata__funding, domain=None, range=Optional[Union[Union[dict, FundingReference], list[Union[dict, FundingReference]]]])

slots.creditMetadata__identifier = Slot(uri=SCHEMA.identifier, name="creditMetadata__identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=BERTRON.creditMetadata__identifier, domain=None, range=URIRef,
                   pattern=re.compile(r'^[a-zA-Z0-9.-_]+:\S'))

slots.creditMetadata__license = Slot(uri=SCHEMA.license, name="creditMetadata__license", curie=SCHEMA.curie('license'),
                   model_uri=BERTRON.creditMetadata__license, domain=None, range=Optional[Union[dict, License]])

slots.creditMetadata__meta = Slot(uri=DCM.meta, name="creditMetadata__meta", curie=DCM.curie('meta'),
                   model_uri=BERTRON.creditMetadata__meta, domain=None, range=Union[dict, Metadata])

slots.creditMetadata__publisher = Slot(uri=SCHEMA.provider, name="creditMetadata__publisher", curie=SCHEMA.curie('provider'),
                   model_uri=BERTRON.creditMetadata__publisher, domain=None, range=Optional[Union[dict, Organization]])

slots.creditMetadata__related_identifiers = Slot(uri=DCM.related_identifiers, name="creditMetadata__related_identifiers", curie=DCM.curie('related_identifiers'),
                   model_uri=BERTRON.creditMetadata__related_identifiers, domain=None, range=Optional[Union[Union[dict, PermanentID], list[Union[dict, PermanentID]]]])

slots.creditMetadata__resource_type = Slot(uri=SCHEMA['@type'], name="creditMetadata__resource_type", curie=SCHEMA.curie('@type'),
                   model_uri=BERTRON.creditMetadata__resource_type, domain=None, range=Union[str, "ResourceType"])

slots.creditMetadata__titles = Slot(uri=DCM.titles, name="creditMetadata__titles", curie=DCM.curie('titles'),
                   model_uri=BERTRON.creditMetadata__titles, domain=None, range=Union[Union[dict, Title], list[Union[dict, Title]]])

slots.creditMetadata__url = Slot(uri=DCM.url, name="creditMetadata__url", curie=DCM.curie('url'),
                   model_uri=BERTRON.creditMetadata__url, domain=None, range=Optional[Union[str, URI]])

slots.creditMetadata__version = Slot(uri=SCHEMA.version, name="creditMetadata__version", curie=SCHEMA.curie('version'),
                   model_uri=BERTRON.creditMetadata__version, domain=None, range=Optional[str])

slots.contributor__contributor_type = Slot(uri=SCHEMA['@type'], name="contributor__contributor_type", curie=SCHEMA.curie('@type'),
                   model_uri=BERTRON.contributor__contributor_type, domain=None, range=Optional[Union[str, "ContributorType"]])

slots.contributor__contributor_id = Slot(uri=SCHEMA.identifier, name="contributor__contributor_id", curie=SCHEMA.curie('identifier'),
                   model_uri=BERTRON.contributor__contributor_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^[a-zA-Z0-9.-_]+:\S'))

slots.contributor__name = Slot(uri=SCHEMA.name, name="contributor__name", curie=SCHEMA.curie('name'),
                   model_uri=BERTRON.contributor__name, domain=None, range=Optional[str])

slots.contributor__given_name = Slot(uri=DCM.given_name, name="contributor__given_name", curie=DCM.curie('given_name'),
                   model_uri=BERTRON.contributor__given_name, domain=None, range=Optional[str])

slots.contributor__family_name = Slot(uri=DCM.family_name, name="contributor__family_name", curie=DCM.curie('family_name'),
                   model_uri=BERTRON.contributor__family_name, domain=None, range=Optional[str])

slots.contributor__affiliations = Slot(uri=SCHEMA.affiliation, name="contributor__affiliations", curie=SCHEMA.curie('affiliation'),
                   model_uri=BERTRON.contributor__affiliations, domain=None, range=Optional[Union[Union[dict, Organization], list[Union[dict, Organization]]]])

slots.contributor__contributor_roles = Slot(uri=SCHEMA.Role, name="contributor__contributor_roles", curie=SCHEMA.curie('Role'),
                   model_uri=BERTRON.contributor__contributor_roles, domain=None, range=Optional[Union[Union[str, "ContributorRole"], list[Union[str, "ContributorRole"]]]])

slots.dataSource__access_timestamp = Slot(uri=DCM.access_timestamp, name="dataSource__access_timestamp", curie=DCM.curie('access_timestamp'),
                   model_uri=BERTRON.dataSource__access_timestamp, domain=None, range=int)

slots.dataSource__source_data_updated = Slot(uri=DCM.source_data_updated, name="dataSource__source_data_updated", curie=DCM.curie('source_data_updated'),
                   model_uri=BERTRON.dataSource__source_data_updated, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dataSource__source_name = Slot(uri=DCM.source_name, name="dataSource__source_name", curie=DCM.curie('source_name'),
                   model_uri=BERTRON.dataSource__source_name, domain=None, range=Optional[str])

slots.dataSource__source_url = Slot(uri=DCM.source_url, name="dataSource__source_url", curie=DCM.curie('source_url'),
                   model_uri=BERTRON.dataSource__source_url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.description__description_text = Slot(uri=DCM.description_text, name="description__description_text", curie=DCM.curie('description_text'),
                   model_uri=BERTRON.description__description_text, domain=None, range=str)

slots.description__description_type = Slot(uri=DCM.description_type, name="description__description_type", curie=DCM.curie('description_type'),
                   model_uri=BERTRON.description__description_type, domain=None, range=Optional[Union[str, "DescriptionType"]])

slots.description__language = Slot(uri=DCM.language, name="description__language", curie=DCM.curie('language'),
                   model_uri=BERTRON.description__language, domain=None, range=Optional[str])

slots.eventDate__date = Slot(uri=DCM.date, name="eventDate__date", curie=DCM.curie('date'),
                   model_uri=BERTRON.eventDate__date, domain=None, range=str,
                   pattern=re.compile(r'\d{4}(-\d{2}){0,2}'))

slots.eventDate__event = Slot(uri=DCM.event, name="eventDate__event", curie=DCM.curie('event'),
                   model_uri=BERTRON.eventDate__event, domain=None, range=Union[str, "EventType"])

slots.fundingReference__funder = Slot(uri=SCHEMA.funder, name="fundingReference__funder", curie=SCHEMA.curie('funder'),
                   model_uri=BERTRON.fundingReference__funder, domain=None, range=Optional[Union[dict, Organization]])

slots.fundingReference__grant_id = Slot(uri=SCHEMA.identifier, name="fundingReference__grant_id", curie=SCHEMA.curie('identifier'),
                   model_uri=BERTRON.fundingReference__grant_id, domain=None, range=Optional[str])

slots.fundingReference__grant_title = Slot(uri=SCHEMA.name, name="fundingReference__grant_title", curie=SCHEMA.curie('name'),
                   model_uri=BERTRON.fundingReference__grant_title, domain=None, range=Optional[str])

slots.fundingReference__grant_url = Slot(uri=SCHEMA.url, name="fundingReference__grant_url", curie=SCHEMA.curie('url'),
                   model_uri=BERTRON.fundingReference__grant_url, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^[a-zA-Z0-9.-_]+:\S'))

slots.license__id = Slot(uri=DCM.id, name="license__id", curie=DCM.curie('id'),
                   model_uri=BERTRON.license__id, domain=None, range=Optional[str])

slots.license__url = Slot(uri=DCM.url, name="license__url", curie=DCM.curie('url'),
                   model_uri=BERTRON.license__url, domain=None, range=Optional[Union[str, URI]])

slots.metadata__credit_metadata_schema_version = Slot(uri=SCHEMA.schemaVersion, name="metadata__credit_metadata_schema_version", curie=SCHEMA.curie('schemaVersion'),
                   model_uri=BERTRON.metadata__credit_metadata_schema_version, domain=None, range=str)

slots.metadata__credit_metadata_source = Slot(uri=DCM.credit_metadata_source, name="metadata__credit_metadata_source", curie=DCM.curie('credit_metadata_source'),
                   model_uri=BERTRON.metadata__credit_metadata_source, domain=None, range=Optional[Union[Union[dict, DataSource], list[Union[dict, DataSource]]]])

slots.metadata__saved_by = Slot(uri=SCHEMA.sdPublisher, name="metadata__saved_by", curie=SCHEMA.curie('sdPublisher'),
                   model_uri=BERTRON.metadata__saved_by, domain=None, range=str)

slots.metadata__timestamp = Slot(uri=SCHEMA.sdDatePublished, name="metadata__timestamp", curie=SCHEMA.curie('sdDatePublished'),
                   model_uri=BERTRON.metadata__timestamp, domain=None, range=int)

slots.organization__organization_id = Slot(uri=SCHEMA.identifier, name="organization__organization_id", curie=SCHEMA.curie('identifier'),
                   model_uri=BERTRON.organization__organization_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^[a-zA-Z0-9.-_]+:\S'))

slots.organization__organization_name = Slot(uri=SCHEMA.name, name="organization__organization_name", curie=SCHEMA.curie('name'),
                   model_uri=BERTRON.organization__organization_name, domain=None, range=str)

slots.permanentID__id = Slot(uri=SCHEMA.identifier, name="permanentID__id", curie=SCHEMA.curie('identifier'),
                   model_uri=BERTRON.permanentID__id, domain=None, range=Union[str, URIorCURIE],
                   pattern=re.compile(r'^[a-zA-Z0-9.-_]+:\S'))

slots.permanentID__description = Slot(uri=SCHEMA.description, name="permanentID__description", curie=SCHEMA.curie('description'),
                   model_uri=BERTRON.permanentID__description, domain=None, range=Optional[str])

slots.permanentID__relationship_type = Slot(uri=DCM.relationship_type, name="permanentID__relationship_type", curie=DCM.curie('relationship_type'),
                   model_uri=BERTRON.permanentID__relationship_type, domain=None, range=Optional[Union[str, "RelationshipType"]])

slots.title__language = Slot(uri=DCM.language, name="title__language", curie=DCM.curie('language'),
                   model_uri=BERTRON.title__language, domain=None, range=Optional[str])

slots.title__title = Slot(uri=SCHEMA.name, name="title__title", curie=SCHEMA.curie('name'),
                   model_uri=BERTRON.title__title, domain=None, range=str)

slots.title__title_type = Slot(uri=DCM.title_type, name="title__title_type", curie=DCM.curie('title_type'),
                   model_uri=BERTRON.title__title_type, domain=None, range=Optional[Union[str, "TitleType"]])

slots.QuantityValue_has_raw_value = Slot(uri=BERTRON.has_raw_value, name="QuantityValue_has_raw_value", curie=BERTRON.curie('has_raw_value'),
                   model_uri=BERTRON.QuantityValue_has_raw_value, domain=QuantityValue, range=Optional[str], mappings = [NMDC["has_raw_value"]])

slots.QuantityValue_has_unit = Slot(uri=BERTRON.has_unit, name="QuantityValue_has_unit", curie=BERTRON.curie('has_unit'),
                   model_uri=BERTRON.QuantityValue_has_unit, domain=QuantityValue, range=Optional[str], mappings = [NMDC["has_unit"], QUD["unit"], SCHEMA["unitCode"]])

slots.QuantityValue_has_numeric_value = Slot(uri=BERTRON.has_numeric_value, name="QuantityValue_has_numeric_value", curie=BERTRON.curie('has_numeric_value'),
                   model_uri=BERTRON.QuantityValue_has_numeric_value, domain=QuantityValue, range=Optional[float], mappings = [NMDC["has_numeric_value"], QUD["quantityValue"], SCHEMA["value"]])

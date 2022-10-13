"""
  Python Class representations of Avro definitions
"""
from pydantic import Field
from pydantic.dataclasses import dataclass


# Union is obsolete in Python 3.10
# List is replaced with list
# Optional[Something] is actually a shortcut for Union[Something, None]

@dataclass
class Link:
  url: str
  summary: str
  category: str = "website"
  title: str | None = Field(default=None)

@dataclass
class Category:
  entity: str
  name: str
  links: set[str] = set()

@dataclass
class Country:
  name: str
  iso2: str
  iso3: str
  official: bool
  sources: set[str] = set()

@dataclass
class CountryState:
  country: Country
  state: str
  name: str

@dataclass(frozen=True)
class Position:
  longitude: float = 0.0
  latitude: float = 0.0
  altitude: float | None = Field(default=None)

class Location:
  country: Country
  state: str | None = Field(default=None)
  city: str | None  = Field(default=None)
  address: str | None = Field(default=None)
  position: Position | None = Field(default=None)

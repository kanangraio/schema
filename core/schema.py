"""
  Python Class representations of Avro definitions
"""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Link:
  url: str
  summary: str
  category: str = "website"
  title: Optional[str] = field(default=None)

@dataclass
class Category:
  entity: str
  name: str
  links: List[str] = None

@dataclass
class Country:
  name: str
  ISO2: str
  ISO3: str
  official: bool
  sources: List[str]

@dataclass
class CountryState:
  country: Country
  state: str
  name: str

@dataclass(frozen=True)
class Position:
  longitude: float = 0.0
  latitude: float = 0.0
  altitude: Optional[float] = field(default=None)

class Location:
  country: Country
  state: Optional[CountryState] = field(default=None)
  city: Optional[str] = field(default=None)
  address: Optional[str] = field(default=None)
  position: Optional[Position] = field(default=None)

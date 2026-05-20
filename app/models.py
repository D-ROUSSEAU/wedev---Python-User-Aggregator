from typing import TypedDict

class Address(TypedDict):
    city: str


class Company(TypedDict):
    name: str


class User(TypedDict):
    id: int
    name: str
    email: str
    address: Address
    company: Company


class NormalizedUser(TypedDict):
    id: int
    full_name: str
    email: str
    city: str
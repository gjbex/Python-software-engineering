#!/usr/bin/env python

from typing import NewType

PersonId = NewType('PersonId', int)
Age = NewType('Age', int)

class Person:
    _person_id: PersonId
    _age: Age

    def __init__(self, person_id: PersonId, age: Age) -> None:
        self._person_id = person_id
        self._age = age

    @property
    def person_id(self) -> PersonId:
        return self._person_id

    @person_id.setter
    def person_id(self, person_id: PersonId) -> None:
        self._person_id = person_id

    @property
    def age(self) -> Age:
        return self._age

    @age.setter
    def age(self, age: Age) -> None:
        self._age = age

    def __repr__(self) -> str:
        return f'Person(person_id={self.person_id}, age={self.age})'


if __name__ == '__main__':
    person = Person(PersonId(1), Age(20))
    print(person)
    person.person_id = PersonId(2)
    person.age = Age(30)
    print(person)
    print(person.person_id)
    print(person.age)
    print(person.person_id + 1)
    print(person.age + 1)
    print(person.person_id + person.age)
    person.age = PersonId(40)
    person.age = 25

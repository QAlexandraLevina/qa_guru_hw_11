import dataclasses
from typing import Tuple


@dataclasses.dataclass
class UserData:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    birthday: Tuple[str, str, str]
    subject: str
    hobbies: Tuple[str, str, str]
    picture: str
    address: str
    state_city: Tuple[str, str]

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def date_of_birth(self) -> str:
        month_data, year_data, day_data = self.birthday
        return f"{int(day_data):02d} {month_data},{year_data}"

    @property
    def hobby(self) -> str:
        hobby_1, hobby_2, hobby_3 = self.hobbies
        return f"{hobby_1}, {hobby_2}, {hobby_3}"

    @property
    def state_n_city(self) -> str:
        state_data, city_data = self.state_city
        return f"{state_data} {city_data}"
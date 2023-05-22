import dataclasses

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: int
    birthday: str
    subjects: str
    hobbies: str
    hobby: str
    image: str
    address: str
    state: str
    city: str


user_1 = User(
    first_name='Alexander',
    last_name='Pupkin',
    email='Pupkin@gmail.com',
    gender='Male',
    phone_number=int(7906777777),
    birthday='10 November,1990',
    subjects='Computer Science',
    hobbies='1',
    hobby='Sports',
    image='pocita.jpg',
    address='914751, Оренбургская область, город Волоколамск, проезд Сталина, 09',
    state='Haryana',
    city='Karnal'
)

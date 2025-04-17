from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

SQLALCHEMY_DATABASE_URL = 'sqlite:///db_app/module10.db?check_same_thread=False'
Base = declarative_base()


class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True, name='memid')
    surname = Column(String)
    first_name = Column(String)
    address = Column(String)
    zipcode = Column(Integer)
    telephone = Column(String)
    recommended_by_id = Column(
        Integer, ForeignKey('members.memid'), name = 'recommendedby'
    )
    recommended_by = relationship('Member', remote_side=[id])
    join_date = Column(Date, name='joindate')

    def __repr__(self):
        return f'{self.id} {self.first_name} {self.surname} {self.zipcode}'


class Facility(Base):
    __tablename__ = 'facilities'

    id = Column(Integer, primary_key=True, name='facid')
    name = Column(String)
    membercost = Column(Integer)
    guestcost = Column(Integer)
    initialoutlay = Column(Integer)
    monthlymaintenance = Column(Integer)

    def __repr__(self):
        return f'{self.name} {self.id} {self.membercost}'

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, name='bookid')
    facility_id = Column(
        Integer, ForeignKey('facilities.facid'), primary_key=True, name='facid'
    )
    facility_rl = relationship('Facility')
    member_id = Column(
        Integer, ForeignKey('members.memid'), primary_key=True, name='memid'
    )
    member_rl = relationship('Member')
    start_time = Column(Date)
    slots = Column(Integer)

    def __repr__(self):
        return f'{self.id} {self.member_id} {self.start_time}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def initialization():
    new_row = Member(surname='Cat', first_name='Jacklyn', address='Yablonevay 7-44', zipcode=76532,
                     telephone='34-906-2352', join_date=datetime.strptime('2024-10-03','%Y-%m-%d'), recommended_by_id=7)

    new_row1 = Member(surname='Smith', first_name='Daniel', address='Oak Street 12-5', zipcode=12345,
                      telephone='11-234-5678', join_date=datetime.strptime('2023-08-15','%Y-%m-%d'), recommended_by_id=5)

    new_row2 = Member(surname='Lopez', first_name='Maria', address='Elm Avenue 3-21', zipcode=54321,
                      telephone='22-345-6789', join_date=datetime.strptime('2022-06-10','%Y-%m-%d'), recommended_by_id=None)

    new_row3 = Member(surname='Nguyen', first_name='Linh', address='Pine Road 9-7', zipcode=98765,
                      telephone='33-456-7890', join_date=datetime.strptime('2024-01-05','%Y-%m-%d'), recommended_by_id=1)

    new_row4 = Member(surname='Johnson', first_name='Alex', address='Maple Blvd 18-2', zipcode=11223,
                      telephone='44-567-8901', join_date=datetime.strptime('2023-03-22','%Y-%m-%d'), recommended_by_id=None)

    new_row5 = Member(surname='Kim', first_name='Hana', address='Cedar Lane 5-19', zipcode=66789,
                      telephone='55-678-9012', join_date=datetime.strptime('2024-10-10','%Y-%m-%d'), recommended_by_id=7)

    new_row6 = Member(surname='Brown', first_name='Eli', address='Spruce St 14-8', zipcode=33445,
                      telephone='66-789-0123', join_date=datetime.strptime('2022-12-01','%Y-%m-%d'), recommended_by_id=None)

    new_row7 = Member(surname='Ivanov', first_name='Sergey', address='Berezovaya 1-3', zipcode=55664,
                      telephone='77-890-1234', join_date=datetime.strptime('2024-05-12','%Y-%m-%d'), recommended_by_id=None)

    new_row8 = Member(surname='Tanaka', first_name='Yuki', address='Sakura Dr 10-9', zipcode=77889,
                      telephone='88-901-2345', join_date=datetime.strptime('2023-11-20','%Y-%m-%d'), recommended_by_id=4)

    session = SessionLocal()
    session.add_all([new_row, new_row1, new_row2, new_row3, new_row4, new_row5, new_row6, new_row7, new_row8])
    session.commit()

    fac0 = Facility(name='Flat 35', membercost='110', guestcost='147', initialoutlay='27', monthlymaintenance='14')
    fac1 = Facility(name='Ocean View', membercost='120', guestcost='150', initialoutlay='35', monthlymaintenance='20')
    fac2 = Facility(name='Garden Retreat', membercost='95', guestcost='130', initialoutlay='22', monthlymaintenance='18')
    fac3 = Facility(name='City Loft', membercost='105', guestcost='140', initialoutlay='30', monthlymaintenance='16')
    fac4 = Facility(name='Mountain Cabin', membercost='100', guestcost='135', initialoutlay='28', monthlymaintenance='17')
    fac5 = Facility(name='Lakeside Gym', membercost='115', guestcost='145', initialoutlay='25', monthlymaintenance='19')
    fac6 = Facility(name='Sunset Club', membercost='130', guestcost='160', initialoutlay='40', monthlymaintenance='21')
    session.add_all([fac0, fac1, fac2, fac3, fac4, fac5, fac6])
    session.commit()

    boo = Booking(id=25,facility_id=1, member_id=1, start_time=datetime.strptime('2020-10-10','%Y-%m-%d'), slots=4)
    boo0 = Booking(id=0, facility_id=8, member_id=7, start_time=datetime.strptime('2023-04-10', '%Y-%m-%d'), slots=20)
    boo1 = Booking(id=1, facility_id=6, member_id=4, start_time=datetime.strptime('2022-05-06', '%Y-%m-%d'), slots=1)
    boo2 = Booking(id=2, facility_id=1, member_id=6, start_time=datetime.strptime('2024-02-27', '%Y-%m-%d'), slots=1)
    boo3 = Booking(id=3, facility_id=2, member_id=3, start_time=datetime.strptime('2021-07-14', '%Y-%m-%d'), slots=14)
    boo4 = Booking(id=4, facility_id=2, member_id=4, start_time=datetime.strptime('2021-01-18', '%Y-%m-%d'), slots=13)
    boo5 = Booking(id=5, facility_id=8, member_id=3, start_time=datetime.strptime('2020-12-20', '%Y-%m-%d'), slots=3)
    boo6 = Booking(id=6, facility_id=9, member_id=2, start_time=datetime.strptime('2020-06-19', '%Y-%m-%d'), slots=11)
    boo7 = Booking(id=7, facility_id=7, member_id=3, start_time=datetime.strptime('2021-08-27', '%Y-%m-%d'), slots=11)
    boo8 = Booking(id=8, facility_id=5, member_id=3, start_time=datetime.strptime('2023-11-28', '%Y-%m-%d'), slots=10)
    boo9 = Booking(id=9, facility_id=9, member_id=2, start_time=datetime.strptime('2020-06-22', '%Y-%m-%d'), slots=11)
    boo10 = Booking(id=10, facility_id=1, member_id=7, start_time=datetime.strptime('2022-02-08', '%Y-%m-%d'), slots=16)
    boo11 = Booking(id=11, facility_id=3, member_id=4, start_time=datetime.strptime('2020-08-13', '%Y-%m-%d'), slots=18)
    boo12 = Booking(id=12, facility_id=5, member_id=6, start_time=datetime.strptime('2023-07-07', '%Y-%m-%d'), slots=3)
    boo13 = Booking(id=13, facility_id=4, member_id=7, start_time=datetime.strptime('2022-04-01', '%Y-%m-%d'), slots=6)
    boo14 = Booking(id=14, facility_id=2, member_id=3, start_time=datetime.strptime('2022-01-02', '%Y-%m-%d'), slots=6)
    boo15 = Booking(id=15, facility_id=1, member_id=2, start_time=datetime.strptime('2022-08-20', '%Y-%m-%d'), slots=11)
    boo16 = Booking(id=16, facility_id=5, member_id=4, start_time=datetime.strptime('2022-04-20', '%Y-%m-%d'), slots=4)
    boo17 = Booking(id=17, facility_id=6, member_id=2, start_time=datetime.strptime('2022-06-18', '%Y-%m-%d'), slots=3)
    boo18 = Booking(id=18, facility_id=8, member_id=3, start_time=datetime.strptime('2021-10-14', '%Y-%m-%d'), slots=10)
    boo19 = Booking(id=19, facility_id=5, member_id=6, start_time=datetime.strptime('2021-10-02', '%Y-%m-%d'), slots=11)

    session.add_all([boo,boo0,boo1,boo2,boo3,boo4,boo5,boo6,boo7,boo8,boo9,boo10,boo11,boo12,boo13,boo14,boo15,boo16,boo17,boo18,boo19])
    session.commit()

if __name__ == '__main__':
    initialization()

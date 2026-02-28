from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,  relationship

from .base import Model

class Region(Model):
    name: Mapped[str] = mapped_column(String)
    districts: Mapped[list['District']] = relationship('District', back_populates='region')

    def str(self):
        return f'{self.id} {self.name}'


class District(Model):
    name: Mapped[str] = mapped_column(String)
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'))

    region: Mapped['Region'] = relationship('Region', back_populates='districts')

    def str(self):
        return f'{self.id} {self.name} {self.region_id}'
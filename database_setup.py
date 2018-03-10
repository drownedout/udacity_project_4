import sys
# For mapper code
from sqlalchemy import Column, ForeignKey, Integer, String
# For configuration
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
# To create Foreign Key relationship
from sqlalchemy.orm import relationship

# Let SQL know to use special SQL Alchemy classes
Base = declarative_base()

class Category(Base):
	# Sets the table name in SQL db
	__tablename__ = 'category'
	# ID Column (Primary Key)
	id = Column(Integer, primary_key = True)
	# Name column
	name = Column(String(80), nullable=False)

class CategoryItem(Base):
	__tablename__ = 'category_item'

	# ID Column (Primary Key)
	id = Column(Integer, primary_key = True)
	# Name column
	name = Column(String(80), nullable=False)
	# Description column
	description = Column(String(250))

	# Creates foreign key relationship between Item and Category
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)

engine = create_engine('sqlite:///categoryitem.db')

# Adds classes as new tables in the database
Base.metadata.create_all(engine)
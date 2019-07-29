from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__='Knowledge'
	a_id = Column(Integer, primary_key=True)
	a_topic= Column(String)
	a_rating=Column(Integer)

	def __repr__(self):
		return ("Knowledge id: {}\n"
			"Knowledge topic: {}\n"
			"Knowledge rating: {}\n").format(
			self.a_id,
			self.a_topic,
			self.a_rating
			)
	def bad_good(a_rating):
		if a_rating<7:
			print("Unfortunately, this article does not have a better rating. Maybe, this is an article that should bereplaced soon")
		else:
			print("a great article")
article1= Knowledge(a_topic="friends", a_rating=11)
article2 = Knowledge(a_topic="himym",a_rating=3)
article3=Knowledge(a_topic="languageus",a_rating=8)


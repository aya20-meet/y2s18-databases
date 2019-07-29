from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(a_topic, a_rating):
	article_object=Knowledge(a_topic=a_topic,a_rating=a_rating)
	session.add(article_object)
	session.commit()
add_article("chicken", 10)
add_article("firends", 11)
add_article("himym",3)	


def query_all_articles():
	artic=session.query(Knowledge).all()
	return artic 
print(query_all_articles())

def query_article_by_topic(a_topic):
	top = session.query(Knowledge).filter_by(a_topic=a_topic).first()
	return top
print(query_article_by_topic("chicken"))

def delete_article_by_topic(a_topic):
	d_top=session.query(Knowledge).filter_by(a_topic=a_topic).delete()
	session.commit()
	
print(delete_article_by_topic("firends"))

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()
delete_all_articles()

def edit_article_rating():
	alert= session.query(Knowledge).all()
	

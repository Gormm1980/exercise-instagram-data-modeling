import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))
    description = Column (String(250))
    email = Column (String(65), nullable=False)

class Follow(Base) :
    __tablename__ = 'follow'
    id =  id = Column(Integer, primary_key=True)
    user_from_id= Column(Integer, ForeignKey('user.id'))
    usert_to_id = Column(Integer, ForeignKey('user.id'))
    user=relationship(User)


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    user_id= Column(Integer, ForeignKey('user.id'))
    user=relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
   

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user=relationship(User)
    
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post= relationship(Post)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
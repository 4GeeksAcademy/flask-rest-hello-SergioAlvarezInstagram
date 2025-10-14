from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(255), nullable=False)
    lastname: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

class Follower(db.Model):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user_to_id: Mapped[int] = mapped_column(ForeignKey('user.id'))


class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    comment_text: Mapped[str] = mapped_column(String(255))
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    

class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    
    
class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(255))
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))

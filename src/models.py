from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(255))
    lastname: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    posts: Mapped[list['Post']] = relationship(back_populates='users')
    comments: Mapped[list['Comment']] = relationship(back_populates='author')
    followers: Mapped[list['Follower']] = relationship(back_populates='followed', foreign_keys='Follower.user_to_id')
    following: Mapped[list['Follower']] = relationship(back_populates='follower', foreign_keys='Follower.user_from_id')
    


class Follower(db.Model):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user_to_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    follower: Mapped['User'] = relationship(back_populates='following', foreign_keys=user_from_id)
    followed: Mapped['User'] = relationship(back_populates='followers', foreign_keys=user_to_id)

    



class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    comment_text: Mapped[str] = mapped_column(String(255))
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    author : Mapped['User'] = relationship(back_populates='comments')


class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    users: Mapped['User'] = relationship(back_populates='posts')
    
    
class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(255))
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))

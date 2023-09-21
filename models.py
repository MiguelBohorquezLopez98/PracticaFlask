from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

#Clase usuario - tabla usuario
class User(db.Model, UserMixin):
    __tablename__= "user_login"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    #Relacion uno a muchos de la tabla usuario a la tabla cursos - Tabla padre
    courses = db.relationship('Courses', backref='user', lazy=True)

    #Hasheando password
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    # para verificar la contraseña del usuario
    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

#Clase cursos - tabla cursos    
class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profesor = db.Column(db.String(60), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(250), nullable=False)
    #Relacion uno a muchos de la tabla usuario a la tabla cursos - Tabla hijo
    user_login_id = db.Column(db.Integer, db.ForeignKey('user_login.id'), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Courses.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Courses.query.get(id)

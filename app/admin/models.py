from app import db



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
from flask_app import db

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Relation one-to-one avec Profil
    profil = db.relationship('Profil', backref='utilisateur', uselist=False)

    def __repr__(self):
        return f"<Utilisateur {self.nom}>"

class Profil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))

    def __repr__(self):
        return f"<Profil {self.id}>"

from extensions import db  # ✅ use extensions, NOT app

class Issue(db.Model):
    ...

class User(db.Model):
    ...

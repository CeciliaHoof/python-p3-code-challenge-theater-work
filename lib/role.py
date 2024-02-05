from lib.audition import Audition


class Role:
    all = []

    def __init__(self, character_name):
        self.character_name = character_name

        Role.all.append(self)
    
    @property
    def character_name(self):
        return self._character_name
    
    @character_name.setter
    def character_name(self, new_name):
        if type(new_name) == str and len(new_name) > 0:
            self._character_name = new_name
        else:
            raise Exception("Character name must be a string")
    
    def auditions(self):
        return [audition for audition in Audition.all if audition.role == self]
    
    def actors(self):
        return [audition.actor for audition in self.auditions()]
    
    def locations(self):
        return [audition.location for audition in self.auditions()]
    
    def lead(self):
        actors = [audition.actor for audition in Audition.hired_actors if audition.role == self]
        if len(actors) == 0:
            return "No actor has been hired for this role"
        else:
            return actors[0]
    
    def understudy(self):
        actors = [audition.actor for audition in Audition.hired_actors if audition.role == self]
        if len(actors) < 2:
            return "No actor has been hired for understudy for this role"
        else:
            return actors[1]
    
    @classmethod
    def not_cast(cls):
        return [role for role in cls.all if role.lead() == "No actor has been hired for this role"]
    
    def __str__(self):
        return f'Role: {self.character_name}'
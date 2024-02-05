class Audition:
    all = []
    hired_actors = []

    def __init__(self, role, actor, location, phone):
        self.role = role
        self.actor = actor
        self.location = location
        self.phone = phone
        self.hired = False

        self.__class__.all.append(self)

    @property
    def actor(self):
        return self._actor
    
    @actor.setter
    def actor(self, new_actor):
        if type(new_actor) == str and 3 < len(new_actor) < 20:
            self._actor = new_actor
        else:
            raise Exception("Actor must be a string between 3 and 20 characters long")
    
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, new_role):
        from lib.role import Role
        if isinstance(new_role, Role):
            self._role = new_role
        else:
            raise Exception("Role must be a role")
    
    def call_back(self):
        self.hired = True
        self.__class__.hired_actors.append(self)
    
    def __str__(self):
        return f'{self.role}. Actor: {self.actor}. Hired: {self.hired}'
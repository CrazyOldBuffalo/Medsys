class Condition:
    def __init__(self, name, description, symptoms, treatment):
        self.name = name
        self.description = description
        self.symptoms = symptoms
        self.treatment = treatment

        super().__init__()

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def get_symptoms(self):
        return self.symptoms

    def get_treatment(self):
        return self.treatment
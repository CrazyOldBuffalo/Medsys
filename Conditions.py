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

Dead = Condition("Mortem", "The Patient is dead mate, they ain't coming back from this one", ['Patient has no pulse', 'Patient is not breathing', 'patient is non-responsive'], "Nothing short of a miracle will bring them back from this one")
Bursitis = Condition("Bursitis", "Joints become painful, tender and swollen that can be treated at home", "Joint is painful, tender or swollen", "Treatment involves Resting, use of Ice on the joint and elevating the affected limb")
Absess = Condition("Absess", "A swollen, pus-filled lump under the surface of the skin caused by a bacterial infection.", ['Pain in affected area','high temperature', 'generally feeling unwell'],"May drain naturally with time. Antibiotics Treatment with incision to drain the pus")
Pancreatitis = Condition("Acute Pancreatitis", "Acute pancreatitis is a condition where the pancreas becomes inflamed over a short period of time", "Severe Pain in the abdomen, feeling sick, diarrhoea, fever", "Hospital admission over several days, Intravenous fluids, and Pain relief")
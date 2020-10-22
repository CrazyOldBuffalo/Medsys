import weakref

class Condition:
    instances = []
    def __init__(self, name, description, symptoms, treatment):
        self.name = name
        self.description = description
        self.symptoms = symptoms
        self.treatment = treatment

        self.__class__.instances.append(weakref.proxy(self))

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def get_symptoms(self):
        return self.symptoms

    def get_treatment(self):
        return self.treatment

absess = Condition("Absess", "A swollen, pus-filled lump under the surface of the skin caused by a bacterial infection.", ['Pain in affected area','high temperature', 'generally feeling unwell'],"May drain naturally with time. Antibiotics Treatment with incision to drain the pus")
acute_pancreatitis = Condition("Acute Pancreatitis", "Acute pancreatitis is a condition where the pancreas becomes inflamed over a short period of time", ['Severe Pain in the abdomen', 'Feeling or being sick', 'Diarrhoea', 'Fever'], "Hospital admission over several days, Intravenous fluids, and Pain relief")
actinomycosis = Condition("actinomycosis", "Actinomycosis is a rare type of bacterial infection. It can be very serious but can usually be cured with antibiotics.", ['Lumps on your Cheeks or neck','Shorness of breath, chest pain, chouging', 'Diarrhoea or Constipation', 'Pain in the lower abdomen'], "Hospital admission for a treatment of antibiotics introvenously, followed by a course of antibiotic tablets")
bursitis = Condition("Bursitis", "Joints become painful, tender and swollen that can be treated at home", ['Joint is painful', 'Join is tender', 'Affected area is swollen'], "Treatment involves Resting, use of Ice on the joint and elevating the affected limb")
botulism = Condition("Botulism", "Botulism is a very rare but life-threatening condition caused by toxins produced by Clostridium botulinum bacteria.", ['Drooping Eyelids', 'Blurred or Double Vision', 'Difficulty Swallowing', 'Breathing Difficulties'],"Hospital treatment required for injections of antitoxins or antibodies, supporting of bodily functions until recovered.")
bronchitis = Condition("Bronchitis","Bronchitis is an infection of the main airways of the lungs (bronchi), causing them to become irritated and inflamed.",['Hacking cough with greenish or yellow-gray phlegm', 'Sore Throat', 'Headache', 'Aches & pains', 'Tiredness'],"Rest and plenty of fluids should clear the infection over time, medicines may help relieve symptoms")
dead = Condition("Dead", "The Patient is dead mate, they ain't coming back from this one", ['Patient has no pulse', 'Patient is not breathing', 'patient is non-responsive'], "Nothing short of a miracle will bring them back from this one")
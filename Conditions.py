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
cirrhosis = Condition("Cirrhosis","Cirrhosis is scarring (fibrosis) of the liver caused by long-term liver damage. The scar tissue prevents the liver working properly.", ['Feeling very tired', "loss of apetite, weight and muscle mass", "nausea", "spider-like blood vessels (spider angiomas) on your stomach"],"No Cure, but you can manage the condition through your gp via weight loss or stopping drinking")
cyanosis = Condition("Cyanosis", "Cyanosis is where your skin or lips turn blue. It can be a sign of a serious problem.", ['Blue coloring on areas of your skin: lips, tongue, nails, etc'], "Usually a sign of a serious condition, Visit A&E or call 999")
coccydynica = Condition("Coccydynia", "Coccydynia is a pain felt in your coccyx (tailbone). This is the last bone at the bottom of the spine (tailbone). You can get it if you injure or strain your coccyx or the surrounding muscles and ligaments.", ['Dull and Achy pain just above the buttocks', 'Sharp pain occasionally in this area', 'Worse pain when sitting down, moving from sitting to standing', 'Pain causing difficulty sleeping and carrying out activities'], "Self care Measures, like cushions and regular movement or painkillers. Physiotherapy if the condition persists")
dengue = Condition("Dengue", "Dengue is a viral infection spread by mosquitoes. It's widespread in many parts of the world.", ['High Temperature', 'Severe Headaches', 'Joint Pain', 'Widespread red rash'], "Taking Paracetamol, drinking plenty of fluids and getting plenty of rest")
diptheria = Condition("Diptheria","Diphtheria is a highly contagious and potentially fatal infection that can affect the nose and throat, and sometimes the skin. It's rare in the UK, but there's a small risk of catching it while travelling in some parts of the world.",['A thick grey-white coating on the back of the throat', 'Fever', 'Difficulty breathing'],"Antibiotics and medicines that kill the bacteria. Thorough cleaning of affected areas which should clear up after 2-3 weeks")
disentry = Condition("Dysentry","Dysentery is an infection of the intestines that causes diarrhoea containing blood or mucus.", ['{ainful stomach cramps', 'Feeling sick or vomiting', 'High temperature'], "Dysentry usually gets better after 7 days, but it's important to drink fluids regularly and take painkillers to relieve the pain and fever")
dead = Condition("Dead", "The Patient is dead mate, they ain't coming back from this one", ['Patient has no pulse', 'Patient is not breathing', 'patient is non-responsive'], "Nothing short of a miracle will bring them back from this one")
embolism = Condition("Embolism","An embolism is a blocked artery caused by a foreign body, such as a blood clot or an air bubble.",['Stroke', 'Sharp stabbing pain in the chest that comes on gradually', 'Deep Vain Thrombosis symptoms'],"Treated by either surgery to remove the embolism or medication such as warfarin can dissolve embolisms")
ebola_virus = Condition("Ebola Virus", "Ebola virus disease is a serious viral infection that originated in sub-Saharan Africa. No one has caught Ebola from someone else in the UK.", ['Headache', 'High Temperature', 'Muscle Pain', 'Sore Throat','Diarrhoea','Rashes', 'Internal Bleeding'], "No licensed treatment exists although therapies and vaccines are being tested, Ebola is usually fatal")
epiglottitis = Condition("Epigolottitisi", "Epiglottitis is inflammation and swelling of the epiglottis. It's often caused by an infection, but can also sometimes happen as a result of a throat injury.", ['A severe sore thoat', 'Difficulty and pain swallowing', 'Difficulty breathing', 'drooling'], "Airways and airflow are secured in the throat before being treated with a course of antibiotics to clear the infection")
frostbite = Condition("Frostbite", "Frostbite is damage to skin and tissue caused by exposure to freezing temperatures – typically any temperature below -0.55C (31F).", ['Pins and needles in the affected area', 'Cold numb and white skin', 'Hard feeling in affected area', 'Blisters that may swell or become itchy', 'loss of affected limb'], 'Move to a warmer location, replace wet clothing with dry, warm clothing. If conditions become severe attend a specialized unit for further treatment')
fibromyalgia = Condition("Fibromyalgia", "Fibromyalgia, also called fibromyalgia syndrome (FMS), is a long-term condition that causes pain all over the body.", ['Widespread sharp or achy pain', 'Extreme sensitivity to pain or feeling pain from touching something', 'Stiffness in affected area', 'Poor sleep quality'], "Seeing a specialist healthcare professional like a neurologist and pain relief such as paracetamol")

from art import *
from Conditions import Condition
pip install -r requirements.txt

Bursitis = Condition("Bursitis", "Joints become painful, tender and swollen that can be treated at home", "Joint is painful, tender or swollen", "Treatment involves Resting, use of Ice on the joint and elevating the affected limb")
Absess = Condition("Absess", "A swollen, pus-filled lump under the surface of the skin caused by a bacterial infection.", "Pain in affected area, high temperature, generally feeling unwell","May drain naturally with time. Antibiotics Treatment with incision to drain the pus")
Pancreatitis = Condition("Acute Pancreatitis", "Acute pancreatitis is a condition where the pancreas becomes inflamed over a short period of time", "Severe Pain in the abdomen, feeling sick, diarrhoea, fever", "Hospital admission over several days, Intravenous fluids, and Pain relief")

print(Bursitis.get_name())

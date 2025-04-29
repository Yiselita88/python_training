from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from io import StringIO
import pickle
from rdkit.Chem.Draw import rdMolDraw2D


template = Chem.MolFromSmiles('c1nccc2n1ccc2')
print(AllChem.Compute2DCoords(template))

ms = [Chem.MolFromSmiles(smi) for smi in ('OCCc1ccn2cnccc12','C1CC1Oc1cc2ccncn2c1','CNC(=O)c1nccc2cccn12')]
_ = [AllChem.GenerateDepictionMatching2DStructure(m,template) for m in ms]
d = rdMolDraw2D.MolDraw2DCairo(250, 200)
d.DrawMolecule(ms[0])
d.FinishDrawing()
png = d.GetDrawingText()
mol = Chem.MolFromPNGString(png)
Chem.MolToSmiles(mol)

# Save the image
with open("molecule.png", "wb") as f:
    f.write(d.GetDrawingText())

## Substructure search
m = Chem.MolFromSmiles('c1ccccc1O')
patt = Chem.MolFromSmarts('ccO')
print(m.HasSubstructMatch(patt))
print(m.GetSubstructMatch(patt)) # this gives the atom idices in m ordered as patt's atoms
print(m.GetSubstructMatches(patt)) # gives all of the matches

patt = Chem.MolFromSmarts('c[NH1]')
matches = []
with Chem.SDMolSupplier('RDKit-Tutorial/actives_5ht3.sdf') as suppl:
    for mol in suppl:
        if mol.HasSubstructMatch(patt):
            matches.append(mol)
print(len(matches))

# similarly, using list comprehension
with Chem.SDMolSupplier('RDKit-Tutorial/actives_5ht3.sdf') as suppl:
    matches = [x for x in suppl if x.HasSubstructMatch(patt)]
print(len(matches))

# Doing matching by using smiles
m = Chem.MolFromSmiles('C1=CC=CC=C1OC')
print(m.HasSubstructMatch(Chem.MolFromSmiles('CO')))
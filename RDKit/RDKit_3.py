from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from io import StringIO
import pickle
from rdkit.Chem.Draw import rdMolDraw2D

# # generate multiple conformers # #
m = Chem.MolFromSmiles('C1CCC1OC')
m2 = Chem.AddHs(m)
cids = AllChem.EmbedMultipleConfs(m2, numConfs=10)
print(len(cids))

rmslist = []
AllChem.AlignMolConformers(m2, RMSlist=rmslist)
print(len(rmslist))
# print(rmslist)
# if you one to choose another conformer as the specific structure to align, then:
rms = AllChem.GetConformerRMS(m2, 1, 9, prealigned=True)

# # PRESERVING MOLECULES
m = Chem.MolFromSmiles('c1ccncc1')
pkl = pickle.dumps(m)
m2=pickle.loads(pkl)
print(Chem.MolToSmiles(m2))

# to encapsulate data as raw binary data
binStr = m.ToBinary()
m2 = Chem.Mol(binStr)
print(Chem.MolToSmiles(m2))
print(len(binStr))

print(len(binStr) < len(pkl))

# # MORE Drawing
with Chem.SDMolSupplier('cdk2.sdf') as suppl:
  ms = [x for x in suppl if x is not None]
for m in ms: tmp=AllChem.Compute2DCoords(m)
Draw.MolToFile(ms[0],'cdk2_mol1.o.png')    
Draw.MolToFile(ms[1],'cdk2_mol2.o.png') 

img = Draw.MolsToGridImage(ms[:8], molsPerRow=4,subImgSize=(200,200), legends=[x.GetProp("_Name") for x in ms[:8]])
img.save('cdk2_molgrid.o.png')

# Highlight atoms and bonds
smi = 'c1cc(F)ccc1Cl'
mol = Chem.MolFromSmiles(smi)
patt = Chem.MolFromSmarts('ClccccF')
hit_ats = list(mol.GetSubstructMatch(patt))
hit_bonds = []
for bond in patt.GetBonds():
    aid1 = hit_ats[bond.GetBeginAtomIdx()]
    aid2 = hit_ats[bond.GetEndAtomIdx()]
    hit_bonds.append(mol.GetBondBetweenAtoms(aid1, aid2).GetIdx())
# Use MolDraw2DCairo for PNG output
d = rdMolDraw2D.MolDraw2DCairo(500, 500)  
rdMolDraw2D.PrepareAndDrawMolecule(d, mol, highlightAtoms=hit_ats, highlightBonds=hit_bonds)
d.FinishDrawing()
d.WriteDrawingText('highlight_atm_bond.png')  # Save as PNG
print("Image saved as 'highlight_atm_bond.png'")

# drawing while minimizing the clashes
mol = Chem.MolFromSmiles(r'Cl[C@H](F)NC\C=C\C')
d = rdMolDraw2D.MolDraw2DCairo(250, 200) # or MolDraw2DSVG to get SVGs
mol.GetAtomWithIdx(2).SetProp('atomNote', 'foo')
mol.GetBondWithIdx(0).SetProp('bondNote', 'bar')
d.drawOptions().addStereoAnnotation = True
d.drawOptions().addAtomIndices = True
d.DrawMolecule(mol)
d.FinishDrawing()
d.WriteDrawingText('atom_annotation_1.png')   

# display atom labels
smi = 'c1nc(*)ccc1* |$;;;R1;;;;R2$|' 
mol = Chem.MolFromSmiles(smi)
mol.GetAtomWithIdx(3).SetProp("_displayLabel","CO<sub>2</sub>H")
mol.GetAtomWithIdx(3).SetProp("_displayLabelW","HO<sub>2</sub>C")
mol.GetAtomWithIdx(7).SetProp("_displayLabel","CO<sub>2</sub><sup>-</sup>")
mol.GetAtomWithIdx(7).SetProp("_displayLabelW","<sup>-</sup>OOC")
d = rdMolDraw2D.MolDraw2DCairo(250, 250)
rdMolDraw2D.PrepareAndDrawMolecule(d,mol)
d.WriteDrawingText("atom_labels_3.png")   
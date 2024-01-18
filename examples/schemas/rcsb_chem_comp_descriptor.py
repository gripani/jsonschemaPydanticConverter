from pydantic import BaseModel


class RcsbChemCompDescriptor(BaseModel):
	"""
	RcsbChemCompDescriptor class

	Attributes
	----------
	InChI:  `str`
		Standard IUPAC International Chemical Identifier (InChI) descriptor for the chemical component.
		
		   InChI, the IUPAC International Chemical Identifier,
		   by Stephen R Heller, Alan McNaught, Igor Pletnev, Stephen Stein and Dmitrii Tchekhovskoi,
		   Journal of Cheminformatics, 2015, 7:23;
	InChIKey:  `str`
		Standard IUPAC International Chemical Identifier (InChI) descriptor key
		 for the chemical component
		
		 InChI, the IUPAC International Chemical Identifier,
		 by Stephen R Heller, Alan McNaught, Igor Pletnev, Stephen Stein and Dmitrii Tchekhovskoi,
		 Journal of Cheminformatics, 2015, 7:23
	SMILES:  `str`
		Simplified molecular-input line-entry system (SMILES) descriptor for the chemical component.
		
		   Weininger D (February 1988). "SMILES, a chemical language and information system. 1.
		   Introduction to methodology and encoding rules". Journal of Chemical Information and Modeling. 28 (1): 31-6.
		
		   Weininger D, Weininger A, Weininger JL (May 1989).
		   "SMILES. 2. Algorithm for generation of unique SMILES notation",
		   Journal of Chemical Information and Modeling. 29 (2): 97-101.
	SMILES_stereo:  `str`
		Simplified molecular-input line-entry system (SMILES) descriptor for the chemical
		 component including stereochemical features.
		
		 Weininger D (February 1988). "SMILES, a chemical language and information system. 1.
		 Introduction to methodology and encoding rules".
		 Journal of Chemical Information and Modeling. 28 (1): 31-6.
		
		 Weininger D, Weininger A, Weininger JL (May 1989).
		 "SMILES. 2. Algorithm for generation of unique SMILES notation".
		 Journal of Chemical Information and Modeling. 29 (2): 97-101.
	comp_id:  `str`
		The chemical component identifier.

	"""
	InChI: str | None = None
	InChIKey: str | None = None
	SMILES: str | None = None
	SMILES_stereo: str | None = None
	comp_id: str

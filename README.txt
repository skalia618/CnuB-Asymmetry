This repository contains all the code used to perform the computations and generate the figures in arXiv:240X.XXXXX.
If you have any questions, please contact the author: Saarik Kalia (kalias@umn.edu)

The Computations folder contains the data used in Figs. 2 and 3, as well as the code to generate them:
- cnub_origin.py: Generates the data used in Fig. 3 (origin.txt). Computes the asymmetry at the surface of the Earth for various values of kR and delta
- cnub_reflection.py: Generates the data used in Fig. 2 (k30000_delta0.001.txt and k30000_delta0.01.txt). Computes the asymmetry as a function of r for fixed kR and delta.

The Figures folder contains the code to generate each of the figures in the paper:
- contour.py: Generates Fig. 3
- earthfig.py: Generates Fig. 1
- potentials.py: Generates Fig. 4
- profiles.py: Generates Fig. 2
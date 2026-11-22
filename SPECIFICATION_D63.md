# Polybrutus D63 — exact 68-point labelled Euclidean squared-distance metric

**Exclusive direct parent scientific source:** Topbrutus/polybrutus-d62@v0.1.0, actual peeled scientific Git commit \`8263a9583993b9d3d8122f4c68a930e5faf23161\`, DOI 10.5281/zenodo.24432169, original full source ZIP SHA256 \`6d9c82a9fe67c194906f111cae8346247f0995427b8ccf010860b792c0a50b09\`, original D62 certificate SHA256 \`8ddea9ddbc5136d81890f76b2cfa8378eb480b13f54650908f8b40f7bcb36d2e\`.

## Conservative perpendicular norm-one extension

Embed all 67 predecessor norm-one vectors p_i as q_i=(p_i,0). Append one perpendicular unit vector q_68. Every one of C(67,2)=2211 old labelled squared distances remains unchanged; all 67 new squared distances equal 2R². Total C(68,2)=2278 labelled unordered pairs.

Construct a rational Gram G as orthogonal sum of seven original canonical norm-one points (Gram rank 3), a separate centered five-point regular unit simplex (rank 4) with mutual inner products -1/4, and **56** independent mutually orthogonal norm-one axes (rank 56). Hence G=XXᵀ is PSD, unit diagonal, exact rank **3+4+56=63**. Set D_ii=0 and D_ij=2-2G_ij. With H=I-11ᵀ/68, B=-(HDH)/2=HGH is PSD of rank **63**. An inherited canonical antipodal point pair implies the origin lies in the affine hull. Minimum affine Euclidean dimension of this particular metric is therefore 63 (64 coordinate storage).

At R=1, \`k=4d²/R²\` exact histogram: 4:6, 7:2, 8:2247, 9:3, 10:10, 12:6, 13:2, 16:2; total 2278. Exact sum of squared pair distances R=1: **18271/4**.

## Independently stipulated ideal weighted graph

Freely choose scalar unit masses, weighted complete edges w_ij=1/d_ij². New point connects to all 67 old points with weight 1/2. The chosen ideal Laplacian is L63=[[L62+I67/2,-1_67/2],[-1_67ᵀ/2,67/2]]. Its characteristic recurrence is chi68(z)=z(z-34)chi67(z-1/2)/(z-1/2).
Using the inherited seven-point factor f6(z)=chiP7(z)/z:
chi68(z)=z(z-34)^57(z-67/2)^4*f6(z-61/2).
Exact rational nullities yield Laplacian eigenvalue **34 multiplicity 57**, and **67/2 multiplicity 4**. These values are dimensionless model eigenmodes, not physical frequencies.

**Bibliography:** immediate D62 DOI 10.5281/zenodo.24432169; historical D7 DOI 10.5281/zenodo.24407952.

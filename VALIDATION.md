# Polybrutus D63 — proof-first validation and controlled publication

1. Direct scientific parent D62 frozen v0.1.0 peeled Git commit 8263a9583993b9d3d8122f4c68a930e5faf23161, DOI 10.5281/zenodo.24432169, entire original source ZIP SHA256 6d9c82a9fe67c194906f111cae8346247f0995427b8ccf010860b792c0a50b09, certificate SHA256 8ddea9ddbc5136d81890f76b2cfa8378eb480b13f54650908f8b40f7bcb36d2e. Both exact programs validate original ZIP SHA/CRC, original certificate bytes and inherited labels.
2. Exhaust all 68 norm-one points and 2278 labelled exact squared distances; 2211 unchanged old D62 pairs and 67 new squared distances 2R²; Euclidean Gram and centered Gram PSD rank 63.
3. Two independent implementations (SymPy exact Gram vs fractions.Fraction separate pair rules), four adversarial negative controls, exact deterministic certificate. Chosen dimensionless ideal graph eigenvalue 34 mult 57 and 67/2 mult 4.
4. Scientific GitHub initial main CI must pass, then freeze source tag v0.1.0 and require tag CI green; after public Zenodo DOI document on main and require third green CI.
5. Public Zenodo originals: full frozen Git scientific source ZIP, two-page mathematical PDF and exact deterministic certificate JSON; all 3 filenames, sizes and MD5 from public API match SHA256-verified originals. Nine current D63 sixty-three/fifty-sevenfold keywords, structured isDerivedFrom direct D62 DOI, separate D62/D7 textual bibliography.
6. Preserve entire historic original source ZIP nesting unchanged, disclose D47/D46 historical parent text SHA mistake, never claim physical spacetime, measured hertz or new universal theorem.

    python -m pip install sympy==1.14.0
    python src/verify_d63.py
    python tests/independent_d63.py
    python src/check_zenodo_metadata.py

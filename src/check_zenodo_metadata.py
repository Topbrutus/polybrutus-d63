#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d63.json').read_text('utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text('utf8'))
assert c['status']=='PASS' and c['dimension']==m['scientific_dimension']==63
assert c['vertices']==m['norm_one_vertices']==68
assert c['pairs']==m['exact_labelled_squared_pairs']==2278
assert c['affine_rank']==c['centered_gram_rank']==63
assert c['eigenvalue_34_multiplicity']==m['model_eigenvalue_34_multiplicity']==57
assert c['eigenvalue_67_over_2_multiplicity']==m['model_eigenvalue_67_over_2_multiplicity']==4
assert c['parent_tag_commit']=='8263a9583993b9d3d8122f4c68a930e5faf23161'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24432169'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24432169','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension sixty-three' in m['keywords']
assert 'fifty-sevenfold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24432169' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not set(m['keywords']).intersection({'affine Euclidean dimension sixty-two','fifty-sixfold ideal eigenvalue','affine Euclidean dimension sixty-four','fifty-eightfold ideal eigenvalue'})
note=(R/'publication/POLYBRUTUS_63D_NOTE.md').read_text('utf8')
assert all(x in note for x in ('## References','10.5281/zenodo.24432169','10.5281/zenodo.24407952'))
print('D63_CURRENT_9_KEYWORDS_STRUCTURED_DIRECT_D62_PARENT_AND_SEPARATE_D62_D7_REFERENCES_PASS')

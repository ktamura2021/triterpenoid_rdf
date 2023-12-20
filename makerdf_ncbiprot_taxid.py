#!/usr/bin/env python3

file_name = 'v20231129_db02_ncbiprot_taxid.tsv'

fp = open(file_name.replace('.tsv', '.ttl'), 'w')

fp.write('@prefix up_taxonomy: <http://purl.uniprot.org/taxonomy/> .\n')
fp.write('@prefix : <https://raw.githubusercontent.com/ktamura2021/triterpenoid_rdf/main/ontology.ttl#> .\n')

num = 0
with open(file_name, encoding='utf-8') as f:
    for row in f:
        if num == 0:
            num += 1
            continue
        else:
            fields = row.strip().split('\t')
            fp.write('\n')
            fp.write(f'[]\n') # blank node

            fp.write(f'    :ID "{fields[0]}" ;\n')
            fp.write(f'    :up_taxonomy up_taxonomy:{fields[1]} .\n')
            num += 1


fp.close()


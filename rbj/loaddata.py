import django
from biomarkers.models import PlasmidBiomarker
django.setup() 

def fix_date(rbj_date):
    print( rbj_date)
    parts  = rbj_date.split('/')
    
    print(parts)
    return "%20s-%s-%s"  % ( parts[2], parts[1] , parts[0])

headings = ['pmid' ,         
            'transcript' ,   
            'ensembl_id' ,   
            'biotype' ,      
            'direction' ,    
            'disease' ,      
            'fluid' ,        
            'patients' ,     
            'controls' ,     
            'method' ,       
            'primer_f' ,     
            'primer_r' ,
             None ,      
            'date_annotated' ,  
            'notes' ,        
]

file = 'rbj/plasma.biomarkers.csv' 



with open(file, 'r') as f :
#     read_data = f.read()
#     print(read_data) 
    for line in f: 
        columns = line.split(',')
        if not columns[0] or  columns[0] == 'PMID' :
            continue
        
        kwargs = { }
        for index,  field in enumerate( headings) : 
            if not field: 
                continue 
            value = columns[index] 
#             if field == 'date_annotated':
#                 value = fix_date(value)
#             
            kwargs.update({ field : value  })
            
        print( kwargs )
        pb = PlasmidBiomarker.objects.create(**kwargs)
        print(pb.id)
        
f.closed 
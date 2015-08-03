import django
from biomarkers.models import PlasmidBiomarker
django.setup() 

def fix_date(rbj_date):
    print( rbj_date)
    parts  = rbj_date.split('/')
    
    print(parts)
    return "20%s-%s-%s"  % ( parts[2], parts[1] , parts[0])

headings = [
    'pmid',           
    'transcript'  ,
    'ensembl_id' ,
    'biotype' , 
    'direction' ,
    'disease' ,    
    'fluid'  ,     
    'date_annotated' ,
    'notes', 
    'patients' ,   
    'controls' ,   
    'method'  ,    
    'primer_f' ,   
    'primer_r' ,   
]


file = 'rbj/plasma.biomarkers2.csv' 



with open(file, 'r') as f :
#     read_data = f.read()
#     print(read_data) 
    for line in f: 
        print( line)
        columns = line.split('\t')
        print( columns)
        if not columns[0] or  columns[0] == 'PMID' :
            continue
        
        kwargs = { }
        for index,  field in enumerate( headings) : 
            if not field: 
                continue 
            value = columns[index] 
            if field == 'date_annotated':
                value = fix_date(value)
             
            kwargs.update({ field : value  })
            
        print( kwargs )
        pb = PlasmidBiomarker.objects.create(**kwargs)
        print(pb.id)
        
f.closed 
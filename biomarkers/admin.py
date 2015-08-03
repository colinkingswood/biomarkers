from django.contrib import admin
from biomarkers.models import PlasmidBiomarker

# Register your models here.

@admin.register(PlasmidBiomarker)
class PlasmidBiomarkerAdmin(admin.ModelAdmin):
    list_display  =  [ 'pmid' , 'transcript' , 'ensembl_id' , 'biotype', 'direction', 'disease', 'fluid','date_annotated'  ]
    search_fields =  [ 'pmid' , 'transcript' , 'ensembl_id' , 'biotype', 'direction', 'disease', 'fluid', 'patients', 'controls', 'method' , 'primer_f', 'primer_r' , 'date_annotated' , 'notes' ]
    list_filter   =  [ 'biotype', 'direction', 'disease', 'fluid', 'method' , 'notes' ]
    readonly_fields = ['pmid' , 'transcript' , 'ensembl_id' , 'biotype', 'direction', 'disease', 'fluid', 'patients', 'controls', 'method' , 'primer_f', 'primer_r' , 'date_annotated' , 'notes' ]
#    exclude = ['patients', 'controls', 'method' , 'primer_f', 'primer_r' , 'notes' ]

    
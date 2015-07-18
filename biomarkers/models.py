# TODO
# Check lengths of transcript names
#
from django.db import models

class PlasmidBiomarker(models.Model):
    """
    initial version from Rory bj's spreadsheet, just using char and text fields to begin with
    """
    pmid        = models.IntegerField(verbose_name='PMID')
    transcript  = models.CharField(max_length=200)    
    ensembl_id  = models.CharField(max_length=100)    
    biotype     = models.CharField(max_length=100)
    direction   = models.CharField(max_length=100)
    disease     = models.CharField(max_length=200)
    fluid       = models.CharField(max_length=100)   
    patients    = models.CharField(max_length=200, null=True, blank=True)
    controls    = models.CharField(max_length=100, null=True, blank=True)
    method      = models.CharField(max_length=100, null=True, blank=True)
    primer_f    = models.CharField(max_length=200, null=True, blank=True)
    primer_r    = models.CharField(max_length=200, null=True, blank=True)
    date_annotated = models.DateField()
    notes       = models.TextField(null=True, blank=True )                                         

    def __str__(self):
        return "%s %s" % (self.transcript , self.ensembl_id)
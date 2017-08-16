# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:14:30 2017

@author: oreilly
"""

from warnings import warn
from .zoteroWrap import ZoteroWrap

class ParamSample:
    
    def __init__(self, searcher, libraryId=None, libraryType=None, apiKey=None):
        
        self.searcher = searcher
        self.sampleDF = searcher.search()
        if not libraryId is None and not libraryType is None and not apiKey is None:
            self.zotWrap = ZoteroWrap()
            self.zotWrap.loadCachedDB(libraryId, libraryType, apiKey)
        else:
            self.zotWrap = None
            
        self.ageUnit = "day"
        
        # For the conversion of age categories (e.g., adult) to 
        # numerical values. "min" species the lower bound of the interval.
        # For example, rats are adult from 5 months up to their dead (around 2-3.5 years)
        # setting this parametes to min, 5 months will be attributed as numerical
        # value for the age "adult" in rats.
        self.ageTypeValue = "min"
            
    def setZoteroLib(self, libraryId, libraryType, apiKey):
        self.zotWrap = ZoteroWrap()
        self.zotWrap.loadCachedDB(libraryId, libraryType, apiKey)    

        
        
    def preprocess(self, steps):
        for step in steps:
            getattr(self, "preprocess_" + step)()
    
    
    
    def preprocess_species(self):
        speciesId = []
        species   = []
        for noRow, row in self.sampleDF.iterrows():
            tags =row["Species"]
            if len(tags) > 1 :
                warn("The annotation with the parameter ID " + row["Parameter instance ID"] + 
                     " is associated with more than one species (" + 
                     str([tag.name for tag in tags]) 
                     + "). The species cannot be automatically attributed unambiguously. " +
                     "Skipping this record.")
                del row
                continue
                
            speciesId.append(tags[0].id)
            species.append(tags[0].name)
            
        self.sampleDF["SpeciesId"] = speciesId
        self.sampleDF["Species"]   = species


    def preprocess_age(self):    
        if not "SpeciesId" in self.sampleDF:
            self.preprocess_species()
            
        ageCategoryIds = []
        ageCategories  = []
        numericalAges  = []
        for noRow, row in self.sampleDF.iterrows():
            tags = row["AgeCategories"]
            if len(tags) > 1 :
                warn("The annotation with the parameter ID " + row["Parameter instance ID"] + 
                     " is associated with more than one age categories (" + 
                     str([tag.name for tag in tags]) 
                     + "). The age cannot be automatically attributed unambiguously. " +
                     "Skipping this record.")
                del row
                continue  
                
            if len(tags) == 0:
                ageCategoryIds.append(None)
                ageCategories.append(None)
                numericalAges.append(None)
                continue
            
            ageCategoryIds.append(tags[0].id)
            ageCategories.append(tags[0].name)
            age = AgeResolver.resolve_fromIDs(row["SpeciesId"], tags[0].id, unit=self.ageUnit, 
                                              typeValue=self.ageTypeValue) 
            numericalAges.append(age)

        self.sampleDF["AgeCategoryId"] = ageCategoryIds
        self.sampleDF["AgeCategory"]   = ageCategories
        self.sampleDF["age"]           = numericalAges

    
    def preprocess_ref(self):    
        if self.zotWrap is None:
            raise ValueError("To add references to the sample, you need first to set " +
                             "the Zotero library by calling LitSample.setZoteroLib()")

        self.sampleDF["ref"] = [self.zotWrap.getInTextCitationFromID(annot.pubId) 
                                           for annot in self.sampleDF["obj_annotation"]]
    
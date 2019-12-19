#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 19:14:29 2019

@author: Mark Barbet
"""

import cantera as ct
import soln2cti as w
import numpy as np
import pandas as pd

#Establish class for description of possible termolecular reaction


class TMRP():
    def __init__(self,base_cti='',fixed_T=False, reversible=True,
                 temperature=None,default_col_freq=5*10**(-10)*6.022*10**23,
                 beta=0.01):
        self.base_cti=base_cti
        self.fixed_T=fixed_T
        self.reversible=reversible
        self.temperature=None
        self.Zc=default_col_freq
        self.beta=beta
        self.run_screening()
        
        
    #Function to perform the screening procedure
    def run_screening(self):
        #Function to create gas
        self.build_gas_object()
        #Function to find pairs
        self.find_pairs()
        
        
        #Build list of termolecular reaction objects
        self.termoleculars=self.build_termolecular_reactions()
        
    def find_pairs(self):     
        
        
        #Function to find R1's
        self.ids_r1=self.find_R1()
        
        #Function to find R2's
        self.ids_r2=self.find_R2()
        
        #Build reaction pairs
        self.id_pairs=self.get_pairs()
        
        
        
        
    def reaction_type_filter(self,types=[]):
        
        '''Function to take a list of reaction types in cantera and return
           indices for all instances of these reactions in a mechanism'''
        if types==[]:
            try:
                return np.arange(len(self.gas.reactions()))
            except:
                print('Ensure that TMRP.gas is provided with a non-zero list of reactions')
        else:
            reaction_list=[]
            for i in range(len(self.gas.reactions())):
                if any(text in self.gas.reaction(i).__class__.__name__ for text in types):
                    reaction_list.append(i)
            return np.array(reaction_lists)
        
    def find_R1(self):
        #search through gas and return all reactions that are Falloff, or Three-Body reactions
        rxn_types=['three_body_reaction','falloff_reaction']
        initial_indices=self.reaction_type_filter(types=rxn_types)
        forward_indices=[]
        reverse_indices=[]
        for i, el in enumerate(initial_indices):
            if len(self.gas.reaction(el).products)-1==len(self.gas.reaction(el).reactants):
                forward_indices.append(el)
            elif len(self.gas.reaction(el).reactants)-1==len(self.gas.reaction(el).products):
                reverse_indices.append(el)
                
        return (forward_indices,reverse_indices)
        
    def find_R2(self):
        
        
    def build_gas_object(self):
        if self.base_cti != '':
            self.gas=ct.Solution(base_cti)
        
        '''If using a fixed temp to calculate R2, set the gas temperature to the 
           desired fixed temp for easy calculation later'''
        if self.fixed_T:
            self.gas.TP=self.temperature,ct.one_atm
            
    def build_termolecular_reactions(self):
        
            
    def get_pairs(self):
        
    def build_new_solution(self):
        
        
    def write_termolecular_cti(self,default_name_convention=True,outputname=''):
        
    def build_termolecular_dataframe(self):
        '''Output a pandas dataframe with the termolecular reaction and the 
           reactions used to construct it'''


class termolecular_reaction():
    
    def __init__(self,reaction1=None,reaction2=None,id_list=[],reversed_tuple=(False,False)):
        self.reaction1=reaction1
        self.reaction2=reaction2
        self.id_list=id_list
        self.reversed_r1=reversed_tuple[0]
        self.reversed_r2=reversed_tuple[1]
        
        
    def rate_estimate(self):
        
        
    def build_rxn_string(self):
        
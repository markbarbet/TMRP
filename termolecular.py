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
        
        #Function to find pairs
        
    def find_pairs(self):     
        #Function to create gas
        self.build_gas_object()
        
        #Function to find R1's
        self.ids_r1=self.find_R1()
        
        #Function to find R2's
        self.ids_r2=self.find_R2()
        
        #Build reaction pairs
        self.id_pairs=self.get_pairs()
        
        #Build list of termolecular reaction objects
        self.termoleculars=self.build_termolecular_reactions()
        
        
        
        
    def find_R1(self):
        
        
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
        
        
    def write_cti(self,default_name_convention=True,outputname=''):


class termolecular_reaction():
    
    def __init__(self,reaction1=None,reaction2=None,id_list=[]):
        self.reaction1=reaction1
        self.reaction2=reaction2
        self.id_list=id_list
        
        
    def rate
        
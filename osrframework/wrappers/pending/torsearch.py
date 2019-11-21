# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

import argparse
import json
import re
import sys
import urllib2

import osrframework.utils.browser as browser
from osrframework.utils.platforms import Platform

class Torsearch(Platform):
    """ 
        A <Platform> object for Torsearch.
    """
    def __init__(self):
        '''
            Constructor...
        '''
        self.platformName = "Torsearch"        
        self.tags = ["tor", "search"]
        
        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}        
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = False
        self.isValidMode["searchfy"] = True      
        
        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}        
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        #self.url["usufy"] = "http://anyurl.com/user/" + "<usufy>"
        self.url["searchfy"] = "https://torsearch.es/en/search?q=" + "<searchfy>"       

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}        
        #self.needsCredentials["phonefy"] = False
        #self.needsCredentials["usufy"] = False
        self.needsCredentials["searchfy"] = False
        
        ###################
        # Valid queries #
        ###################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any query.
        #self.validQuery["phonefy"] = ".*"
        #self.validQuery["usufy"] = ".*"
        self.validQuery["searchfy"] = ".+"
        
        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        #self.notFoundText["usufy"] = []   
        self.notFoundText["searchfy"] = []        
        
        #########################
        # Fields to be searched #
        #########################
        self.fieldsRegExp = {}
        
        # Definition of regular expressions to be searched in phonefy mode
        #self.fieldsRegExp["phonefy"] = {}
        # Example of fields:
        #self.fieldsRegExp["phonefy"]["i3visio.location"] = ""
        
        # Definition of regular expressions to be searched in usufy mode
        #self.fieldsRegExp["usufy"] = {}
        # Example of fields:
        #self.fieldsRegExp["usufy"]["i3visio.location"] = ""
        
        # Definition of regular expressions to be searched in searchfy mode
        self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        self.delimiters = {}
        # These two fields are REQUIRED to grab the results
        self.searchfyDelimiterStart = "<div class='page-listing col-sm-12'>"
        self.searchfyDelimiterEnd = "<div class='row'>"        
        # These rest of fields to extract
        self.fieldsRegExp["searchfy"]["i3visio.uri"] = {"start": "<span class='path'>", "end": "</span>"}       
        self.fieldsRegExp["searchfy"]["i3visio.text"] = {"start": "<div class='description'>", "end": "</div>"}
        self.fieldsRegExp["searchfy"]["i3visio.title"] = {"start": "<div class='title'>", "end": "</a>"}
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}

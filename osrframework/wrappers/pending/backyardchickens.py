# !/usr/bin/python
# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2016-2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
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

class Backyardchickens(Platform):
    """ 
    A <Platform> object for Backyardchickens.
    """
    def __init__(self):
        """ 
        Constructor... 
        """
        self.platformName = "Backyardchickens"
        self.tags = ["image"]

        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}        
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = True
        self.isValidMode["searchfy"] = False      
        
        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}        
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        self.url["usufy"] = "http://www.backyardchickens.com/members/" + "<usufy>"       
        #self.url["searchfy"] = "http://anyurl.com/search/" + "<searchfy>"       

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}        
        #self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = False
        #self.needsCredentials["searchfy"] = False 
        
        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any query.
        #self.validQuery["phonefy"] = ".*"
        self.validQuery["usufy"] = "[^@, \.]+"
        #self.validQuery["searchfy"] = ".*"
        
        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = ["<h1>There Seems to be a Problem</h1>"]  
        #self.notFoundText["searchfy"] = []        
        
        #########################
        # Fields to be searched #
        #########################
        self.fieldsRegExp = {}
        
        # Definition of regular expressions to be searched in phonefy mode
        #self.fieldsRegExp["phonefy"] = {}
        # Example of fields:
        #self.fieldsRegExp["phonefy"]["i3visio.location"] = ""
        
        # Definition of regular expressions to be searched in usufy mode
        self.fieldsRegExp["usufy"] = {}
        # Example of fields:
        self.fieldsRegExp["usufy"]["i3visio.fullname"] = {"start": 'class="indexable profile-header">', "end": '</h1>'}
        self.fieldsRegExp["usufy"]["i3visio.location"] = {"start": '<td class="label indexable">Location:<br><br></td>\n\t\t\t<td class="data indexable">', "end": '<br><br></td>'}
        self.fieldsRegExp["usufy"]["@real_name"] = {"start": '<td class="label indexable">Real Name:<br><br></td>\n\t\t\t<td class="data indexable">', "end": '<br><br></td>'}
        self.fieldsRegExp["usufy"]["i3visio.i3visio.uri_image_profile"] = {"start": 'alt="Avatars" src="', "end": '"'}
        self.fieldsRegExp["usufy"]["@created_at"] = {"start": '<td class="label indexable">Join Date:<br><br></td>\n\t\t\t<td class="data indexable">', "end": '<br><br></td>'}
        self.fieldsRegExp["usufy"]["@last_active"] = {"start": '<td class="label indexable">Last Online:<br><br></td>\n\t\t\t<td class="data indexable">', "end": '<br><br></td>'}
        
        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""        
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}


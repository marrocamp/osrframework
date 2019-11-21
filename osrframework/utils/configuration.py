# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of OSRFramework. You can redistribute it and/or modify
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

try:
    import ConfigParser
except:
    # For Python 3 compatibility
    import configparser
import os
import sys
import osrframework.utils.errors as errors


def changePermissionsRecursively(path, uid, gid):
    """
    Function to recursively change the user id and group id.

    It sets 700 permissions.
    """
    os.chown(path, uid, gid)
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        if os.path.isfile(itempath):
            # Setting owner
            try:
                os.chown(itempath, uid, gid)
            except Exception as e:
                # If this crashes it may be because we are running the
                # application in Windows systems, where os.chown does NOT work.
                pass
            # Setting permissions
            os.chmod(itempath, 600)
        elif os.path.isdir(itempath):
            # Setting owner
            try:
                os.chown(itempath, uid, gid)
            except Exception as e:
                # If this crashes it may be because we are running the
                # application in Windows systems, where os.chown does NOT work.
                pass
            # Setting permissions
            os.chmod(itempath, 6600)
            # Recursive function to iterate the files
            changePermissionsRecursively(itempath, uid, gid)


def getConfigPath(configFileName = None):
    """
    Auxiliar function to get the configuration paths depending on the system

    Args:
    -----
        configFileName: TODO.

    Returns:
    --------
        A dictionary with the following keys: appPath, appPathDefaults,
            appPathTransforms, appPathPlugins, appPathPatterns, appPathPatterns.
    """
    paths = {}
    applicationPath = "./"

    # Returning the path of the configuration folder
    if sys.platform == 'win32':
        applicationPath = os.path.expanduser(os.path.join('~\\', 'OSRFramework'))
    else:
        applicationPath = os.path.expanduser(os.path.join('~/', '.config', 'OSRFramework'))

    # Defining additional folders
    paths = {
        "appPath": applicationPath,
        "appPathData": os.path.join(applicationPath, "data"),
        "appPathDefaults": os.path.join(applicationPath, "default"),
        "appPathPlugins": os.path.join(applicationPath, "plugins"),
        "appPathWrappers": os.path.join(applicationPath, "plugins", "wrappers"),
        "appPathPatterns": os.path.join(applicationPath, "plugins", "patterns"),
    }

    # Creating them if they don't exist
    for path in paths.keys():
        if not os.path.exists(paths[path]):
            os.makedirs(paths[path])

    return paths


def returnListOfConfigurationValues(util):
    """
    Method that recovers the configuration information about each program

    TODO: Grab the default file from the package data instead of storing it in
    the main folder.

    Args:
    -----
        util: Any of the utils that are contained in the framework: domainfy,
            entify, mailfy, phonefy, searchfy, usufy.

    Returns:
    --------
        A dictionary containing the default configuration.
    """

    VALUES = {}

    # If a api_keys.cfg has not been found, creating it by copying from default
    configPath = os.path.join(getConfigPath()["appPath"], "general.cfg")

    # Checking if the configuration file exists
    if not os.path.exists(configPath):
        # Copy the data from the default folder
        defaultConfigPath = os.path.join(getConfigPath()["appPathDefaults"], "general.cfg")

        try:
            # Recovering default file
            with open(defaultConfigPath) as iF:
                cont = iF.read()
                # Moving its contents as the default values
                with open(configPath, "w") as oF:
                    oF.write(cont)
        except Exception as e:
            raise errors.DefaultConfigurationFileNotFoundError(configPath, defaultConfigPath);

    # Reading the configuration file
    config = ConfigParser.ConfigParser()
    config.read(configPath)

    LISTS = ["tlds", "domains", "platforms", "extension", "exclude_platforms", "exclude_domains"]

    # Iterating through all the sections, which contain the platforms
    for section in config.sections():
        incomplete = False
        if section.lower() == util.lower():
            # Iterating through parameters
            for (param, value) in config.items(section):
                if value == '':
                    # Manually setting an empty value
                    if param in LISTS:
                        value = []
                    else:
                        value = ""
                # Splitting the parameters to create the arrays when needed
                elif param in LISTS:
                    value = value.split(' ')
                # Converting threads to int
                elif param == "threads":
                    try:
                        value = int(value)
                    except Exception as err:
                        raise errors.ConfigurationParameterNotValidError(configPath, section, param, value)
                elif param == "debug":
                    try:
                        if int(value) == 0:
                            value = False
                        else:
                            value = True
                    except Exception as err:
                        print("Something happened when processing this debug option. Resetting to default.")
                        # Copy the data from the default folder
                        defaultConfigPath = os.path.join(getConfigPath()["appPathDefaults"], "general.cfg")

                        try:
                            # Recovering default file
                            with open(defaultConfigPath) as iF:
                                cont = iF.read()
                                # Moving its contents as the default values
                                with open(configPath, "w") as oF:
                                    oF.write(cont)
                        except Exception as e:
                            raise errors.DefaultConfigurationFileNotFoundError(configPath, defaultConfigPath);

                        #raise errors.ConfigurationParameterNotValidError(configPath, section, param, value)
                VALUES[param] = value
            break

    return VALUES

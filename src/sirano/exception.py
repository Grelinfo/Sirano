# -*- coding: utf-8 -*-
#
# This file is a part of Sirano.
#
# Copyright (C) 2015  HES-SO // HEIA-FR
# Copyright (C) 2015  Loic Gremaud <loic.gremaud@grelinfo.ch>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


class SiranoException(Exception):
    """
    Root Exception for the Sirano application
    """

    def __init__(self, message):
        """
        Initialize the exception with a message

        :param message: The message
        :type message: str
        """
        self.message = message

    def __str__(self):
        return "sirano: " + self.message

class ScapyPacketException(SiranoException):
    """
    Exception for the file plugin
    """
    def __init__(self, message = ''):
        super(ScapyPacketException, self).__init__(message)

class DropException(ScapyPacketException):
    """
    Exception when the entire element must be dropped
    """
    def __str__(self):
        return "sirano:file:drop: " + self.message


class ImplicitDropException(DropException):
    """
    Exception when the DropException is not explicitly requested by the user
    """
    def __str__(self):
        return "sirano:file:drop:implicit: " + self.message


class ExplicitDropException(DropException):
    """
    Exception when the DropException is explicitly requested by the user
    """

    def __str__(self):
        return "sirano:file:drop:explicit: " + self.message


class ActionException(SiranoException):
    """
    Exception for Action plugins
    """

    def __str__(self):
        return "sirano:action: " + self.message

class DataException(SiranoException):
    """
    Exception for Data plugins
    """

    def __init__(self, data, message):
        super(DataException, self).__init__(message)
        self.data = data

    def __str__(self):
        return "sirano:data:{}:".format(self.data.name) + self.message

class FormatException(ActionException):
    """
    Exception when the format of a value is invalid
    """

    def __init__(self, action, value):
        """Initialize the exception for a specified action and value

         :param action: The name of the action that generate this exception
         :type action: Action
         :param value: The value concerned by this exception
         :type value: str
        """
        self.action = action
        self.value = value

    def __str__(self):
        return "sirano:action:format: Unsupported format: action = '{}', value = '{}'".format(self.action.name, self.value)


class PassException(ActionException):
    """
    Exception when the anonymize function must be skipped
    """
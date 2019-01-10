# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2018 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtPositioning, except for defaults which are replaced by "...".
"""

# Module PySide2.QtPositioning
import shiboken2 as Shiboken
from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtPositioning


class QGeoAddress(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoAddress): ...
    def __copy__(self): ...
    def city(self) -> str: ...
    def clear(self): ...
    def country(self) -> str: ...
    def countryCode(self) -> str: ...
    def county(self) -> str: ...
    def district(self) -> str: ...
    def isEmpty(self) -> bool: ...
    def isTextGenerated(self) -> bool: ...
    def postalCode(self) -> str: ...
    def setCity(self, city:str): ...
    def setCountry(self, country:str): ...
    def setCountryCode(self, countryCode:str): ...
    def setCounty(self, county:str): ...
    def setDistrict(self, district:str): ...
    def setPostalCode(self, postalCode:str): ...
    def setState(self, state:str): ...
    def setStreet(self, street:str): ...
    def setText(self, text:str): ...
    def state(self) -> str: ...
    def street(self) -> str: ...
    def text(self) -> str: ...


class QGeoAreaMonitorInfo(Shiboken.Object):

    @typing.overload
    def __init__(self, name:str=...): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoAreaMonitorInfo): ...
    def __copy__(self): ...
    def __lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def area(self) -> PySide2.QtPositioning.QGeoShape: ...
    def expiration(self) -> PySide2.QtCore.QDateTime: ...
    def identifier(self) -> str: ...
    def isPersistent(self) -> bool: ...
    def isValid(self) -> bool: ...
    def name(self) -> str: ...
    def notificationParameters(self) -> dict: ...
    def setArea(self, newShape:PySide2.QtPositioning.QGeoShape): ...
    def setExpiration(self, expiry:PySide2.QtCore.QDateTime): ...
    def setName(self, name:str): ...
    def setNotificationParameters(self, parameters:dict): ...
    def setPersistent(self, isPersistent:bool): ...


class QGeoAreaMonitorSource(PySide2.QtCore.QObject):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    @typing.overload
    def activeMonitors(self) -> PySide2.QtPositioning.QGeoAreaMonitorInfo: ...
    @typing.overload
    def activeMonitors(self, lookupArea:PySide2.QtPositioning.QGeoShape) -> PySide2.QtPositioning.QGeoAreaMonitorInfo: ...
    @staticmethod
    def availableSources() -> typing.List: ...
    @staticmethod
    def createDefaultSource(parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoAreaMonitorSource: ...
    @staticmethod
    def createSource(sourceName:str, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoAreaMonitorSource: ...
    def error(self) -> PySide2.QtPositioning.QGeoAreaMonitorSource.Error: ...
    def positionInfoSource(self) -> PySide2.QtPositioning.QGeoPositionInfoSource: ...
    def requestUpdate(self, monitor:PySide2.QtPositioning.QGeoAreaMonitorInfo, signal:str) -> bool: ...
    def setPositionInfoSource(self, source:PySide2.QtPositioning.QGeoPositionInfoSource): ...
    def sourceName(self) -> str: ...
    def startMonitoring(self, monitor:PySide2.QtPositioning.QGeoAreaMonitorInfo) -> bool: ...
    def stopMonitoring(self, monitor:PySide2.QtPositioning.QGeoAreaMonitorInfo) -> bool: ...
    def supportedAreaMonitorFeatures(self) -> PySide2.QtPositioning.QGeoAreaMonitorSource.AreaMonitorFeatures: ...


class QGeoCircle(PySide2.QtPositioning.QGeoShape):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, center:PySide2.QtPositioning.QGeoCoordinate, radius:float=...): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoCircle): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoShape): ...
    def __copy__(self): ...
    def center(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def extendCircle(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def radius(self) -> float: ...
    def setCenter(self, center:PySide2.QtPositioning.QGeoCoordinate): ...
    def setRadius(self, radius:float): ...
    def toString(self) -> str: ...
    def translate(self, degreesLatitude:float, degreesLongitude:float): ...
    def translated(self, degreesLatitude:float, degreesLongitude:float) -> PySide2.QtPositioning.QGeoCircle: ...


class QGeoCoordinate(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, latitude:float, longitude:float): ...
    @typing.overload
    def __init__(self, latitude:float, longitude:float, altitude:float): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoCoordinate): ...
    def __copy__(self): ...
    def __lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def altitude(self) -> float: ...
    def atDistanceAndAzimuth(self, distance:float, azimuth:float, distanceUp:float=...) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def azimuthTo(self, other:PySide2.QtPositioning.QGeoCoordinate) -> float: ...
    def distanceTo(self, other:PySide2.QtPositioning.QGeoCoordinate) -> float: ...
    def isValid(self) -> bool: ...
    def latitude(self) -> float: ...
    def longitude(self) -> float: ...
    def setAltitude(self, altitude:float): ...
    def setLatitude(self, latitude:float): ...
    def setLongitude(self, longitude:float): ...
    def toString(self, format:PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat=...) -> str: ...
    def type(self) -> PySide2.QtPositioning.QGeoCoordinate.CoordinateType: ...


class QGeoLocation(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoLocation): ...
    def __copy__(self): ...
    def address(self) -> PySide2.QtPositioning.QGeoAddress: ...
    def boundingBox(self) -> PySide2.QtPositioning.QGeoRectangle: ...
    def coordinate(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def isEmpty(self) -> bool: ...
    def setAddress(self, address:PySide2.QtPositioning.QGeoAddress): ...
    def setBoundingBox(self, box:PySide2.QtPositioning.QGeoRectangle): ...
    def setCoordinate(self, position:PySide2.QtPositioning.QGeoCoordinate): ...


class QGeoPath(PySide2.QtPositioning.QGeoShape):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoPath): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoShape): ...
    @typing.overload
    def __init__(self, path:list, width:float=...): ...
    def __copy__(self): ...
    def addCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def clearPath(self): ...
    def containsCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate) -> bool: ...
    def coordinateAt(self, index:int) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def insertCoordinate(self, index:int, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def length(self, indexFrom:int=..., indexTo:int=...) -> float: ...
    def path(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    @typing.overload
    def removeCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    @typing.overload
    def removeCoordinate(self, index:int): ...
    def replaceCoordinate(self, index:int, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def setPath(self, path:list): ...
    def setVariantPath(self, path:list): ...
    def setWidth(self, width:float): ...
    def size(self) -> int: ...
    def toString(self) -> str: ...
    def translate(self, degreesLatitude:float, degreesLongitude:float): ...
    def translated(self, degreesLatitude:float, degreesLongitude:float) -> PySide2.QtPositioning.QGeoPath: ...
    def variantPath(self) -> typing.Any: ...
    def width(self) -> float: ...


class QGeoPolygon(PySide2.QtPositioning.QGeoShape):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoPolygon): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoShape): ...
    @typing.overload
    def __init__(self, path:list): ...
    def __copy__(self): ...
    def addCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    @typing.overload
    def addHole(self, holePath:list): ...
    @typing.overload
    def addHole(self, holePath:typing.Any): ...
    def containsCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate) -> bool: ...
    def coordinateAt(self, index:int) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def hole(self, index:int) -> typing.Any: ...
    def holePath(self, index:int) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def holesCount(self) -> int: ...
    def insertCoordinate(self, index:int, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def length(self, indexFrom:int=..., indexTo:int=...) -> float: ...
    def path(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def perimeter(self) -> typing.Any: ...
    @typing.overload
    def removeCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    @typing.overload
    def removeCoordinate(self, index:int): ...
    def removeHole(self, index:int): ...
    def replaceCoordinate(self, index:int, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def setPath(self, path:list): ...
    def setPerimeter(self, path:list): ...
    def size(self) -> int: ...
    def toString(self) -> str: ...
    def translate(self, degreesLatitude:float, degreesLongitude:float): ...
    def translated(self, degreesLatitude:float, degreesLongitude:float) -> PySide2.QtPositioning.QGeoPolygon: ...


class QGeoPositionInfo(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, coordinate:PySide2.QtPositioning.QGeoCoordinate, updateTime:PySide2.QtCore.QDateTime): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoPositionInfo): ...
    def __copy__(self): ...
    def __lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def attribute(self, attribute:PySide2.QtPositioning.QGeoPositionInfo.Attribute) -> float: ...
    def coordinate(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def hasAttribute(self, attribute:PySide2.QtPositioning.QGeoPositionInfo.Attribute) -> bool: ...
    def isValid(self) -> bool: ...
    def removeAttribute(self, attribute:PySide2.QtPositioning.QGeoPositionInfo.Attribute): ...
    def setAttribute(self, attribute:PySide2.QtPositioning.QGeoPositionInfo.Attribute, value:float): ...
    def setCoordinate(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def setTimestamp(self, timestamp:PySide2.QtCore.QDateTime): ...
    def timestamp(self) -> PySide2.QtCore.QDateTime: ...


class QGeoPositionInfoSource(PySide2.QtCore.QObject):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    @staticmethod
    def availableSources() -> typing.List: ...
    @staticmethod
    def createDefaultSource(parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource: ...
    @staticmethod
    def createSource(sourceName:str, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource: ...
    def error(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.Error: ...
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly:bool=...) -> PySide2.QtPositioning.QGeoPositionInfo: ...
    def minimumUpdateInterval(self) -> int: ...
    def preferredPositioningMethods(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods: ...
    def requestUpdate(self, timeout:int=...): ...
    def setPreferredPositioningMethods(self, methods:PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods): ...
    def setUpdateInterval(self, msec:int): ...
    def sourceName(self) -> str: ...
    def startUpdates(self): ...
    def stopUpdates(self): ...
    def supportedPositioningMethods(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods: ...
    def updateInterval(self) -> int: ...


class QGeoPositionInfoSourceFactory(Shiboken.Object):

    def __init__(self): ...
    def areaMonitor(self, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoAreaMonitorSource: ...
    def positionInfoSource(self, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource: ...
    def satelliteInfoSource(self, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource: ...


class QGeoRectangle(PySide2.QtPositioning.QGeoShape):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, center:PySide2.QtPositioning.QGeoCoordinate, degreesWidth:float, degreesHeight:float): ...
    @typing.overload
    def __init__(self, coordinates:list): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoRectangle): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoShape): ...
    @typing.overload
    def __init__(self, topLeft:PySide2.QtPositioning.QGeoCoordinate, bottomRight:PySide2.QtPositioning.QGeoCoordinate): ...
    def __copy__(self): ...
    def __ior__(self, rectangle:PySide2.QtPositioning.QGeoRectangle) -> PySide2.QtPositioning.QGeoRectangle: ...
    def __or__(self, rectangle:PySide2.QtPositioning.QGeoRectangle) -> PySide2.QtPositioning.QGeoRectangle: ...
    def bottomLeft(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def bottomRight(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def center(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    @typing.overload
    def contains(self, coordinate:PySide2.QtPositioning.QGeoCoordinate) -> bool: ...
    @typing.overload
    def contains(self, rectangle:PySide2.QtPositioning.QGeoRectangle) -> bool: ...
    def extendRectangle(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def height(self) -> float: ...
    def intersects(self, rectangle:PySide2.QtPositioning.QGeoRectangle) -> bool: ...
    def setBottomLeft(self, bottomLeft:PySide2.QtPositioning.QGeoCoordinate): ...
    def setBottomRight(self, bottomRight:PySide2.QtPositioning.QGeoCoordinate): ...
    def setCenter(self, center:PySide2.QtPositioning.QGeoCoordinate): ...
    def setHeight(self, degreesHeight:float): ...
    def setTopLeft(self, topLeft:PySide2.QtPositioning.QGeoCoordinate): ...
    def setTopRight(self, topRight:PySide2.QtPositioning.QGeoCoordinate): ...
    def setWidth(self, degreesWidth:float): ...
    def toString(self) -> str: ...
    def topLeft(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def topRight(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def translate(self, degreesLatitude:float, degreesLongitude:float): ...
    def translated(self, degreesLatitude:float, degreesLongitude:float) -> PySide2.QtPositioning.QGeoRectangle: ...
    def united(self, rectangle:PySide2.QtPositioning.QGeoRectangle) -> PySide2.QtPositioning.QGeoRectangle: ...
    def width(self) -> float: ...


class QGeoSatelliteInfo(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoSatelliteInfo): ...
    def __copy__(self): ...
    def __lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def attribute(self, attribute:PySide2.QtPositioning.QGeoSatelliteInfo.Attribute) -> float: ...
    def hasAttribute(self, attribute:PySide2.QtPositioning.QGeoSatelliteInfo.Attribute) -> bool: ...
    def removeAttribute(self, attribute:PySide2.QtPositioning.QGeoSatelliteInfo.Attribute): ...
    def satelliteIdentifier(self) -> int: ...
    def satelliteSystem(self) -> PySide2.QtPositioning.QGeoSatelliteInfo.SatelliteSystem: ...
    def setAttribute(self, attribute:PySide2.QtPositioning.QGeoSatelliteInfo.Attribute, value:float): ...
    def setSatelliteIdentifier(self, satId:int): ...
    def setSatelliteSystem(self, system:PySide2.QtPositioning.QGeoSatelliteInfo.SatelliteSystem): ...
    def setSignalStrength(self, signalStrength:int): ...
    def signalStrength(self) -> int: ...


class QGeoSatelliteInfoSource(PySide2.QtCore.QObject):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    @staticmethod
    def availableSources() -> typing.List: ...
    @staticmethod
    def createDefaultSource(parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource: ...
    @staticmethod
    def createSource(sourceName:str, parent:PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource: ...
    def error(self) -> PySide2.QtPositioning.QGeoSatelliteInfoSource.Error: ...
    def minimumUpdateInterval(self) -> int: ...
    def requestUpdate(self, timeout:int=...): ...
    def setUpdateInterval(self, msec:int): ...
    def sourceName(self) -> str: ...
    def startUpdates(self): ...
    def stopUpdates(self): ...
    def updateInterval(self) -> int: ...


class QGeoShape(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtPositioning.QGeoShape): ...
    def __copy__(self): ...
    def __lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def boundingGeoRectangle(self) -> PySide2.QtPositioning.QGeoRectangle: ...
    def center(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def contains(self, coordinate:PySide2.QtPositioning.QGeoCoordinate) -> bool: ...
    def extendShape(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def isEmpty(self) -> bool: ...
    def isValid(self) -> bool: ...
    def toString(self) -> str: ...
    def type(self) -> PySide2.QtPositioning.QGeoShape.ShapeType: ...


class QNmeaPositionInfoSource(PySide2.QtPositioning.QGeoPositionInfoSource):

    def __init__(self, updateMode:PySide2.QtPositioning.QNmeaPositionInfoSource.UpdateMode, parent:PySide2.QtCore.QObject=...): ...
    def device(self) -> PySide2.QtCore.QIODevice: ...
    def error(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.Error: ...
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly:bool=...) -> PySide2.QtPositioning.QGeoPositionInfo: ...
    def minimumUpdateInterval(self) -> int: ...
    def parsePosInfoFromNmeaData(self, data:str, size:int, posInfo:PySide2.QtPositioning.QGeoPositionInfo, hasFix:bool) -> bool: ...
    def requestUpdate(self, timeout:int=...): ...
    def setDevice(self, source:PySide2.QtCore.QIODevice): ...
    def setUpdateInterval(self, msec:int): ...
    def setUserEquivalentRangeError(self, uere:float): ...
    def startUpdates(self): ...
    def stopUpdates(self): ...
    def supportedPositioningMethods(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods: ...
    def updateMode(self) -> PySide2.QtPositioning.QNmeaPositionInfoSource.UpdateMode: ...
    def userEquivalentRangeError(self) -> float: ...

# eof

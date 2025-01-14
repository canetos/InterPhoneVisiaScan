#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import logging

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *


from src_backend.ui_set_data_event import manager_data


class Backend(QObject):
    """Classe Backend pour gérer les interactions entre QML et Python."""

    def __init__(self,view,db_backend, LIST_HABITANT_BACKEND):
        super().__init__()
        self.view = view
        self.stored_values = []

        logging.debug(f"Liste reçu depuis Firebase : {[LIST_HABITANT_BACKEND]}")  
        logging.debug(db_backend)

    # Signal pour indiquer qu'un événement s'est produit
    eventOccurred = pyqtSignal(str)
    
    @pyqtSlot(str)
    def handleButtonPress(self, eventData):
        """
        Méthode pour gérer l'événement transmis par les boutons dans QML.

        Args:
            eventData (str): Les données de l'événement.
        """
        try:
            logging.debug(f"Événement reçu : {eventData}")
            self.eventOccurred.emit(eventData)
            manager_data(self, eventData)
            
        except Exception as e:
            # Handle the exception here, you can log it or take other actions as needed
            logging.error(f"An exception occurred: {str(e)}")
            # You can also emit a signal to notify QML of the exception if necessary
            self.eventOccurred.emit(f"An exception occurred: {str(e)}")
        
    @pyqtSlot(str, result=str)
    def receive_textonPYTHON(self, label_name):
        """
        Méthode pour recevoir du texte depuis QML.

        Args:
            label_name (str): Le nom du QLabel dans QML.

        Returns:
            str: Le texte reçu.
        """
        o = self.view.rootObjects()[0].findChild(QObject, label_name)
        if o is not None:
            text = o.property("text")
            logging.debug(f"Texte reçu depuis QML : {text}")
            return text
        return ""

    @pyqtSlot(str, str)
    def transmit_textonQML(self, text, label_name):
        """
        Méthode pour transmettre du texte depuis Python et l'afficher dans un QLabel QML.

        Args:
            text (str): Le texte à afficher.
            label_name (str): Le nom du QLabel dans QML.
        """
        o = self.view.rootObjects()[0].findChild(QObject, label_name)
        if o is not None:
            o.setProperty("text", text)
            logging.debug(f"Texte transmis vers QML : {text}")
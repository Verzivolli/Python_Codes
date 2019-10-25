# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:07:04 2019

@author: Ani Verzivolli
"""

import os
import comtypes.client

path=r"path to my folder containing file.docx"

word=comtypes.client.CreateObject("Word.Application")
docx=word.Documents.Open(r"F:\Dropbox\TENDERA\Dokumente Standarde Tenderi\Dokumentet Stadarde të procedurës së hapur shërbime\Automation approach\Testing Notebooks\testing_.docm", ReadOnly=0)
docx=word.Application.Run("InsertTextAtEndOfDocument")
word.Documents(1).Close(SaveChanges=True)
word.Application.Quit()
wd=0
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GIMP Python plug-in Engraver
# Copyright 2015 Karl Hofmeyr <karlhofmeyr@yahoo.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

#
# Note: gimpfu.py is the most up-to-date list of UI items.
# desaturate
# posterise to 4 colours
# colour select using hue?check?
# bucketfill with the appropriate pattern for the level of darkness
# loop through all 4 colours

from gimpfu import *
import sys
# import time
# import pickle
# import os, glob

# import gettext
# gettext.install("gimp20-python", gimp.locale_directory, unicode=True)
    
# def gimp_log(text):
#    pdb.gimp_message(text)
#    return


def engrave_bluepatts(inImage, inLayer) :
    # First say hello
    # pdb.gimp_message ( "hello Karl" )
    # sys.print "hello"
    # pdb.gimp_message ( "after hello Karl ")
    gimp.context_push()
    inImage.undo_group_start()
   
    #pdb.gimp_message("trying to string stuff")
    #i = 4
    #pattstring = "Eng109A"
    #together = pattstring + str (i)
    #pdb.gimp_message(together)
    
    # Set the master posteriselevels number
    posteriselevels = 7
    
    # pdb.gimp_message ( "after hello Karl 5 ")
    # gimp.context_push() and gimp.context.pop() right at the end
    
    # pdb.gimp_message ( "hello Karl 10" )	
    # pdb.gimp_image_undo_group_start( image )
    numlay , listlay = pdb.gimp_image_get_layers (inImage)
    # pdb.gimp_message ( numlay )
    # pdb.gimp_message ( listlay )
    wasnotset = False
    if (numlay <=1 ): 
        pdb.gimp_message ( "no layer - therefore create it" )
        engravelayer2 = gimp.Layer(inImage, "engravelayer2", inLayer.width, inLayer.height, RGB_IMAGE, 100, NORMAL_MODE)
        inImage.add_layer ( engravelayer2, 1 )
        #borderLayer = inLayer.copy( True )
        #borderLayer22 = inLayer.copy( True )
        #inImage.add_layer( borderLayer, -1 )
        #inImage.lower_layer( borderLayer )
        pdb.gimp_image_set_active_layer (inImage, engravelayer2)
        #inImage.add_layer ( borderLayer22, 1 )
        wasnotset = True
    
    # gimp.progress_init( _("Add engraving") ) 
    # secondImage = pdb.gimp_image_duplicate ( inImage )
    # interimimage = gimp.Image( width, height, INDEXED )
    # interimimage = pdb.gimp_image_convert_indexed (secondImage, NO_DITHER, MAKE_PALETTE, 16, False, True, '')
    
    pdb.gimp_selection_none( inImage )
    height=inLayer.height
    width=inLayer.width
    engravelayer = gimp.Layer(inImage, "Engravelayer", width, height, RGB_IMAGE, 100, NORMAL_MODE)
    engravelayer = inLayer.copy()
    engravelayer.mode = NORMAL_MODE
    engravelayer.name = "engraved layer"
    inImage.add_layer(engravelayer,0)
        
    # is_indexed2 = pdb.gimp_drawable_is_indexed ( engravelayer )
    # pdb.gimp_message ( is_indexed2 )
    # pdb.gimp_message ( "interim success" )
    
    # dont use pdb.gimp_image_set_active_layer (inImage, inLayer)
    pdb.gimp_image_set_active_layer (inImage, engravelayer)
    
    pdb.gimp_selection_none( inImage )
    pdb.gimp_desaturate ( engravelayer )
    # pdb.gimp_message ( "desaturating...1" )
    
    #pdb.gimp_desaturate ( parentLayer )
    # pdb.gimp_message ( "posterising..." )
    #  dont use pdb.gimp_posterize(inLayer, posteriselevels)
    pdb.gimp_posterize(engravelayer, posteriselevels)
    # pdb.gimp_message ( "posterising...1" )
    
    parentlayer = gimp.Layer(inImage, "parentlayer", width, height, RGB_IMAGE, 100, NORMAL_MODE)
    parentlayer.mode = NORMAL_MODE
    parentlayer.name = "parent layer"
    inImage.add_layer(parentlayer,0)
    pdb.gimp_edit_fill( parentlayer, BACKGROUND_FILL )
    #parentlayer = pdb.gimp_image_get_active_layer (inImage)
    
    #acolour = pdb.gimp_image_pick_color (inImage, parentlayer, 10, 15, False, True, 5 )
    #pdb.gimp_message ( acolour )
    #bcolour = ((100,0,0))
    #pdb.gimp_context_set_foreground((0,0,0))
    #pdb.gimp_context_set_background(acolour)
    #pdb.gimp_image_select_rectangle( inImage, CHANNEL_OP_REPLACE, 10, 20, 150, 200)
    #pdb.gimp_edit_fill(parentlayer, FOREGROUND_FILL)
    
    # colourvalue = 255/(posteriselevels-1)
    colourvalue = 255/(posteriselevels-1)
    pdb.gimp_context_set_sample_criterion (SELECT_CRITERION_COMPOSITE)
    pdb.gimp_context_set_sample_threshold(0.05)
    
    # do black and white at the end
    # acolour = ((5,5,5))
    # pdb.gimp_context_set_pattern ("Eng111A13")
    # pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, acolour)
    # dont use pdb.gimp_edit_fill(parentlayer, FOREGROUND_FILL)
    # pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    # pdb.gimp_selection_none( inImage )
    
    pdb.gimp_message(colourvalue)
    pdb.gimp_message ((colourvalue*1))
    calccolourval= int(colourvalue*1)
    gcolour = ((calccolourval, calccolourval, calccolourval))
    pdb.gimp_context_set_sample_criterion (SELECT_CRITERION_COMPOSITE)
    pdb.gimp_context_set_sample_threshold(0.05)
    pdb.gimp_context_set_pattern ("Big Blue")
    pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, gcolour)
    # dont use pdb.gimp_edit_fill(parentlayer, FOREGROUND_FILL)
    pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    pdb.gimp_selection_none( inImage )
    
    calccolourval= int(colourvalue*2)
    pdb.gimp_message ((colourvalue*2))
    fcolor = ((calccolourval, calccolourval, calccolourval))
    # dont use pdb.gimp_context_set_pattern ("Engrave 106 multi A")
    pdb.gimp_context_set_pattern ("Electric Blue")
    pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, fcolor)
    pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    pdb.gimp_selection_none( inImage )
    
    calccolourval= int(colourvalue*3)
    pdb.gimp_message ((colourvalue*3))
    fcolor = ((calccolourval, calccolourval, calccolourval))
    # dont use fcolor = ((colourvalue*3,colourvalue*3,colourvalue*3))
    # dont use pdb.gimp_context_set_pattern ("Engrave 106 multi A")
    pdb.gimp_context_set_pattern ("Blue Web")
    pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, fcolor)
    pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    pdb.gimp_selection_none( inImage )
    
    calccolourval= int(colourvalue*4)
    pdb.gimp_message ((colourvalue*4))
    # dont use dcolor = ((170,170,170))
    dcolor = ((calccolourval, calccolourval, calccolourval))
    # dont use pdb.gimp_context_set_pattern ("KHEngrave2")
    pdb.gimp_context_set_pattern ("Blue Grid")
    pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, dcolor)
    pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    pdb.gimp_selection_none( inImage )
    
    calccolourval= int(colourvalue*5)
    pdb.gimp_message ((colourvalue*5))
    # dont use dcolor = ((170,170,170))
    dcolor = ((calccolourval, calccolourval, calccolourval))
    # dont use pdb.gimp_context_set_pattern ("KHEngrave2")
    pdb.gimp_context_set_pattern ("Blue Squares")
    pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, dcolor)
    pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    pdb.gimp_selection_none( inImage )
    
    calccolourval= int(colourvalue*6)
    pdb.gimp_message ((colourvalue*6))
    # dont use dcolor = ((170,170,170))
    dcolor = ((calccolourval, calccolourval, calccolourval))
    # dont use pdb.gimp_context_set_pattern ("KHEngrave2")
    pdb.gimp_context_set_pattern ("Ice")
    pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, dcolor)
    pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    pdb.gimp_selection_none( inImage )
    
    # calccolourval= int(colourvalue*7)
    # pdb.gimp_message ((colourvalue*7))
    # dont use dcolor = ((170,170,170))
    # dcolor = ((calccolourval, calccolourval, calccolourval))
    # dont use pdb.gimp_context_set_pattern ("KHEngrave2")
    # pdb.gimp_context_set_pattern ("Engrave 102 K")
    # pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, dcolor)
    # pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    # pdb.gimp_selection_none( inImage )
    
    #calccolourval= int(colourvalue*8)
    #pdb.gimp_message ((colourvalue*8))
    # dont use dcolor = ((170,170,170))
    #dcolor = ((calccolourval, calccolourval, calccolourval))
    # dont use pdb.gimp_context_set_pattern ("KHEngrave2")
    #pdb.gimp_context_set_pattern ("Eng111A01")
    #pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, dcolor)
    #pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    #pdb.gimp_selection_none( inImage )
    
    # calccolourval= int(colourvalue*9)
    # pdb.gimp_message ((colourvalue*9))
    # dont use dcolor = ((170,170,170))
    # dcolor = ((calccolourval, calccolourval, calccolourval))
    # dont use  pdb.gimp_context_set_pattern ("KHEngrave2")
    # pdb.gimp_context_set_pattern ("Eng111A04")
    # pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, dcolor)
    # pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    # pdb.gimp_selection_none( inImage )
    
    # calccolourval= int(colourvalue*10)
    # pdb.gimp_message ((colourvalue*10))
    #dcolor = ((170,170,170))
    # dcolor = ((calccolourval, calccolourval, calccolourval))
    #pdb.gimp_context_set_pattern ("KHEngrave2")
    # pdb.gimp_context_set_pattern ("Eng111A03")
    # pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, dcolor)
    # pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    # pdb.gimp_selection_none( inImage )
    
    # calccolourval= int(colourvalue*11)
    # pdb.gimp_message ((colourvalue*11))
    # dont use dcolor = ((170,170,170))
    # dcolor = ((calccolourval, calccolourval, calccolourval))
    # dont use pdb.gimp_context_set_pattern ("KHEngrave2")
    # pdb.gimp_context_set_pattern ("Eng111A02")
    # pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, dcolor)
    # pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    # pdb.gimp_selection_none( inImage )
    
    #calccolourval= (colourvalue*7)
    #dcolor = ((170,170,170))
    #dcolor = ((calccolourval, calccolourval, calccolourval))
    # pdb.gimp_context_set_pattern ("KHEngrave2")
    #pdb.gimp_context_set_pattern ("Eng107A0pt2")
    #pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, parentlayer, dcolor)
    #pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    #pdb.gimp_selection_none( inImage )
    
    ecolor = ((255,255,255))
    # dont use pdb.gimp_context_set_pattern ("Engrave 007 A")
    pdb.gimp_context_set_pattern ("Ice")
    pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, ecolor)
    pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    pdb.gimp_selection_none( inImage )
    
    ecolor = ((2,2,2))
    # dont use pdb.gimp_context_set_pattern ("Engrave 007 A")
    pdb.gimp_context_set_pattern ("Big Blue")
    pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, engravelayer, ecolor)
    pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    pdb.gimp_selection_none( inImage )
    
    #ecolor = ((250,0,0))
    #pdb.gimp_context_set_pattern ("C Patt 1")
    #pdb.gimp_image_select_color (inImage, CHANNEL_OP_REPLACE, parentlayer, ecolor)
    #pdb.gimp_edit_bucket_fill (parentlayer, PATTERN_BUCKET_FILL, NORMAL_MODE, 100.0, 0.05, False, 10.0, 15.0)
    #pdb.gimp_selection_none( inImage )
    
    # pdb.gimp_message ( "inserted" )
    # gimp.progress_update( 0.25 )
    #  
    # pdb.gimp_message ( "desaturating...")
    # dont use pdb.gimp_desaturate ( inLayer )
    # pdb.gimp_selection_none( inImage )
    # pdb.gimp_desaturate ( engravelayer )
    # pdb.gimp_message ( "desaturating...1" )
    
    #pdb.gimp_desaturate ( parentLayer )
    # pdb.gimp_message ( "posterising..." )
    #  dont use pdb.gimp_posterize(inLayer, posteriselevels)
    # pdb.gimp_posterize(engravelayer, posteriselevels)
    # pdb.gimp_message ( "posterising...1" )
    # ccolour = pdb.gimp_image_pick_color (inImage, engravelayer, 10, 15, False, True, 5 )
    # pdb.gimp_message ( acolour )
    
    # test1 = pdb.gimp_item_is_layer ( inLayer )
    # pdb.gimp_message ( test1 )
    # is_indexed = pdb.gimp_drawable_is_indexed ( engravelayer )
    # pdb.gimp_message ( is_indexed )
    
    # parentlayer = pdb.gimp_image_get_active_layer (inImage)
    # bcolour = pdb.gimp_image_pick_color (inImage, engravelayer, 10.0, 15.5, False, True, 5 )
    # pdb.gimp_message ( bcolour )
    # stepcolors = (255 / posterislevels)
	
    # for i in xrange (0,255, setcolors)
    # pdb.gimp_image_select_color (inImage, CHANNEL_OP_ADD, drawable, (0, 0, 0) )
    # sys.ext(1)
       
    # inImage.flatten()
    # nextImage = pdb.gimp_image_convert_indexed (secondImage, 0, 0, 16, False, True, '')
    # is_indexed3 = pdb.gimp_drawable_is_indexed ( engravelayer )
    # pdb.gimp_message ( is_indexed3 )
    
    # not needed - pdb.gimp_levels(timg.layers[0], 0, 10, 230, 1.0, 0, 255)
    
    # (bytesCount, colorMap) = pdb.gimp_image_get_colormap(interimimage)
	# pdb.gimp_message(bytesCount)
	# pdb.gimp_message(colorMap)
    # pdb.gimp_message("Consider saving as PNG now!")
    
    # bcolour = pdb.gimp_image_pick_color (inImage, inLayer, 10.0, 15.0, False, False, 5 )
    # pdb.gimp_message ( "col="+bcolour )
    # colour1 = (125,125,125,1)
    # colour2 = (0,1,0,1)
    # colour3 = (120,123,123,1)
	# pdb.gimp_message ( "crashed by now")
    
	# Make a new image. Size 10x10 for now -- we'll resize later.
    # img = gimp.Image(1, 1, RGB)
        
    # Save the current foreground color:
    # pdb.gimp_context_push()
    
    # Set the text color
    # gimp.set_foreground(color)
    
    # Create a new text layer (-1 for the layer means create a new layer)
    # layer = pdb.gimp_text_fontname(img, None, 0, 0, initstr, 10,
    #                               True, size, PIXELS, font)
    
    # Resize the image to the size of the layer
    # img.resize(layer.width, layer.height, 0, 0)
    
    # Background layer.
    # Can't add this first because we don't know the size of the text layer.
    # background = gimp.Layer(img, "Background", layer.width, layer.height,
    #                        RGB_IMAGE, 100, NORMAL_MODE)
    # background.fill(BACKGROUND_FILL)
    # img.add_layer(background, 1)
      
    # Create a new image window
    # gimp.Display(img)
    # Show the new image window
    gimp.displays_flush()
    inImage.undo_group_end()
    # Restore the old foreground color:
    pdb.gimp_context_pop()
    return

register(
    "engrave-bluepatts",
    "Engrave an image with a pattern",
    "Create an engraved image. Longer description",
    "Karl Hofmeyr",
    "Karl Hofmeyr",
    "2015",
    "Engrave using blue patterns",
    "*",
    [
        (PF_IMAGE, "inImage", "Input image", None),
        (PF_DRAWABLE, "inLayer", "Input drawable", None)
    ],
    [],
    engrave_bluepatts,
    menu="<Image>/Filters/Languages/Python-Fu/")

main()

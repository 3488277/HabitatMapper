# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterField,
                       QgsProcessingParameterVectorDestination)
from qgis import processing


    
class habitatBoundaryArea(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    ANIMAL_SPECIES = 'ANIMAL_SPECIES'
    HABITAT_ID= 'HABITAT_ID'
    SPECIES_DISTANCE = 'SPECIES_DISTANCE'
    WATERBODY = 'WATERBODY'
    PERENNIAL = 'PERENNIAL'

    
    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return habitatBoundaryArea()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'habitatBoundaryArea'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Habitat Boundary Area')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Example scripts')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'examplescripts'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("This tool returns the habitat boundary area for a chosen species poetntial flight or travel distance and summarises all waterway habitat within")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                self.HABITAT_ID,
                self.tr('Species ID or Name'),
                ' ',
                self.INPUT
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                self.SPECIES_DISTANCE,
                self.tr('Species Distance'),
                ' ',
                self.INPUT
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.WATERBODY,
                self.tr('Waterbody Area'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )


        self.addParameter(
            QgsProcessingParameterVectorDestination(
                'MINBOUNDARY_OUTPUT',
                self.tr('Minimum Boundary Output'),
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                'MINBOUNDARY_OUTPUT',
                self.tr('Minimum Boundary Output'),
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                'MINBOUNDARY_OUTPUT',
                self.tr('Minimum Boundary Output'),
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                'MINBOUNDARY_OUTPUT',
                self.tr('Minimum Boundary Output'),
            )
        )    
        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        #self.addParameter(
        #    QgsProcessingParameterFeatureSink(
        #        self.OUTPUT,
        ##        self.tr('Output layer')
        #    )
        #)

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        input = self.parameterAsSource(
            parameters,
            self.INPUT,
            context)
        habitat_ID = self.parameterAsFields(
            parameters,
            self.HABITAT_ID,
            context)
        species_distance = self.parameterAsDouble(
            parameters, 
            self.SPECIES_DISTANCE,
            context)
        waterbody = self.parameterAsSource(
            parameters,
            self.WATERBODY,
            context)
             
        for feature in migAreaMeasure:
            speciesMig = processing.run("native:buffer",
            {'INPUT': parameters['input'],    
            'DISTANCE' : parameters['species_distance'],
            'SEGMENTS': 10,
            'JOIN_STYLE': 2,
            'MITER_LIMIT': 10,
            'OUTPUT': parameters['BUFFER_OUTPUT']
            })
            split = processing.run("native:buffer",
            {'INPUT': parameters['BUFFER_OUTPUT'],
            'FIELD': parameters['habitat_id'],
            'FILE_TYPE': 1,
            'OUTPUT': parameters['SPLIT_OUTPUT']
            })
            extract = processing.run("native:extractbylocation", 
            {'INPUT': parameters['SPLIT_OUTPUT'], 
            'PREDICATE': 0, 
            'INTERSECT':  parameters['WATERBODY'],
            'OUTPUT': parameters['EXTRACT_OUTPUT']    
            })
            convexHull = processing.run("qgis:minimumboundinggeometry",
            { 'INPUT': parameters['EXTRACT_OUTPUT'],
            'TYPE':3,
            'OUTPUT': parameters['MINBOUNDARY_OUTPUT'],
            })
        return {'OUTPUT': append['OUTPUT']}
    #overlapLayer = processing.run("native:calculatevectoroverlaps",
    #{   'INPUT': convexHull['OUTPUT'],
    #    'LAYERS': extract['OUTPUT'], 
    #    'OUTPUT': folderPath + xfiles +'overlapAnalysis4.shp',
    #})
        
    
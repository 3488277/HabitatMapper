# -*- coding: utf-8 -*-



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
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return habitatBoundaryArea()

    def name(self):
        return 'habitatBoundaryArea'

    def displayName(self):
        return self.tr('Habitat Boundary Area')

    def group(self):
        return self.tr('Example scripts')

    def groupId(self):
        return 'examplescripts'

    def shortHelpString(self):
        return self.tr("This tool returns the habitat boundary area for a chosen species poetntial flight or travel distance and summarises all waterway habitat within")

    def initAlgorithm(self, config=None):
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
    def processAlgorithm(self, parameters, context, feedback):
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
            split = processing.run("native:splitvectorlayer",
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
        return {'OUTPUT': append['OUTPUT']}
    #overlapLayer = processing.run("native:calculatevectoroverlaps",
    #{   'INPUT': convexHull['OUTPUT'],
    #    'LAYERS': extract['OUTPUT'], 
    #    'OUTPUT': folderPath + xfiles +'overlapAnalysis4.shp',
    #})
        
    
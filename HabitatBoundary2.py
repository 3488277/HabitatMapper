# -*- coding: utf-8 -*-



from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterField)
from qgis import processing


class habitatBoundaryArea(QgsProcessingAlgorithm):

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
       
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return habitatBoundaryArea()

    def name(self):
        
        return 'habitatBoundaryArea'

    def displayName(self):
        
        return self.tr('This tool returns the habitat boundary area for a chosen species poetntial flight or travel distance and summarises all waterway habitat within')

    def group(self):
        
        return self.tr('Example scripts')

    def groupId(self):
        
        return 'examplescripts'

    def shortHelpString(self):
        
        return self.tr("Example algorithm short description")

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
                self.INPUT,
                self.tr('Animal Species'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                self.INPUT,
                self.tr('Species ID or Name'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Waterbody Areas'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureField(
                self.INPUT,
                self.tr('Perennial'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Habitat Determinants'),
                [QgsProcessing.TypeVectorAnyGeometry]
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
        

        
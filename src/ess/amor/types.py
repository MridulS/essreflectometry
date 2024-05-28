from typing import Any, NewType

import sciline
import scipp as sc

from ..reflectometry.types import Run

WavelengthResolution = NewType('WavelengthResolution', sc.Variable)
AngularResolution = NewType('AngularResolution', sc.Variable)
SampleSizeResolution = NewType('SampleSizeResolution', sc.Variable)


class ChopperFrequency(sciline.Scope[Run, sc.Variable], sc.Variable):
    """Frequency of the choppers used in the run."""


class ChopperPhase(sciline.Scope[Run, sc.Variable], sc.Variable):
    """Phase of the choppers in the run."""


class Chopper1Position(sciline.Scope[Run, sc.Variable], sc.Variable):
    """Position of the first chopper relative the source of the beam."""


class Chopper2Position(sciline.Scope[Run, sc.Variable], sc.Variable):
    """Position of the second chopper relative to the source of the beam."""


class RawChopper(sciline.Scope[Run, sc.DataGroup], sc.DataGroup):
    """Chopper data loaded from nexus file"""


class ThetaBins(sciline.Scope[Run, sc.Variable], sc.Variable):
    '''Binning in theta that takes into consideration that some
    detector pixels have the same theta value'''


WavelengthThetaFigure = NewType('WavelengthThetaFigure', Any)
WavelengthZIndexFigure = NewType('WavelengthZIndexFigure', Any)
QThetaFigure = NewType('QThetaFigure', Any)
ReflectivityDiagnosticsView = NewType('ReflectivityDiagnosticsView', Any)

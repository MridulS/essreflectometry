# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2023 Scipp contributors (https://github.com/scipp)
import scipp as sc

from ..types import IncidentBeam, Run, SamplePosition
from .types import Chopper1Position, Chopper2Position


def incident_beam(
    source_chopper_1_position: Chopper1Position[Run],
    source_chopper_2_position: Chopper2Position[Run],
    sample_position: SamplePosition[Run],
) -> IncidentBeam[Run]:
    """
    Compute the incident beam vector from the source chopper position vector,
    instead of the source_position vector.
    """
    chopper_midpoint = (
        source_chopper_1_position + source_chopper_2_position
    ) * sc.scalar(0.5)
    return sample_position - chopper_midpoint


providers = (incident_beam,)

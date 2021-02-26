import pytest
from tetra_plug import test

from . import play, spec, tone


@pytest.mark.parametrize("spec", spec.tone)
def test_tone(spec):
    test.test_tone(spec=spec, tone=tone)


@pytest.mark.parametrize("spec", spec.play)
def test_play(spec):
    test.test_play(spec=spec, play=play)

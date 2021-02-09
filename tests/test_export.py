import os
import tempfile
import pytest

from app.query.nucleotide import get_family_export


def test_family_export():
    result = get_family_export('Coronaviridae', **{'scoreMin': 100})
    assert (len(result) == 2839)

    result = get_family_export('Coronaviridae', **{'scoreMin': 50})
    assert (len(result) == 3637)

    result = get_family_export('Coronaviridae', **{'scoreMin': 100, 'scoreMax': 50})
    assert (len(result) == 0)

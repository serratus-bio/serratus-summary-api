import os
import tempfile
import pytest

import application
from model.nucleotide import nsra, nfamily, nsequence
from query.nucleotide import (
    get_sra_properties,
    get_sra_families,
    get_sra_sequences,
    get_family_pagination,
    get_genbank_pagination
)
from route.nucleotide import get_sra, sra_cache


def test_sra():
    result = get_sra_properties('ERR2756788')
    assert result == nsra(sra_id='ERR2756788', read_length=150, genome='cov3ma', version='200818', date='200817-21:05')

    result = get_sra_families('ERR2756788')
    assert len(result) == 12
    assert result[0] == nfamily(sra_id='ERR2756788', family_name='AMR', coverage_bins='mooaoooUmmmmmooooaaoawwwm', score=100, percent_identity=97, depth=214.8, n_reads=1382, n_global_reads=301, length=1000)

    result = get_sra_sequences('ERR2756788')
    assert len(result) == 349
    assert result[0] == nsequence(sra_id='ERR2756788', family_name='Coronaviridae', genbank_id='HQ728485.1', coverage_bins=':a..__uu__a_________o____', score=28, percent_identity=85, depth=0.7, n_reads=119, n_global_reads=98, length=13015, genbank_name='Miniopterus bat coronavirus/Kenya/KY33/2006 polyprotein (ORF1ab) gene, partial cds; and spike protein (S), ORF3 protein (ORF3), envelope protein (E), membrane protein (M), nucleocapsid protein (N), and hypothetical protein ORFx (ORFx) genes, complete cds')


def test_sra_cache():
    orig = get_sra('ERR2756788')
    cache = sra_cache.get('ERR2756788')
    assert orig.data == cache.data


def test_family():
    pagination = get_family_pagination('Coronaviridae', scoreMin=100)
    assert len(pagination.items) == 20
    assert pagination.items[0] == nfamily(sra_id='SRR9966511', family_name='Coronaviridae', coverage_bins='mUmmUmmmUmUmmUmmUUmmUmUmm', score=100, percent_identity=99, depth=14.9, n_reads=2923, n_global_reads=401, length=30000)
    assert pagination.total == 2839

    pagination = get_family_pagination('Coronaviridae', scoreMin=100, perPage=3)
    assert len(pagination.items) == 3


def test_genbank():
    pagination = get_genbank_pagination('EU769558.1', scoreMax=50)
    assert len(pagination.items) == 20
    assert pagination.items[0] == nsequence(sra_id='ERR2756788', family_name='Coronaviridae', genbank_id='EU769558.1', coverage_bins='aUAUmmm__________________', score=45, percent_identity=85, depth=9.6, n_reads=1694, n_global_reads=399, length=14335, genbank_name='Bat coronavirus Trinidad/1CO7BA/2007 nonstructural protein 1b` gene, partial cds')
    assert pagination.total == 365

    pagination = get_genbank_pagination('EU769558.1', scoreMax=50, perPage=3)
    assert len(pagination.items) == 3

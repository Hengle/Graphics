from ruamel.yaml.scalarstring import DoubleQuotedScalarString as dss
from ..utils.namer import abv_job_id_all_smoke_tests


def get_job_definition(editor, test_platforms):

    dependencies = []
    for test_platform in test_platforms:
        dependencies.append({
            'path': f'.yamato/upm-ci-abv.yml#smoke_test_{test_platform["name"]}_{editor["version"]}',
            'rerun': 'on-new-revision'
        })

    job = {
        'name': f'All Smoke Tests - {editor["version"]}',
        'agent': {
            'type':'Unity::VM',
            'image':'cds-ops/ubuntu-18.04-agent:stable',
            'flavor':'b1.small'
        }, 
        'commands': ['dir'],
        'dependencies': dependencies
    }

    if editor['version'] == 'CUSTOM-REVISION':
        job['variables'] = {'CUSTOM_REVISION':'custom_revision_not_set'}
    
    return job


class ABV_AllSmokeTestsJob():
    
    def __init__(self, editor, test_platforms):
        self.job_id = abv_job_id_all_smoke_tests(editor["version"])
        self.yml = get_job_definition(editor, test_platforms)
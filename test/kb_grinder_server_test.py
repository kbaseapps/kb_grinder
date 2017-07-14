# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from kb_grinder.kb_grinderImpl import kb_grinder
from kb_grinder.kb_grinderServer import MethodContext
from kb_grinder.authclient import KBaseAuth as _KBaseAuth


class kb_grinderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('kb_grinder'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'kb_grinder',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = kb_grinder(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_kb_grinder_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_kb_grinder_KButil_Build_InSilico_Metagenomes_with_Grinder_test_01(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods

        # input_data
        reference_prok_genomes_WS = 'ReferenceDataManager'  # PROD and CI
        #reference_prok_genomes_WS = '19217'  # PROD
        #reference_prok_genomes_WS = '15792'  # CI

        genome_ref_1 = reference_prok_genomes_WS+'/GCF_001566335.1/1'  # E. coli K-12 MG1655
        genome_ref_2 = reference_prok_genomes_WS+'/GCF_000021385.1/1'  # D. vulgaris str. 'Miyazaki F'
        genome_ref_3 = reference_prok_genomes_WS+'/GCF_900129775.1/1'  # Halobaculum gomorrense (16 contigs)
        
        parameters = { 'workspace': self.getWsName(),
                       'desc': 'test',
                       'input_refs': [genome_ref_1, genome_ref_2, genome_ref_3],
                       'output_name': 'foo.PERS',
                       'num_reads_per_lib': '1000000',
                       'population_percs': "Genome\tS1\tS2\tS3\tetc.\nG1\t10.0%\t60.0%\t35.0%\nG2\t30.0%\t30.0%\t30.0%\nG3\t60.0%\t10.0%\t35.0%\n",
                       'read_len_mean': "150",
                       'read_len_stddev': "15.0",
                       'pairs_flag': "1",
                       'mate_orientation': "FR",
                       'insert_len_mean': "450",
                       'insert_len_stddev': "45",
                       'mutation_dist': "poly4 3e-3 3.3e-8",
                       'mutation_ratio': "80 20",
                       'qual_good': "30",
                       'qual_bad': "10",
                       'len_bias_flag': "1",
                       'random_seed': "1"
                     }

        ret = self.getImpl().KButil_Build_InSilico_Metagenomes_with_Grinder(self.getContext(), parameters)

        pass

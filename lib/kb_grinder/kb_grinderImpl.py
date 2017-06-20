# -*- coding: utf-8 -*-
#BEGIN_HEADER
from __future__ import print_function
from __future__ import division

import os
import sys
import shutil
import hashlib
import subprocess
import requests
requests.packages.urllib3.disable_warnings()
import re
import traceback
import uuid
from datetime import datetime
from pprint import pprint, pformat

import numpy as np
import math
from Bio import SeqIO

from biokbase.workspace.client import Workspace as workspaceService
from DataFileUtil.DataFileUtilClient import DataFileUtil as DFUClient
from KBaseReport.KBaseReportClient import KBaseReport

#END_HEADER


class kb_grinder:
    '''
    Module Name:
    kb_grinder

    Module Description:
    ** A KBase module: kb_grinder
**
** This module contains Grinder
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/kbaseapps/kb_grinder.git"
    GIT_COMMIT_HASH = "dacf8f19d6f5295fc9034d546e9711636e707aea"

    #BEGIN_CLASS_HEADER

    def log(self, target, message):
        if target is not None:
            target.append(message)
        print(message)
        sys.stdout.flush()

    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        self.shockURL = config['shock-url']
        self.handleURL = config['handle-service-url']
        self.serviceWizardURL = config['service-wizard-url']
        self.callbackURL = os.environ['SDK_CALLBACK_URL']
        self.scratch = os.path.abspath(config['scratch'])

        pprint(config)

        if not os.path.exists(self.scratch):
            os.makedirs(self.scratch)
        #END_CONSTRUCTOR
        pass


    def KButil_Build_InSilico_Metagenomes_with_Grinder(self, ctx, params):
        """
        :param params: instance of type
           "KButil_Build_InSilico_Metagenomes_with_Grinder_Params"
           (KButil_Build_InSilico_Metagenomes_with_Grinder() ** **  Use
           Grinder to generate in silico shotgun metagenomes) -> structure:
           parameter "workspace_name" of type "workspace_name" (** The
           workspace object refs are of form: ** **    objects =
           ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_refs" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String,
           parameter "num_reads_per_lib" of Long, parameter
           "population_percs" of String, parameter "read_len_mean" of Long,
           parameter "read_len_stddev" of Double, parameter "pairs_flag" of
           Long, parameter "mate_orientation" of String, parameter
           "insert_len_mean" of Long, parameter "insert_len_stddev" of
           Double, parameter "mutation_dist" of String, parameter
           "mutation_ratio" of String, parameter "qual_good" of Long,
           parameter "qual_bad" of Long, parameter "len_bias_flag" of Long,
           parameter "random_seed" of Long
        :returns: instance of type
           "KButil_Build_InSilico_Metagenomes_with_Grinder_Output" ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN KButil_Build_InSilico_Metagenomes_with_Grinder
        #END KButil_Build_InSilico_Metagenomes_with_Grinder

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method KButil_Build_InSilico_Metagenomes_with_Grinder return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]

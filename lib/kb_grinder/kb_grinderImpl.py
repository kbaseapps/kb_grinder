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
    GIT_COMMIT_HASH = "77a95c1c911a4e21ccead89151cf30b86d181a25"

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
        #### STEP 0: basic init
        ##
        console = []
        self.log(console, 'Running KButil_Build_InSilico_Metagenomes_with_Grinder(): ')
        self.log(console, "\n"+pformat(params))

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        headers = {'Authorization': 'OAuth '+token}
        env = os.environ.copy()
        env['KB_AUTH_TOKEN'] = token

        #SERVICE_VER = 'dev'  # DEBUG
        SERVICE_VER = 'release'

        # param checks
        required_params = ['input_refs',
                           'output_name',
                           'num_reads_per_lib',
                           'population_percs',
                           'read_len_mean',
                           'read_len_stddev',
                           'pairs_flag',
                           'mate_orientation',
                           'insert_len_mean',
                           'insert_len_stddev',
                           'mutation_dist',
                           'mutation_ratio',
                           'qual_good',
                           'qual_bad',
                           'len_bias_flag',
                           'random_seed'
                          ]
        for arg in required_params:
            if arg not in params or params[arg] == None or params[arg] == '':
                raise ValueError ("Must define required param: '"+arg+"'")


        # load provenance
        provenance = [{}]
        if 'provenance' in ctx:
            provenance = ctx['provenance']
        provenance[0]['input_ws_objects']=[]
        for input_ref in params['input_refs']:
            provenance[0]['input_ws_objects'].append(input_ref)


        # set the output path
        timestamp = int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds()*1000)
        output_dir = os.path.join(self.scratch,'output.'+str(timestamp))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)


        #### STEP 1: get genome scaffold sequences
        ##
        accepted_input_types = ["KBaseGenomes.Genome"]
        genome_refs = params['input_refs']
        genome_obj_names = []
        genome_sci_names = []
        scaffold_refs = dict()
        
        for i,input_ref in enumerate(genome_refs):
            try:
                [OBJID_I, NAME_I, TYPE_I, SAVE_DATE_I, VERSION_I, SAVED_BY_I, WSID_I, WORKSPACE_I, CHSUM_I, SIZE_I, META_I] = range(11)  # object_info tuple
                input_obj_info = wsClient.get_object_info_new ({'objects':[{'ref':input_ref}]})[0]
                input_obj_type = re.sub ('-[0-9]+\.[0-9]+$', "", input_obj_info[TYPE_I])  # remove trailing version
                genome_obj_names.append(input_obj_info[NAME_I])

            except Exception as e:
                raise ValueError('Unable to get object from workspace: (' + input_ref +')' + str(e))
            if input_obj_type not in accepted_input_types:
                raise ValueError ("Input object of type '"+input_obj_type+"' not accepted.  Must be one of "+", ".join(accepted_input_types))

            try:
                genome_obj = wsClient.get_objects([{'ref':input_ref}])[0]['data']
                genome_sci_names.append(genome_obj['scientific_name'])
            except:
                raise ValueError ("unable to fetch genome: "+input_ref)

            # Get sequences
            scaffold_refs[input_ref] = []
            if ('contigset_ref' not in genome_obj or genome_obj['contigset_ref'] == None) \
                    and ('assembly_ref' not in genome_obj or genome_obj['assembly_ref'] == None):
                raise ValueError ("Genome "+genome_obj_name[i]+" (ref:"+input_ref+") "+genome_sci_names[i]+" MISSING BOTH contigset_ref AND assembly_ref")
            elif 'assembly_ref' in genome_obj and genome_obj['assembly_ref'] != None:
                self.log (console, "Genome "+genome_obj_name[i]+" (ref:"+input_ref+") "+genome_sci_names[i]+" USING assembly_ref")
            elif 'contigset_ref' in genome_obj and genome_obj['contigset_ref'] != None:
                self.log (console, "Genome "+genome_obj_name[i]+" (ref:"+input_ref+") "+genome_sci_names[i]+" USING contigset_ref")


        # build report
        #
        reportName = 'kb_grinder_report_'+str(uuid.uuid4())
        reportObj = {'objects_created': [],
                     #'text_message': '',  # or is it 'message'?
                     'message': '',  # or is it 'text_message'?
                     'direct_html': '',
                     'direct_html_link_index': 0,
                     'file_links': [],
                     'html_links': [],
                     'workspace_name': params['workspace_name'],
                     'report_object_name': reportName
                     }

	# ADD REPORT HTML HERE
        #html_report_str = "\n".join(html_report_lines)
        #reportObj['direct_html'] = html_report_str

        # write html to file and upload
        #html_file = os.path.join (output_dir, 'domain_profile_report.html')
        #with open (html_file, 'w', 0) as html_handle:
        #    html_handle.write(html_report_str)
        #dfu = DFUClient(self.callbackURL)
        #try:
        #    upload_ret = dfu.file_to_shock({'file_path': html_file,
        #                                    'make_handle': 0,
        #                                    'pack': 'zip'})
        #except:
        #    raise ValueError ('Logging exception loading html_report to shock')
        #
        #reportObj['html_links'] = [{'shock_id': upload_ret['shock_id'],
        #                            'name': 'domain_profile_report.html',
        #                            'label': 'Functional Domain Profile report'}
        #                           ]


        # save report object
        #
        reportClient = KBaseReport(self.callbackURL, token=ctx['token'], service_ver=SERVICE_VER)
        #report_info = report.create({'report':reportObj, 'workspace_name':params['workspace_name']})
        report_info = reportClient.create_extended_report(reportObj)

        output = { 'report_name': report_info['name'], 'report_ref': report_info['ref'] }
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

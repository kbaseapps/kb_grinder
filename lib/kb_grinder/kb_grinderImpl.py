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
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
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
    workspaceURL = None
    GRINDER = '/usr/local/bin/grinder'

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
        invalid_msgs = []
        report_text = ''
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

        # set the output paths
        timestamp = int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds()*1000)
        output_dir = os.path.join(self.scratch,'output.'+str(timestamp))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        html_output_dir = os.path.join(output_dir,'html')
        if not os.path.exists(html_output_dir):
            os.makedirs(html_output_dir)


        #### STEP 1: Parse population_percs and write to file
        ##
        abundance_str = params['population_percs'].strip()
        abundance_file_path = os.path.join(output_dir,'my_abundances.txt')
        abundance_config_num_libs = 0
        abundance_config_num_libs_set = False
        grinder_genome_ids = []
        out_buf = []

        for row in abundance_str.split("\n"):
            cols = row.split()
            if cols[0].upper() == "GENOME":
                continue
            grinder_genome_ids.append(cols[0])
            self.log(console, "GRINDER GENOME ID: '"+cols[0]+"'")  # DEBUG
            out_row = []
            for col in cols:
                if col == '':
                    continue
                elif col == '%':
                    continue
                elif col.endswith('%'):
                    col = col.rstrip('%')
                out_row.append(col)
            out_buf.append("\t".join(out_row))
            if not abundance_config_num_libs_set:
                abundance_config_num_libs_set = True
                abundance_config_num_libs = len(out_row) - 1  # first col is genome id

        with open(abundance_file_path, 'w') as abundance_fh:
            for out_line in out_buf:
                abundance_fh.write(out_line+"\n")
        # DEBUG
        with open(abundance_file_path, 'r') as abundance_fh:
            for out_line in abundance_fh.readlines():
                out_line = out_line.rstrip()
                self.log(console, "ABUNDANCE_CONFIG: '"+out_line+"'")


        #### STEP 2: get genome scaffold sequences
        ##
        genomes_src_db_file_path = os.path.join (output_dir, 'genomes.fna')
        read_buf_size  = 65536
        write_buf_size = 65536
        accepted_input_types = ["KBaseGenomes.Genome"]
        genome_refs = params['input_refs']
        genome_obj_names = []
        genome_sci_names = []
        assembly_refs    = []
        
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

            # Get assembly_refs
            if ('contigset_ref' not in genome_obj or genome_obj['contigset_ref'] == None) \
                    and ('assembly_ref' not in genome_obj or genome_obj['assembly_ref'] == None):
                msg = "Genome "+genome_obj_names[i]+" (ref:"+input_ref+") "+genome_sci_names[i]+" MISSING BOTH contigset_ref AND assembly_ref.  Cannot process.  Exiting."
                self.log(console, msg)
                self.log(invalid_msgs, msg)
                continue
            elif 'assembly_ref' in genome_obj and genome_obj['assembly_ref'] != None:
                msg = "Genome "+genome_obj_names[i]+" (ref:"+input_ref+") "+genome_sci_names[i]+" USING assembly_ref: "+str(genome_obj['assembly_ref'])
                self.log (console, msg)
                assembly_refs.append(genome_obj['assembly_ref'])
            elif 'contigset_ref' in genome_obj and genome_obj['contigset_ref'] != None:
                msg = "Genome "+genome_obj_names[i]+" (ref:"+input_ref+") "+genome_sci_names[i]+" USING contigset_ref: "+str(genome_obj['contigset_ref'])
                self.log (console, msg)
                assembly_refs.append(genome_obj['contigset_ref'])

        # get fastas for scaffolds
        contig_file_paths = []
        if len(invalid_msgs) > 0:
            report_text = "\n".join(invalid_msgs)
        else:
            SERVICE_VER='release'
            auClient = AssemblyUtil(self.callbackURL, token=ctx['token'], service_ver=SERVICE_VER)
            dfu = DFUClient(self.callbackURL)

            for genome_i,input_ref in enumerate(genome_refs):
                contig_file = auClient.get_assembly_as_fasta({'ref':assembly_refs[genome_i]}).get('path')
                sys.stdout.flush()
                contig_file_path = dfu.unpack_file({'file_path': contig_file})['file_path']
                contig_file_paths.append(contig_file_path)

            # reformat FASTA IDs for Grinder
            with open (genomes_src_db_file_path, 'w', write_buf_size) as genomes_src_db_fh:
                for genome_i,contig_file_path in enumerate(contig_file_paths):
                    #self.log(console,str(genome_i)+" CONTIG_FILE: "+contig_file_path)  # DEBUG
                    #contig_ids = []
                    with open (contig_file_path, 'r', read_buf_size) as contig_fh:
                        genome_seq = ''
                        contig_seq = ''
                        contig_seqs = []
                        for contig_line in contig_fh.readlines():
                            contig_line = contig_line.rstrip()
                            if contig_line.startswith('>'):
                                #contig_id = contig_line.strip()[1:].split(' ')[0]
                                #contig_ids.append(contig_id)
                                #genomes_src_db_fh.write(">"+grinder_genome_ids[genome_i]+"\n")
                                if contig_seq != '':
                                    contig_seqs.append (contig_seq)
                                contig_seq = ''
                                continue
                            else:
                                #genomes_src_db_fh.write(contig_line)
                                contig_seq += contig_line
                        if contig_seq != '':
                            contig_seqs.append (contig_seq)
                        contig_seq = ''
                    
                    # write joined contigs to file
                    genome_seq = "NNNNNNNNNN".join(contig_seqs)  # NOTE: Using "-exclude_chars" grinder opt on N to avoid contig joins
                    genome_seq = genome_seq.upper()  # grinder might require upper case?
                    genomes_src_db_fh.write(">"+grinder_genome_ids[genome_i]+"\n")
                    genomes_src_db_fh.write(genome_seq+"\n")
                    genome_seq = ''
                    contig_seqs = []

            """
                    # DEBUG
                    #for contig_id in contig_ids:
                    #    self.log(console, "\tCONTIG_ID: "+contig_id)  # DEBUG
            # DEBUG
            toggle = 0
            with open (genomes_src_db_file_path, 'r', write_buf_size) as genomes_src_db_fh:
                for contig_line in genomes_src_db_fh.readlines():
                    contig_line = contig_line.rstrip()
                    if contig_line.startswith('>'):
                        self.log(console, 'GENOMES_SRC_DB: '+contig_line)
                        genome_id = contig_line[1:]
                        #toggle = 0
                    #elif toggle == 0:
                    elif genome_id == 'G3':
                        self.log(console, 'GENOMES_SRC_DB: '+contig_line[0:10000])
                        #toggle += 1
            """


        #### STEP 3: Run Grinder
        ##
        if len(invalid_msgs) == 0:
            cmd = []
            cmd.append (self.GRINDER)
            # output
            cmd.append ('-base_name')
            cmd.append (params['output_name'])
            cmd.append ('-output_dir')
            cmd.append (output_dir)
            # contigs input
            cmd.append ('-reference_file')
            cmd.append (genomes_src_db_file_path)
            # abundances
            cmd.append ('-abundance_file')
            cmd.append (abundance_file_path)
            # library size
            cmd.append ('-total_reads')
            cmd.append (str(params['num_reads_per_lib']))
            # num libraries (overridden by abundance file?)
            cmd.append ('-num_libraries')
            cmd.append (str(abundance_config_num_libs))
            # read and insert lens
            cmd.append ('-read_dist')
            cmd.append (str(params['read_len_mean']))
            cmd.append ('normal')
            cmd.append (str(params['read_len_stddev']))
            if params['pairs_flag'] == 1:
                cmd.append ('-insert_dist')
                cmd.append (str(params['insert_len_mean']))
                cmd.append ('normal')
                cmd.append (str(params['insert_len_stddev']))
                # mate orientation
                cmd.append ('-mate_orientation')
                cmd.append (params['mate_orientation'])
            # genome len bias
            cmd.append ('-length_bias')
            cmd.append (str(params['len_bias_flag']))
            # mutation model
            cmd.append ('-mutation_dist')
            cmd.append (str(params['mutation_dist']))
            cmd.append ('-mutation_ratio')
            cmd.append (str(params['mutation_ratio']))
            # qual scores
            cmd.append ('-fastq_output')
            cmd.append ('1')
            cmd.append ('-qual_levels')
            cmd.append (str(params['qual_good']))
            cmd.append (str(params['qual_bad']))
            # skip contig joins
            cmd.append ('-exclude_chars')
            cmd.append ('NX')
            # explicitly request bidirectional
            cmd.append ('-unidirectional')
            cmd.append ('0')
            # random seed
            if 'random_seed' in params and params['random_seed'] != None and params['random_seed'] != '':
                cmd.append ('-random_seed')
                cmd.append (str(params['random_seed']))


            # RUN
            cmd_str = " ".join(cmd)
            self.log (console, "\n===========================================================")
            self.log (console, "RUNNING: "+cmd_str)
            self.log (console, "===========================================================\n")

            cmdProcess = subprocess.Popen(cmd_str, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            outputlines = []
            while True:
                line = cmdProcess.stdout.readline()
                outputlines.append(line)
                if not line: break
                self.log(console, line.replace('\n', ''))
                
            cmdProcess.stdout.close()
            cmdProcess.wait()
            self.log(console, 'return code: ' + str(cmdProcess.returncode) + '\n')
            if cmdProcess.returncode != 0:
                raise ValueError('Error running kb_grinder, return code: ' +
                                 str(cmdProcess.returncode) + '\n')

            #report_text += "\n".join(outputlines)
            #report_text += "cmdstring: " + cmdstring + " stdout: " + stdout + " stderr " + stderr

            # capture output for report and paths to out files
            report_text_buf   = []
            struct_file_paths = []
            fastq_file_paths  = []
            for out_line in outputlines:
                if 'Community structure' in out_line:
                    clean_line = out_line.strip()
                    struct_file_paths.append (clean_line.split()[2])
                elif 'FASTQ file' in out_line:
                    clean_line = out_line.strip()
                    fastq_file_paths.append (clean_line.split()[2])
                else:
                    report_text_buf.append (out_line)
            report_text += "\n".join(report_text_buf)


        #### STEP 4: Upload Read Libs
        ##
        if len(invalid_msgs) == 0:
            lib_obj_refs = []
            lib_obj_names = []
            for sample_i,fastq_file_path in enumerate(fastq_file_paths):

                if not os.path.isfile (fastq_file_path) \
                   or os.path.getsize (fastq_file_path) == 0:

                    raise ValueError ("empty read lib generated: "+fastq_file_path)
                else:

                    # lib obj name
                    if len(fastq_file_paths) == 0:
                        output_obj_name = input_params['output_name']
                    else:
                        if params['pair_flag'] == 1:
                            output_obj_name = input_params['output_name']+'-'+str(sample_i+1)+".PairedEndLib"
                        else:
                            output_obj_name = input_params['output_name']+'-'+str(sample_i+1)+".SingleEndLib"
                    lib_obj_names.append (output_obj_name)

                    # upload lib and get obj ref
                    self.log(console, 'Uploading trimmed paired reads: '+output_obj_name)
                    sequencing_tech = 'artificial reads'
                    if params['pair_flag'] == 1:
                        interleaved = 1
                    else:
                        interleaved = 0
                    lib_obj_refs.append (readsUtils_Client.upload_reads ({ 'wsname': str(params['workspace_name']),
                                                                           'name': output_obj_name,
                                                                           'fwd_file': output_fwd_paired_file_path,
                                                                           'interleaved': interleaved,
                                                                           'sequencing_tech': sequencing_tech
                                                                       })['obj_ref'])

                    os.remove(fastq_file_path)  # free up disk
            
            

        #### STEP 5: Build report
        ##
        reportName = 'kb_grinder_report_'+str(uuid.uuid4())
        reportObj = {'objects_created': [],
                     #'text_message': '',  # or is it 'message'?
                     'message': '',  # or is it 'text_message'?
                     'direct_html': '',
                     'direct_html_link_index': 0,
                     'file_links': [],
                     'html_links': [],
                     'workspace_name': params['workspace'],
                     'report_object_name': reportName
                     }

        #if len(invalid_msgs) > 0:
        reportObj['message'] = report_text


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

        returnVal = { 'report_name': report_info['name'], 'report_ref': report_info['ref'] }
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

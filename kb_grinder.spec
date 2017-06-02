/*
** A KBase module: kb_grinder
**
** This module contains Grinder
*/

module kb_grinder {

    /* 
    ** The workspace object refs are of form:
    **
    **    objects = ws.get_objects([{'ref': params['workspace_id']+'/'+params['obj_name']}])
    **
    ** "ref" means the entire name combining the workspace id and the object name
    ** "id" is a numerical identifier of the workspace or object, and should just be used for workspace
    ** "name" is a string identifier of a workspace or object.  This is received from Narrative.
    */
    typedef string workspace_name;
    typedef string sequence;
    typedef string data_obj_name;
    typedef string data_obj_ref;
    typedef int    bool;


    /* KButil_Build_InSilico_Metagenomes_with_Grinder()
    **
    **  Use Grinder to generate in silico shotgun metagenomes
    */
    typedef structure {
        workspace_name workspace_name;
	data_obj_ref   input_refs;    /* Genomes */
        data_obj_name  output_name;   /* ReadsSet or ReadsLib if only one MG being generated */
	string         desc;

	/* params */
	int     num_reads_per_lib;
	string  population_percs;
	
	/* advanced params */
	int     read_len_mean;
	float   read_len_stddev;
	int     pairs_flag;
	string  mate_orientation;
	int     insert_len_mean;
	float   insert_len_stddev;
	string  mutation_dist;
	string  mutation_ratio;
	int     qual_good;
	int     qual_bad;
	int     len_bias_flag;
	int     random_seed;

    } KButil_Build_InSilico_Metagenomes_with_Grinder_Params;

    typedef structure {
	data_obj_name report_name;
	data_obj_ref  report_ref;
    } KButil_Build_InSilico_Metagenomes_with_Grinder_Output;

    funcdef KButil_Build_InSilico_Metagenomes_with_Grinder (KButil_Build_InSilico_Metagenomes_with_Grinder_Params params)  returns (KButil_Build_InSilico_Metagenomes_with_Grinder_Output) authentication required;

};


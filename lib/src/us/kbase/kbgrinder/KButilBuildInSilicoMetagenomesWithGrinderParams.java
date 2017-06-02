
package us.kbase.kbgrinder;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: KButil_Build_InSilico_Metagenomes_with_Grinder_Params</p>
 * <pre>
 * KButil_Build_InSilico_Metagenomes_with_Grinder()
 * **
 * **  Use Grinder to generate in silico shotgun metagenomes
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "input_refs",
    "output_name",
    "desc",
    "num_reads_per_lib",
    "population_percs",
    "read_len_mean",
    "read_len_stddev",
    "pairs_flag",
    "mate_orientation",
    "insert_len_mean",
    "insert_len_stddev",
    "mutation_dist",
    "mutation_ratio",
    "qual_good",
    "qual_bad",
    "len_bias_flag",
    "random_seed"
})
public class KButilBuildInSilicoMetagenomesWithGrinderParams {

    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("input_refs")
    private String inputRefs;
    @JsonProperty("output_name")
    private String outputName;
    @JsonProperty("desc")
    private String desc;
    @JsonProperty("num_reads_per_lib")
    private Long numReadsPerLib;
    @JsonProperty("population_percs")
    private String populationPercs;
    @JsonProperty("read_len_mean")
    private Long readLenMean;
    @JsonProperty("read_len_stddev")
    private Double readLenStddev;
    @JsonProperty("pairs_flag")
    private Long pairsFlag;
    @JsonProperty("mate_orientation")
    private String mateOrientation;
    @JsonProperty("insert_len_mean")
    private Long insertLenMean;
    @JsonProperty("insert_len_stddev")
    private Double insertLenStddev;
    @JsonProperty("mutation_dist")
    private String mutationDist;
    @JsonProperty("mutation_ratio")
    private String mutationRatio;
    @JsonProperty("qual_good")
    private Long qualGood;
    @JsonProperty("qual_bad")
    private Long qualBad;
    @JsonProperty("len_bias_flag")
    private Long lenBiasFlag;
    @JsonProperty("random_seed")
    private Long randomSeed;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("input_refs")
    public String getInputRefs() {
        return inputRefs;
    }

    @JsonProperty("input_refs")
    public void setInputRefs(String inputRefs) {
        this.inputRefs = inputRefs;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withInputRefs(String inputRefs) {
        this.inputRefs = inputRefs;
        return this;
    }

    @JsonProperty("output_name")
    public String getOutputName() {
        return outputName;
    }

    @JsonProperty("output_name")
    public void setOutputName(String outputName) {
        this.outputName = outputName;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withOutputName(String outputName) {
        this.outputName = outputName;
        return this;
    }

    @JsonProperty("desc")
    public String getDesc() {
        return desc;
    }

    @JsonProperty("desc")
    public void setDesc(String desc) {
        this.desc = desc;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withDesc(String desc) {
        this.desc = desc;
        return this;
    }

    @JsonProperty("num_reads_per_lib")
    public Long getNumReadsPerLib() {
        return numReadsPerLib;
    }

    @JsonProperty("num_reads_per_lib")
    public void setNumReadsPerLib(Long numReadsPerLib) {
        this.numReadsPerLib = numReadsPerLib;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withNumReadsPerLib(Long numReadsPerLib) {
        this.numReadsPerLib = numReadsPerLib;
        return this;
    }

    @JsonProperty("population_percs")
    public String getPopulationPercs() {
        return populationPercs;
    }

    @JsonProperty("population_percs")
    public void setPopulationPercs(String populationPercs) {
        this.populationPercs = populationPercs;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withPopulationPercs(String populationPercs) {
        this.populationPercs = populationPercs;
        return this;
    }

    @JsonProperty("read_len_mean")
    public Long getReadLenMean() {
        return readLenMean;
    }

    @JsonProperty("read_len_mean")
    public void setReadLenMean(Long readLenMean) {
        this.readLenMean = readLenMean;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withReadLenMean(Long readLenMean) {
        this.readLenMean = readLenMean;
        return this;
    }

    @JsonProperty("read_len_stddev")
    public Double getReadLenStddev() {
        return readLenStddev;
    }

    @JsonProperty("read_len_stddev")
    public void setReadLenStddev(Double readLenStddev) {
        this.readLenStddev = readLenStddev;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withReadLenStddev(Double readLenStddev) {
        this.readLenStddev = readLenStddev;
        return this;
    }

    @JsonProperty("pairs_flag")
    public Long getPairsFlag() {
        return pairsFlag;
    }

    @JsonProperty("pairs_flag")
    public void setPairsFlag(Long pairsFlag) {
        this.pairsFlag = pairsFlag;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withPairsFlag(Long pairsFlag) {
        this.pairsFlag = pairsFlag;
        return this;
    }

    @JsonProperty("mate_orientation")
    public String getMateOrientation() {
        return mateOrientation;
    }

    @JsonProperty("mate_orientation")
    public void setMateOrientation(String mateOrientation) {
        this.mateOrientation = mateOrientation;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withMateOrientation(String mateOrientation) {
        this.mateOrientation = mateOrientation;
        return this;
    }

    @JsonProperty("insert_len_mean")
    public Long getInsertLenMean() {
        return insertLenMean;
    }

    @JsonProperty("insert_len_mean")
    public void setInsertLenMean(Long insertLenMean) {
        this.insertLenMean = insertLenMean;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withInsertLenMean(Long insertLenMean) {
        this.insertLenMean = insertLenMean;
        return this;
    }

    @JsonProperty("insert_len_stddev")
    public Double getInsertLenStddev() {
        return insertLenStddev;
    }

    @JsonProperty("insert_len_stddev")
    public void setInsertLenStddev(Double insertLenStddev) {
        this.insertLenStddev = insertLenStddev;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withInsertLenStddev(Double insertLenStddev) {
        this.insertLenStddev = insertLenStddev;
        return this;
    }

    @JsonProperty("mutation_dist")
    public String getMutationDist() {
        return mutationDist;
    }

    @JsonProperty("mutation_dist")
    public void setMutationDist(String mutationDist) {
        this.mutationDist = mutationDist;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withMutationDist(String mutationDist) {
        this.mutationDist = mutationDist;
        return this;
    }

    @JsonProperty("mutation_ratio")
    public String getMutationRatio() {
        return mutationRatio;
    }

    @JsonProperty("mutation_ratio")
    public void setMutationRatio(String mutationRatio) {
        this.mutationRatio = mutationRatio;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withMutationRatio(String mutationRatio) {
        this.mutationRatio = mutationRatio;
        return this;
    }

    @JsonProperty("qual_good")
    public Long getQualGood() {
        return qualGood;
    }

    @JsonProperty("qual_good")
    public void setQualGood(Long qualGood) {
        this.qualGood = qualGood;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withQualGood(Long qualGood) {
        this.qualGood = qualGood;
        return this;
    }

    @JsonProperty("qual_bad")
    public Long getQualBad() {
        return qualBad;
    }

    @JsonProperty("qual_bad")
    public void setQualBad(Long qualBad) {
        this.qualBad = qualBad;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withQualBad(Long qualBad) {
        this.qualBad = qualBad;
        return this;
    }

    @JsonProperty("len_bias_flag")
    public Long getLenBiasFlag() {
        return lenBiasFlag;
    }

    @JsonProperty("len_bias_flag")
    public void setLenBiasFlag(Long lenBiasFlag) {
        this.lenBiasFlag = lenBiasFlag;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withLenBiasFlag(Long lenBiasFlag) {
        this.lenBiasFlag = lenBiasFlag;
        return this;
    }

    @JsonProperty("random_seed")
    public Long getRandomSeed() {
        return randomSeed;
    }

    @JsonProperty("random_seed")
    public void setRandomSeed(Long randomSeed) {
        this.randomSeed = randomSeed;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withRandomSeed(Long randomSeed) {
        this.randomSeed = randomSeed;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((((((((((((((((((((((((((((("KButilBuildInSilicoMetagenomesWithGrinderParams"+" [workspaceName=")+ workspaceName)+", inputRefs=")+ inputRefs)+", outputName=")+ outputName)+", desc=")+ desc)+", numReadsPerLib=")+ numReadsPerLib)+", populationPercs=")+ populationPercs)+", readLenMean=")+ readLenMean)+", readLenStddev=")+ readLenStddev)+", pairsFlag=")+ pairsFlag)+", mateOrientation=")+ mateOrientation)+", insertLenMean=")+ insertLenMean)+", insertLenStddev=")+ insertLenStddev)+", mutationDist=")+ mutationDist)+", mutationRatio=")+ mutationRatio)+", qualGood=")+ qualGood)+", qualBad=")+ qualBad)+", lenBiasFlag=")+ lenBiasFlag)+", randomSeed=")+ randomSeed)+", additionalProperties=")+ additionalProperties)+"]");
    }

}


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
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "input_refs",
    "output_name",
    "subsample_fraction",
    "desc",
    "seed"
})
public class KButilBuildInSilicoMetagenomesWithGrinderParams {

    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("input_refs")
    private String inputRefs;
    @JsonProperty("output_name")
    private String outputName;
    /**
     * <p>Original spec-file type: InSilico_Reads_Options</p>
     * <pre>
     * KButil_Build_InSilico_Metagenomes_with_Grinder()
     * **
     * **  Use Grinder to generate in silico shotgun metagenomes
     * </pre>
     * 
     */
    @JsonProperty("subsample_fraction")
    private InSilicoReadsOptions subsampleFraction;
    @JsonProperty("desc")
    private String desc;
    @JsonProperty("seed")
    private Long seed;
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

    /**
     * <p>Original spec-file type: InSilico_Reads_Options</p>
     * <pre>
     * KButil_Build_InSilico_Metagenomes_with_Grinder()
     * **
     * **  Use Grinder to generate in silico shotgun metagenomes
     * </pre>
     * 
     */
    @JsonProperty("subsample_fraction")
    public InSilicoReadsOptions getSubsampleFraction() {
        return subsampleFraction;
    }

    /**
     * <p>Original spec-file type: InSilico_Reads_Options</p>
     * <pre>
     * KButil_Build_InSilico_Metagenomes_with_Grinder()
     * **
     * **  Use Grinder to generate in silico shotgun metagenomes
     * </pre>
     * 
     */
    @JsonProperty("subsample_fraction")
    public void setSubsampleFraction(InSilicoReadsOptions subsampleFraction) {
        this.subsampleFraction = subsampleFraction;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withSubsampleFraction(InSilicoReadsOptions subsampleFraction) {
        this.subsampleFraction = subsampleFraction;
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

    @JsonProperty("seed")
    public Long getSeed() {
        return seed;
    }

    @JsonProperty("seed")
    public void setSeed(Long seed) {
        this.seed = seed;
    }

    public KButilBuildInSilicoMetagenomesWithGrinderParams withSeed(Long seed) {
        this.seed = seed;
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
        return ((((((((((((((("KButilBuildInSilicoMetagenomesWithGrinderParams"+" [workspaceName=")+ workspaceName)+", inputRefs=")+ inputRefs)+", outputName=")+ outputName)+", subsampleFraction=")+ subsampleFraction)+", desc=")+ desc)+", seed=")+ seed)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

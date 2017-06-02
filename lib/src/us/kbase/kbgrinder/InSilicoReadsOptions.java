
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
 * <p>Original spec-file type: InSilico_Reads_Options</p>
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
    "reads_num",
    "population_percs"
})
public class InSilicoReadsOptions {

    @JsonProperty("reads_num")
    private Long readsNum;
    @JsonProperty("population_percs")
    private String populationPercs;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("reads_num")
    public Long getReadsNum() {
        return readsNum;
    }

    @JsonProperty("reads_num")
    public void setReadsNum(Long readsNum) {
        this.readsNum = readsNum;
    }

    public InSilicoReadsOptions withReadsNum(Long readsNum) {
        this.readsNum = readsNum;
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

    public InSilicoReadsOptions withPopulationPercs(String populationPercs) {
        this.populationPercs = populationPercs;
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
        return ((((((("InSilicoReadsOptions"+" [readsNum=")+ readsNum)+", populationPercs=")+ populationPercs)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

#include "weight_dv_impl.h"

//---------------------------------------
// Globals
//---------------------------------------
// Global plasticity parameter data
plasticity_weight_region_data_t
    plasticity_weight_region_data[SYNAPSE_TYPE_COUNT];

//---------------------------------------
// Functions
//---------------------------------------
address_t weight_initialise(address_t address,
                            uint32_t *ring_buffer_to_input_buffer_left_shifts) {
    use(ring_buffer_to_input_buffer_left_shifts);

    log_info("weight_initialise: starting");
    log_info("\tDvDt weight dependance");

    // Copy plasticity region data from address
    // **NOTE** this seems somewhat safer than relying on sizeof
    int32_t *plasticity_word = (int32_t*) address;
    for (uint32_t s = 0; s < SYNAPSE_TYPE_COUNT; s++) {
        plasticity_weight_region_data[s].min_weight = *plasticity_word++;
        plasticity_weight_region_data[s].max_weight = *plasticity_word++;
        plasticity_weight_region_data[s].scale = *plasticity_word++;

        log_info(
            "\tSynapse type %u: Min weight:%d, Max weight:%d, scale+:%d",
            s, plasticity_weight_region_data[s].min_weight,
            plasticity_weight_region_data[s].max_weight,
            plasticity_weight_region_data[s].scale);
    }
    log_info("weight_initialise: completed successfully");

    // Return end address of region
    return (address_t) plasticity_word;
}
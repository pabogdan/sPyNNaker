"""
Synfirechain-like example
"""
#!/usr/bin/python
import unittest

import spynnaker.plot_utils as plot_utils
import spynnaker.spike_checker as spike_checker

import p7_integration_tests.scripts.synfire_run as synfire_run


class Synfire130n10pc13cWithNoDelaysSpikeRecording(unittest.TestCase):

    def test_run(self):
        nNeurons = 130  # number of neurons in each population
        results = synfire_run.do_run(nNeurons,  delay=1, neurons_per_core=10,
                                     record_v=False, record_gsyn=False)
        (v, gsyn, spikes) = results
        self.assertEquals(333, len(spikes))
        spike_checker.synfire_spike_checker(spikes, nNeurons)


if __name__ == '__main__':
    nNeurons = 130  # number of neurons in each population
    results = synfire_run.do_run(nNeurons, delay=1, neurons_per_core=10,
                                 record_v=False, record_gsyn=False)
    (v, gsyn, spikes) = results
    print len(spikes)
    plot_utils.plot_spikes(spikes)
    # v and gysn are None
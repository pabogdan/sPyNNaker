from six import add_metaclass

from spinn_utilities.abstract_base import AbstractBase, abstractmethod, \
    abstractproperty


@add_metaclass(AbstractBase)
class AbstractPopulationInitializable(object):
    """ Indicates that this object has properties that can be initialised by a\
        PyNN Population
    """

    __slots__ = ()

    @abstractmethod
    def initialize(self, variable, value):
        """ Set the initial value of one of the state variables of the neurons\
            in this population.

        """

    @abstractproperty
    def initial_values(self):
        """A dict containing the initial values of the state variables."""

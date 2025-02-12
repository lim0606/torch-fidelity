from abc import ABC, abstractmethod

import numpy as np
import torch
from torch_fidelity.registry import NOISE_SOURCE_REGISTRY


class GenerativeModelBase(ABC, torch.nn.Module):
    """
    Base class for generative models that can be used as inputs in :func:`calculate_metrics`.
    """

    @property
    @abstractmethod
    def z_size(self):
        """
        Size of the noise dimension of the generative model (positive integer).
        """
        pass

    @property
    @abstractmethod
    def z_type(self):
        """
        Type of the noise used by the generative model (see :ref:`registry <Registry>` for a list of preregistered noise
        types, see :func:`register_noise_source` for registering a new noise type).
        """
        pass

    @property
    @abstractmethod
    def num_classes(self):
        """
        Number of classes used by a conditional generative model. Must return zero for unconditional models.
        """
        pass

    def sample_z(self, sz, rng=None):
        if rng is None:
            rng = np.random.RandomState(None)
        noise = NOISE_SOURCE_REGISTRY[self.z_type](rng, (sz, self.z_size))
        return noise

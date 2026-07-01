"""TorchRL tensor-spec helpers compatible with torchrl >= 0.7."""

import torch

try:
    from torchrl.data import (
        BinaryDiscreteTensorSpec,
        DiscreteTensorSpec,
        MultiDiscreteTensorSpec,
    )
except ImportError:
    from torchrl.data import Binary, Categorical, MultiCategorical

    class DiscreteTensorSpec(Categorical):
        def __init__(self, n, shape=(), device=None, dtype=None, **kwargs):
            super().__init__(
                n=n,
                shape=shape,
                device=device,
                dtype=dtype or torch.long,
                **kwargs,
            )

    class BinaryDiscreteTensorSpec(Binary):
        def __init__(self, n=2, shape=(), device=None, dtype=None, **kwargs):
            super().__init__(
                n=n,
                shape=shape,
                device=device,
                dtype=dtype or torch.long,
                **kwargs,
            )

    class MultiDiscreteTensorSpec(MultiCategorical):
        pass


def done_spec(num_envs, device):
    """Bool done/terminated/truncated specs for vectorized envs."""
    from torchrl.data import CompositeSpec

    try:
        from torchrl.data import Categorical

        entry = Categorical(2, (1,), dtype=torch.bool)
    except ImportError:
        entry = DiscreteTensorSpec(2, (1,), dtype=torch.bool)
    return CompositeSpec(
        {
            "done": entry,
            "terminated": entry,
            "truncated": entry,
        }
    ).expand(num_envs).to(device)

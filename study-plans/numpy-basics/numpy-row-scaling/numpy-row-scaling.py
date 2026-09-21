import numpy as np

def scale_rows(data: list, weights: list) -> np.ndarray:
    """
    Returns a float64 matrix with each row multiplied by its weight.
    """
    data = np.asarray(data, dtype=np.float64)
    weights = np.asarray(weights, dtype=np.float64)

    return data * weights[:, None]

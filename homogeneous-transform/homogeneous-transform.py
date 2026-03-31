import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    

    points = np.array(points) #Turn points into a np array
    T = np.array(T) #Turns  T into np ndim array

    # Track whether the input is a single point
    single_point = False
    
    if points.ndim == 1: # If the input is a single point, reshape it to a 2D row array
        points = points.reshape(1, -1) 
        single_point = True # Check whether the input is a single point
        
    N = points.shape[0] # Get number of rows in points
    ones = np.ones((N, 1)) 
    p_h = np.concatenate((points, ones),  axis=1)
    T = T.T # Transpose  T to turn column vectors into row vectors to make appropriate for matmul

    # Compute matrix multiplication
    p_prime_h  = np.dot(p_h, T)

    #Store Result
    result = p_prime_h[:,:-1]

    # Return a 1D array for a single point
    if single_point:
        return result[0]
    else:
        return result
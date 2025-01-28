

def Rydberg(m,n,Z=1):
    """Computes the color of light, in nanometer, emitted/absorbed by a hydrogen-like chemical element
    when an electron transitions between a lower level m and upper level n.
    """
    if n < m:
        raise RuntimeError("Argument n (second) must be larger than argument m (first)")


    if m < 1:
        raise RuntimeError("Quantum number m (first argument) must be greater than or equal to 1.")

    one_over_m_squared = 1/m**2

    if n < 1:
        raise RuntimeError("Quantum number n (second argument) must be greater than or equal to 1.")

    one_over_n_squared = 1/m**2

    if Z < 1:
        raise RuntimeError("Atomic number Z (third argument) must be greater than or equal to 1.")

    one_over_lambda = one_over_m_squared - one_over_n_squared
    one_over_lambda *= 1.9677e7 #  R in 1/m
    one_over_lambda *= Z*Z

    wavelength = 1 / one_over_lambda

    wavelength *= 1e9 # convert to nm

    return wavelength






    
    



# write unti tests here

print(Rydberg(1,3))

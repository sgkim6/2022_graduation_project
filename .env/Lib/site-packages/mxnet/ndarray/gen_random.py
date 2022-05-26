# coding: utf-8# File content is auto-generated. Do not modify.
# pylint: skip-file
from ._internal import NDArrayBase
from ..base import _Null

def exponential(lam=_Null, shape=_Null, ctx=_Null, dtype=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from an exponential distribution.

    Samples are distributed according to an exponential distribution parametrized by *lambda* (rate).

    Example::

       exponential(lam=4, shape=(2,2)) = [[ 0.0097189 ,  0.08999364],
                                          [ 0.04146638,  0.31715935]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L137

    Parameters
    ----------
    lam : float, optional, default=1
        Lambda parameter (rate) of the exponential distribution.
    shape : Shape(tuple), optional, default=None
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def exponential_like(data=None, lam=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from an exponential distribution according to the input array shape.

    Samples are distributed according to an exponential distribution parametrized by *lambda* (rate).

    Example::

       exponential(lam=4, data=ones(2,2)) = [[ 0.0097189 ,  0.08999364],
                                             [ 0.04146638,  0.31715935]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L243

    Parameters
    ----------
    lam : float, optional, default=1
        Lambda parameter (rate) of the exponential distribution.
    data : NDArray
        The input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def gamma(alpha=_Null, beta=_Null, shape=_Null, ctx=_Null, dtype=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a gamma distribution.

    Samples are distributed according to a gamma distribution parametrized by *alpha* (shape) and *beta* (scale).

    Example::

       gamma(alpha=9, beta=0.5, shape=(2,2)) = [[ 7.10486984,  3.37695289],
                                                [ 3.91697288,  3.65933681]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L125

    Parameters
    ----------
    alpha : float, optional, default=1
        Alpha parameter (shape) of the gamma distribution.
    beta : float, optional, default=1
        Beta parameter (scale) of the gamma distribution.
    shape : Shape(tuple), optional, default=None
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def gamma_like(data=None, alpha=_Null, beta=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a gamma distribution according to the input array shape.

    Samples are distributed according to a gamma distribution parametrized by *alpha* (shape) and *beta* (scale).

    Example::

       gamma(alpha=9, beta=0.5, data=ones(2,2)) = [[ 7.10486984,  3.37695289],
                                                   [ 3.91697288,  3.65933681]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L232

    Parameters
    ----------
    alpha : float, optional, default=1
        Alpha parameter (shape) of the gamma distribution.
    beta : float, optional, default=1
        Beta parameter (scale) of the gamma distribution.
    data : NDArray
        The input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def generalized_negative_binomial(mu=_Null, alpha=_Null, shape=_Null, ctx=_Null, dtype=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a generalized negative binomial distribution.

    Samples are distributed according to a generalized negative binomial distribution parametrized by
    *mu* (mean) and *alpha* (dispersion). *alpha* is defined as *1/k* where *k* is the failure limit of the
    number of unsuccessful experiments (generalized to real numbers).
    Samples will always be returned as a floating point data type.

    Example::

       generalized_negative_binomial(mu=2.0, alpha=0.3, shape=(2,2)) = [[ 2.,  1.],
                                                                        [ 6.,  4.]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L179

    Parameters
    ----------
    mu : float, optional, default=1
        Mean of the negative binomial distribution.
    alpha : float, optional, default=1
        Alpha (dispersion) parameter of the negative binomial distribution.
    shape : Shape(tuple), optional, default=None
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def generalized_negative_binomial_like(data=None, mu=_Null, alpha=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a generalized negative binomial distribution according to the
    input array shape.

    Samples are distributed according to a generalized negative binomial distribution parametrized by
    *mu* (mean) and *alpha* (dispersion). *alpha* is defined as *1/k* where *k* is the failure limit of the
    number of unsuccessful experiments (generalized to real numbers).
    Samples will always be returned as a floating point data type.

    Example::

       generalized_negative_binomial(mu=2.0, alpha=0.3, data=ones(2,2)) = [[ 2.,  1.],
                                                                           [ 6.,  4.]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L284

    Parameters
    ----------
    mu : float, optional, default=1
        Mean of the negative binomial distribution.
    alpha : float, optional, default=1
        Alpha (dispersion) parameter of the negative binomial distribution.
    data : NDArray
        The input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def negative_binomial(k=_Null, p=_Null, shape=_Null, ctx=_Null, dtype=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a negative binomial distribution.

    Samples are distributed according to a negative binomial distribution parametrized by
    *k* (limit of unsuccessful experiments) and *p* (failure probability in each experiment).
    Samples will always be returned as a floating point data type.

    Example::

       negative_binomial(k=3, p=0.4, shape=(2,2)) = [[ 4.,  7.],
                                                     [ 2.,  5.]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L164

    Parameters
    ----------
    k : int, optional, default='1'
        Limit of unsuccessful experiments.
    p : float, optional, default=1
        Failure probability in each experiment.
    shape : Shape(tuple), optional, default=None
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def negative_binomial_like(data=None, k=_Null, p=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a negative binomial distribution according to the input array shape.

    Samples are distributed according to a negative binomial distribution parametrized by
    *k* (limit of unsuccessful experiments) and *p* (failure probability in each experiment).
    Samples will always be returned as a floating point data type.

    Example::

       negative_binomial(k=3, p=0.4, data=ones(2,2)) = [[ 4.,  7.],
                                                        [ 2.,  5.]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L268

    Parameters
    ----------
    k : int, optional, default='1'
        Limit of unsuccessful experiments.
    p : float, optional, default=1
        Failure probability in each experiment.
    data : NDArray
        The input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def normal(loc=_Null, scale=_Null, shape=_Null, ctx=_Null, dtype=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a normal (Gaussian) distribution.

    .. note:: The existing alias ``normal`` is deprecated.

    Samples are distributed according to a normal distribution parametrized by *loc* (mean) and *scale*
    (standard deviation).

    Example::

       normal(loc=0, scale=1, shape=(2,2)) = [[ 1.89171135, -1.16881478],
                                              [-1.23474145,  1.55807114]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L113

    Parameters
    ----------
    loc : float, optional, default=0
        Mean of the distribution.
    scale : float, optional, default=1
        Standard deviation of the distribution.
    shape : Shape(tuple), optional, default=None
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def normal_like(data=None, loc=_Null, scale=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a normal (Gaussian) distribution according to the input array shape.

    Samples are distributed according to a normal distribution parametrized by *loc* (mean) and *scale*
    (standard deviation).

    Example::

       normal(loc=0, scale=1, data=ones(2,2)) = [[ 1.89171135, -1.16881478],
                                                 [-1.23474145,  1.55807114]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L221

    Parameters
    ----------
    loc : float, optional, default=0
        Mean of the distribution.
    scale : float, optional, default=1
        Standard deviation of the distribution.
    data : NDArray
        The input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def pdf_dirichlet(sample=None, alpha=None, is_log=_Null, out=None, name=None, **kwargs):
    r"""Computes the value of the PDF of *sample* of
    Dirichlet distributions with parameter *alpha*.

    The shape of *alpha* must match the leftmost subshape of *sample*.  That is, *sample*
    can have the same shape as *alpha*, in which case the output contains one density per
    distribution, or *sample* can be a tensor of tensors with that shape, in which case
    the output is a tensor of densities such that the densities at index *i* in the output
    are given by the samples at index *i* in *sample* parameterized by the value of *alpha*
    at index *i*.

    Examples::

        random_pdf_dirichlet(sample=[[1,2],[2,3],[3,4]], alpha=[2.5, 2.5]) =
            [38.413498, 199.60245, 564.56085]

        sample = [[[1, 2, 3], [10, 20, 30], [100, 200, 300]],
                  [[0.1, 0.2, 0.3], [0.01, 0.02, 0.03], [0.001, 0.002, 0.003]]]

        random_pdf_dirichlet(sample=sample, alpha=[0.1, 0.4, 0.9]) =
            [[2.3257459e-02, 5.8420084e-04, 1.4674458e-05],
             [9.2589635e-01, 3.6860607e+01, 1.4674468e+03]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\pdf_op.cc:L316

    Parameters
    ----------
    sample : NDArray
        Samples from the distributions.
    alpha : NDArray
        Concentration parameters of the distributions.
    is_log : boolean, optional, default=0
        If set, compute the density of the log-probability instead of the probability.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def pdf_exponential(sample=None, lam=None, is_log=_Null, out=None, name=None, **kwargs):
    r"""Concurrent sampling from multiple
    exponential distributions with parameters lambda (rate).

    The parameters of the distributions are provided as an input array.
    Let *[s]* be the shape of the input array, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input array, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input value at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input array.

    Examples::

       lam = [ 1.0, 8.5 ]

       // Draw a single sample for each distribution
       sample_exponential(lam) = [ 0.51837951,  0.09994757]

       // Draw a vector containing two samples for each distribution
       sample_exponential(lam, shape=(2)) = [[ 0.51837951,  0.19866663],
                                             [ 0.09994757,  0.50447971]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\pdf_op.cc:L305

    Parameters
    ----------
    sample : NDArray
        Samples from the distributions.
    lam : NDArray
        Lambda (rate) parameters of the distributions.
    is_log : boolean, optional, default=0
        If set, compute the density of the log-probability instead of the probability.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def pdf_gamma(sample=None, alpha=None, beta=None, is_log=_Null, out=None, name=None, **kwargs):
    r"""Concurrent sampling from multiple
    gamma distributions with parameters *alpha* (shape) and *beta* (scale).

    The parameters of the distributions are provided as input arrays.
    Let *[s]* be the shape of the input arrays, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input arrays, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input values at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input arrays.

    Examples::

       alpha = [ 0.0, 2.5 ]
       beta = [ 1.0, 0.7 ]

       // Draw a single sample for each distribution
       sample_gamma(alpha, beta) = [ 0.        ,  2.25797319]

       // Draw a vector containing two samples for each distribution
       sample_gamma(alpha, beta, shape=(2)) = [[ 0.        ,  0.        ],
                                               [ 2.25797319,  1.70734084]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\pdf_op.cc:L303

    Parameters
    ----------
    sample : NDArray
        Samples from the distributions.
    alpha : NDArray
        Alpha (shape) parameters of the distributions.
    is_log : boolean, optional, default=0
        If set, compute the density of the log-probability instead of the probability.
    beta : NDArray
        Beta (scale) parameters of the distributions.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def pdf_generalized_negative_binomial(sample=None, mu=None, alpha=None, is_log=_Null, out=None, name=None, **kwargs):
    r"""Concurrent sampling from multiple
    generalized negative binomial distributions with parameters *mu* (mean) and *alpha* (dispersion).

    The parameters of the distributions are provided as input arrays.
    Let *[s]* be the shape of the input arrays, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input arrays, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input values at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input arrays.

    Samples will always be returned as a floating point data type.

    Examples::

       mu = [ 2.0, 2.5 ]
       alpha = [ 1.0, 0.1 ]

       // Draw a single sample for each distribution
       sample_generalized_negative_binomial(mu, alpha) = [ 0.,  3.]

       // Draw a vector containing two samples for each distribution
       sample_generalized_negative_binomial(mu, alpha, shape=(2)) = [[ 0.,  3.],
                                                                     [ 3.,  1.]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\pdf_op.cc:L314

    Parameters
    ----------
    sample : NDArray
        Samples from the distributions.
    mu : NDArray
        Means of the distributions.
    is_log : boolean, optional, default=0
        If set, compute the density of the log-probability instead of the probability.
    alpha : NDArray
        Alpha (dispersion) parameters of the distributions.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def pdf_negative_binomial(sample=None, k=None, p=None, is_log=_Null, out=None, name=None, **kwargs):
    r"""Concurrent sampling from multiple
    negative binomial distributions with parameters *k* (failure limit) and *p* (failure probability).

    The parameters of the distributions are provided as input arrays.
    Let *[s]* be the shape of the input arrays, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input arrays, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input values at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input arrays.

    Samples will always be returned as a floating point data type.

    Examples::

       k = [ 20, 49 ]
       p = [ 0.4 , 0.77 ]

       // Draw a single sample for each distribution
       sample_negative_binomial(k, p) = [ 15.,  16.]

       // Draw a vector containing two samples for each distribution
       sample_negative_binomial(k, p, shape=(2)) = [[ 15.,  50.],
                                                    [ 16.,  12.]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\pdf_op.cc:L310

    Parameters
    ----------
    sample : NDArray
        Samples from the distributions.
    k : NDArray
        Limits of unsuccessful experiments.
    is_log : boolean, optional, default=0
        If set, compute the density of the log-probability instead of the probability.
    p : NDArray
        Failure probabilities in each experiment.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def pdf_normal(sample=None, mu=None, sigma=None, is_log=_Null, out=None, name=None, **kwargs):
    r"""Concurrent sampling from multiple
    normal distributions with parameters *mu* (mean) and *sigma* (standard deviation).

    The parameters of the distributions are provided as input arrays.
    Let *[s]* be the shape of the input arrays, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input arrays, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input values at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input arrays.

    Examples::

       mu = [ 0.0, 2.5 ]
       sigma = [ 1.0, 3.7 ]

       // Draw a single sample for each distribution
       sample_normal(mu, sigma) = [-0.56410581,  0.95934606]

       // Draw a vector containing two samples for each distribution
       sample_normal(mu, sigma, shape=(2)) = [[-0.56410581,  0.2928229 ],
                                              [ 0.95934606,  4.48287058]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\pdf_op.cc:L300

    Parameters
    ----------
    sample : NDArray
        Samples from the distributions.
    mu : NDArray
        Means of the distributions.
    is_log : boolean, optional, default=0
        If set, compute the density of the log-probability instead of the probability.
    sigma : NDArray
        Standard deviations of the distributions.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def pdf_poisson(sample=None, lam=None, is_log=_Null, out=None, name=None, **kwargs):
    r"""Concurrent sampling from multiple
    Poisson distributions with parameters lambda (rate).

    The parameters of the distributions are provided as an input array.
    Let *[s]* be the shape of the input array, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input array, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input value at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input array.

    Samples will always be returned as a floating point data type.

    Examples::

       lam = [ 1.0, 8.5 ]

       // Draw a single sample for each distribution
       sample_poisson(lam) = [  0.,  13.]

       // Draw a vector containing two samples for each distribution
       sample_poisson(lam, shape=(2)) = [[  0.,   4.],
                                         [ 13.,   8.]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\pdf_op.cc:L307

    Parameters
    ----------
    sample : NDArray
        Samples from the distributions.
    lam : NDArray
        Lambda (rate) parameters of the distributions.
    is_log : boolean, optional, default=0
        If set, compute the density of the log-probability instead of the probability.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def pdf_uniform(sample=None, low=None, high=None, is_log=_Null, out=None, name=None, **kwargs):
    r"""Concurrent sampling from multiple
    uniform distributions on the intervals given by *[low,high)*.

    The parameters of the distributions are provided as input arrays.
    Let *[s]* be the shape of the input arrays, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input arrays, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input values at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input arrays.

    Examples::

       low = [ 0.0, 2.5 ]
       high = [ 1.0, 3.7 ]

       // Draw a single sample for each distribution
       sample_uniform(low, high) = [ 0.40451524,  3.18687344]

       // Draw a vector containing two samples for each distribution
       sample_uniform(low, high, shape=(2)) = [[ 0.40451524,  0.18017688],
                                               [ 3.18687344,  3.68352246]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\pdf_op.cc:L298

    Parameters
    ----------
    sample : NDArray
        Samples from the distributions.
    low : NDArray
        Lower bounds of the distributions.
    is_log : boolean, optional, default=0
        If set, compute the density of the log-probability instead of the probability.
    high : NDArray
        Upper bounds of the distributions.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def poisson(lam=_Null, shape=_Null, ctx=_Null, dtype=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a Poisson distribution.

    Samples are distributed according to a Poisson distribution parametrized by *lambda* (rate).
    Samples will always be returned as a floating point data type.

    Example::

       poisson(lam=4, shape=(2,2)) = [[ 5.,  2.],
                                      [ 4.,  6.]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L150

    Parameters
    ----------
    lam : float, optional, default=1
        Lambda parameter (rate) of the Poisson distribution.
    shape : Shape(tuple), optional, default=None
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def poisson_like(data=None, lam=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a Poisson distribution according to the input array shape.

    Samples are distributed according to a Poisson distribution parametrized by *lambda* (rate).
    Samples will always be returned as a floating point data type.

    Example::

       poisson(lam=4, data=ones(2,2)) = [[ 5.,  2.],
                                         [ 4.,  6.]]


    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L255

    Parameters
    ----------
    lam : float, optional, default=1
        Lambda parameter (rate) of the Poisson distribution.
    data : NDArray
        The input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def randint(low=_Null, high=_Null, shape=_Null, ctx=_Null, dtype=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a discrete uniform distribution.

    Samples are uniformly distributed over the half-open interval *[low, high)*
    (includes *low*, but excludes *high*).

    Example::

       randint(low=0, high=5, shape=(2,2)) = [[ 0,  2],
                                              [ 3,  1]]



    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L194

    Parameters
    ----------
    low : long, required
        Lower bound of the distribution.
    high : long, required
        Upper bound of the distribution.
    shape : Shape(tuple), optional, default=None
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'int32', 'int64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to int32 if not defined (dtype=None).

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def uniform(low=_Null, high=_Null, shape=_Null, ctx=_Null, dtype=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a uniform distribution.

    .. note:: The existing alias ``uniform`` is deprecated.

    Samples are uniformly distributed over the half-open interval *[low, high)*
    (includes *low*, but excludes *high*).

    Example::

       uniform(low=0, high=1, shape=(2,2)) = [[ 0.60276335,  0.85794562],
                                              [ 0.54488319,  0.84725171]]



    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L96

    Parameters
    ----------
    low : float, optional, default=0
        Lower bound of the distribution.
    high : float, optional, default=1
        Upper bound of the distribution.
    shape : Shape(tuple), optional, default=None
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def uniform_like(data=None, low=_Null, high=_Null, out=None, name=None, **kwargs):
    r"""Draw random samples from a uniform distribution according to the input array shape.

    Samples are uniformly distributed over the half-open interval *[low, high)*
    (includes *low*, but excludes *high*).

    Example::

       uniform(low=0, high=1, data=ones(2,2)) = [[ 0.60276335,  0.85794562],
                                                 [ 0.54488319,  0.84725171]]



    Defined in C:\Jenkins\workspace\mxnet-tag\mxnet\src\operator\random\sample_op.cc:L209

    Parameters
    ----------
    low : float, optional, default=0
        Lower bound of the distribution.
    high : float, optional, default=1
        Upper bound of the distribution.
    data : NDArray
        The input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

__all__ = ['exponential', 'exponential_like', 'gamma', 'gamma_like', 'generalized_negative_binomial', 'generalized_negative_binomial_like', 'negative_binomial', 'negative_binomial_like', 'normal', 'normal_like', 'pdf_dirichlet', 'pdf_exponential', 'pdf_gamma', 'pdf_generalized_negative_binomial', 'pdf_negative_binomial', 'pdf_normal', 'pdf_poisson', 'pdf_uniform', 'poisson', 'poisson_like', 'randint', 'uniform', 'uniform_like']
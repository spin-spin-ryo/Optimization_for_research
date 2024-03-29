from jax import random
import jax.numpy as jnp
from jax import config
config.update("jax_enable_x64", True)
key = random.PRNGKey(0)
DATAPATH = "./data"
RESULTPATH = "./results"
DTYPE = jnp.float64

# 目的関数一覧
QUADRATIC = "Quadratic"
SPARSEQUADRATIC = "SparseQuadratic"
MATRIXFACTORIZATION = "MatrixFactorization"
MATRIXFACTORIZATION_COMPLETION = "MatrixFactorization_Completions"
LEASTSQUARE = "LeastSquare"
MLPNET = "MLPNET"
CNN = "CNN"
SOFTMAX = "Softmax"
LOGISTIC = "Logistic"
SPARSEGAUSSIANPROCESS = "SparseGaussianProcess"
REGULARIZED = "Regularized"

# 制約一覧
POLYTOPE = "Polytope"
NONNEGATIVE = "NonNegative"
FUSEDLASSO = "FusedLasso"
BALL = "Ball"
HUBER = "Huber"
NOCONSTRAINTS = "NoConstraint"

# アルゴリズム手法一覧
GRADIENT_DESCENT = "GD"
SUBSPACE_GRADIENT_DESCENT = "SGD"
ACCELERATED_GRADIENT_DESCENT = "AGD"
NEWTON = "Newton"
SUBSPACE_NEWTON = "RSNewton"
LIMITED_MEMORY_NEWTON = "LMN"
LIMITED_MEMORY_BFGS = "LM_BFGS"
BFGS_QUASI_NEWTON = "bfgs"
RANDOM_BFGS = "Randomized_bfgs"
SUBSPACE_REGULARIZED_NEWTON = "RSRNM" 
SUBSPACE_QUASI_NEWTON = "Proposed"
PROXIMAL_GRADIENT_DESCENT = "PGD"
ACCELERATED_PROXIMAL_GRADIENT_DESCENT = "APGD"
MARUMO_AGD = "AGD(2022)"
GRADIENT_PROJECTION = "GPD"
DYNAMIC_BARRIER = "Dynamic"
PRIMALDUAL = "PrimalDual"
RSG_LC = "proposed_linear"
RSG_NC = "proposed_nonlinear"
RGF = "RGF"
RSRGF = "proposed_zeroth"

# ディレクトリ名の形式 
# results/{objectives}/{param}@{value}~{param}@{value}~..../{constraints}/{param}@{value}~{param}@{value}~..../{solver_name}/{param}@{value}~{param}@{value}

DISTINCT_PARAM_VALUE = "@"
DISTINCT_PARAMS = "~"

# 勾配計算の仕方
DIRECTIONALDERIVATIVE = "DD"
FINITEDIFFERENCE = "FD"

# スケッチ行列の決め方
RANDOM = "random"
LEESELECTION = "Lee"

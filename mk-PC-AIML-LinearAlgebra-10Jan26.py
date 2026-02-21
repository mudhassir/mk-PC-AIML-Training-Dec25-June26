# Linear Algebra Module for AIML
# This module contains functions for basic linear algebra operations
# such as vector addition, scalar multiplication, matrix multiplication, etc.

# Very frequently used terminology in Linear Algebra:
# Ecludian Distance: Measure of the true straight line distance between two points in Euclidean space.
# Manhattan Distance: Measure of distance between two points in a grid-based system (like city blocks).
# Dot Product: Algebraic operation that takes two equal-length sequences of numbers and returns a single number.
# Cross Product: A binary operation on two vectors in three-dimensional space producing a vector perpendicular to both.
# Norm: A function that assigns a strictly positive length or size to all vectors in a vector space.
# Cosine Similarity: A measure of similarity between two non-zero vectors of an inner product space.


import numpy as np
def vector_addition(v1, v2):
    """Adds two vectors."""
    return np.add(v1, v2)


def scalar_multiplication(scalar, vector):
    """Multiplies a vector by a scalar."""
    return np.multiply(scalar, vector)

print("\n")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Vector Addition of a and b:", vector_addition(a, b))
scalar = 3
print("Scalar Multiplication of a with", scalar, ":", scalar_multiplication(scalar, a))
dot_product = np.dot(a, b)
print("Dot Product of a and b:", dot_product)
norm_a = np.linalg.norm(a)
print("Norm of vector a:", norm_a)
norm_b = np.linalg.norm(b)
print("Norm of vector b:", norm_b)
cross_product = np.cross(a, b)
print("Cross Product of a and b:", cross_product)
cos_theta = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print("Cosine of the angle between a and b:", cos_theta)

# Cosine similarity
import numpy as np
def cosine_similarity(v1, v2):
    """Calculates the cosine similarity between two vectors."""
    v2_trans = np.transpose(v2)
    dot_prod = np.dot(v1, v2_trans)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_prod / (norm_v1 * norm_v2)
a1 = np.array([[1, 2, 3, 4]])
a2 = np.array([[4, 5, 6, 7]])
cos_similarity = cosine_similarity(a1, a2)
print("\nCosine Similarity between a1 and a2:", cos_similarity[0][0])
manhattan_distance = np.sum(np.abs(a - b))
print("Manhattan Distance between a and b:", manhattan_distance)
euclidean_distance = np.linalg.norm(a - b)
print("Euclidean Distance between a and b:", euclidean_distance)

# Revising on 25-Jan-26
print ("\n===== Revising Linear Algebra Concepts: on 25-Jan-26 ======")
import numpy as np
customer = np.array([25, 50000, 80]) # Age, Income, Spending Score
product = np.array([30, 60000, 70])  # Age, Income, Spending Score
print (customer)
print (product)
print (customer.shape)

# Matrix addition and subtraction
matrix_A = np.array([[1, 2, 3], [4, 5, 6]])
matrix_B = np.array([[7, 8, 9], [10, 11, 12]])
matrix_add = np.add(matrix_A, matrix_B)
matrix_sub = np.subtract(matrix_A, matrix_B)
print ("\nMatrix A:\n", matrix_A)
print ("Matrix B:\n", matrix_B)
print ("Matrix Addition (A + B):\n", matrix_add)
print ("Matrix Subtraction (A - B):\n", matrix_sub)
print ("Matrix Addition traditional way: A+B =\n", matrix_A + matrix_B)
print ("Matrix Subtraction traditional way: A-B =\n", matrix_A - matrix_B)

# Dot product and Cross product
A = np.array ([[1, 2], [3, 4]])
B = np.array ([[5, 6], [7, 8]])
dot_product = np.dot(A, B)
cross_product = np.cross(A, B)
print ("\nMatrix A:\n", A)
print ("Matrix B:\n", B)
print ("Dot Product of A and B:\n", dot_product)
print ("Cross Product of A and B:\n", cross_product)

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
l1_norm_a = np.linalg.norm(a, ord=1)
l2_norm_a = np.linalg.norm(a, ord=2)
l1_norm_b = np.linalg.norm(b, ord=1)
l2_norm_b = np.linalg.norm(b, ord=2)
print ("\nVector a:", a)
print ("L1 Norm of a:", l1_norm_a)
print ("L2 Norm of a:", l2_norm_a)
print ("Vector b:", b)
print ("L1 Norm of b:", l1_norm_b)
print ("L2 Norm of b:", l2_norm_b)

# Cosine Similarity
def cosine_similarity(v1, v2):
    """Calculates the cosine similarity between two vectors."""
    dot_prod = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_prod / (norm_v1 * norm_v2)
a1 = np.array([1, 2, 3, 4])
a2 = np.array([4, 5, 6, 7])
cos_similarity = cosine_similarity(a1, a2)
print ("\nCosine Similarity between a1 and a2:", cos_similarity)
manhattan_distance = np.sum(np.abs(a - b))
print ("Manhattan Distance between a and b:", manhattan_distance)
euclidean_distance = np.linalg.norm(a - b)
print ("Euclidean Distance between a and b:", euclidean_distance)
print ("\n===== End of Revising Linear Algebra Concepts ======")

# sklearn for Linear Algebra
'''
from sklearn.preprocessing import StandardScalar, cosine_similarity
x = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
scaler = StandardScalar()
x_scaled = scaler.fit_transform(x)
print ("\nOriginal Data:\n", x)
print ("Standard Scaled Data:\n", x_scaled)
cos_sim = cosine_similarity(x)
print ("Cosine Similarity Matrix:\n", cos_sim)
'''

import pandas as pd
from sklearn.decomposition import PCA
# sample housing data
data = {
    'Bedrooms': [2, 3, 4, 3, 5],
    'Bathrooms': [1, 2, 3, 2, 4],
    'SquareFeet': [800, 1200, 1500, 1300, 2000],
    'Price': [150000, 250000, 350000, 300000, 450000]
}
df = pd.DataFrame(data)
print ("\nOriginal Data:\n", df)

def find_eigenvalues(matrix):
    # Extract matrix elements
    a, b, c, d = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]
    # Calculate the characteristic polynomial coefficients
    trace = a + d
    determinant = a * d - b * c
    # Calculate the eigenvalues using the quadratic formula
    discriminant = trace**2 - 4 * determinant
    eigenvalue1 = (trace + np.sqrt(discriminant)) / 2
    eigenvalue2 = (trace - np.sqrt(discriminant)) / 2
    return eigenvalue1, eigenvalue2

def find_eigenvectors(matrix, eigenvalues):
    eigenvectors = []
    for eigenvalue in eigenvalues:
        a, b, c, d = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]
        vec_matrix = np.array([[a - eigenvalue, b], [c, d - eigenvalue]])
        if vec_matrix[0, 0] != 0:
            eigenvector = np.array([-vec_matrix[0, 1] / vec_matrix[0, 0], 1])
        else:
            eigenvector = np.array([1, -vec_matrix[1, 0] / vec_matrix[1, 1]])
        eigenvectors.append(eigenvector)
    return eigenvectors

import statistics as stats
data = [10, 20, 30, 40, 50]
mean_data = stats.mean(data)
print ("\nMean of data:", mean_data)
median_data = stats.median(data)
print ("Median of data:", median_data)
mode_data = stats.mode(data)
print ("Mode of data:", mode_data)
variance_data = stats.variance(data)
print ("Variance of data:", variance_data)
stdev_data = stats.stdev(data)
print ("Standard Deviation of data:", stdev_data)

import numpy as np
# player A
scores_A = np.array([10, 20, 30, 40, 50])
freq_A = np.array([1, 2, 4, 2, 1])
data_A = np.repeat(scores_A, freq_A)
scores_B = np.array([15, 25, 35, 45, 55])
freq_B = np.array([2, 3, 2, 2, 1])
data_B = np.repeat(scores_B, freq_B)
mean_A = np.mean(data_A)
median_A = np.median(data_A)
mean_B = np.mean(data_B)
median_B = np.median(data_B)
print ("\nPlayer A Scores Data:", data_A)
print ("Mean of Player A Scores:", mean_A)
print ("Median of Player A Scores:", median_A)
print ("Player B Scores Data:", data_B)
print ("Mean of Player B Scores:", mean_B)
print ("Median of Player B Scores:", median_B)

import numpy as np
from statsmodels.stats.stattools import medcouple
from statsmodels.stats.stattools import robust_skewness
x = np.array([10, 20, 30, 40, 50])
sk = robust_skewness(x)
print ("\nRobust Skewness of x:", sk)
mc = medcouple(x)
print ("\nMedcouple of x:", mc)

# robust kurtosis
from statsmodels.stats.stattools import robust_kurtosis
x = np.array([10, 20, 30, 40, 50])
rk = robust_kurtosis(x)
print ("\nRobust Kurtosis of x:", rk)

# Covariance and Correlation
import pandas as pd
import numpy as np
x = np.array([10, 20, 30, 40, 50])
y = np.array([15, 25, 35, 45, 55])
cov_xy = np.cov(x, y)[0, 1]
corr_xy = np.corrcoef(x, y)[0, 1]
print ("\nCovariance between x and y:", cov_xy)
print ("Correlation between x and y:", corr_xy)

data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [5, 4, 3, 2, 1],
    'Feature3': [2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)
print ("\nDataFrame:\n", df)
cov_matrix = df.cov()
corr_matrix = df.corr()
print ("\nCovariance Matrix:\n", cov_matrix)
print ("\nCorrelation Matrix:\n", corr_matrix)

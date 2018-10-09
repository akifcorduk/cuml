 # Copyright (c) 2018, NVIDIA CORPORATION.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #

from cuML import TruncatedSVD
import pygdf
import numpy as np

print("\n***********TESTING FOR FLOAT DATATYPE***********")

gdf_float = pygdf.DataFrame()
gdf_float['0']=np.asarray([1.0,2.0,5.0],dtype=np.float32)
gdf_float['1']=np.asarray([4.0,2.0,1.0],dtype=np.float32)
gdf_float['2']=np.asarray([4.0,2.0,1.0],dtype=np.float32)

print("\ninput:")
print(gdf_float)

print("Calling fit")
tsvd_float = TruncatedSVD(n_components = 2, algorithm="jacobi", n_iter=20, tol=1e-9)
tsvd_float.fit(gdf_float)

print("\ncomponents:")
print(tsvd_float.components_)
print("\nexplained variance:")
print(tsvd_float.explained_variance_)
print("\nexplained variance ratio:")
print(tsvd_float.explained_variance_ratio_)
print("\nsingular values:")
print(tsvd_float.singular_values_)

print("Calling transform")
trans_gdf_float = tsvd_float.transform(gdf_float)

print("\nTransformed matrix")
print(trans_gdf_float)
print("\nCalling inverse_transform")
print("\nInput Matrix:")
input_gdf_float = tsvd_float.inverse_transform(trans_gdf_float)
print(input_gdf_float)
 
print("\n***********TESTING FOR DOUBLE DATATYPE***********")

gdf_double = pygdf.DataFrame()
gdf_double['0']=np.asarray([1.0,2.0,5.0],dtype=np.float64)
gdf_double['1']=np.asarray([4.0,2.0,1.0],dtype=np.float64)
gdf_double['2']=np.asarray([4.0,2.0,1.0],dtype=np.float64)

print("\ninput:")
print(gdf_double)

print("Calling fit_transform")
tsvd_double = TruncatedSVD(n_components = 2)
trans_gdf_double = tsvd_double.fit_transform(gdf_double)
print(trans_gdf_double)

print("\ncomponents:")
print(tsvd_double.components_)
print("\nexplained variance:")
print(tsvd_double.explained_variance_)
print("\nexplained variance ratio:")
print(tsvd_double.explained_variance_ratio_)
print("\nsingular values:")
print(tsvd_double.singular_values_)

print("\nTransformed matrix")
print(trans_gdf_double)
print("\nCalling inverse_transform")
print("\nInput Matrix:")
input_gdf_double = tsvd_double.inverse_transform(trans_gdf_double)

print(input_gdf_double)

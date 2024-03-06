#! Flow Proccess
# 1. Load the classification data into two arrays: one for the personality and one for the sexuality.
# 2. Especify the root directory with the data to be classified.
# 3. Especify the destination directory for each category for the classified data.
# 4. Clasify the data into the specified categories.
## 4.1. For each file in the root directory, take the name of the file and compare it with the personality array.
## 4.2. If the name of the file contains a word from the personality array, move the file to the corresponding category directory.
# 5. Repeat the process for the sexuality array. 

# Import the necessary libraries.
import os
import shutil
import re
import pandas as pd

# Load the classification data into two arrays: one for the personality and one for the sexuality with de img_code
#Read from the excel file
df = pd.read_csv('Label_Data.csv', sep=';')
#get the column img_code
img_code = df['img_code'].to_list()
personality = df['Personality'].to_list()
sexuality = df['Sexuality'].to_list()
#Join to dict for reference the clasification
img_personality = dict(zip(img_code, personality))
img_sexuality = dict(zip(img_code, sexuality))

# Especify the root directory with the data to be classified.
root_directory = r'C:\Users\vinic\Documents\Classify_signatures\Classify_docs_Google_Drive\Signatures'
# Especify the destination directory for each category for the classified data.
p_nervioso_path = 'G:\\Mi unidad\\Personality\\Nervioso'
p_sanguineo_path= 'G:\\Mi unidad\\Personality\\Sanguineo'
p_bilioso_path= 'G:\\Mi unidad\\Personality\\Bilioso'
p_linfatico_path= 'G:\\Mi unidad\\Personality\\Linfatico'



# # Iterar sobre las claves del diccionario img_personality
# for img_code, personality in img_personality.items():
#     # Construir el nombre de archivo con la extensión .jpg
#     file_name = img_code + '.jpg'
    
#     # Verificar si el archivo existe en el directorio raíz
#     if file_name in os.listdir(root_directory):
#         print(f"Archivo encontrado para img_code '{img_code}': {file_name}")
#         # como el archivo existe en el directorio raíz, se procede a moverlo a la carpeta correspondiente
#         if personality == 'Nervioso':
#             print(f"Clasificando '{file_name}' en la carpeta '{p_nervioso_path}'")
#             # Mover el archivo a la carpeta correspondiente
#             shutil.move(os.path.join(root_directory, file_name), os.path.join(p_nervioso_path, file_name))
#         elif personality == 'Sanguineo':
#             print(f"Clasificando '{file_name}' en la carpeta '{p_sanguineo_path}'")
#             # Mover el archivo a la carpeta correspondiente
#             shutil.move(os.path.join(root_directory, file_name), os.path.join(p_sanguineo_path, file_name))
#         elif personality == 'Bilioso':
#             print(f"Clasificando '{file_name}' en la carpeta '{p_bilioso_path}'")
#             # Mover el archivo a la carpeta correspondiente
#             shutil.move(os.path.join(root_directory, file_name), os.path.join(p_bilioso_path, file_name))
#         elif personality == 'Linfatico':
#             print(f"Clasificando '{file_name}' en la carpeta '{p_linfatico_path}'")
#             # Mover el archivo a la carpeta correspondiente
#             shutil.move(os.path.join(root_directory, file_name), os.path.join(p_linfatico_path, file_name))
#     else:
#         print(f"Archivo no encontrado para img_code '{img_code}': {file_name}")

#Destiny for sexuality folders
s_emotivo= 'G:\\Mi unidad\\Sexuality\\Emotivo'
s_racional= 'G:\\Mi unidad\\Sexuality\\Racional'
s_instintivo= 'G:\\Mi unidad\\Sexuality\\Instintivo' 


for img_code , sexuality in img_sexuality.items():
    # Construir el nombre de archivo con la extensión .jpg
    file_name = img_code + '.jpg'
    
    # Verificar si el archivo existe en el directorio raíz
    if file_name in os.listdir(root_directory):
        print(f"Archivo encontrado para img_code '{img_code}': {file_name}")
        # como el archivo existe en el directorio raíz, se procede a moverlo a la carpeta correspondiente
        if sexuality == 'Emotivo':
            print(f"Clasificando '{file_name}' en la carpeta '{s_emotivo}'")
            # Mover el archivo a la carpeta correspondiente
            shutil.move(os.path.join(root_directory, file_name), os.path.join(s_emotivo, file_name))
        elif sexuality == 'Racional':
            print(f"Clasificando '{file_name}' en la carpeta '{s_racional}'")
            # Mover el archivo a la carpeta correspondiente
            shutil.move(os.path.join(root_directory, file_name), os.path.join(s_racional, file_name))
        elif sexuality == 'Instintivo':
            print(f"Clasificando '{file_name}' en la carpeta '{s_instintivo}'")
            # Mover el archivo a la carpeta correspondiente
            shutil.move(os.path.join(root_directory, file_name), os.path.join(s_instintivo, file_name))
    else:
        print(f"Archivo no encontrado para img_code '{img_code}': {file_name}")


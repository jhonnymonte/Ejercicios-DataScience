#%%
import pandas as pd
import os
import seaborn as sns


directorio = '../Data'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
fname_veredas = os.path.join(directorio,archivo_veredas)
df_veredas = pd.read_csv(fname_veredas)

directorio = '../Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
fname_parques = os.path.join(directorio,archivo_parques)
df_parques = pd.read_csv(fname_parques)
# busco la indo que necesito
#df_parques.columns
#set(df_parques['nombre_cie'])
df_tipas_parques=(df_parques[['altura_tot','diametro']])
[df_parques['nombre_cie']== 'Tipuana Tipu'].copy
# busco la indo que necesito
#df_veredas.columns
#set(df_veredas['nombre_cie'])

df_tipas_veredas=(df_veredas[['altura_arbol','diametro_altura_pecho']])
[df_veredas['nombre_cientifico']== 'Tipuana tipu'].copy

#renombro los valores de las colummnas
df_tipas_parques.rename(columns={'altura_tot':'altura'},inplace=True)
df_tipas_veredas.rename(columns={'altura_arbol':'altura','diametro_altura_pecho':'diametro'},inplace=True)
#agrego columna ambiente

df_tipas_parques['ambiente']='parque'
df_tipas_veredas['ambiente']='vereda'
#concateno los dataset
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro',by = 'ambiente')

df_tipas.boxplot('altura',by = 'ambiente')

df_tipas.boxplot(by = 'ambiente')

# %%

def boxplot_por_especie(especie1,especie2):
    df_especie_veredas=(df_veredas[['altura_arbol','diametro_altura_pecho']])
[df_veredas['nombre_cientifico']== especie1].copy
    


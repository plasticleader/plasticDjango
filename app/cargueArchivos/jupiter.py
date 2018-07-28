
# coding: utf-8

# In[1]:


from configparser import ConfigParser
import psycopg2
from config import config
import pandas as pd


# In[2]:


conn = None
vendor_id = None
try:
    # read database configuration
    params = config()
    # connect to the PostgreSQL database
    conn = psycopg2.connect(**params)
    # create a new cursor
except (Exception, psycopg2.DatabaseError) as error:
    print(error)


# In[3]:


asignacionid = 1
archivo = "upload-files/TDC VNTO 5 (1-30) - INTELIBPO.xlsx"


# In[6]:


df = pd.read_excel(archivo)
df = df[['num_documento','NOMBRE', 'Tipo_documento','fecha_apertura','fechaasigna','saldo_total','cupo','dias_mora','Rango','habito_pago','cuenta','TlfCelular','teldom1','TelefCom1','Calle_Corresp','Depto_Correspondencia','Ciudad_Correspondencia','barrio','Calle_Com','Depto_Com','Ciudad_Com','Mail']]
df = df.head(20)
print(df)


# In[7]:


cant_columns = len(df.columns)
cant_cc = df['num_documento'].count()
columns_obli = list(df.columns.values)
sum_saldo_capital = round(df['saldo_total'].sum(),2)
df.head(3)


# ### Cargue de Personas

# In[6]:


df_personas = df.copy()


# In[7]:


df_personas.drop_duplicates(subset=["num_documento","Tipo_documento"], keep='first', inplace=True)


# In[8]:


tipoDoc = {1:"CC", 3:"CE"}
df_personas["Tipo_documento"]=df_personas["Tipo_documento"].map(tipoDoc)
df_personas.head()


# In[9]:


df_personas.rename(columns={"num_documento":"persona_identificacion",
                                 "NOMBRE":"persona_nombre",
                                 "Tipo_documento":"persona_tipoidentificacion"},inplace=True)
df_personas.head()


# In[10]:


sql = """INSERT INTO strauss_asignacion.data_persona(persona_asignacion_id, persona_identificacion, persona_nombre, persona_tipoidentificacion)
             VALUES(%s,%s,%s,%s) RETURNING persona_id;"""

def insertPersona(row):
    try:
        cur = conn.cursor()
        cur.execute(sql,(str(asignacionid), row['persona_identificacion'],row['persona_nombre'],row['persona_tipoidentificacion']))
        persona_id = cur.fetchone()[0]
        conn.commit()
        row['persona_id'] = persona_id
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return row


# In[11]:


df_person = pd.DataFrame()
for index, row in df_personas.iterrows():
    df_person = df_person.append(insertPersona(row))
df_personas = df_person
df_personas.head()


# ### Cargue Obligaciones

# In[12]:


sql = """INSERT INTO strauss_asignacion.data_obligaciones(obligacion_fechacreacionobligacion,obligacion_fecha_vencimientoobligacion,
             obligacion_saldocapital,obligacion_saldointerescorriente,obligacion_saldointeresmora,obligacion_saldototal,obligacion_variable1,
             obligacion_variable1_descripcion,obligacion_variable2,obligacion_variable2_descripcion,obligacion_variable3,obligacion_variable3_descripcion,
             obligacion_variable4,obligacion_variable4_descripcion,obligacion_persona,obligacion_tipoobligacion,obligacion_producto,obligacion_tipo_producto)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
def insertobligaciones(row):
    try:
        cur = conn.cursor()
        cur.execute(sql,(row['fechacreacionobligacion'],row['fecha_vencimientoobligacion'],row['saldototal'],row['saldointerescorriente'],row['saldointeresmora'],row['saldototal'],row['variable1'],row['variable1_descripcion'],row['variable2'],row['variable2_descripcion'],row['variable3'],row['variable3_descripcion'],row['variable4'],row['variable4_descripcion'],row['persona_id'],row['tipoobligacion'],row['cuenta'],row['tipo_producto']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return row


# In[13]:


df_obligaciones = df[['num_documento','fecha_apertura','fechaasigna','saldo_total','cupo','dias_mora','Rango','habito_pago','cuenta']].copy()
df_obligaciones['persona_id'] = df_obligaciones['num_documento'].map(df_personas.set_index('persona_identificacion')['persona_id'])
df_obligaciones['saldointerescorriente'] = 0
df_obligaciones['saldointeresmora'] = 0
df_obligaciones['tipoobligacion'] = 'Administrativa'
df_obligaciones['tipo_producto'] = 'Tarjeta Credito'
df_obligaciones['variable1_descripcion'] = 'cupo tarjeta credito'
df_obligaciones['variable2_descripcion'] = 'dias de mora'
df_obligaciones['variable3_descripcion'] = 'etapa de mora'
df_obligaciones['variable4_descripcion'] = 'frecuencia de pago'
df_obligaciones = df_obligaciones.drop(['num_documento'],axis=1)
df_obligaciones = df_obligaciones.rename(columns={'fecha_apertura':'fechacreacionobligacion','fechaasigna':'fecha_vencimientoobligacion','saldo_total':'saldototal'})
df_obligaciones = df_obligaciones.rename(columns={'cupo':'variable1','dias_mora':'variable2','Rango':'variable3','habito_pago':'variable4'})
df_obligaciones['fechacreacionobligacion'] = df_obligaciones['fechacreacionobligacion'].apply(lambda x: str(x)[0:4]+"-"+str(x)[4:6]+"-"+str(x)[6:])
df_obligaciones.head()


# In[14]:


df_obligacion = pd.DataFrame()
for index, row in df_obligaciones.iterrows():
    df_obligacion = df_obligacion.append(insertobligaciones(row))
df_obligaciones = df_obligacion
df_obligaciones.head()


# ### Cargue Telefonos

# In[15]:


sql = """INSERT INTO strauss_asignacion.data_telefonos(telefono_numero,telefono_persona_id)
             VALUES(%s,%s);"""
def inserttelefonos(row):
    try:
        cur = conn.cursor()
        cur.execute(sql,(int(row['numero']),row['persona_id']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return row


# In[16]:


df_telefonos = df[['num_documento','TlfCelular','teldom1','TelefCom1']].copy()
df_telefonos['persona_id'] = df_telefonos['num_documento'].map(df_personas.set_index('persona_identificacion')['persona_id'])
df_telefonos = df_telefonos.drop(['num_documento'],axis=1)
df_telefonos = df_telefonos.melt(id_vars=['persona_id'])
df_telefonos = df_telefonos.rename(columns={'value':'numero'}).drop(['variable'],axis=1).sort_values('persona_id')
df_telefonos.head()


# In[17]:


df_telefono = pd.DataFrame()
for index, row in df_telefonos.iterrows():
    df_telefono = df_telefono.append(inserttelefonos(row))
df_telefonos = df_telefono
df_telefonos.head()


# ### Cargue Ubicacion

# In[18]:


sql = """INSERT INTO strauss_asignacion.data_ubicacion(ubicacion_direccion,ubicacion_pais,ubicacion_departamento,
             ubicacion_ciudad,ubicacion_barrio,ubicacion_persona_id)
             VALUES(%s,%s,%s,%s,%s,%s);"""
def insertubicaciones(row):
    try:
        cur = conn.cursor()
        cur.execute(sql,(row['Calle_Corresp'],row['pais'],row['Depto_Correspondencia'],row['Ciudad_Correspondencia'],row['barrio'],row['persona_id']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return row


# In[19]:


df_ubicaciones = df[['num_documento','Calle_Corresp','Depto_Correspondencia','Ciudad_Correspondencia','barrio']].copy()
df_ubicaciones['persona_id'] = df_ubicaciones['num_documento'].map(df_personas.set_index('persona_identificacion')['persona_id'])
df_ubicaciones['pais'] = 'Colombia'
df_ubicaciones = df_ubicaciones.drop(['num_documento'],axis=1)
df_ubicaciones.head()


# In[20]:


df_ubicacion = pd.DataFrame()
for index, row in df_ubicaciones.iterrows():
    df_ubicacion = df_ubicacion.append(insertubicaciones(row))
df_ubicaciones = df_ubicacion
df_ubicaciones.head()


# ### Cargue Ubicacion Empresa

# In[21]:


sql = """INSERT INTO strauss_asignacion.data_ubicacion_empresa(empresa_direccion,empresa_pais,empresa_departamento,
             empresa_ciudad,empresa_persona_id)
             VALUES(%s,%s,%s,%s,%s);"""
def insertubicaciones_empresas(row):
    try:
        cur = conn.cursor()
        cur.execute(sql,(row['Calle_Com'],row['pais'],row['Depto_Com'],row['Ciudad_Com'],row['persona_id']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return row


# In[22]:


df_ubicaciones_empresas = df[['num_documento','Calle_Com','Depto_Com','Ciudad_Com']].copy()
df_ubicaciones_empresas['persona_id'] = df_ubicaciones_empresas['num_documento'].map(df_personas.set_index('persona_identificacion')['persona_id'])
df_ubicaciones_empresas['pais'] = 'Colombia'
df_ubicaciones_empresas = df_ubicaciones_empresas.drop(['num_documento'],axis=1)
df_ubicaciones_empresas.head()


# In[23]:


df_ubicacion_empresa = pd.DataFrame()
for index, row in df_ubicaciones_empresas.iterrows():
    df_ubicacion_empresa = df_ubicacion_empresa.append(insertubicaciones_empresas(row))
df_ubicaciones_empresas = df_ubicacion_empresa
df_ubicaciones_empresas.head()


# ### Cargue Correo Electronico

# In[24]:


sql = """INSERT INTO strauss_asignacion.data_correoelectronico(correoelectronico_correo,correoelectronico_persona_id)
             VALUES(%s,%s);"""
def insertcorreoelectronico(row):
    try:
        cur = conn.cursor()
        cur.execute(sql,(row['Mail'],row['persona_id']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return row


# In[25]:


df_correoelectronico = df[['num_documento','Mail']].copy()
df_correoelectronico['persona_id'] = df_correoelectronico['num_documento'].map(df_personas.set_index('persona_identificacion')['persona_id'])
df_correoelectronico['pais'] = 'Colombia'
df_correoelectronico = df_correoelectronico.drop(['num_documento'],axis=1)
df_correoelectronico.head()


# In[26]:


df_correo = pd.DataFrame()
for index, row in df_correoelectronico.iterrows():
    df_correo = df_correo.append(insertcorreoelectronico(row))
df_correoelectronico = df_correo
df_correoelectronico.head()



# coding: utf-8

# # Aula 4 - Exercícios

# # Exercício

# ### Faça uma pesquisa simples na coleção Vocabulary pelo termo “feliz” no campo text e diga:

# In[2]:

get_ipython().run_cell_magic('bash', '', '\nmongo\n\nuse nosqlclass\n\ndb.Vocabulary.find({"text":"feliz",}).explain({"executionStats":1})')


# ### A) Número de documentos que foi escaneado:
# 
# ### "totalDocsExamined" : 291214

# ### B) Tempo que levou para fazer a consulta
# 
# ### "executionTimeMillis" : 148

# ### C) Crie um índice simples no campo text

# In[3]:

get_ipython().run_cell_magic('bash', '', '\nmongo\n\nuse nosqlclass\n\ndb.Vocabulary.createIndex({"text":1})')


# In[4]:

get_ipython().run_cell_magic('bash', '', '\nmongo\n\nuse nosqlclass\n\ndb.Vocabulary.find({"text":"feliz",}).explain({"executionStats":1})')


# ### D) Número de documentos que foi escaneado
# 
# ### "docsExamined" : 1

# ### E) Tempo que levou para fazer a consulta
# 
# ### executionTimeMillis" : 0

# In[ ]:




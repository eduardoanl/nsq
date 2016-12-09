
# coding: utf-8

# # Aula 3 - Exercícios

# # Exercício 1

# ### Na coleção Vocabulary
# 
# ### A) Utilizando as funções de mapReduce do mongo, conte o número de palavras que terminam em ar, er, ir, or, ur.

# In[6]:

get_ipython().run_cell_magic('bash', '', '\nmongo\n\nuse nosqlclass\n\nvar map = function(){\n    emit(this.text[-2],1);\n}\nvar reduce = function(key, value){\n    return Array.sum(value);\n}\ndb.Vocabulary.mapReduce(map, reduce, {query: {text: /.*[a, e, i]r$/}, out: "Resultado"})')


# ### B) Utilizando as funções de mapReduce do mongo, conte o total de cada caracter existente no vocabulario. Por exemplo: aula -> a:2, u:1, l:1

# In[8]:

get_ipython().run_cell_magic('bash', '', '\nmongo\n\nuse nosqlclass\n\nvar map = function(){\n    if (this.text == undefined) return;\n    for (var letra = 0; letra < this.text.length; letra++){\n          emit(this.text[letra], 1);\n    }\n}\nvar reduce = function(key, value){\n    return Array.sum(value);\n}\ndb.Vocabulary.mapReduce(map, reduce, {query:{}, out:"Resultado"})')


# ## Exercício 2

# ### Utilizando a função de agregação contar quantos itens cujo o campo total seja maior do que 1000, agrupando-os por tipo, (campo type) e exiba o resultado em ordem crescente.

# In[9]:

get_ipython().run_cell_magic('bash', '', '\nmongo\n\nuse nosqlclass\n\ndb.Vocabulary.aggregate([\n     { $group: {\n            _id:{\n                    type:{type:"$type"},\n                },\n                    total:{$sum:1}\n                } },\n     { $sort: {\'total\': 1} },\n  ])')


# In[ ]:




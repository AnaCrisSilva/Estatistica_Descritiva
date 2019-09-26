
# coding: utf-8

# ***
# # <font color=green size=10>CURSO DE ESTATÍSTICA - PARTE 1</font>
# ***
# 
# ## Trabalho de Análise Descritiva de um Conjunto de Dados
# 
# Utilizando os conhecimentos adquiridos em nosso treinamento realize uma análise descritiva básica de um conjunto de dados retirados da Pesquisa Nacional por Amostra de Domicílios - 2015 do IBGE. 
# 
# Vamos construir histogramas, calcular e avaliar medidas de tendência central, medidas separatrizes e de dispersão dos dados.
# 
# Siga o roteiro proposto e vá completando as células vazias. Procure pensar em mais informações interessantes que podem ser exploradas em nosso dataset.

# # <font color=green>DATASET DO PROJETO</font>
# ***

# ### Pesquisa Nacional por Amostra de Domicílios - 2015
# 
# A <b>Pesquisa Nacional por Amostra de Domicílios - PNAD</b> investiga anualmente, de forma permanente, características gerais da população, de educação, trabalho, rendimento e habitação e outras, com periodicidade variável, de acordo com as necessidades de informação para o país, como as características sobre migração, fecundidade, nupcialidade, saúde, segurança alimentar, entre outros temas. O levantamento dessas estatísticas constitui, ao longo dos 49 anos de realização da pesquisa, um importante instrumento para formulação, validação e avaliação de políticas orientadas para o desenvolvimento socioeconômico e a melhoria das condições de vida no Brasil.

# ### Fonte dos Dados
# 
# https://ww2.ibge.gov.br/home/estatistica/populacao/trabalhoerendimento/pnad2015/microdados.shtm

# ### Variáveis utilizadas
# 
# > ### Renda
# > ***
# 
# Rendimento mensal do trabalho principal para pessoas de 10 anos ou mais de idade.
# 
# > ### Idade
# > ***
# 
# Idade do morador na data de referência em anos.
# 
# > ### Altura (elaboração própria)
# > ***
# 
# Altura do morador em metros.
# 
# > ### UF
# > ***
# 
# |Código|Descrição|
# |---|---|
# |11|Rondônia|
# |12|Acre|
# |13|Amazonas|
# |14|Roraima|
# |15|Pará|
# |16|Amapá|
# |17|Tocantins|
# |21|Maranhão|
# |22|Piauí|
# |23|Ceará|
# |24|Rio Grande do Norte|
# |25|Paraíba|
# |26|Pernambuco|
# |27|Alagoas|
# |28|Sergipe|
# |29|Bahia|
# |31|Minas Gerais|
# |32|Espírito Santo|
# |33|Rio de Janeiro|
# |35|São Paulo|
# |41|Paraná|
# |42|Santa Catarina|
# |43|Rio Grande do Sul|
# |50|Mato Grosso do Sul|
# |51|Mato Grosso|
# |52|Goiás|
# |53|Distrito Federal|
# 
# > ### Sexo	
# > ***
# 
# |Código|Descrição|
# |---|---|
# |0|Masculino|
# |1|Feminino|
# 
# > ### Anos de Estudo
# > ***
# 
# |Código|Descrição|
# |---|---|
# |1|Sem instrução e menos de 1 ano|
# |2|1 ano|
# |3|2 anos|
# |4|3 anos|
# |5|4 anos|
# |6|5 anos|
# |7|6 anos|
# |8|7 anos|
# |9|8 anos|
# |10|9 anos|
# |11|10 anos|
# |12|11 anos|
# |13|12 anos|
# |14|13 anos|
# |15|14 anos|
# |16|15 anos ou mais|
# |17|Não determinados| 
# ||Não aplicável|
# 
# > ### Cor
# > ***
# 
# |Código|Descrição|
# |---|---|
# |0|Indígena|
# |2|Branca|
# |4|Preta|
# |6|Amarela|
# |8|Parda|
# |9|Sem declaração|

# #### <font color='red'>Observação</font>
# ***
# > Os seguintes tratamentos foram realizados nos dados originais:
# > 1. Foram eliminados os registros onde a <b>Renda</b> era inválida (999 999 999 999);
# > 2. Foram eliminados os registros onde a <b>Renda</b> era missing;
# > 3. Foram considerados somente os registros das <b>Pessoas de Referência</b> de cada domicílio (responsável pelo domicílio).

# ***
# ***

# ### Utilize a célula abaixo para importar as biblioteca que precisar para executar as tarefas
# #### <font color='red'>Sugestões: pandas, numpy, seaborn</font>

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().magic('matplotlib inline')


# ### Importe o dataset e armazene o conteúdo em uma DataFrame

# In[2]:


dados = pd.read_csv("dados.csv")


# ### Visualize o conteúdo do DataFrame

# In[3]:


dados.head(3)


# ### Para avaliarmos o comportamento da variável RENDA vamos construir uma tabela de frequências considerando as seguintes classes em salários mínimos (SM)
# #### <font color='blue'>Descreva os pontos mais relevantes que você observa na tabela e no gráfico.</font>
# 
# Classes de renda:
# 
# <b>A</b> ► Acima de 25 SM
# 
# <b>B</b> ► De 15 a 25 SM
# 
# <b>C</b> ► De 5 a 15 SM
# 
# <b>D</b> ► De 2 a 5 SM
# 
# <b>E</b> ► Até 2 SM
# 
# Para construir as classes de renda considere que o salário mínimo na época da pesquisa era de <b>R$ 788,00</b>.
# 
# #### Siga os passos abaixo:

# A ► Acima de 19.700
# 
# B ► De 11.820 a 19.700
# 
# C ► De 3.940 a 11.820
# 
# D ► De 1.576 a 3.940
# 
# E ► Até 1.576

# In[4]:


dados.Renda.min()


# In[5]:


dados.Renda.max()


# ### 1º Definir os intevalos das classes em reais (R$)

# In[6]:


classes = [0, 1576, 3940, 11820, 19700, 200000]


# ### 2º Definir os labels das classes

# In[7]:


labels = ['E', 'D', 'C', 'B', 'A']


# ### 3º Construir a coluna de frequências

# In[8]:


frequencia = pd.value_counts(
  pd.cut(x = dados.Renda,
         bins = classes,
         labels = labels,
         include_lowest = True)
)
frequencia


# ### 4º Construir a coluna de percentuais

# In[9]:


percentual = pd.value_counts(
  pd.cut(x = dados.Renda,
         bins = classes,
         labels = labels,
         include_lowest = True),
  normalize = True
) * 100
percentual


# ### 5º Juntar as colunas de frequência e percentuais e ordenar as linhas de acordo com os labels das classes

# In[10]:


frequencias_percentual = pd.DataFrame(
    {'Frequência': frequencia, 'Porcentagem (%)': percentual}
)
frequencias_percentual 


# ### Construa um gráfico de barras para visualizar as informações da tabela de frequências acima

# In[11]:


frequencias_percentual ['Frequência'].plot.bar(width= 1, color = 'blue', alpha = 0.7, figsize=(12, 6))


# > ### Conclusões
# 
# Há uma concetração grande de pessoas na faixa E e uma muito pequena na faixa A.
# 

# ### Crie um histograma para as variáveis QUANTITATIVAS de nosso dataset
# #### <font color='blue'>Descreva os pontos mais relevantes que você observa nos gráficos (assimetrias e seus tipos, possíveis causas para determinados comportamentos etc.)</font>

# In[12]:


dados.head()


# In[13]:


ax = sns.distplot(dados.Idade)

ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Idade', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax


# In[14]:


ax = sns.distplot(dados['Anos de Estudo'])

ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Anos de Estudo', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax


# In[15]:


ax = sns.distplot(dados.Renda)

ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
ax


# In[16]:


ax = sns.distplot(dados.Altura)

ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax


# > ### Conclusões
# 
# As pessoas possuem idade especialmente em torono dos quarenta anos. E estudaram quase o mesmo. Porém a renda é um disparate de desigual!!

# ### Para a variável RENDA, construa um histograma somente com as informações das pessoas com rendimento até R$ 20.000,00

# In[17]:


ax = sns.distplot(dados.query('Renda < 20000').Renda)
ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Renda até R$ 20000,00', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
ax


# ### Construa uma tabela de frequências e uma com os percentuais do cruzando das variáveis SEXO e COR
# #### <font color='blue'>Avalie o resultado da tabela e escreva suas principais conclusões</font>
# #### <font color='red'>Utilize os dicionários abaixo para renomear as linha e colunas das tabelas de frequências e dos gráficos em nosso projeto</font>

# In[18]:


sexo = {
    0: 'Masculino', 
    1: 'Feminino'
}
cor = {
    0: 'Indígena', 
    2: 'Branca', 
    4: 'Preta', 
    6: 'Amarela', 
    8: 'Parda', 
    9: 'Sem declaração'
}
anos_de_estudo = {
    1: 'Sem instrução e menos de 1 ano', 
    2: '1 ano', 
    3: '2 anos', 
    4: '3 anos', 
    5: '4 anos', 
    6: '5 anos', 
    7: '6 anos', 
    8: '7 anos', 
    9: '8 anos', 
    10: '9 anos', 
    11: '10 anos', 
    12: '11 anos', 
    13: '12 anos', 
    14: '13 anos', 
    15: '14 anos', 
    16: '15 anos ou mais', 
    17: 'Não determinados'
}
uf = {
    11: 'Rondônia', 
    12: 'Acre', 
    13: 'Amazonas', 
    14: 'Roraima', 
    15: 'Pará', 
    16: 'Amapá', 
    17: 'Tocantins', 
    21: 'Maranhão', 
    22: 'Piauí', 
    23: 'Ceará', 
    24: 'Rio Grande do Norte', 
    25: 'Paraíba', 
    26: 'Pernambuco', 
    27: 'Alagoas', 
    28: 'Sergipe', 
    29: 'Bahia', 
    31: 'Minas Gerais', 
    32: 'Espírito Santo', 
    33: 'Rio de Janeiro', 
    35: 'São Paulo', 
    41: 'Paraná', 
    42: 'Santa Catarina', 
    43: 'Rio Grande do Sul', 
    50: 'Mato Grosso do Sul', 
    51: 'Mato Grosso', 
    52: 'Goiás', 
    53: 'Distrito Federal'
}


# In[19]:


frequencia = pd.crosstab(dados.Sexo,
                    dados.Cor)
frequencia.rename(index = sexo, inplace = True)
frequencia.rename(columns = cor, inplace = True)
frequencia


# In[20]:


percentual = pd.crosstab(dados.Sexo,
                    dados.Cor,
                    normalize = True) * 100
percentual.rename(index = sexo, inplace = True)
percentual.rename(columns = cor, inplace = True)
percentual.round(2)


# > ### Conclusões
# 
# Os maiores percentuais são de homens da cor branca e parda. 

# ## Realize, para a variável RENDA, uma análise descritiva com as ferramentas que aprendemos em nosso treinamento

# ### Obtenha a média aritimética

# In[21]:


dados.Renda.mean()


# ### Obtenha a mediana

# In[22]:


dados.Renda.median()


# ### Obtenha a moda

# In[23]:


dados.Renda.mode()[0]


# ### Obtenha o desvio médio absoluto

# In[24]:


dados.Renda.mad()


# ### Obtenha a variância

# In[25]:


dados.Renda.var()


# ### Obtenha o desvio-padrão

# In[26]:


dados.Renda.std()


# ### Obtenha a média, mediana e valor máximo da variável RENDA segundo SEXO e COR
# #### <font color='blue'>Destaque os pontos mais importante que você observa nas tabulações</font>
# #### <font color='red'>O parâmento <i>aggfunc</i> da função <i>crosstab()</i> pode receber uma lista de funções. Exemplo: <i>aggfunc = {'mean', 'median', 'max'}</i></font>

# In[27]:


stats_renda = pd.crosstab(dados.Cor,
                         dados.Sexo,
                         values = dados.Renda,
                         aggfunc = ['mean', 'median', 'max'])
stats_renda.rename(index = cor, inplace = True)
stats_renda.rename(columns = sexo, inplace = True)
stats_renda


# > ### Conclusões
# 
# Para a maior parte das cores a média de renda masculina é maior. A excessão é o indígena.

# ### Obtenha as medidas de dispersão da variável RENDA segundo SEXO e COR
# #### <font color='blue'>Destaque os pontos mais importante que você observa nas tabulações</font>
# #### <font color='red'>O parâmento <i>aggfunc</i> da função <i>crosstab()</i> pode receber uma lista de funções. Exemplo: <i>aggfunc = {'mad', 'var', 'std'}</i></font>

# In[28]:


disp_renda = pd.crosstab(dados.Cor,
                         dados.Sexo,
                         aggfunc = ['mad', 'var', 'std'],
                         values = dados.Renda).round(2)
disp_renda.rename(index = cor, inplace = True)
disp_renda.rename(columns = sexo, inplace = True)
disp_renda


# > ### Conclusões
# 
# Há a confirmação dos dados anteriores. 

# ### Construa um box plot da variável RENDA segundo SEXO e COR
# #### <font color='blue'>É possível verificar algum comportamento diferenciado no rendimento entre os grupos de pessoas analisados? Avalie o gráfico e destaque os pontos mais importantes.</font>
# #### <font color='red'>1º - Utilize somente as informações de pessoas com renda abaixo de R$ 10.000</font>
# #### <font color='red'>2º - Para incluir uma terceira variável na construção de um boxplot utilize o parâmetro <i>hue</i> e indique a variável que quer incluir na subdivisão.</font>
# #### Mais informações: https://seaborn.pydata.org/generated/seaborn.boxplot.html

# In[30]:


ax = sns.boxplot(x = 'Renda', y = 'Anos de Estudo', hue = 'Sexo', data=dados.query('Renda < 10000 and Idade == 50'), orient='h')

ax.figure.set_size_inches(14, 8)    # Personalizando o tamanho da figura

ax.set_title('Box-plot da RENDA por SEXO e ANOS DE ESTUDO', fontsize=18)    # Configurando o título do gráfico

ax.set_xlabel('R$', fontsize=14)    # Configurando o label do eixo X

ax.set_ylabel('Anos de Estudo', fontsize=14)    # Configurando o label do eixo Y
ax.set_yticklabels([key for key in anos_de_estudo.values()], fontsize=12)    # Configurando o label de cada categoria do eixo Y

# Configurações da legenda do gráfico (Sexo)
handles, _ = ax.get_legend_handles_labels()
ax.legend(handles, ['Masculino', 'Feminino'], fontsize=12)

ax


# > ### Conclusões
# 
# As pessoas com mior renda são os homens amarelos, seguidas dos homens brancos. 

# ### Construa um box plot da variável RENDA segundo ANOS DE ESTUDO e SEXO
# #### <font color='blue'>É possível verificar algum comportamento diferenciado no rendimento entre os grupos de pessoas analisados? Avalie o gráfico e destaque os pontos mais importantes.</font>
# #### <font color='red'>1º - Utilize somente as informações de pessoas com renda abaixo de R$ 10.000</font>
# #### <font color='red'>2º - Utilize a variável IDADE para identificar se a desigualdade se verifica para pessoas de mesma idade. Exemplo: <i>data=dados.query('Renda < 10000 and Idade == 40')</i> ou <i>data=dados.query('Renda < 10000 and Idade == 50')</i></font>
# #### <font color='red'>3º - Para incluir uma terceira variável na construção de um boxplot utilize o parâmetro <i>hue</i> e indique a variável que quer incluir na subdivisão.</font>
# #### Mais informações: https://seaborn.pydata.org/generated/seaborn.boxplot.html

# In[31]:


renda_estatisticas_por_uf = dados.groupby(['UF']).agg({'Renda': ['mean', 'median', 'max', 'std']})
renda_estatisticas_por_uf.rename(index = uf)


# > ### Conclusões
# 
# O Maranhão possui a menor média e o DF a maior.

# ### Obtenha a média, mediana, valor máximo e desvio-padrão da variável RENDA segundo as UNIDADES DA FEDERAÇÃO
# #### <font color='blue'>Destaque os pontos mais importante que você observa nas tabulações</font>
# #### <font color='red'>Utilize o método <i>groupby()</i> do <i>pandas</i> juntamente com o método <i>agg()</i> para contruir a tabulação. O método <i>agg()</i> pode receber um dicionário especificando qual coluna do DataFrame deve ser utilizada e qual lista de funções estatísticas queremos obter, por exemplo: <i>dados.groupby(['UF']).agg({'Renda': ['mean', 'median', 'max', 'std']})</i></font>

# In[33]:


renda_estatisticas_por_uf = dados.groupby(['UF']).agg({'Renda': ['mean', 'median', 'max', 'std']})
renda_estatisticas_por_uf.rename(index = uf)


# ### Construa um box plot da variável RENDA segundo as UNIDADES DA FEDERAÇÃO
# #### <font color='blue'>É possível verificar algum comportamento diferenciado no rendimento entre os grupos analisados? Avalie o gráfico e destaque os pontos mais importantes.</font>
# #### <font color='red'>1º - Utilize somente as informações de pessoas com renda abaixo de R$ 10.000</font>

# In[34]:


ax = sns.boxplot(x = 'Renda', y = 'UF', data=dados.query('Renda < 10000'), orient='h')

ax.figure.set_size_inches(14, 8)    # Personalizando o tamanho da figura

ax.set_title('Box-plot da RENDA por ESTADOS', fontsize=18)    # Configurando o título do gráfico

ax.set_xlabel('R$', fontsize=14)    # Configurando o label do eixo X

ax.set_ylabel('Estados', fontsize=14)    # Configurando o label do eixo Y
ax.set_yticklabels([key for key in uf.values()], fontsize=12)    # Configurando o label de cada categoria do eixo Y

ax


# > ### Conclusões
# 
# Todos os estados possuem a maior ocncetraçaõ de renda em até 4000 reais com uma quantidade menor de pessoas além deste valor. De uma forma geral as médias não ultrapassam 2000 reais.

import lightgbm as lgb
import pandas as pd
import numpy as np
import pickle
df = pd.read_csv("stanbic.csv")
df = df.iloc[:,:-3]
df.credit_cards = df.credit_cards.apply(lambda x:x.strip("[]"))
df_test = df.credit_cards.str.get_dummies(sep = ',')
df = df.drop(['credit_cards'],axis=1)
df = df.join(df_test)
df = df.drop('cust_id',axis=1)
obj_feat = list(df.loc[:, df.dtypes == 'object'].columns.values)
for feature in obj_feat:
    df[feature] = pd.Series(df[feature], dtype="category")

def reco_prod(pk):
    reco = []
    for i in range(46,90):
        md_name = df.iloc[:,i].name
        pr = str(md_name).replace("'","")
        pr = pr.replace(" ","")
        filename = f'/home/abhinav-dev/reco-task/Models_cards/Model_{md_name}.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        y_pred = loaded_model.predict(df.iloc[[pk],:45])
        if(y_pred >= 0.5):
            reco.append(pr)
    print(reco)

print("Enter Row Number to find product recommendation")
pk = int(input())
reco_prod(pk)



# # df['profession_subclass'] = enc.fit_transform(np.array(df['profession_subclass']).reshape(-1,1))
# df = df.drop('cust_id',axis=1)
# # df['credit_cards'] = enc.fit_transform(np.array(df['credit_cards']).reshape(-1,1))
# catColumnsPos = [df.columns.get_loc(col) for col in list(df.select_dtypes('object').columns)]
# cost = []
# dfMatrix = df.to_numpy()
# for cluster in range(1, 10):
#     kprototype = KPrototypes(n_jobs = -1, n_clusters = cluster, init = 'Huang', random_state = 0)
#     kprototype.fit_predict(dfMatrix, categorical = catColumnsPos)
#     cost.append(kprototype.cost_)
#     print('Cluster initiation: {}'.format(cluster))
# print(cost)
# df_cost = pd.DataFrame({'Cluster':range(1, 6), 'Cost':cost})# Data viz
# plotnine.options.figure_size = (8, 4.8)
# (
#     ggplot(data = df_cost)+
#     geom_line(aes(x = 'Cluster',
#                   y = 'Cost'))+
#     geom_point(aes(x = 'Cluster',
#                    y = 'Cost'))+
#     geom_label(aes(x = 'Cluster',
#                    y = 'Cost',
#                    label = 'Cluster'),
#                size = 10,
#                nudge_y = 1000) +
#     labs(title = 'Optimal number of cluster with Elbow Method')+
#     xlab('Number of Clusters k')+
#     ylab('Cost')+
#     theme_minimal()
# )
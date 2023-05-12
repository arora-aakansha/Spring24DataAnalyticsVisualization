#Manupulating the gender based data

def manipulateCountryGenderData(df):
    #describe the data
    print("data Discription")
    print(df.describe())
    
    #finding ratio of male : female in each country and saving it in a coulmn
    # convert column A and B to integers
    df['GNI_PC_Male'] = df['GNI_PC_Male'].astype(float)
    df['GNI_PC_Female'] = df['GNI_PC_Female'].astype(float)
    df['GNI_Ratio'] = df['GNI_PC_Male'] / df['GNI_PC_Female']
    
    #Rouding ration upto 2 digits
    df['GNI_Ratio'] =df['GNI_Ratio'].round(2)
    #cleaning 
    df['GNI_Ratio'] = df['GNI_Ratio'].fillna(df['GNI_Ratio'].mean())
    
    #Adding HDI Ratio column of ratio in M:F format
    df['HDI_Ratio']=df.apply(lambda row: f"{row['HDI_Male']}:{row['HDI_Female']}", axis=1)
    
    
   
    
    #finding if female life longer than male in boolean
    df['Lif_Expec_Female'] = df['Lif_Expec_Female'].astype(float)
    df['Lif_Excep_Male'] = df['Lif_Excep_Male'].astype(float)
    
    df['Female_live_longer']= df['Lif_Expec_Female']>df['Lif_Excep_Male']
    
     #printing new column
    print(df['GNI_Ratio'], df['HDI_Ratio'], df['Female_live_longer'])
    
    #finding the false value in above column
    false_values = df[df['Female_live_longer'] == False]
    
    print(false_values)
    
    
    
    return df
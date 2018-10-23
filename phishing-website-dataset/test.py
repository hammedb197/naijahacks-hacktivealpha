
# coding: utf-8

# In[4]:


import joblib, phishingfeatures, sys

def main():
    url=sys.argv[1]

    features_test = phishingfeatures.main(url)

    jl = joblib.load('phishnot.pkl')

    pred=jl.predict(features_test)

    if int(pred[0]) == 1:
        print ("This is a safe website.")
    elif int(pred[0]) == -1:
        print ("This is a phishing website !")

if __name__== "__main__":
    main()


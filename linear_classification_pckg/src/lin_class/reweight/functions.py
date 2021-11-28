import numpy as np
import pandas as pd


def reweight_multiclass(classes, probs, rj):
    q = (classes.value_counts()/classes.value_counts().sum()).sort_index()
    q.index = range(1, len(q)+1)
    reweighted_probs = []
    for pi in probs:
        tot = 0
        for j in range(1,len(q)+1):
            tot = tot + pi[j-1]*(q[j]/rj)
        probs_rew_row = []
        for i in range(1,len(q)+1):
            w = (pi[i-1]*(q[i]/rj))/tot
            probs_rew_row.append(w)
        reweighted_probs.append(probs_rew_row)
    return np.array(reweighted_probs)



    
def reweight(pi,q1=0.5,r1=0.5):
    r0 = 1-r1
    q0 = 1-q1
    tot = pi*(q1/r1)+(1-pi)*(q0/r0)
    w = pi*(q1/r1)
    w /= tot
    return w

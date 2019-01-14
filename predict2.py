def bays2(model, A, B):
    pB = model == 'xxx'
    for bi in B:
        pB =  pB | (model == bi)

    pAB =  (((model == A) | pB ).sum(axis = 1) > len(B)).sum()
    return  pAB /     (pB.sum(axis = 1) > len(B) -1).sum()


def predict2(df, brand_df, wear, k = 15):
    prob = []

    for brand in brand_df.index:
        prob.append(bays2(df, brand, wear))

    best_k = sorted(range(len(prob)), key=lambda i: prob[i], reverse=True)[:k]
    return list(map(lambda k:brand_df.index[k], best_k))

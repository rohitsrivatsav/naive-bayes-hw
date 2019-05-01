from bayescoin import BayesCoin

bc = BayesCoin()
bc.choose_coin()
for i in range(10):
    f = bc.flip_coin()
    bc.update_priors(f)
    print('i:', i, 'coin:', bc.coin, 'flip:', f, 'priors:', bc.priors)

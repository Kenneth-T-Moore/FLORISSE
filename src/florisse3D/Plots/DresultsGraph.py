import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":

  #   """shear exponent"""
  #   shear_ex = np.array([0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3])
  #   shear_exDIFF = np.array([0.08,0.09,0.1,0.11,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3])
  #   shear_ex2 = np.array([0.08,0.09,0.1,0.11,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3])
  #   shear_exdiff2 = np.array([0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.27,0.28,0.29,0.3])
  #   shear_exdiff3 = np.array([0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29])
  #
  #
  #   COE = np.array([72.56429431, 72.56003538, 72.12026028, 72.14086257, 72.27311255, 71.78823907, 71.89202164, 71.31025759, 70.86439612, 71.54335898,
  #           69.55369941 , 69.02297158 , 68.52157007,  68.52157007, 68.69950649, 67.74959657,
  #           67.26615442 , 67.20774747, 66.06535292, 65.63431452, 65.4411585, 64.953411, 64.57610685])
  #   AEP = np.array([2.78120479e+08, 2.78120915e+08, 2.79956690e+08, 2.79807891e+08, 2.79276826e+08, 2.81322848e+08, 2.80885328e+08, 2.92658575e+08, 2.97445979e+08,
  #                   2.93955236e+08, 3.00018540e+08, 3.08117875e+08, 20, 21, 22, 23, 24, 25, 26, 27, 28, 3.31941054e+08, 3.34059655e+08])
  #
  #   """different heights, regular start"""
  #   COE1 = np.array([ 72.56429431,  72.9078423,   72.12026028,  72.6432162,   72.45860047,
  #         72.5710393 ,  72.08776118 , 71.64655626 , 71.8830588,   71.17486769,
  #         70.49744751,  69.72161641 , 69.64868265 , 69.4001219,   68.04433947,
  #         68.01562954 , 67.23682353 , 66.06535292 , 66.30906905 , 66.26899803,
  #         64.953411  ,  64.86518475])
  #   shear_XYZdt_AEP = np.array([  2.78120479e+08,   2.76672783e+08 ,  2.79956690e+08,   2.77739576e+08,
  #          2.78480090e+08,   2.77993349e+08,   2.80014200e+08,   2.81884164e+08,
  #          2.82637269e+08,   2.95964072e+08,   3.03601689e+08,   3.07277509e+08,
  #          3.07603757e+08,   3.08785825e+08,   3.15519362e+08,   3.15640264e+08,
  #          3.19636594e+08,   3.25856876e+08,   3.24513182e+08,   3.24705403e+08,
  #          3.31941054e+08,   3.32416068e+08])
  #   shear_XYZdt_diff = np.array([  4.44125775e+01,   4.43991268e+01,   4.43859561e+01,   4.43730599e+01,
  #          4.43480686e+01,   4.43359630e+01,   4.43241131e+01,   4.43125066e+01,
  #          4.55555065e+01,   6.99401166e+00,   4.26325641e-13,   1.65130132e-11,
  #          2.94875235e-11,   3.58113539e-12,   5.04485342e-12,   9.54401003e-11,
  #          7.24753590e-13,   1.57740487e-12,   1.01354540e-06,   8.06039679e-11])
  #
  #
  #   """warm start at x y locations of optimizedXYZdtSAME"""
  #   COE2 = np.array([ 72.58448921,  72.56003538,  72.39093832,  72.3478099 ,  71.89422717,
  #         71.89202164,  72.13982607,  71.74837492,  71.60141777,  71.03423043,
  #         69.87493167,  69.11105421,  68.46931911,  68.62123607,  68.65568612,
  #         67.42030138,  67.63597404,  65.63431452,  65.65580737,  65.60413432,
  #         64.57610685])
  #   shear_XYZdt2_AEP = np.array([  2.78035987e+08,   2.78120915e+08 ,  2.78813408e+08 ,  2.78978241e+08,
  #          2.80885328e+08 ,  2.80878631e+08,   2.79808811e+08,   2.81462054e+08,
  #          2.82078456e+08 ,  2.96605182e+08,   3.06565652e+08,   3.07696260e+08,
  #          3.13421278e+08 ,  3.12633275e+08,   3.12435349e+08 ,  3.18705157e+08,
  #          3.17562948e+08 ,  3.28191793e+08,   3.28049153e+08 ,  3.28310414e+08,
  #          3.34059655e+08])
  #   shear_XYZdt2_diff = np.array([  4.44125775e+01 ,  4.43991268e+01 ,  4.43859561e+01 ,  4.43730599e+01,
  #          4.43604325e+01 ,  4.43480686e+01,   4.43359630e+01,   4.43241106e+01,
  #          4.43125066e+01 ,  6.99401166e+00,   3.05533376e-12,   3.76893627e+00,
  #          2.25099939e-11 ,  7.72502062e-11,   4.73221462e-12,   5.35322897e-11,
  #          4.37694325e-12 ,  5.71520644e-08,   2.92743607e-11,   7.77617970e-11,
  #          3.51008111e-12])
  #
  #   COE3 = np.array([ 72.80243075,  72.87684492,  72.39803518,  73.7981604 ,  72.70218454,
  #         72.21223426,  71.31025759,  70.86439612,  70.47237464,  69.55369941,
  #         69.02297158,  68.52157007,  68.82300354,  67.74959657,  67.26615442,
  #         67.20774747,  66.16041172,  65.79236644,  65.79374939,  65.25115864])
  #   # shear_XYZdt3_AEP = np.array([  2.77065895e+08   2.76784291e+08   2.78766850e+08   2.77099946e+08
  #   #        2.81668350e+08   2.86657039e+08   2.92658575e+08   2.97445979e+08
  #   #        3.00018540e+08   3.08117875e+08   3.10689808e+08   3.13158882e+08
  #   #        3.11627436e+08   3.17028085e+08   3.19508469e+08   3.19788707e+08
  #   #        3.25341050e+08   3.27322670e+08   3.27290961e+08   3.30269888e+08])
  #   shear_XYZdt3_diff = np.array([  4.43991268e+01,   4.43859561e+01 ,  4.43730599e+01 ,  6.30957974e+00,
  #          6.20886981e+00 ,  9.14610609e-11 ,  3.06167100e+00 ,  6.98064186e+00,
  #          5.66077722e+00 ,  1.91846539e-12 ,  1.10844667e-12 ,  1.23350219e-11,
  #          1.28750344e-11 ,  9.81117410e-11 ,  8.55493454e-12 ,  1.69535497e-11,
  #          7.45217221e-11 ,  3.77156084e-11 ,  1.16529009e-11 ,  4.34141612e-11])
  #
  #
  #
  #   """4"""
  #   shear_ex4 = np.array([0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.2,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3])
  #
  #   COE4 = np.array([ 72.75670458, 72.63979169,  72.52032038,  72.39803518 , 72.27311255,
  #         72.14556806 , 72.01542934,  71.88271232,  71.74743491 , 69.75380726,
  #         68.69950649 , 68.17465076,  67.66732845,  67.23750347 , 66.32541586,
  #         66.3794655  , 66.06232673,  65.29671053,  65.3164107 ])
  #
  # #   COE:  [ 72.75670458  72.63979169  72.52032038  72.39803518  72.27311255
  # # 72.14556806  72.01542934  71.88271232  71.74743491  72.53444629
  # # 72.23698427  72.10387136  71.92645169  71.9198313   71.43395701
  # # 72.04669931  71.7337846   71.5712904   71.69589934]
  #   # shear_XYZdt4_AEP = np.array([  2.77317541e+08   2.77787505e+08   2.78270211e+08   2.78766850e+08
  #   #        2.79276826e+08   2.79800184e+08   2.80336945e+08   2.80887177e+08
  #   #        2.81450945e+08   3.07122089e+08   3.12242316e+08   3.14856896e+08
  #   #        3.17426206e+08   3.19633039e+08   3.24449540e+08   3.24134143e+08
  #   #        3.25824747e+08   3.30015703e+08   3.29882648e+08])
  #   shear_XYZdt4_diff = np.array([  4.44125775e+01  , 4.43991268e+01 ,  4.43859561e+01 ,  4.43730599e+01,
  #          4.43604325e+01,   4.43480686e+01 ,  4.43359630e+01 ,  4.43241107e+01,
  #          4.43125066e+01,   3.69482223e-13 ,  5.85913540e-11 ,  1.84741111e-13,
  #          1.39976919e-11,   3.68629571e-11 ,  1.26476607e-11 ,  2.20268248e-12,
  #          8.10160827e-11,   1.10489395e-10 ,  3.81419341e-11])
  #   """5"""
  #   shear_ex5 = np.array([0.17,0.18,0.22,0.26,0.27,0.28,0.29,0.3])
  #   shear_XYZdt5_COE = np.array([ 71.31305184 , 70.82076271,  68.71413357 , 66.00209103,  65.54423622,
  #       64.96498605 , 64.855435,    64.8905902 ])
  #   shear_XYZdt5_AEP = np.array([  2.95367760e+08 ,  2.97583622e+08  , 3.12169363e+08 ,  3.26201067e+08,
  #       3.28689199e+08  , 3.31899691e+08,   3.32494667e+08 ,  3.32272395e+08])
  #   shear_XYZdt5_diff = np.array([  6.98735435e+00 ,  6.99401166e+00 ,  3.34949846e-11 ,  5.81223958e-11,
  #       4.26041424e-11 ,  4.70379291e-12 ,  6.21014351e-12  , 2.84501311e-11])
  #
  #   shear_ex6 = np.array([0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29])
  #
  #   """6"""
  #   COE6 = np.array([ 72.60778492,  72.80243075 , 72.87684492,  72.39803518 , 73.7981604,
  #         72.70218454 , 72.21223426 , 71.31025759,  70.86439612,  70.47237464,
  #         69.55369941 , 69.02297158 , 68.52157007,  68.82300354,  67.74959657,
  #         67.26615442 , 67.20774747 , 66.16041172,  65.79236644,  65.79374939,
  #         65.25115864])
  #  #  AEP = [  2.77938587e+08   2.77065895e+08   2.76784291e+08   2.78766850e+08
  #  # 2.77099946e+08   2.81668350e+08   14 -> 2.86657039e+08   2.92658575e+08
  #  # 2.97445979e+08   3.00018540e+08   3.08117875e+08   3.10689808e+08
  #  # 3.13158882e+08   3.11627436e+08   3.17028085e+08   3.19508469e+08
  #  # 3.19788707e+08   3.25341050e+08   3.27322670e+08   3.27290961e+08
  #  # 3.30269888e+08]
  #
  #   shear_ex7 = np.array([0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.28,0.29,0.3])
  #   """7"""
  #   COE7 = np.array([ 72.88502208 , 72.75577038 , 72.62806528 , 72.14086257,  73.78782852,
  #         72.5392604  , 72.96701583,  72.53123556 , 72.0386515  , 71.54375203,
  #         71.04822989 , 70.51363127,  69.87202461 , 68.71206314 , 69.19582203,
  #         68.37327291 , 67.48791466 , 67.35719601 , 65.47445062 , 65.06079866,
  #         64.88691152])
  #
  #   """8"""
  #   COE8 = np.array([ 72.96119662,  74.83172518  ,74.53666059  ,72.71621587  ,73.78472192,
  #         71.78823907 , 72.96700007 , 72.52967054,  72.03826286,  71.54335898,
  #         71.04802646 , 70.50393087 , 69.96434851,  68.73192511,  69.20327154,
  #         68.37323549 , 67.47628974 , 67.34770772,  66.46701999,  65.71209694,
  #         65.4411585  , 65.06060365 , 64.88713973])
  #
  #   """9"""
  #   COE9 = np.array([ 72.96051123 , 74.83168528 , 72.75603302  ,72.67314774  ,73.789183,
  #         73.40681156 , 72.96701532,  72.53762755,  72.03308905,  71.54326929,
  #         71.0599034  , 70.50387955,  69.96763588,  68.73140198,  69.25516025,
  #         68.37380477 , 67.48331168,  67.336705  ,  66.25197756,  65.7130788,
  #         65.46910691 , 65.06082468,  64.88691081])
  #
  #
  #   # shear_XYZdtSAME_COE = np.array([ 79.23087632,  78.29813257,  78.50420394,  77.60217853 , 76.4745946,
  #   #         76.44594315 , 76.45989384,  76.02749103,  75.44378711 , 74.50310612,
  #   #         73.88675181 , 73.34899813,  72.80761783,  72.23235263 , 71.73121055,
  #   #         70.50106784 , 69.71349439,  69.02745351,  68.74401311 , 68.56797513,
  #   #         68.45178588 , 67.93724377 , 67.39011172])
  #   # shear_XYZdtSAME_AEP = np.array([  2.63136578e+08 ,  2.68236609e+08  , 2.67526569e+08 ,  2.71637177e+08,
  #   #        2.78102862e+08  , 2.80374830e+08,   2.80295653e+08,   2.82005814e+08,
  #   #        2.85592170e+08  , 2.94623717e+08,   2.97712102e+08 ,  3.00076084e+08,
  #   #        3.02494998e+08  , 3.05110144e+08 ,  3.07423907e+08 ,  3.13280727e+08,
  #   #        3.17143817e+08  , 3.20585953e+08 ,  3.22021049e+08 ,  3.22913302e+08,
  #   #        3.23500076e+08  , 3.26177484e+08 ,  3.29075079e+08])
  #   #
  #   # shear_XYZdtSAME2_COE = np.array([ 77.98840922,  77.8515058 ,  77.59068449 , 76.27519252,  77.19028332,
  #   #       76.92938366,  74.77136188,  74.92045365 , 73.74644893 , 72.40217057,
  #   #       73.0401192 ,  71.26939571,  70.78984305 , 70.60696686 , 70.15222569,
  #   #       69.22798441,  68.73221587,  68.7020291  , 67.141137   , 66.79061848,
  #   #       66.10158161])
  #   # shear_XYZdtSAME2_AEP = np.array([  2.67457451e+08,   2.69906517e+08,   2.70945545e+08,   2.76774464e+08,
  #   #        2.77438794e+08 ,  2.78437462e+08 ,  2.87164986e+08,   2.87764222e+08,
  #   #        2.97449838e+08 ,  3.04379221e+08 ,  3.01460919e+08,   3.09619208e+08,
  #   #        3.11898235e+08 ,  3.12766344e+08 ,  3.14971174e+08,   3.19567426e+08,
  #   #        3.22081714e+08 ,  3.22221715e+08 ,  3.30447268e+08 ,  3.32340957e+08,
  #   #        3.36143123e+08])
  #
  #
  #   shear_XYZdtSAME3_COE = np.array([ 74.79107272 , 74.38222718 , 74.08594544 , 73.68061504,  73.14206642,
  #         72.5394332  , 72.10830769 , 71.67958988,  71.11965817 , 70.15023073,
  #         69.55700341 , 69.02685456 , 68.50544486,  67.30161079 , 67.85360308,
  #         66.9627088  , 66.08866913 , 65.95538133,  65.09640457 , 64.39735669,
  #         64.13100625 , 63.72729853 , 63.55809211])
  #
  #
  #   shear_XYZdtSAME3_AEP = np.array([  2.66474936e+08,   2.69655122e+08 ,  2.70875446e+08 ,  2.73139952e+08,
  #          2.77193351e+08 ,  2.81604162e+08 ,  2.83420815e+08,   2.85251277e+08,
  #          2.88815495e+08 ,  2.97724723e+08 ,  3.01053730e+08,   3.03573550e+08,
  #          3.06093683e+08 ,  3.12098867e+08 ,  3.09292528e+08,   3.13804588e+08,
  #          3.18361589e+08 ,  3.19055035e+08 ,  3.23685712e+08,   3.27552379e+08,
  #          3.29040965e+08 ,  3.31331616e+08 ,  3.32292954e+08])
  #
  #
  #
  #
  #
  #   shear_XYdt_COE = np.array([ 74.89070847,  75.4454226,   75.37759998,  75.38552765,  75.39847857,
  #         75.44144568,  75.37682869,  75.37790272,  75.38872419,  75.36400187,
  #         75.38842372,  75.39323966,  75.44342729,  75.3758353 ,  74.86633175,
  #         75.37538768,  74.76213709,  75.4523128 ,  75.38135095,  75.48278883,
  #         75.3866085 ,  75.37561623,  75.39336695])
  #   shear_XYdt_AEP = np.array([  2.60565765e+08 ,  2.58480402e+08,   2.58732777e+08,   2.58702465e+08,
  #          2.58653416e+08 ,  2.58492436e+08  , 2.58732899e+08 ,  2.58728221e+08,
  #          2.58687148e+08 ,  2.58778844e+08  , 2.58686977e+08 ,  2.58668360e+08,
  #          2.58480494e+08 ,  2.58732108e+08  , 2.60648767e+08 ,  2.58732562e+08,
  #          2.61043145e+08 ,  2.58444348e+08  , 2.58708515e+08 ,  2.58329650e+08,
  #          2.58687732e+08 ,  2.58728221e+08  , 2.58661376e+08])
  #
  #
  #   shear_dt_COE = np.array([ 78.13788324 , 78.13768198,  78.13748346,  78.13728764 , 78.13709444,
  #         78.13690379 , 78.13671563,  78.13652987,  78.13634646 , 78.1361653,
  #         78.13598634 , 78.13580955,  78.13563488,  78.13546228 , 78.13529172,
  #         78.13512318 , 78.1349566 ,  78.13479197,  78.13462927 , 78.13446845,
  #         78.13430949 , 78.13415238,  78.13399708])
  #   shear_dt_AEP = np.array([  2.48818899e+08 ,  2.48818899e+08,   2.48818899e+08 ,  2.48818899e+08,
  #          2.48818899e+08  , 2.48818899e+08,   2.48818899e+08 ,  2.48818899e+08,
  #          2.48818899e+08  , 2.48818899e+08,   2.48818899e+08 ,  2.48818899e+08,
  #          2.48818899e+08  , 2.48818899e+08,   2.48818899e+08 ,  2.48818899e+08,
  #          2.48818899e+08  , 2.48818899e+08,   2.48818899e+08 ,  2.48818899e+08,
  #          2.48818899e+08  , 2.48818899e+08,   2.48818899e+08])
  #
  #   # plt.plot(shear_exDIFF, COE1, 'or', label='1')
  #   # plt.plot(shear_ex2, COE2, 'ob', label='2')
  #   # plt.plot(shear_exdiff3, COE3, 'ok', label='3')
  #   # plt.plot(shear_ex4, COE4, 'oy', label='4')
  #   # plt.plot(shear_ex6, COE6, 'oc', label='6')
  #   # plt.plot(shear_ex7, COE7, 'og', label='7')
  #   # plt.plot(shear_ex, COE8, 'om', label='8')
  #   # plt.plot(shear_ex, COE9, 'ow', label='9')
  #   #
  #   # plt.plot(shear_ex, COE, 'ok', label='low')
  #   # plt.legend()
  #   # plt.show()
  #
  #   COEdiff = np.zeros(len(shear_ex))
  #   AEPdiff = np.zeros(len(shear_ex))
  #   for i in range(len(shear_ex)):
  #       if COE[i] > shear_XYZdtSAME3_COE[i]:
  #           COEdiff[i] = shear_XYZdtSAME3_COE[i]
  #           AEPdiff[i] = shear_XYZdtSAME3_AEP[i]
  #       else:
  #           COEdiff[i] = COE[i]
  #           AEPdiff[i] = AEP[i]
  #
  #   AEPdiff[11] = shear_XYZdtSAME3_AEP[11]
  #   AEPdiff[10] = shear_XYZdtSAME3_AEP[10]
  #
  #   DIFF = np.array([44.412,44.412, 44.412, 44.412, 44.412, 44.412, 44.412, 3.0619, 6.9807, 0.,0.,0.,0.,
  #           0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
  #
  #
  #   plt.figure(1)
  #   plt.plot(shear_ex, shear_dt_COE, 'c', label='Original Grid')
  #   plt.plot(shear_ex, shear_XYdt_COE, 'k', label='Optimized Layout')
  #   plt.plot(shear_ex, shear_XYZdtSAME3_COE, 'r', label='1 Height Group')
  #   plt.plot(shear_ex, COEdiff, 'b', label='2 Height Groups')
  #   plt.legend(loc=3)
  #   plt.plot(shear_ex, COEdiff, 'ob')
  #   plt.plot(shear_ex, shear_XYZdtSAME3_COE, 'or')
  #   plt.plot(shear_ex, shear_XYdt_COE, 'ok')
  #   plt.plot(shear_ex, shear_dt_COE, 'oc')
  #   plt.title('Wind Farm COE vs. Shear Exponent')
  #   plt.xlabel(r'Shear Exponent ($\alpha$)')
  #   plt.ylabel('COE ($/MWhr)')
  #
  #   AEPdiff /= 10.**6
  #   shear_XYZdtSAME3_AEP /= 10.**6
  #   shear_XYdt_AEP /= 10.**6
  #   shear_dt_AEP /= 10.**6
  #
  #   plt.figure(2)
  #   plt.plot(shear_ex, shear_XYZdtSAME3_AEP, 'r', label='1 Height Group')
  #   plt.plot(shear_ex, AEPdiff, 'b', label='2 Height Groups')
  #   plt.plot(shear_ex, shear_XYdt_AEP, 'k', label='Optimized Layout')
  #   plt.plot(shear_ex, shear_dt_AEP, 'c', label='Original Grid')
  #   plt.plot(shear_ex, AEPdiff, 'ob')
  #   plt.plot(shear_ex, shear_XYZdtSAME3_AEP, 'or')
  #   plt.plot(shear_ex, shear_XYdt_AEP, 'ok')
  #   plt.plot(shear_ex, shear_dt_AEP, 'oc')
  #   plt.title('Wind Farm AEP vs. Shear Exponent')
  #   plt.xlabel(r'Shear Exponent ($\alpha$)')
  #   plt.ylabel('AEP (GWhrs)')
  #
  #   plt.figure(3)
  #   plt.plot(shear_ex, DIFF,'k')
  #   plt.plot(shear_ex, DIFF,'ok')
  #   plt.title('Difference in Height between \n Height Groups vs. Shear Exponent')
  #   plt.xlabel(r'Shear Exponent ($\alpha$)')
  #   plt.ylabel('Height Difference (m)')
  #   plt.axis([0.078,0.302,-0.5,50])
  #   plt.show()
  #
  #
  #
  #
  #   # plt.figure(2)
  #   # plt.plot(shear_exdiff2, shear_XYZdt2_AEP, 'r', label='XYZdt')
  #   # plt.plot(shear_ex2, shear_XYZdtSAME2_AEP, 'b', label='XYZdtSAME')
  #   # plt.plot(shear_ex, shear_XYdt_AEP, 'k', label='XYdt')
  #   # plt.plot(shear_ex, shear_dt_AEP, 'c', label='dt')
  #   # plt.legend()
  #   #
  #   # plt.figure(3)
  #   # plt.plot(shear_exdiff3, shear_XYZdt3_diff, 'b')
  #
  #   plt.show()



    """spacing"""
    spacing = np.array([2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0])
    spacing2 = np.array([2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,10.0])


    spacing_dt_COE = np.array([ 103.28319704,   89.71764439,   81.4524095 ,   76.0049225  ,  72.20093401,
           69.46741984 ,  67.43221966,   65.85488169 ,  64.63411473 ,  63.64763946,
           62.85668712 ,  62.21672817 ,  61.67944119 ,  61.23186106 ,  60.86247103,
           60.55219726 ,  60.28808344])
    spacing_dt_AEP = np.array([  1.92919698e+08,   2.24221308e+08,   2.48818899e+08  , 2.68211324e+08,
           2.83648733e+08 ,  2.95886535e+08,   3.05706603e+08,   3.13777631e+08,
           3.20322641e+08 ,  3.25814531e+08,   3.30355832e+08,   3.34123903e+08,
           3.37354463e+08 ,  3.40093724e+08,   3.42388182e+08,   3.44339501e+08,
           3.46018128e+08])


    spacing_XYdt_COE = np.array([ 103.28281492 ,  87.30930401 ,  78.4338137  ,  73.69154391,   70.83873915,
           68.43143489 ,  66.57870788 ,  65.15574124 ,  64.25327295 ,  63.32367325,
           62.61441868 ,  62.02674837 ,  61.57413091 ,  61.16765004 ,  60.82651031,
           60.50686264 ,  60.25738229])
    spacing_XYdt_AEP = np.array([  1.92919698e+08 ,  2.30872100e+08  , 2.59204461e+08 ,  2.77393116e+08,
           2.89618726e+08  , 3.00805896e+08 ,  3.10022418e+08 ,  3.17493771e+08,
           3.22421737e+08  , 3.27660402e+08 ,  3.31773255e+08 ,  3.35260106e+08,
           3.37996011e+08  , 3.40491375e+08 ,  3.42614230e+08 ,  3.44627506e+08,
           3.46215353e+08])

    spacing_XYZdt_COE = np.array([ 90.89933826 , 78.81668394 , 72.12026028 , 69.31229216  ,66.26773831,
          64.93054987 , 63.23809306,  62.00516598 , 60.97291448 , 60.17741192,
          59.47698369 , 58.92244667,  58.48117673  ,58.17500649 , 57.84946765,
          57.5884306  , 57.35818757])
    spacing_XYZdt_AEP = np.array([  2.22706977e+08,   2.54172148e+08 ,  2.79956690e+08,   2.92394680e+08,
           3.07192633e+08 ,  3.14176152e+08  , 3.24447967e+08 ,  3.31604591e+08,
           3.37843766e+08 ,  3.42814516e+08  , 3.47313870e+08 ,  3.50960708e+08,
           3.53917838e+08 ,  3.55999065e+08  , 3.58238971e+08 ,  3.60055530e+08,
           3.61673154e+08])
    spacing_XYZdt_diff = np.array([  4.87192351e+01 ,  4.43859561e+01 ,  4.43859561e+01 ,  4.43859561e+01,
           4.43859561e+01,   4.43859561e+01 ,  4.46220838e-12 ,  9.03810360e-11,
           1.80193638e-11,   3.09086090e-11 ,  3.38928885e-11  , 2.17703872e-06,
           5.19406740e-11,   4.12114787e-12 ,  4.43662884e-11   ,8.24371682e-11,
           3.62661012e-11])

    spacing_XYZdt2_COE = np.array([ 90.88682649,  78.68435257 , 72.24329025 , 69.15939324 , 66.64583348,
          64.89106805 , 63.23809308,  62.00516607,  60.97291452 , 60.17739325,
          59.47698374 , 58.92244692,  58.4811768 ,  58.17500679 , 57.8494678,
          57.58843092 , 57.35818749])
    spacing_XYZdt2_AEP = np.array(  [2.22715992e+08 ,  2.53345287e+08 ,  2.78068174e+08,   2.91669169e+08,
           3.06183835e+08 ,  3.15324206e+08 ,  3.24447967e+08 ,  3.31604590e+08,
           3.37843766e+08 ,  3.42814634e+08 ,  3.47313870e+08 ,  3.50960706e+08,
           3.53917837e+08 ,  3.55999063e+08 ,  3.58238970e+08 ,  3.60055528e+08,
           3.61673154e+08])
    spacing_XYZdt2_diff = np.array([  4.87267389e+01 ,  4.43859561e+01 ,  4.43859561e+01  , 4.43859561e+01,
           6.08224582e-12 ,  1.69109171e-12  , 3.05959702e-11 ,  5.54223334e-13,
           9.94759830e-14 ,  4.68958206e-13  , 1.42108547e-14  , 1.05302433e-11,
           9.66338121e-13 ,  9.09494702e-13  , 3.26849658e-13  , 2.94846814e-10,
           1.06581410e-12])


    spacing_XYZdtSAME_COE = np.array([ 101.75176696 ,  86.61242985,   78.50420394,   73.32936556 ,  70.05654381,
           67.58934979 ,  65.80357479,   64.6753802,    63.57699499 ,  62.63161526,
           61.87478002 ,  61.33804729,   60.90581369,   60.49593453 ,  60.16962484,
           59.86716202 ,  59.60039249])
    spacing_XYZdtSAME_AEP = np.array([  2.02497686e+08 ,  2.40581223e+08 ,  2.67526569e+08 ,  2.88121925e+08,
           3.02868174e+08 ,  3.15022411e+08,   3.24446526e+08  , 3.30696615e+08,
           3.37017326e+08 ,  3.42654273e+08,   3.47304750e+08  , 3.50680025e+08,
           3.53446216e+08 ,  3.56109960e+08,   3.58259478e+08  , 3.60275213e+08,
           3.62071993e+08])

    spacing_XYZdtSAME2_COE = np.array([ 101.75110375  , 86.10522451,   77.16764699,   72.41843774 ,  70.00396132,
           67.70364605,   65.74106466   ,64.42051794,   63.53820442,   62.53300333,
           61.93742807,   61.35466329 ,  60.87443741 ,  60.47942011 ,  60.15298492,
           59.6202718 ])
    spacing_XYZdtSAME2_AEP = np.array([  2.02501630e+08,   2.42106615e+08 ,  2.72558603e+08 ,  2.92080068e+08,
           3.03117424e+08   ,3.14437839e+08 ,  3.24786638e+08,   3.32142016e+08,
           3.37244968e+08   ,3.43253139e+08 ,  3.46915014e+08,   3.50574550e+08,
           3.53648716e+08   ,3.56218127e+08 ,  3.58369787e+08,   3.61937481e+08])

    spacing_XYZdtSAME3_COE = np.array([ 96.35523114,  80.60157426 , 72.85730099,  69.44950696 , 65.79651474,
          64.06496352  ,63.23809306 , 62.00516598 , 60.97291448 , 60.17741192,
          59.47698369 , 58.92244656 , 58.48117673 , 58.17500649 , 57.84946765,
          57.5884287  , 57.35818757])
    spacing_XYZdtSAME3_AEP = np.array([  2.02500308e+08 ,  2.45324427e+08 ,  2.73787891e+08,   2.88518235e+08,
           3.06176410e+08,   3.15324205e+08,   3.24447967e+08,   3.31604591e+08,
           3.37843766e+08,   3.42814516e+08,   3.47313870e+08,   3.50960710e+08,
           3.53917838e+08,   3.55999065e+08,   3.58238971e+08,   3.60055544e+08,
           3.61673154e+08])


    COE = np.zeros(len(spacing))
    AEP = np.zeros(len(spacing))
    DIFF = np.zeros(len(spacing))
    space = np.zeros(len(spacing))
    for i in range(len(spacing)):
        space[i] = (4*(spacing[i]))**2
        if spacing_XYZdt_COE[i] >= spacing_XYZdtSAME3_COE[i]:
            COE[i] = spacing_XYZdtSAME3_COE[i]
            AEP[i] = spacing_XYZdtSAME3_AEP[i]
            DIFF[i] = 0
        else:
            COE[i] = spacing_XYZdt_COE[i]
            AEP[i] = spacing_XYZdt_AEP[i]
            DIFF[i] = 44.3859

    DIFF[6] = 0

    spacing = space

    plt.figure(4)
    plt.plot(spacing, spacing_dt_COE, 'c', label='Original Grid')
    plt.plot(spacing, spacing_XYdt_COE, 'k', label='Optimized Layout')
    plt.plot(spacing, spacing_XYZdtSAME3_COE, 'r', label='1 Height Group')
    plt.plot(spacing, COE, 'b', label='2 Height Groups')
    plt.plot(spacing, spacing_dt_COE, 'oc')
    plt.plot(spacing, spacing_XYdt_COE, 'ok')
    plt.plot(spacing, COE, 'ob')
    plt.plot(spacing, spacing_XYZdtSAME3_COE, 'or')
    plt.legend()
    plt.title('Wind Farm COE vs. Farm Size')
    plt.xlabel('Farm Size (square rotor diameters)')
    plt.ylabel('COE ($/MWhr)')
    plt.axis([0,403,60,110])

    AEP /= 10.**6
    spacing_XYZdtSAME3_AEP /= 10.**6
    spacing_XYdt_AEP /= 10.**6
    spacing_dt_AEP /= 10.**6

    plt.figure(5)
    plt.plot(spacing, spacing_dt_AEP, 'c')
    plt.plot(spacing, spacing_XYdt_AEP, 'k')
    plt.plot(spacing, spacing_XYZdtSAME3_AEP, 'r')
    plt.plot(spacing, AEP, 'b')
    plt.plot(spacing, spacing_dt_AEP, 'oc')
    plt.plot(spacing, spacing_XYdt_AEP, 'ok')
    plt.plot(spacing, AEP, 'ob')
    plt.plot(spacing, spacing_XYZdtSAME3_AEP, 'or')
    plt.title('Wind Farm AEP vs. Farm Size')
    plt.xlabel('Farm Size (square rotor diameters)')
    plt.ylabel('AEP (GWhrs)')
    plt.axis([0,403,175,350])
    plt.legend()

    plt.figure(6)
    plt.plot(spacing, DIFF,'k')
    plt.plot(spacing, DIFF,'ok')
    plt.title('Difference in Height between \n Height Groups vs. Farm Size')
    plt.xlabel('Farm Size (square rotor diameters)')
    plt.ylabel('Height Difference (m)')
    plt.axis([0,403,-0.5,50])
    plt.show()


    # plt.figure(5)
    # plt.plot(spacing, spacing_XYZdt_AEP, 'r', label='XYZdt')
    # plt.plot(spacing, spacing_XYZdtSAME_AEP, 'b', label='XYZdtSAME')
    # plt.plot(spacing, spacing_XYdt_AEP, 'k', label='XYdt')
    # plt.plot(spacing, spacing_dt_AEP, 'c', label='dt')
    # plt.legend()
    #
    # plt.figure(6)
    # plt.plot(spacing, spacing_XYZdt_diff, 'b')
    plt.show()
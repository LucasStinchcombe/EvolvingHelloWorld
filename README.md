#Evolving Strings

This is a python script modeled off of evolution of dna through mutation. The script uses four sources of mutation (insertion, deletion, replacement, and point mutation) as well as random "crossing-over" of parent dna to produce variations in our gene pool. The "fitness" of an individual piece of dna is computed by taking the absolute difference between the unicode values of each character of the target dna and the individual's dna. Those with the lowest "fitness" values will successfully pass on their genes.

    Output for target="Lucas Stinchcombe made this"

    0 ------------------------------
         1       6553  =>                                      'M'
         2       6557  =>                                      'Q'
         3       6557  =>                                      'G'
         4       6559  =>                                      'E'
         5       6560  =>                                      'D'
         6       6564  =>                                      '@'
         7       6568  =>                                     '\\'
         8       6573  =>                                      'a'
         9       6581  =>                                      '/'
        10       6581  =>                                      'i'
    25 ------------------------------
         1       4552  =>                             "dSt'LLYyjF"
         2       4627  =>                             "dSt'LLFw H"
         3       4638  =>                             "dSt'LLF jF"
         4       4677  =>                             "'Z -LLFw H"
         5       4712  =>                          'dSt~BXj\x1f H'
         6       4744  =>                         "'Z \\BXj\x1f H"
         7       4776  =>                              '()~ftFEjH'
         8       4777  =>                           '()\x7fftFEjH'
         9       4825  =>                           ')RGXjFD\x1fF'
        10       4825  =>                              "RZ'f]FE H"
    50 ------------------------------
         1       1992  =>             "dSZ8D'A\\MF\x1f` #^FwFE [I"
         2       2031  =>              "dTZ8E'6`7\x0cA  _mOFE [II"
         3       2060  =>             "dTZ8D'A\\7\x0cXA  _mO`E [I"
         4       2136  =>              "dTZ8D'6`7\x0cA  #^FwbE [I"
         5       2160  =>                  'dTZ8D(\\`MMwh_mOFw [I'
         6       2181  =>                  'dTZ8D(\\`MGvh_mFvE![I'
         7       2220  =>                  "dTZ8D'6`MF  #^FwbE [I"
         8       2221  =>                  "dSZ8D'6`MF  #^FwbE [I"
         9       2223  =>              "dSZ8D'A\\7\x0cA  _mOaE [I"
        10       2228  =>                 ';SY8D(\\`MGw  _FvEw [I'
    75 ------------------------------
         1        651  =>     "dSZ8W'6^6A\\K`d\x0cwA\x1f_nGE u[[K"
         2        654  =>     "dSZ8V'o^6A\\L`M\x0cvR\x1f_nGE t[[K"
         3        654  =>     "dSZ8V'o^6A\\L`M\x0cvR\x1f_nGE t[[K"
         4        654  =>     "cSZ8V'o^6A\\L`M\x0cwR\x1f_nGE t[[K"
         5        655  =>     "eSZ8V'o^6A\\L`M\x0cvR\x1f_nGE t[[K"
         6        655  =>     "dRZ8V'o^6A\\L`M\x0cvR\x1f_nGE t[[K"
         7        655  =>     "dSZ9V'o^6A\\L`M\x0bwR\x1f_nGE t[[K"
         8        655  =>     "dSZ9V'o^6A\\L`M\x0bwR\x1f_nGE t[[K"
         9        655  =>     "dSZ8V'o]6A\\L`M\x0cvR\x1f_nGE t[[K"
        10        655  =>     "dSZ8V'o^6@\\L`M\x0cvR\x1f_nGE t[[K"
    100 ------------------------------
         1        401  =>        "dRZaV'o^dB\\aacMul\x1fdnGj ti[K"
         2        403  =>        "dR[aV'o^dB\\aacOvl\x1f_mGj ti[K"
         3        404  =>        "dRZaV'o^dB\\aacMul\x1fdnFj!ui[K"
         4        443  =>           "dR[bW'n^6A\\aacOvl dmGj ti[K"
         5        448  =>        "dRZbW'n^6A\\aacMvl\x1fdnGj ti[K"
         6        451  =>       "dRZaW'n^6A\\ba\\Nul\x1fdnGj ti[K"
         7        452  =>          "dR[bW'n^6A\\ba\\Mvl dmGj!ti[K"
         8        452  =>          "dRZaV'o^6B\\ba\\Mvl enGj ti[K"
         9        453  =>       'dR[bV\'o^6B\\aacOvl\x1f_mGj"ui[K'
        10        453  =>          "dR[bV'o^6B\\ba\\Lvl dnGi ti[K"
    125 ------------------------------
         1        321  =>          'CSZaV&V^dZ\\bacOvl dmyj ti\\L'
         2        322  =>          'CSZaV&V^dZ\\bacOvl dmyj ti\\K'
         3        322  =>          'CSZaV&V^dZ\\aacOvl dmyj ti\\L'
         4        323  =>          'CSZaV&V^dZ\\aacOvl dmyk ti\\L'
         5        323  =>          'BSZaV&V^dZ\\aacOvl dmyj ti\\L'
         6        341  =>          'CSZ`W%V^dD\\aacOul dmxj ti\\L'
         7        341  =>          'CSZ`W%V^dD\\bacOvl emyj ti\\L'
         8        342  =>          'CSZaV&V^dD\\bacOvl emyj ti\\L'
         9        342  =>          'CSZaV%V^dD\\aacPvl dmyj ti\\L'
        10        343  =>          'CSZaV%V^dD\\aacOul dmyj tj\\L'
    150 ------------------------------
         1        260  =>       'DSZat&V^dZ\\abcOll emyj\x1eth\\b'
         2        260  =>       'DSZat&V^dZ\\abcOll emyj\x1eth\\b'
         3        260  =>        'CSZat%V^d~]aacPll fmyj\x1fth\\['
         4        264  =>        'CSZat&V^d[]aacOjl emyj\x1fth\\['
         5        266  =>       'CSZat%V^dZ\\aacOll fmyj\x1fth\\['
         6        266  =>       'CS[at&V^dZ\\aacOll fmyj\x1fth\\['
         7        266  =>        'CSZat&V^dZ\\abcOll emyj\x1fth]['
         8        275  =>        'CSZat%V^d[]aacPjl emxi\x1fth\\L'
         9        276  =>           'CSZat&V^d[]aacOjl emxi th\\L'
        10        277  =>        'CSZat%V^d[]aacPjl emx_\x1fth\\L'
    175 ------------------------------
         1        234  =>        'CTZat$U_d}]aacPbl emyj\x1fth\\g'
         2        236  =>        'DTZat$U_d}]aacPbl emxj\x1fth\\c'
         3        236  =>        'CTZat$U_d|^aacQcl emyj\x1fth\\c'
         4        237  =>         'CTZat$U_d|^aacQcl emyj\x1fth[c'
         5        238  =>     'DTZat$U_d}]aacPcl\x1femxj\x1fth\\c'
         6        238  =>        'DTZat#W_d~]abcPcl emxj\x1fth\\c'
         7        238  =>     'DTZat$U_d\x7f]aacPbl gnyj\x1fth\\c'
         8        239  =>        'CTZat$U_d}]aacPcl emxj\x1fth\\b'
         9        239  =>        'DTZat$W_d}]aacPbl emxj\x1fth\\b'
        10        239  =>        'DTZbt$U^d}]aacPbl emxj\x1fth\\b'
    200 ------------------------------
         1        196  =>        'DY[at$Vue|_aacQck emVj\x1fth\\g'
         2        212  =>        'DZZat$T_e{_aacQbk emVj\x1fth\\g'
         3        212  =>        'DZZat$T_e{_aacQbk emVj\x1fth\\g'
         4        212  =>        'DZZat$T_e{`aacQck emVj\x1fth\\g'
         5        213  =>        'DZZat$T_e{_aacQck emVj\x1fth\\g'
         6        213  =>         'DZZat$T`e{_aacQbk dmVj\x1fth[g'
         7        213  =>        'DZZ`t$T_e{`aacQck emVj\x1fth\\g'
         8        213  =>        'DZZat$T_e|_abcQck emVj\x1fth\\g'
         9        213  =>        'DZZas$T_e|_aacQck emVj\x1fth\\g'
        10        213  =>         'DZZ`t$T_e{`abcQck emVj\x1fth[g'
    225 ------------------------------
         1        156  =>         'E[aas$T_e{`acckbk gmVh\x1fthig'
         2        157  =>         'E[aas$T_e{`acckbk gmVi\x1fthig'
         3        157  =>         'E[`as$T_ez`acckbk gmVi\x1fthig'
         4        162  =>         'E[Zar$S_e{`acekbj fmVi\x1fthig'
         5        163  =>         'E[Zar$S_e{`acekbk fmVi\x1fthig'
         6        163  =>         'E[Zas$T_e{`abekbk gmVi\x1fthig'
         7        165  =>         'E[Zar$S_e{`abekbk fmVi\x1fthhg'
         8        165  =>         'E[Zas$T_e{`abekbk fnVi\x1fthig'
         9        165  =>         'E[Zar$S_e{`acckck fmVh\x1fthig'
        10        165  =>         'E[Zar$S_e{`acckck fmVh\x1fthig'
    250 ------------------------------
         1        126  =>         'Edaas$Tae{`ccfkbk gmdh\x1fthig'
         2        126  =>         'Fd`as#T`e{`bcgkbk gmdh\x1fthig'
         3        127  =>            'Edaas$Tae{`bcfkbk gmch thig'
         4        127  =>            'Fd`as$T`e{`bcgkbk gmch thig'
         5        127  =>         'Fd`as#T`e{`bcgkbk gmch\x1fthig'
         6        128  =>         'Fd`as$Tae{`bcfkbk gmch\x1fthig'
         7        128  =>         'Edaas#U`e{`bcfkbk gmdh\x1fthig'
         8        128  =>            'Fd`as$T`e{`bcfkbk gmch thig'
         9        128  =>         'Fd`as$T`ez`bcfkbk gmch\x1fthig'
        10        128  =>         'Edaas$T`ez`bcfkbk gmch\x1fthig'
    275 ------------------------------
         1        113  =>            'Eeaas#Ube{`bcfkbi g^dh thig'
         2        113  =>            'Eeaas#Tbe{`bcfkbj g^dh thig'
         3        113  =>            'Eeaas#Tbe{`bcfkbj g^dh thig'
         4        114  =>            'Edaas#Tbe{`bcfkbj g^dg tgig'
         5        114  =>            'Edaas"Tbe{`bcfkbk g^dh thig'
         6        115  =>            'Edaas#Tae{`bcfkbj g^dh thig'
         7        115  =>            'Eeaas#Ubd{`bcfkbj g^dh shih'
         8        115  =>            'Edaat#Tbe{`bcfkbj g^dg tgig'
         9        115  =>            'Edaas#Tbe{`bcfkbk g^dh thig'
        10        115  =>            'Edaas#Tbe{`bbfkbj f^dg thig'
    300 ------------------------------
         1         79  =>            'Ifaas!Sbeyaccnlbj g^dg this'
         2         86  =>            'Ifaas"Sbeyacchlbj g^dg this'
         3         86  =>            'Ifaas"Sbeyaccglbj g^df this'
         4         87  =>            'Ifaas"Sbeyaccglbj g^dg this'
         5         87  =>            'Igaas"Sbeyaccglbj g^dh this'
         6         89  =>            'Ffaas"Sbeyacchlbj g^dg this'
         7         89  =>            'Efaas"Sbeyacchmcj g_dg this'
         8         90  =>            'Efaas"Sbeyacchlbj g^dg this'
         9         90  =>            'Efaas"Sbeyacchlbj g^dg this'
        10         91  =>            'Efaas"Sbezaccglbj g_dg this'
    325 ------------------------------
         1         52  =>            'Ggaas!Sweoaccnlbj h^de this'
         2         52  =>            'Igaas!Sxeoaccnlbj g_df this'
         3         53  =>            'Ggaas!Sweoaccnlbj h^de thjs'
         4         53  =>            'Gfaas!Sweoaccnlbj h^de this'
         5         53  =>            'Fgaas!Sxeoaccnlbj i^de this'
         6         57  =>            'Ggcas!Sweybccnmbj i^de this'
         7         59  =>            'Gfbas Sveyaccnlbj i^de this'
         8         60  =>            'Gfbas!Sveyaccnlbj i^de this'
         9         60  =>            'Gfbas!Sveyaccnlbj i^de this'
        10         60  =>            'Ggbas!Sweybccnlbj g_de this'
    350 ------------------------------
         1         40  =>            'Kgaas Svencdcmlbi j_de thjs'
         2         40  =>            'Kgaas Swencdcmlbi j_de this'
         3         40  =>            'Kgaas Swencdcmlbi j_de this'
         4         40  =>            'Kgaas!Svencdcmlbi j_de this'
         5         41  =>            'Khaas!Swencdcmlbh h_de this'
         6         41  =>            'Jhaas Swencdcmlbh h_de this'
         7         41  =>            'Khaas Swencdcmlbh h_de thjs'
         8         42  =>            'Khaas!Swenddcmlbh h_de this'
         9         42  =>            'Khaas Swencdcllbh h_de tgis'
        10         42  =>            'Khaas!Swencdcllbh h_de this'
    375 ------------------------------
         1         24  =>            'Lhbas Svgncgcombg k`de this'
         2         25  =>            'Lhbas Svgncfcombg k`de this'
         3         28  =>            'Lgbas Svgncfcmmbf k_de this'
         4         28  =>            'Lhbas Svgnbfcmmbg k`de this'
         5         28  =>            'Lha`s Svgncfcmmbf k`de this'
         6         28  =>            'Lhaas Svgncfcmmbf k_de this'
         7         28  =>            'Lhaas Svgncfcmmbg k`de this'
         8         29  =>            'Lhaas Svgncfcmmbh k`de this'
         9         29  =>            'Lhaas Svgncfcmmbh k`de this'
        10         30  =>            'Lha`s Svgnbfcmmbg k`de this'
    400 ------------------------------
         1          8  =>            'Ltcas Svincgcombg kade this'
         2          9  =>            'Ltcat Svimcgcombf l`de this'
         3          9  =>            'Ltbas Svincgcombg kade this'
         4          9  =>            'Ltbat Svincgcombg m`de this'
         5          9  =>            'Ltbat Svincgcombg m`de this'
         6          9  =>            'Ltcas Svincgcombg k`de this'
         7          9  =>            'Ltcas Svincgcombg k`de this'
         8         10  =>            'Ltbas Svincgcombg k`de this'
         9         11  =>            'Ltbat Svincgcombg l`de thit'
        10         11  =>            'Ltcas Svhmcgcomcg kade this'
    425 ------------------------------
         1          3  =>            'Lucas Svinchcomce made this'
         2          3  =>            'Lucas Svinchcomce made this'
         3          3  =>            'Lucas Svinchcomce made this'
         4          4  =>            'Lucas Svinchcomce lade this'
         5          4  =>            'Lucas Svinchcomce lade this'
         6          4  =>            'Lucas Svinchcomce lade this'
         7          4  =>            'Lucas Svinchconce made this'
         8          4  =>            'Lucas Svinchcomce lade this'
         9          4  =>            'Lucas Svinchconce made this'
        10          4  =>            'Lucas Svinchcomce lade this'
    450 ------------------------------
         1          1  =>            'Lucas Suinchcombe made this'
         2          1  =>            'Lucas Suinchcombe made this'
         3          2  =>            'Lucas Suinchcombe made thir'
         4          2  =>            'Lucas Suinchcomce made this'
         5          2  =>            'Lucas Suinchcomce made this'
         6          2  =>            'Lucas Suinchcomce made this'
         7          2  =>            'Lucas Suinchcomce made this'
         8          2  =>            'Lucas Suinchcomce made this'
         9          2  =>            'Lucas Suinchcomce made this'
        10          2  =>            'Lucas Suinchcomce made this'
    460 ------------------------------
         **1          0  =>            'Lucas Stinchcombe made this'**
         2          1  =>            'Lucas Suinchcombe made this'
         3          1  =>            'Lucas Suinchcombe made this'
         4          1  =>            'Lucas Suinchcombe made this'
         5          1  =>            'Lucas Suinchcombe made this'
         6          1  =>            'Lucas Suinchcombe made this'
         7          1  =>            'Lucas Suinchcombe made this'
         8          1  =>            'Lucas Suinchcombe made this'
         9          1  =>            'Lucas Suinchcombe made this'
        10          2  =>            'Lucas Suinchcombe mbde this'

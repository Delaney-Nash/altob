genes = {}

seq = 'GTAAACCAAAAAAATGGGGCAAATAAGAATTTGATAAGTACCACTTAAATTTAACTCCTTTGGTTTAAGATGGGCAGCAACTCATTGAGCATGATAAAAGTTAGATTGCAAAATCTGTTTGACAATGATGAAGTAGCATTGTTAAAAATAACATGCTATACTGACAAATTAATACAGTTAACCAATGCTTTGGCTAAGGCAGTTATACATACAATCAAATTGAATGGCATTGTATTTGTGCATGTTATTACAAGTAGTGATATTTGCCCTAATAATAATATTGTAGTGAAATCCAATTTCACAACAATGCCAGTATTACAAAATGGAGGTTATATATGGGAAATGATGGAATTAACACACTGCTCTCAACCTAATGGCCTAATAGATGACAATTGTGAAATTAAATTCTCCAAAAAACTAAGTGATTCAACAATGACCAATTATATGAATCAATTATCTGAATTACTTGGATTTGACCTCAATCCATAAATCATAATAAATATCAACTAGCAAATCAATGTCACTAACACCATTAGTTAATATAAAACTTGACAGAAGATAAAAATGGGGCAAATAAATCAATTCAGCCGACCCAACCATGGACACAACACACAATGATACCACACCACAAAGACTGATGATCACAGACATGAGACCATTATCGCTTGAGACTATAATAACATCTCTAACCAGAGATATCATAACACATAAATTTATATACTTGATAAATCATGAATGCATAGTGAGAAAACTTGATGAAAGACAGGCCACATTTACATTTCTGGTCAACTATGAAATGAAACTATTGCACAAAGTGGGAAGCACTAAATATAAAAAATATACTGAATACAACACAAAATATGGCACTTTCCCTATGCCAATATTTATCAATCATGATGGGTTCTTAGAATGCATTGGCATTAAGCCTACCAAGCACACACCCATAATATACAAGTATGATCTCAATCCATGAATATCAAACCAAGATTCAAACAATCCGAAATAACAACTCTATGCATAATCACACTCCATAGTCCAAATGGAGCCTGGAAATTATAGTTATTTAAAATTAAGGAGAGACATAAGATGAAAGATGGGGCAAATACAAAAATGGCTCTTAGCAAAGTCAAGTTGAATGATACACTCAACAAAGATCAACTTCTATCATCCAGCAAATATACCATCCAACGGAGCACAGGAGACAGCATTGACACTCCTAATTATGATGTGCAGAAACACATTAATAAGTTATGTGGCATGTTATTAATCACAGAAGATGCTAATCATAAATTCACTGGGTTAATAGGTATGTTATATGCTATGTCTAGATTAGGAAGAGAAGACACCATAAAAATACTTAAAGATGCGGGATATCATGTTAAGGCAAATGGAGTGGATGTAACAACACATCGTCAAGACATTAATGGGAAAGAAATGAAATTTGAAGTGTTAACATTAGCAAGCTTAACAACTGAAATTCAAATCAACATTGAGATAGAATCTAGAAAATCCTACAAAAAAATGCTAAAAGAAATGGGAGAGGTGGCTCCAGAATACAGGCATGACTCTCCTGATTGTGGGATGATAATATTATGTATAGCAGCATTAGTAATAACCAAATTAGCAGCAGGAGATAGATCAGGTCTTACAGCTGTGATTAGGAGAGCTAATAATGTCCTAAAAAATGAAATGAAACGTTATAAAGGTTTATTACCCAAGGATATAGCCAACAGCTTCTATGAAGTGTTTGAAAAATATCCTCACTTTATAGATGTTTTTGTTCATTTCGGTATAGCACAATCTTCCACCAGAGGTGGCAGTAGAGTTGAAGGGATTTTTGCAGGATTGTTTATGAATGCCTATGGTGCAGGGCAAGTGATGTTACGGTGGGGGGTCTTAGCAAAATCAGTTAAAAACATTATGTTAGGACACGCTAGTGTACAAGCAGAAATGGAACAAGTTGTGGAGGTGTATGAGTATGCTCAGAAATTGGGTGGAGAAGCAGGATTCTACCATATATTGAACAACCCAAAAGCATCACTATTATCTTTGACTCAATTTCCTCACTTCTCTAGTGTAGTATTGGGCAATGCTGCTGGCCTAGGCATAATGGGAGAATACAGAGGTACACCAAGGAATCAAGATTTATATGATGCTGCAAAAGTATATGCTGAACAACTCAAAGAAAATGGTGTGATTAACTACAGTGTATTAGATTTGACAGCAGAAGAACTAGAGGCTATCAAACATCAGCTTAATCCAAAAGATAATGATGTAGAGCTTTGAGTTAATAAAAAGGTGGGGCAAATAAATCATCATGGAAAAGTTTGCTCCTGAATTCCATGGAGAAGATGCAAACAACAGAGCCACCAAATTCCTAGAATCAATAAAAGGCAAATTCACATCACCCAAAGATCCCAAGAAAAAAGATAGTATCATATCTGTCAACTCAATAGATATAGAAGTAACCAAAGAAAGCCTTATAACATCAAATTCAACCATTATAAACCCAATAAATGAGACAGATGATACTGTAGGGAACAAGCCCAATTATCAAAGAAAGCCTCTAGTAAGTTTCAAAGAAGACCCTACGCCAAGTGATAATCCTTTTTCAAAACTATACAAAGAAACCATAGAAACATTTGATAACAATGAAGAAGAATCTAGCTATTCATATGAAGAAATAAATGATCAAACAAACGATAATATAACAGCAAGATTAGATAGGATTGATGAGAAATTAAGTGAAATACTAGGAATGCTTCACACATTAGTAGTAGCGAGTGCAGGACCCACATCTGCTCGGGATGGTATAAGAGATGCCATGGTTGGTTTAAGAGAAGAAATGATAGAAAAAATCAGAACTGAAGCATTAATGACCAATGACAGACTAGAAGCTATGGCAAGACTCAGGAATGAAGAAAGTGAAAAGATGGCAAAAGACACATCAGATGAAGTGTCTCTCAATCCAACATCAGAGAAACTGAACAACCTGTTGGAAGGGAATGATAGTGACAATGATCTATCACTTGAAGATTTCTGATTAGCTACCAAACTGTACATCAAAACACAACACCAATAGAAAACCAACAAACAAACCAACTCACCTATCCAACCAAACATCCATCTGCTGATTAGCCAACCAGCCAAAAAACAACCAGCTAATCCAAAACTAGCTACTCGAAAAAAATCGATACTATAGTTACAAAAAAAGATGGGGCAAATATGGAAACATACGTGAATAAACTTCACGAGGGCTCCACATACACAGCTGCTGTTCAATACAATGTCCTAGAAAAAGACGACGATCCTGCATCACTTACAATATGGGTGCCCATGTTCCAATCATCCATGCCAGCAGATCTACTCATAAAAGAACTAGCCAATGTCAATATACTAGTGAAACAAATATCCACACCCAAGGGACCCTCATTAAGAGTCATGATAAACTCAAGAAGTGCAGTGCTAGCACAAATGCCCAGTAAATTTACCATATGTGCCAATGTGTCCTTGGATGAAAGAAGCAAGCTGGCATATGATGTAACCACACCCTGTGAAATTAAAGCATGCAGTCTAACATGCCTAAAATCAAAAAATATGTTAACTACAGTTAAAGATCTCACCATGAAAACACTCAACCCAACACATGACATCATTGCTTTATGTGAATTTGAAAATATAGTAACATCAAAAAAAGTCATAATACCAACATACCTAAGATCTATCAGCGTCAGAAATAAAGATCTGAACACACTTGAAAATATAACAACCACTGAATTCAAAAATGCCATTACAAATGCAAAAATTATCCCTTACTCAGGATTACTGTTAGTCATCACAGTGACTGACAACAAAGGAGCATTCAAATACATAAAGCCACAAAGTCAATTCATAGTAGATCTTGGAGCTTACCTAGAAAAAGAAAGCATATATTATGTTACAACAAATTGGAAGCACACAGCTACACGATTTGCAATCAAACCCATGGAAGATTAACCTTTTTCCTCTACATCAATGAGTAGATTCATACAAACTTCCCAACTACATTCTTCACTTCACAATCATAATCACCAACCCTCTGTGGTTCAATCAATCAAACAAAACTCATCAGGAGTTCCAGATCATCCCAAGTCATTGTTCATCAGATCCAGTACTCAAATAAGTTAATAAAAAATCCACATGGGGCAAATAATCATTTAGGGAAATCCAACTAATCACAACATCTGTCAACATAGACAAGTCAGCACGCTAGATAAAATCAACCAATGGAAAATACATCCATAACTATAGAATTCTCAAGCAAATTCTGGCCTTACTTTACACTAATACACATGATAACAACAATAATCTCTTTGATAATAATAATCTCCATCATGATTGCAATACTAAACAAACTCTGCGAATATAATGTATTCCATAACAAAACCTTTGAGCTACCACGAGCTCGAGTCAATACATAGCATTCACCAATCTGATAGCTCAAAACAGTAACCTTGTATTTGTAAATGAACTACCCTCACTTCTTCACAAAACCACATCAACATCTCACCATGCAAGCCATCATCTATACCATAAAGTAGTTAATTAAAAAATAGTCATAACAATGAACTAGGATATTAAGACCAAAAACAACGCTGGGGCAAATGCAAACATGTCCAAAACCAAGGACCAACGCACCGCCAAGACACTAGAAAGGACCTGGGACACTCTCAATCATCTATTATTCATATCATCGTGCTTATACAAGTTAAATCTTAAATCTATAGCACAAATCACATTATCTATTTTGGCAATGATAATCTCAACCTCACTTATAATTGCAGCCATCATATTCATAGCCTCGGCAAACCACAAAGTCACACCAACAACTGCAATCATACAAGATGCAACGAACCAGATCAAGAACACAACCCCAACACACCTCACCCAGAATCCTCAGCTTGGAATCAGCCTCTCCAATCTGTCCGGAACTACATCACAATCCACCACCATACTAGCTTCAACAACACCAAGTGCTGAGTCAACCCCACAATCCACAACAGTCAAGATCATAAACACAACAACAACCCAAATATTACCTAGCAAACCCACCACAAAACAACGCCAAAATAAACCACAAAACAAACCCAACAATGATTTTCACTTTGAAGTGTTCAATTTTGTACCCTGCAGCATATGCAGCAACAATCCAACCTGCTGGGCCATCTGCAAGAGAATACCAAACAAAAAACCTGGAAAGAAAACCACCACCAAGCCCACAAAAAAACCAACCCTCAAGACAACCAAAAAAGATCCCAAACCTCAAACCACAAAACCAAAGGGAGTACTCACTACCAAGCCTACAGGAAAGCCAACCATCAACACCACTAAAACCAACAGCAGAACTACACTGCTCACCTCCAACACCAAAGGAAATCCAGAACACACAAGTCAAAAGGAAACCATCCACTCAACCACCTCCGAAGGCTATCCAAGCCCATCACAAGTCTATACAACATCCGATCAAGAGGAAACCCTCCACTCAACCACCTCCGAAGGCTATCCAAGCCCATCACAAGTCTATACAACATCCGAGTACCTATCACAATCTCTATCTTCATCCAACACAACAAAATGATAGTCATTAAAAAGCGTATTGTTGCAAAAGGCCATGACCAAATCAAACAGAATCAAAATCAACTTTGGGGCAAATAACAATGGAGTTGCCAATCCTCAAAACAAATGCTATTACCACAATCCTTGCTGCAGTCACACTCTGTTTTGCTTCCAGTCAAAACATCACTGAAGAATTTTATCAATCAACATGCAGTGCAGTTAGCAAAGGCTATCTTAGTGCTCTAAGAACTGGTTGGTATACTAGTGTTATAACTATAGAATTAAGTAATATCAAGGAAAATAAGTGTAATGGTACAGACGCTAAGGTAAAATTAATAAAACAAGAATTAGATAAATATAAAAATGCTGTAACAGAATTGCAGTTGCTCATGCAAAGCACACCAGCAGCCAACAGTCGAGCCAGAAGAGAACTACCAAGATTTATGAATTATACACTCAACAACACCAAAAACACCAATGTAACATTAAGTAAGAAAAGGAAAAGAAGATTTCTTGGATTTTTGTTAGGTGTTGGATCTGCAATCGCCAGTGGCATTGCCGTATCCAAGGTCCTGCACCTAGAAGGGGAAGTGAACAAAATCAAAAGTGCTCTACTATCCACAAACAAGGCTGTAGTCAGCTTATCTAATGGAGTCAGTGTCTTAACCAGCAAGGTGTTAGACCTCAAAAACTATATAGATAAACAGTTGTTACCTATTGTTAACAAGCAAAGTTGCAGCATATCAAACATTGAAACTGTGATAGAGTTCCAACAAAAGAACAACAGACTACTAGAGATTACCAGAGAATTTAGTGTTAATGCAGGTGTAACTACACCTGTAAGCACTTATATGTTAACTAATAGTGAGTTATTATCATTAATCAATGATATGCCTATAACAAATGATCAGAAAAAGTTAATGTCCAGCAATGTTCAAATAGTTAGACAGCAAAGTTACTCTATCATGTCAATAATAAAAGAGGAAGTCTTAGCATATGTAGTACAATTACCACTATATGGTGTAATAGATACTCCTTGTTGGAAACTACACACATCCCCTCTATGTACAACTAACACAAAGGAAGGATCCAACATCTGCTTAACAAGAACCGACAGAGGATGGTACTGTGACAATGCAGGATCAGTATCCTTTTTCCCACAAGCTGAAACATGTAAAGTTCAATCGAATCGGGTGTTTTGTGACACAATGAACAGTTTAACATTACCAAGTGAGGTAAATCTCTGCAACATTGACATATTCAACCCCAAATATGATTGCAAAATTATGACTTCAAAAACAGATGTAAGCAGCTCCGTTATCACATCTCTAGGAGCCATTGTGTCATGCTATGGCAAAACCAAATGTACAGCATCCAATAAAAATCGTGGGATCATAAAGACATTCTCTAATGGGTGTGATTATGTATCAAATAAGGGGGTGGATACTGTGTCTGTAGGTAATACATTATATTATGTAAATAAGCAAGAAGGCAAAAGTCTCTATGTAAAAGGTGAACCAATAATAAATTTCTATGATCCATTAGTGTTCCCCTCTGATGAATTTGATGCATCAATATCTCAAGTCAATGAGAAAATTAATCAGAGTCTAGCATTTATCCGTAAATCAGATGAATTATTACATAATGTAAATGCTGGTAAATCCACCACAAATATCATGATAACTACCATAATTATAGTAATTATAGTAATATTGTTAGCATTAATTGCAGTTGGACTGCTTCTATACTGCAAGGCCAGAAGCACACCAGTCACATTAAGTAAGGATCAACTGAGTGGTATAAATAACATTGCATTTAGTAACTGAATAAAAATAGCACCTAATCATATTCTTACAATGGTTCGCTATTTGACCATAGATAACCCATCTATAATTAGATTATCCTAAAATTTGAACTTCATCACAACTTTCATTTATAAACCATCTTACTTACACTTTTTAAGTAGATTCCTATTTTATAGTTATATAAAACAATTGAATACCAAATTAACTTACTATTTGTAAAAATGAGAACTGGGGCAAATATGTCACGAAGGAATCCTTGCAAATTCGAAATTCGAGGTCATTGCTTGAATGGTAAAAGGTGTCATTTTAGTCATAATTATTTTGAATGGCCACCCCATGCACTGCTTGTAAGACAAAACTTTATGTTAAACAGAATACTTAAGTCTATGGATAAAAGCATAGATACATTGTCAGAAATAAGTGGAGCTGCAGAGTTGGACAGAACAGAAGAGTATGCCCTCGGTGTAGTTGGAGTGCTAGAGAGTTATATAGGATCAATAAATAATATAACTAAACAATCAGCATGTGTTGCCATGAGCAAACTCCTTACTGAACTCAACAGCGATGACATCAAAAAACTAAGGGACAATGAAGAGCCAAACTCACCCAAAGTAAGAGTGTACAATACTGTCATATCATATATTGAAAGCAACAGGAAGAACAATAAACAAACTATCCATTTGTTAAAAAGATTGCCAGCAGACGTATTGAAGAAAACCATCAAAAACACATTGGATATCCACAAGAGCATAACCATCAATAACTCAAAAGAATCAACTGTTAGTGATACGAACGACCATGCCAAAAATAATGATACTACCTGACAAATATCCTTGTAGTATAAATTCCATACTAATAACAAGTAATTATAGAGTCACTATGTATAATCAAAAAAACACACTATATATCAATCAAAACAACCAAAATAGCCATATATACCCACCAGATCAACCATTCAATGAAATCCATTGGACCTCTCAAGACTTGATTGATGCAACTCAAAATTTTCTACAACATCTAGGTATTACTGATGATATATACACAATATATATATTAGTGTCATAATACTCAATCCTAATACTTACCACATCATCAAATTATTAACTCAAACAATTCAAGCTATGGGACAAAATGGATCCCATTATTAGTGGAAATTCTGCTAATGTTTATCTAACTGATAGTTATTTAAAAGGTGTTATTTCTTTCTCAGAATGTAACGCTTTAGGAAGTTACATATTCAATGGTCCTTATCTCAAAAATGATTATACCAACTTAATTAGTAGACAAAATCCATTAATAGAACACATAAATCTAAAGAAACTAAATATAACACAGTCCTTAATATCTAAGTATCATAAAGGTGAAATAAAAATAGAAGAACCTACTTACTTTCAGTCATTACTTATGACATACAAGAGTATGACCTCTTCAGAACAGACTACTACTACTAATTTACTTAAAAAGATAATAAGAAGAGCTATAGAAATCAGTGATGTCAAAGTCTATGCTATATTGAATAAACTGGGGCTCAAAGAAAAAGACAAGATTAAATCCAATAATGGACAAGATGAAGACAACTCAGTCATTACTACCATAATCAAAGATGATATACTTCTAGCTGTCAAGGATAATCAATCTCATCCTAAAGCAGACAAAAATCAATCCACGAAACAAAAAGATACAATCAAAACAACACTTTTGAAGAAATTAATGTGTTCAATGCAACATCCTCCATCATGGTTAATACATTGGTTTAATTTATACACAAAATTAAACAGCATATTAACACAATATCGATCTAGTGAGGTAAAAAACCATGGTTTTATATTGATAGATAATCATACTCTTAGTGGATTCCAATTTATTTTGAATCAATATGGTTGTATAGTTTATCATAGGGAACTCAAAAGAATTACTGTGACTACTTATAATCAATTCTTGACATGGAAAGATATTAGCCTTAGTAGATTAAATGTTTGTTTGATTACATGGATTAGTAACTGTTTGAACACATTAAACAAGAGCTTAGGCTTAAGATGTGGATTCAATAATGTTATCTTGACACAATTATTCCTTTATGGAGATTGTATACTAAAACTATTCCACAATGAGGGGTTCTACATAATAAAAGAGGTAGAGGGATTTATTATGTCTCTAATTTTAAATATAACAGAAGAAGATCAATTCAGAAAACGGTTTTATAATAGTATGCTCAACAACATCACAGATGCCGCCAACAAAGCTCAAAAAAATCTGCTATCAAGAGTATGTCATACATTATTAGATAAGACAATATCAGATAATATAATAAATGGCAGATGGATAATTCTATTGAGTAAGTTCCTAAAATTAATTAAGCTTGCAGGTGACAATAACCTCAACAATCTGAGTGAATTATATTTTTTGTTCAGAATATTTGGACACCCAATGGTAGATGAAAGACAAGCCATGGATGCTGTTAAAGTTAATTGCAACGAGACCAAATTTTACTTGTTAAGTAGTTTGAGTATGTTAAGAGGAGCTTTTATATATAGAATTATAAAAGGGTTTGTAAATAATTACAACAGATGGCCTACTTTAAGAAATGCCATTGTCTTACCCTTAAGATGGTTAACTTACTATAAACTAAACACTTATCCTTCCTTGTTGGAACTTACAGAAAGAGATTTGATTGTTCTATCAGGACTACGTTTCTATCGAGAGTTTCGGTTGCCTAAAAAAGTGGATCTTGAAATGATCATAAATGATAAGGCTATATCACCTCCTAAAAATTTAATATGGACTAGTTTCCCTAGAAATTATATGCCATCACACATACAAAATTATATAGAACATGAAAAATTAAAATTCTCTGATAGTGATAAATCAAGAAGAGTATTAGAGTATTATTTAAGAGATAACAAATTCAATGAATGTGATTTATACAACTGTGTAGTTAATCAAAGTTATCTTAACAACCCGAATCATGTGGTATCATTGACAGGCAAAGAAAGAGAACTCAGTGTAGGTAGAATGTTTGCAATGCAACCAGGAATGTTCAGACAAGTTCAAATATTAGCAGAGAAAATGATAGCAGAAAACATATTACAATTTTTCCCTGAAAGTCTTACAAGATATGGTGATCTAGAACTACAGAAAATATTAGAATTGAAAGCAGGAATAAGTAACAAATCAAATCGTTACAATGATAATTACAACAATTACATTAGTAAGTGCTCTATCATCACAGATCTCAGCAAATTCAATCAAGCATTTCGATATGAAACATCATGTATTTGTAGTGATGTACTGGATGAACTGCATGGTGTACAATCTCTATTTTCCTGGTTACATTTAACTATTCCTCATGTCACAATAATATGCACATATAGGCATGCACCCCCCTATATAAAGGATCATATTGTAGATCTTAACAATGTAGATGAGCAAAGTGGACTATATAGATATCATATGGGTGGTATCGAAGGGTGGTGTCAAAAACTATGGACCATAGAAGCTATATCACTATTAGATCTAATATCTCTCAAAGGGAAATTCTCAATTACTGCTTTAATTAATGGTGACAATCAATCAATAGATATAAGTAAACCAGTCAGACTCATGGAAGGTCAAACTCATGCTCAAGCAGATTATTTGCTAGCATTAAATAGTCTCAAATTACTGTATAAAGAGTATGCAGGAATAGGCCACAAATTAAAAGGAACTGAGACTTATATATCGAGGGATATGCAATTTATGAGTAAAACGATCCAACATAACGGTGTATATTACCCAGCTAGTATAAAGAAAGTCCTAAGAGTGGGACCGTGGATAAACACTATACTTGATGACTTCAAAGTGAGTCTAGAATCTATAGGTAGTTTGACACAAGAATTAGAATATAGAGGTGAAAGTCTATTATGCAGTTTAATATTTAGAAATGTATGGTTATATAATCAAATTGCATTACAACTTAAAAATCATGCATTATGTAACAACAAATTATATTTGGATATATTAAAAGTTCTAAAACACTTAAAAACCTTTTTTAATCTTGATAACATTGATACAGCATTAACATTGTATATGAATTTGCCCATGTTATTTGGTGGTGGTGATCCCAACTTGTTATATCGAAGTTTCTATAGAAGAACTCCTGATTTCCTCACAGAGGCTATAGTTCACTCTGTGTTCATACTTAGTTATTATACAAACCATGATTTAAAAGATAAACTTCAAGATCTGTCAGATGATAGATTGAATAAGTTCTTAACATGCATAATCACGTTTGACAAAAACCCCAATGCTGAATTCGTTACATTGATGAGAGATCCTCAAGCTTTAGGATCTGAGAGGCAAGCTAAAATTACTAGCGAAATCAATAGACTGGCAGTTACCGAGGTTTTGAGCACAGCTCCAAACAAAATATTTTCCAAAAGTGCACAACACTATACCACTACAGAGATAGATCTTAATGATATTATGCAAAATATAGAACCTACATATCCTCACGGGCTAAGAGTTGTTTATGAAAGTTTACCCTTTTATAAAGCAGAGAAAATAGTAAATCTTATATCCGGTACAAAATCTATAACTAACATACTGGAAAAGACTTCTGCCATAGACTTAACAGATATTGATAGAGCCACTGAGATGATGAGGAAAAACATAACTTTGCTTATAAGGATATTACCATTAGATTGTAACAGAGATAAAAGAGAAATATTGAGTATGGAAAACCTAAGTATTACTGAATTAAGCAAATACGTTAGAGAAAGATCCTGGTCTTTATCCAATATAGTTGGTGTTACATCACCCAGTATCATGTATACAATGGACATAAAATATACAACAAGCACTATAGCTAGTGGCATAATCATAGAGAAATATAATGTCAACAGTTTAACACGTGGTGAGAGAGGACCCACTAAACCATGGGTTGGTTCATCTACACAAGAGAAAAAGACAATGCCAGTTTATAATAGACAAGTTTTAACCAAAAAACAGAGAGATCAAATAGATCTATTAGCAAAATTGGATTGGGTGTATGCATCTATAGATAACAAGGATGAATTTATGGAGGAACTTAGCATAGGAACTCTTGGGTTAACATATGAGAAGGCCAAAAAATTATTCCCACAATATTTAAGTGTTAACTATTTGCATCGTCTTACAGTCAGTAGTAGACCATGTGAATTCCCTGCATCTATACCAGCTTATAGAACTACAAATTATCACTTTGATACTAGCCCTATTAATCGCATATTAACAGAAAAGTATGGTGATGAAGATATTGATATAGTATTCCAAAACTGTATAAGCTTTGGCCTCAGCTTAATGTCTGTAGTAGAACAATTTACTAATGTATGTCCTAACAGAATTATTCTCATACCCAAGCTTAATGAGATACATTTGATGAAACCTCCCATATTCACAGGTGATGTTGATATTCACAAGTTAAAACTAGTGATACAAAAACAACATATGTTTTTACCAGACAAAATAAGTTTGACTCAATATGTGGAATTATTCTTAAGTAATAAAACACTCAAATCTGGATCTAATGTTAATTCTAATTTAATATTGGCGCATAAGATATCTGACTATTTTCATAATACTTACATTTTAAGTACTAATTTAGCTGGACATTGGATTCTTATTATACAACTTATGAAAGATTCTAAGGGTATTTTTGAAAAAGATTGGGGAGAGGGATATATAACTGATCATATGTTCATTAATTTGAAAGTTTTCTTCAATGCTTATAAGACATATCTCTTGTGTTTTCACAAAGGTTACGGCAGAGCAAAGCTGGAGTGTGATATGAATACTTCAGATCTCCTATGTGTATTGGAATTAATAGACAGTAGTTATTGGAAGTCTATGTCTAAGGTGTTTTTAGAACAAAAAGTTATCAAATACATTCTTAGCCAAGATGCAAGTTTACATAGAGTAAAAGGATGTCATAGCTTCAAACTATGGTTTCTTAAACGTCTTAATGTAGCAGAATTCACAGTTTGCCCTTGGGTTGTTAACATAGATTATCATCCAACACATATGAAAGCAATATTAACTTATATTGATCTTGTTAGAATGGGATTGATAAATATAGATAGAATATACATTAAAAATAAACACAAGTTCAATGATGAGTTTTATACTTCTAATCTGTTTTACATTAATTATAACTTCTCAGATAATACTCATCTATTAACTAAACATATAAGGATTGCTAATTCCGAATTAGAAAGTAATTACAACAAATTATATCATCCCACACCAGAAACCCTAGAAAATATACTAACCAATCCGGTTAAAAATAATGAAAAAAAGACACTGAGTGGCTATTGTATAGGTAAAAATGTTGACTCAATAATGTTACCATCGTTATCTAATAAGAAGCTTATTAAATCGTCTACTATGATTAGAACCAATTACAGCAGACAAGATTTGTATAATTTATTTCCTACGGTTGTGATTGATAAAATTATAGATCATTCAGGTAATACAGCCAAATCTAACCAACTTTACACTACTACTTCTCATCAAATATCCTTAGTGCACAATAGCACATCACTTTATTGCATGCTTCCTTGGCATCATATTAATAGATTCAATTTTGTATTTAGTTCTACAGGTTGTAAAATTAGTATAGAGTATATTTTAAAAGATCTTAAAATTAAGGATCCTAATTGTATAGCATTCATAGGTGAAGGAGCAGGGAATTTATTATTGCGTACAGTAGTGGAACTTCATCCTGATATAAGATATATTTACAGAAGTCTGAAAGATTGCAATGATCATAGTTTACCAATTGAGTTTTTAAGGCTGTACAATGGACATATCAACATTGATTATGGTGAAAATTTGACCATTCCTGCTACAGATGCAACCAACAACATTCATTGGTCTTATTTACATATAAAGTTTGCTGAACCTATCAGTCTTTTTGTCTGTGATGCTGAATTGCCTGTAACAGTCAACTGGAGTAAGATTATAATAGAGTGGAGCAAGCATGTAAGAAAATGCAAATACTGCTCTTCAGTTAATAAATGTACATTAATAGTAAAATATCATGCTCAAGATGATATCGATTTCAAATTAGACAACATAACTATATTAAAAACTTATGTATGCTTAGGTAGTAAGTTAAAGGGATCTGAAGTTTACTTAGTCCTTACAATAGGTCCTGCAAATGTGTTCCCAGTATTTAATGTAGTACAAAATGCTAAATTGATACTATCAAGAACCAAAAATTTCATCATGCCTAAAAAAGCTGATAAAGAGTCTATTGATGCAAATATTAAGAGTTTGATACCCTTTCTTTGTTACCCCATAACAAAAAAAGGAATTAATACTGCATTGTCTAAATTAAAGAGTGTTGTTAGTGGAGATATACTATCATATTCTATAGCTGGACGTAATGAAGTTTTCAGCAATAAACTTATAAATCATAAGCATATGAACATCTTAAAGTGGTTCAATCATGTTTTGAATTTCAGATCAACAGAATTAAACTATAATCATTTATATATGGTAGAATCTACTTATCCTCATCTAAGTGAATTGTTAAACAGCTTGACAACCAATGAACTTAAAAAACTGATTAAAATCACAGGTAGTTTGTTATACAACTTTTATAATGAATAATGAGCAAAAATCTTATAACAAAAATAGCTACACACTAACATTGTATTCAATTATAGTTATTTAAAATTAATAATTATATAATTTTTAATAACTTCTAGTGAACTAATCCTAAAATTATCATTTTGATCTAGGAAGAATAAGTTTAAATCCAAATCTAATTGGTTTATATGTATATTGACTAAATTACGAGATATTA'

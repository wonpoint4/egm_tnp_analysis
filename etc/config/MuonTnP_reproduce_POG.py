from libPython.tnpClassUtils import tnpSample
#############################################################
########## Setting (IsoMu24, Mu50 || OldMu100 || TkMu100) vs pT, eta, tag_nVertices
############################################################# 

wonjuntnpdir = '/data9/Users/wonjun/public/TnP_Trees/'
filename = 'TnPTreeZ_12Nov2019_UL2018_SingleMuon_Run2018ABCDv2.root'
filenameMC = 'TnPTreeZ_106XSummer19_UL18RECO_DYJetsToLL_M50_MadgraphMLM_WithWeights.root'

baseOutDir = 'UL2018_POG_Reproduce/IsoMu24_nvtx/'
passcondition = 'IsoMu24'
eventexp = '(tag_IsoMu24==1 && tag_pt > 26 && mass > 60 && mass < 130 && tag_abseta < 2.4 && Tight2012 && combRelIsoPF04dBeta < 0.15 && pair_deltaR > 0.3)'

#baseOutDir = 'UL2018_POG_Reproduce/Mu50_eta/'#pt/'#eta/'#nvtx/'
#passcondition = 'Mu50 || OldMu100 || TkMu100'
#eventexp = '(tag_IsoMu24==1 && tag_pt > 26 && mass > 60 && mass < 130 && tag_abseta < 2.4 && CutBasedIdGlobalHighPt_new && relTkIso < 0.10 && pair_deltaR > 0.3)'

eventexpMC = eventexp+' * (weight<4?weight:4)'
eventexpGen = eventexpMC.replace('mass > 60', 'mcTrue && mass > 60')

#############################################################
########## Binning Definition  [can be nD bining]
#############################################################
#biningDef = [    { 'var' : 'eta' , 'type': 'float', 'bins': [-2.4, 2.4] },
#                 { 'var' : 'pt' , 'type': 'float', 'bins': [2, 18, 22, 24, 26, 30, 40, 50, 60, 120, 200, 300, 500, 1200] } ]
#                 { 'var' : 'pt' , 'type': 'float', 'bins': [2, 44, 48, 50, 52, 56, 60, 120, 200, 300, 500, 1200] } ]

#biningDef = [    { 'var' : 'eta' , 'type': 'float', 'bins': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4] },
#                 { 'var' : 'pt' , 'type': 'float', 'bins': [26,9999] } ]
#                 { 'var' : 'pt' , 'type': 'float', 'bins': [52,9999] } ]

biningDef = [    { 'var' : 'tag_nVertices' , 'type': 'float', 'bins': [0.5, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 26.5, 28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5, 44.5, 46.5, 48.5, 50.5, 52.5, 54.5, 56.5, 58.5, 60.5] },
                 { 'var' : 'pt' , 'type': 'float', 'bins': [26,9999] } ]
#                 { 'var' : 'pt' , 'type': 'float', 'bins': [52,9999] } ]

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
## Convolution with Gaussian, and Exponential for Bkg
tnpParNomFit = [
    "meanGaussP[0.0, -5.0,5.0]","sigmaGaussP[0.8, 0.5,3.5]",  ## [0.5, 0.4,5.0]
    "meanGaussF[0.0, -5.0,5.0]","sigmaGaussF[0.7, 0.5,3.5]", ## [0.5, 0.4,5.0]
    "aExpoP[-0.1, -1,0.1]",
    "aExpoF[-0.1, -1,0.1]",
    "Gaussian::sigResPass(mass,meanGaussP,sigmaGaussP)",
    "Gaussian::sigResFail(mass,meanGaussF,sigmaGaussF)",
    "Exponential::backgroundPass(mass, aExpoP)",
    "Exponential::backgroundFail(mass, aExpoF)",
    ]
## Convolution with CBShape, and Exponential for Bkg
tnpParNomFit2 = [
    "meanCBP[0.0, -5.0,5.0]","sigmaCBP[1, 0.5,3.5]","aCBP[2.0, 1.2,3.5]",'nCBP[3, 0.1,5]',
    "meanCBF[0.0, -5.0,5.0]","sigmaCBF[2, 0.5,3.5]","aCBF[2.0, 1.2,3.5]",'nCBF[3, 0.1,5]',
    "aExpoP[-0.1, -1,0.1]",
    "aExpoF[-0.1, -1,0.1]",
    "RooCBShape::sigResPass(mass,meanCBP,sigmaCBP,aCBP,nCBP)",
    "RooCBShape::sigResFail(mass,meanCBF,sigmaCBF,aCBF,nCBF)",
    "Exponential::backgroundPass(mass, aExpoP)",
    "Exponential::backgroundFail(mass, aExpoF)",
    ]
## Convolution with Gaussian, and RooCMS for Bkg
tnpParAltBkgFit = [
    "meanGaussP[0.0, -5.0,5.0]","sigmaGaussP[0.8, 0.5,2.5]",
    "meanGaussF[0.0, -5.0,5.0]","sigmaGaussF[1.2, 0.55,2.5]",
    "aCMSP[60., 50.,80.]","bCMSP[0.05, 0.01,0.08]","cCMSP[0.1, 0, 1]","peakCMSP[90.0]",
    "aCMSF[60., 50.,80.]","bCMSF[0.05, 0.01,0.08]","cCMSF[0.1, 0, 1]","peakCMSF[90.0]",
    "Gaussian::sigResPass(mass,meanGaussP,sigmaGaussP)",
    "Gaussian::sigResFail(mass,meanGaussF,sigmaGaussF)",
    "RooCMSShape::backgroundPass(mass, aCMSP, bCMSP, cCMSP, peakCMSP)",
    "RooCMSShape::backgroundFail(mass, aCMSF, bCMSF, cCMSF, peakCMSF)",
    ]
     
tnpParAltSigFit = [
    #"meanP[0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",  ## These are used at CBExGaussShape funtion
    #"meanF[0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"aCMSP[60.,50.,75.]","bCMSP[0.04,0.01,0.06]","cCMSP[0.1, 0.005, 1]","peakCMSP[90.0]",                                     ## These are used at CMS function
    #"aCMSF[60.,50.,75.]","bCMSF[0.04,0.01,0.06]","cCMSF[0.1, 0.005, 1]","peakCMSF[90.0]",
    "meanCBP[0.0, -5.0,5.0]","sigmaCBP[1, 0.5,2.5]","aCBP[2.0, 1.2,3.5]",'nCBP[3, 0.1,5]', #Sigma 1, 0.4,6
    "meanCBF[0.0, -5.0,5.0]","sigmaCBF[2, 0.5,2.5]","aCBF[2.0, 1.2,3.5]",'nCBF[3, 0.1,5]', #Sigma 2, 0.4,15
    "aExpoP[-0.1, -1,0.1]",
    "aExpoF[-0.1, -1,0.1]",
    "Exponential::backgroundPass(mass, aExpoP)",
    "Exponential::backgroundFail(mass, aExpoF)",
    ]
tnpParAltSigFit2 = [
    "meanCBP[0.0, -5.0,5.0]","sigmaCBP[1, 0.4,2.5]","aCBP[2.0, 1.2,3.5]",'nCBP[3, 0.1,5]', #Sigma 1, 0.4,6
    "meanCBF[0.0, -5.0,5.0]","sigmaCBF[2, 0.4,2.5]","aCBF[2.0, 1.2,3.5]",'nCBF[3, 0.1,5]', #Sigma 2, 0.4,15
    "aCMSP[60., 50.,80.]","bCMSP[0.05, 0.01,0.08]","cCMSP[0.1, 0, 1]","peakCMSP[90.0]",
    "aCMSF[60., 50.,80.]","bCMSF[0.05, 0.01,0.08]","cCMSF[0.1, 0, 1]","peakCMSF[90.0]",
    "RooCMSShape::backgroundPass(mass, aCMSP, bCMSP, cCMSP, peakCMSP)",
    "RooCMSShape::backgroundFail(mass, aCMSF, bCMSF, cCMSF, peakCMSF)",
    ]

#############################################################
########## Setting Systematic
#############################################################

flags = {
    'data'              : tnpSample([wonjuntnpdir+filename],eventexp,tnpParNomFit,60,70,130,81,101),
    'data_altsig'       : tnpSample([wonjuntnpdir+filename],eventexp,tnpParNomFit2,60,70,130,81,101),
    'data_massbroad'    : tnpSample([wonjuntnpdir+filename],eventexp,tnpParNomFit,70,60,130,76,106),
    'data_massnarrow'   : tnpSample([wonjuntnpdir+filename],eventexp,tnpParNomFit,50,70,120,86,96),
    'data_massbin50'    : tnpSample([wonjuntnpdir+filename],eventexp,tnpParNomFit,50,70,130,81,101),
    'data_massbin75'    : tnpSample([wonjuntnpdir+filename],eventexp,tnpParNomFit,75,70,130,81,101),
    'data_tagiso015'    : tnpSample([wonjuntnpdir+filename],eventexp.replace('tag_abseta < 2.4','tag_abseta < 2.4 && tag_combRelIsoPF04dBeta < 0.15'),tnpParNomFit,60,70,130,81,101),
#    'data_tagiso010'    : tnpSample([wonjuntnpdir+filename],eventexp.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.1'),tnpParNomFit,60,70,130,81,101),
#    'data_tagiso020'    : tnpSample([wonjuntnpdir+filename],eventexp.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.2'),tnpParNomFit,60,70,130,81,101),
 
    'mc'                : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit,60,70,130,81,101),
    'mc_altsig'         : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit2,60,70,130,81,101),
    'mc_massbroad'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit,70,60,130,76,106),
    'mc_massnarrow'     : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit,50,70,120,86,96),
    'mc_massbin50'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit,50,70,130,81,101),
    'mc_massbin75'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit,75,70,130,81,101),
    'mc_tagiso015'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC.replace('tag_abseta < 2.4','tag_abseta < 2.4 && tag_combRelIsoPF04dBeta < 0.15'),tnpParNomFit,60,70,130,81,101),
#    'mc_tagiso010'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.1'),tnpParNomFit,60,70,130,81,101),
#    'mc_tagiso020'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.2'),tnpParNomFit,60,70,130,81,101),
 
    'genmc'             : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit,60,70,130,81,101),
    'genmc_altsig'      : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit2,60,70,130,81,101),
    'genmc_massbroad'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit,70,60,130,76,106),
    'genmc_massnarrow'  : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit,50,70,120,86,96),
    'genmc_massbin50'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit,50,70,130,81,101),
    'genmc_massbin75'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit,75,70,130,81,101),
    'genmc_tagiso015'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen.replace('tag_abseta < 2.4','tag_abseta < 2.4 && tag_combRelIsoPF04dBeta < 0.15'),tnpParNomFit,60,70,130,81,101),
#    'genmc_tagiso010'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.1'),tnpParNomFit,60,70,130,81,101),
#    'genmc_tagiso020'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.2'),tnpParNomFit,60,70,130,81,101),
}

systematicDef = {
    'data' : [['data_massbroad','data_massnarrow'], ['data_massbin50','data_massbin75'],['data_tagiso015'], ['data_altsig']],
    'mc' :   [['mc_massbroad','mc_massnarrow'],     ['mc_massbin50','mc_massbin75'],    ['mc_tagiso015'],     ['mc_altsig']]
#    'data' : [['data_massbroad','data_massnarrow'], ['data_tagiso015']],
#    'mc' :   [['mc_massbroad','mc_massnarrow'],     ['mc_tagiso015']]
}

#############################################################
########## Cuts definition for all samples
#############################################################

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
#### or remove any additional cut (default)
additionalCuts = None


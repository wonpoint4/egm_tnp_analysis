from libPython.tnpClassUtils import tnpSample
#############################################################
########## Setting
############################################################# 

#### Choose one of these ####################
#Period = {'2016BF', '2016GH', '2017', '2018', 'UL2016a', 'UL2016b', 'UL2017', 'UL2018' }
#Measure = {'IDISO', 'Mu17', 'Mu8', 'IsoMu24', 'IsoMu27' }
#Charge = {'+', '-', 'all' }

Period = 'UL2018'
Measure = 'IDISO'
Charge = '+'

#############################################################
########## General Settings (default = 'UL2018', 'Mu17', 'all')
#############################################################
if Period == '2017' and Measure == 'IsoMu24' :
  Measure = 'IsoMu27'
#elif Period == 'UL2017' and Measure == 'IsoMu24' :
#  #Measure = 'IsoMu2427'
if '2017' not in Period and Measure == 'IsoMu27' :
  Measure = 'IsoMu24'

baseOutDir = Period+'_'+Measure+'_'+Charge+'_MiNNLO/'
baseOutDir = Period+'_'+Measure+'_'+Charge+'/'

passcondition = 'DoubleIsoMu17Mu8_IsoMu17leg || DoubleIsoMu17TkMu8_IsoMu17leg'
eventexp = 'tag_IsoMu24==1 && tag_pt > 26 && mass > 60 && mass < 130 && tag_charge*charge < 0 && tag_combRelIsoPF04dBeta < 0.15 && Medium && relTkIso < 0.10 && pair_deltaR > 0.3'

wonjuntnpdir = '/data9/Users/wonjun/public/TnP_Trees/'
filename = 'TnPTreeZ_12Nov2019_UL2018_SingleMuon_Run2018ABCDv2.root'
filenameMC = 'TnPTreeZ_106XSummer19_UL18RECO_DYJetsToLL_M50_MadgraphMLM_WithWeights.root'

#### Measure Option ########################################################
if Measure == 'Mu8' :
  passcondition = 'DoubleIsoMu17Mu8_IsoMu8leg || DoubleIsoMu17TkMu8_IsoMu8leg'
elif Measure == 'IsoMu27' :
  passcondition = 'IsoMu27'
  eventexp = eventexp.replace('tag_IsoMu24==1 && tag_pt > 26', 'tag_IsoMu27==1 && tag_pt > 29')
elif Measure == 'IsoMu2427' :
  passcondition = 'IsoMu24 || IsoMu27'
  eventexp = eventexp.replace('tag_IsoMu24==1 && tag_pt > 26', 'tag_IsoMu27==1 && tag_pt > 29')
elif Measure == 'IsoMu24' :
  if '2016' in Period :
    passcondition = 'IsoMu24 || IsoTkMu24'
  else :
    passcondition = 'IsoMu24'
elif Measure == 'IDISO' :
  passcondition = 'Medium && relTkIso < 0.10'
  eventexp = eventexp.replace('Medium && relTkIso < 0.10', 'TM')

#### Charge Option ########################################################
if Charge == "+" :
  eventexp = eventexp.replace('tag_charge*charge < 0','tag_charge*charge < 0 && charge > 0')
elif Charge == "-" :
  eventexp = eventexp.replace('tag_charge*charge < 0','tag_charge*charge < 0 && charge < 0')

#### Period Option ########################################################
if Period == "2016BF" :
  wonjuntnpdir = '/data9/Users/wonjun/public/TnP_Trees/TnPTreeZ_LegacyRereco07Aug17_SingleMuon_Run2016/'
  filename = 'TnPTreeZ_LegacyRereco07Aug17_SingleMuon_BCDEF.root'
  filenameMC = 'DY_Summer16PremixMoriond_weighted_BCDEF.root'
  if Measure == 'IDISO':
    passcondition = passcondition.replace('Medium','Medium2016') #From Simranjit's presentation
  else :
    eventexp = eventexp.replace('Medium','Medium2016')
elif Period == "2016GH" :
  wonjuntnpdir = '/data9/Users/wonjun/public/TnP_Trees/TnPTreeZ_LegacyRereco07Aug17_SingleMuon_Run2016/'
  filename = 'TnPTreeZ_LegacyRereco07Aug17_SingleMuon_GH.root'
  filenameMC = 'DY_Summer16PremixMoriond_weighted_GH.root'
elif Period == "2017" :
  eventexp = eventexp.replace('tag_IsoMu24==1 && tag_pt > 26', 'tag_IsoMu27==1 && tag_pt > 29')
  wonjuntnpdir = '/data9/Users/wonjun/public/TnP_Trees/TnPTreeZ_17Nov2017_SingleMuon_Run2017/'
  filename = 'TnPTreeZ_17Nov2017_SingleMuon_Run2017BCDEFv1_GoldenJSON.root'
  filenameMC = 'TnPTreeZ_94X_DYJetsToLL_M50_Madgraph_WithWeights.root'
elif Period == "2018" :
  wonjuntnpdir = '/data9/Users/wonjun/public/TnP_Trees/TnPTreeZ_EarlyRereco_PromptReco_17Sep2018_SingleMuon_Run2018/'
  filename = 'TnPTreeZ_17Sep2018_SingleMuon_Run2018ABCD_GoldenJSON.root'
  filenameMC = 'TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_weighted_ABCD.root'

### Ultra Legacy ###
elif Period == "UL2016a" :
  filename = 'TnPTreeZ_21Feb2020_UL2016_SingleMuon_Run2016BCDEF_HIPMv1.root'
  filenameMC = 'TnPTreeZ_106XSummer19_UL16RECOAPV_DYJetsToLL_M50_MadgraphMLM_WithWeights.root'
  ##filenameMC = 'TnPTreeZ_106XSummer19_UL16RECOAPV_DYJetsToMuMu_M50_powhegMiNNLO_WithWeights.root'
  if Measure == 'IDISO':
    passcondition = passcondition.replace('Medium','Medium2016') #From Simranjit's presentation
  else :
    eventexp = eventexp.replace('Medium','Medium2016')
  #From KyeongPil's presentation
  eventexp = eventexp.replace('pair_deltaR > 0.3','pair_deltaR > 0.3 && !(tag_eta*eta > 0 && abs(tag_eta) > 0.9 && abs(eta) > 0.9 && abs(tag_phi-phi) < 70/180*3.141592)')
elif Period == "UL2016b" :
  filename = 'TnPTreeZ_21Feb2020_UL2016_SingleMuon_Run2016FGHv1.root'
  filenameMC = 'TnPTreeZ_106XSummer19_UL16RECO_DYJetsToLL_M50_MadgraphMLM_WithWeights.root'
  ##filenameMC = 'TnPTreeZ_106XSummer19_UL16RECO_DYJetsToMuMu_M50_powhegMiNNLO_WithWeights.root'
elif Period == "UL2017" :
  if Measure != 'IsoMu24' :
    eventexp = eventexp.replace('tag_IsoMu24==1 && tag_pt > 26', 'tag_IsoMu27==1 && tag_pt > 29')
  filename = 'TnPTreeZ_09Aug2019_UL2017_SingleMuon_Run2017BCDEFv1.root'
  filenameMC = 'TnPTreeZ_106XSummer19_UL17RECO_DYJetsToLL_M50_MadgraphMLM_pdfwgt_F_WithWeights.root'

eventexpMC = '('+eventexp+') * weight'
eventexpGen = eventexpMC.replace('mass > 60', 'mcTrue && mass > 60')

#############################################################
########## Binning Definition  [can be nD bining]
#############################################################
biningDef = [              ### For IDISO or Mu8 
    { 'var' : 'eta' , 'type': 'float', 'bins': [-2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4] },
    { 'var' : 'pt' , 'type': 'float', 'bins': [10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 120] },
]
if Measure == 'Mu17' :
  biningDef = [            ### For Mu17
    { 'var' : 'eta' , 'type': 'float', 'bins': [-2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4] },
    #{ 'var' : 'pt' , 'type': 'float', 'bins': [20, 25, 30, 35, 40, 45, 50, 60, 120] },
    { 'var' : 'pt' , 'type': 'float', 'bins': [14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 120] }, 
  ]
elif Measure == 'IsoMu27' and Period == "2017" :
  biningDef = [          ### For IsoMu27 (Regacy 2017)
      { 'var' : 'eta' , 'type': 'float', 'bins': [-2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4] },
      { 'var' : 'pt' , 'type': 'float', 'bins': [29, 32, 35, 40, 45, 50, 60, 120] },
  ]
elif Measure == 'IsoMu24' or Measure == 'IsoMu2427' or Measure == 'IsoMu27':
  biningDef = [          ### For IsoMu24 or (IsoMu24 || IsoMu27)
      { 'var' : 'eta' , 'type': 'float', 'bins': [-2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4] },
      #{ 'var' : 'pt' , 'type': 'float', 'bins': [26, 30, 35, 40, 45, 50, 60, 120] },
      { 'var' : 'pt' , 'type': 'float', 'bins': [20, 22, 24, 26, 28, 30, 35, 40, 45, 50, 60, 120] },
  ]

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
## Convolution with Gaussian, and Exponential for Bkg
tnpParNomFit = [
    "meanGaussP[0.0, -5.0,5.0]","sigmaGaussP[0.8, 0.5,2.5]",  ## [0.5, 0.4,5.0]
    "meanGaussF[0.0, -5.0,5.0]","sigmaGaussF[0.7, 0.5,2.5]", ## [0.5, 0.4,5.0]
    "aExpoP[-0.1, -1,0.1]",
    "aExpoF[-0.1, -1,0.1]",
    "Gaussian::sigResPass(mass,meanGaussP,sigmaGaussP)",
    "Gaussian::sigResFail(mass,meanGaussF,sigmaGaussF)",
    "Exponential::backgroundPass(mass, aExpoP)",
    "Exponential::backgroundFail(mass, aExpoF)",
    ]
## Convolution with CBShape, and Exponential for Bkg
tnpParNomFit2 = [
    "meanCBP[0.0, -5.0,5.0]","sigmaCBP[1, 0.5,2.5]","aCBP[2.0, 1.2,3.5]",'nCBP[3, 0.1,5]',
    "meanCBF[0.0, -5.0,5.0]","sigmaCBF[2, 0.5,2.5]","aCBF[2.0, 1.2,3.5]",'nCBF[3, 0.1,5]',
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
    'data_tagiso010'    : tnpSample([wonjuntnpdir+filename],eventexp.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.1'),tnpParNomFit,60,70,130,81,101),
    'data_tagiso020'    : tnpSample([wonjuntnpdir+filename],eventexp.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.2'),tnpParNomFit,60,70,130,81,101),
    #'data_altbkd'       : tnpSample([wonjuntnpdir+filename],eventexp,tnpParAltBkgFit,40,70,130),

    'mc'                : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit,60,70,130,81,101),
    'mc_altsig'         : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit2,60,70,130,81,101),
    'mc_massbroad'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit,70,60,130,76,106),
    'mc_massnarrow'     : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit,50,70,120,86,96),
    'mc_massbin50'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit,50,70,130,81,101),
    'mc_massbin75'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParNomFit,75,70,130,81,101),
    'mc_tagiso010'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.1'),tnpParNomFit,60,70,130,81,101),
    'mc_tagiso020'      : tnpSample([wonjuntnpdir+filenameMC],eventexpMC.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.2'),tnpParNomFit,60,70,130,81,101),
    #'mc_altsig2'         : tnpSample([wonjuntnpdir+filenameMC],eventexpMC,tnpParAltBkgFit,40,70,130), 

    'genmc'             : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit,60,70,130,81,101),
    'genmc_altsig'      : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit2,60,70,130,81,101),
    'genmc_massbroad'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit,70,60,130,76,106),
    'genmc_massnarrow'  : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit,50,70,120,86,96),
    'genmc_massbin50'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit,50,70,130,81,101),
    'genmc_massbin75'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen,tnpParNomFit,75,70,130,81,101),
    'genmc_tagiso010'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.1'),tnpParNomFit,60,70,130,81,101),
    'genmc_tagiso020'   : tnpSample([wonjuntnpdir+filenameMC],eventexpGen.replace('tag_combRelIsoPF04dBeta < 0.15','tag_combRelIsoPF04dBeta < 0.2'),tnpParNomFit,60,70,130,81,101),
}

systematicDef = {
    'data' : [['data_massbroad','data_massnarrow'], ['data_massbin50','data_massbin75'],['data_tagiso010','data_tagiso020'], ['data_altsig']],
    'mc' :   [['mc_massbroad','mc_massnarrow'],     ['mc_massbin50','mc_massbin75'],    ['mc_tagiso010','mc_tagiso020'],     ['mc_altsig']]
}

#############################################################
########## Cuts definition for all samples
#############################################################

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
#### or remove any additional cut (default)
additionalCuts = None


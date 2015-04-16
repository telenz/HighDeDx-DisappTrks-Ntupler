//-----------------------------------------------------------------------------
// Subsystem:   Ntuples
// Package:     MyNtuple
// Description: TheNtupleMaker helper class for pat::Electron
// Created:     Wed Apr 15 16:15:07 2015
// Author:      Teresa Lenz      
//-----------------------------------------------------------------------------
#include "Ntuples/MyNtuple/interface/patElectronHelper.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "EGamma/EGammaAnalysisTools/interface/ElectronEffectiveArea.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
//-----------------------------------------------------------------------------
using namespace std;
using namespace pat;
//-----------------------------------------------------------------------------
// This constructor is called once per job
ElectronHelper::ElectronHelper()
  : HelperFor<pat::Electron>() {

  isRECOfile = config->getUntrackedParameter<bool>("isRECOfile");

}
    
ElectronHelper::~ElectronHelper() {}

// -- Called once per event
//void ElectronHelper::analyzeEvent()
//{
//
//}

// -- Called once per object

void ElectronHelper::analyzeObject()
{
    _Aeff04 = ElectronEffectiveArea::GetElectronEffectiveArea(ElectronEffectiveArea::kEleGammaAndNeutralHadronIso04, object->superCluster()->eta(), ElectronEffectiveArea::kEleEAData2012);

}

// -- User access methods
 float ElectronHelper::Aeff04()
 {return _Aeff04;}

//double ElectronHelper::someMethod()  const
//{
//  return  //-- some-value --
//}

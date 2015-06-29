//-----------------------------------------------------------------------------
// Subsystem:   Ntuples
// Package:     MyNtuple
// Description: TheNtupleMaker helper class for pat::Jet
// Created:     Mon Jun 29 17:26:51 2015
// Author:      Teresa Lenz      
//-----------------------------------------------------------------------------
#include "Ntuples/MyNtuple/interface/patJetHelper.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
//-----------------------------------------------------------------------------
using namespace std;
using namespace pat;
//-----------------------------------------------------------------------------
// This constructor is called once per job
JetHelper::JetHelper()
  : HelperFor<pat::Jet>() {}
    
JetHelper::~JetHelper() {}

// -- Called once per event
void JetHelper::analyzeEvent()
{
  edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
  eventsetup->get<JetCorrectionsRecord>().get("AK5PFchs",JetCorParColl);

  JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
  jecUncertainties = new JetCorrectionUncertainty(JetCorPar);

  //for (PFJetCollection::const_iterator jet = jets->begin(); jet != jets->end(); jet++)  {
  //}


}

// -- Called once per object
void JetHelper::analyzeObject()
{
  jecUncertainties->setJetEta((float) object->eta());
  jecUncertainties->setJetPt((float) object->pt()); // here you must use the CORRECTED jet pt
  _jecUnc = jecUncertainties->getUncertainty(true);
}

// -- User access methods
float JetHelper::jecUnc()
{return _jecUnc;}
//double JetHelper::someMethod()  const
//{
//  return  //-- some-value --
//}

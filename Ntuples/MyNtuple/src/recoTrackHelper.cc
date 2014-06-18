//-----------------------------------------------------------------------------
// Subsystem:   Ntuples
// Package:     MyNtuple
// Description: TheNtupleMaker helper class for reco::Track
// Created:     Mon Jun  2 14:23:27 2014
// Author:      Teresa Lenz      
//-----------------------------------------------------------------------------
#include "Ntuples/MyNtuple/interface/recoTrackHelper.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "PhysicsTools/IsolationAlgos/interface/IsoDepositExtractorFactory.h"
#include "RecoMuon/MuonIdentification/plugins/MuonIdProducer.h"

//-----------------------------------------------------------------------------
using namespace std;
using namespace reco;
//-----------------------------------------------------------------------------
// This constructor is called once per job
TrackHelper::TrackHelper()
  : HelperFor<reco::Track>() {}
    
TrackHelper::~TrackHelper() {}

// -- Called once per event
void TrackHelper::analyzeEvent()
{

  // 1a.) Calo Isolation (my Version)
  event->getByLabel("towerMaker",towers);
  
  // 1b.) Calo Isolation (Wells version)
  event -> getManyByType(prods);


}

// -- Called once per object
void TrackHelper::analyzeObject()
{


  _caloEMDeltaRp3  = 0;  
  _caloHadDeltaRp3 = 0;  
  _caloEMDeltaRp4  = 0;  
  _caloHadDeltaRp4 = 0;  
  _caloEMDeltaRp5  = 0;  
  _caloHadDeltaRp5 = 0;  

  // 1a.) Calculate calo isolation (my Version)

  for ( cal = towers->begin(); cal != towers->end(); ++cal ) {

    double deltaEta = fabs(object->eta() - cal->eta());  
    double deltaPhi = fabs(fabs(fabs(object->phi() - cal->phi()) - TMath::Pi()) - TMath::Pi()); 
    double deltaR   = sqrt(pow(deltaEta, 2) + pow(deltaPhi, 2));
    double Eem      = cal->emEnergy();  
    double Ehad     = cal->hadEnergy();  


    if (cal->emEt()  < 0.2) Eem  = 0;  
    if (cal->hadEt() < 0.5) Ehad = 0;  

    //cout<<"Eem = "<<Eem<<endl;    

    if (deltaR<0.3) { 
      _caloEMDeltaRp3  += Eem;  
      _caloHadDeltaRp3 += Ehad;  
    }      
    if (deltaR<0.4) { 
      _caloEMDeltaRp4  += Eem;  
      _caloHadDeltaRp4 += Ehad;  
    }
    if (deltaR<0.5) { 
      _caloEMDeltaRp5  += Eem;  
      _caloHadDeltaRp5 += Ehad;  
     
    }

  }


  //cout<<"My result: _caloEMDeltaRp5 = "<<_caloEMDeltaRp5<<endl;
  //cout<<" _caloHadDeltaRp5 = "<< _caloHadDeltaRp5<<endl;

  _caloEMDeltaRp3W  = 0;  
  _caloHadDeltaRp3W = 0;  
  _caloEMDeltaRp4W  = 0;  
  _caloHadDeltaRp4W = 0;  
  _caloEMDeltaRp5W  = 0;  
  _caloHadDeltaRp5W = 0; 
  
  // 1b.) Calculate Calo isolation (Wells version)
  std::vector<edm::Handle<CaloTowerCollection> >::iterator i = prods.begin();
  const CaloTowerCollection& c=*(*i);
  for (CaloTowerCollection::const_iterator j=c.begin(); j!=c.end(); j++) {
    double deltaEta = fabs(object->eta() - j->eta());  
    double deltaPhi = fabs(fabs(fabs(object->phi() - j->phi()) - TMath::Pi()) - TMath::Pi()); 
    double deltaR   = sqrt(pow(deltaEta, 2) + pow(deltaPhi, 2));
    double Eem  = j->emEnergy();  
    double Ehad = j->hadEnergy();  

    if (j->emEt()  < 0.2) Eem  = 0;  
    if (j->hadEt() < 0.5) Ehad = 0;  
	 
    if (deltaR<0.3) { 
      _caloEMDeltaRp3W  += Eem;  
      _caloHadDeltaRp3W += Ehad;  
    }      
    if (deltaR<0.4) { 
      _caloEMDeltaRp4W  += Eem;  
      _caloHadDeltaRp4W += Ehad;  
    }
    if (deltaR<0.5) { 
      _caloEMDeltaRp5W  += Eem;  
      _caloHadDeltaRp5W += Ehad;  
    }

  }
   
  
  //cout<<"Wells' result: _caloEMDeltaRp5 = "<<_caloEMDeltaRp5W<<endl;
  //cout<<" _caloHadDeltaRp5 = "<< _caloHadDeltaRp5W<<endl;
 

  //-----

  // 2.) Save wether high Purity track  
  reco::TrackBase::TrackQuality _highPurityNumber = reco::TrackBase::qualityByName("highPurity");
  if( object->quality(_highPurityNumber) ) _trackHighPurity=1;
  else _trackHighPurity=0;

  //-----

  edm::ParameterSet trackExtractorPSet = config->getParameter<edm::ParameterSet>("TrackExtractorPSet");
  std::string trackExtractorName = trackExtractorPSet.getParameter<std::string>("ComponentName");
  reco::isodeposit::IsoDepositExtractor *muIsoExtractorTrack_;
  muIsoExtractorTrack_ = IsoDepositExtractorFactory::get()->create( trackExtractorName,trackExtractorPSet);
 
  reco::IsoDeposit depTrk = muIsoExtractorTrack_->deposit(*event, *eventsetup , *object);
  reco::IsoDeposit::Vetos noVetos;
  double depTrkRp3 = depTrk.depositWithin(0.3, noVetos, true);
  _trackRelIso03 = max(0.,(depTrkRp3 - object->pt()) / object->pt());
   
}



// -- User access methods
bool TrackHelper::trackHighPurity()
{return _trackHighPurity;}
double TrackHelper::trackRelIso03()
{return _trackRelIso03;}
double TrackHelper::caloEMDeltaRp3()
{return _caloEMDeltaRp3;}
double TrackHelper::caloHadDeltaRp3()
{return _caloHadDeltaRp3;}
double TrackHelper::caloEMDeltaRp4()
{return _caloEMDeltaRp4;}
double TrackHelper::caloHadDeltaRp4()
{return _caloHadDeltaRp4;}
double TrackHelper::caloEMDeltaRp5()
{return _caloEMDeltaRp5;}
double TrackHelper::caloHadDeltaRp5()
{return _caloHadDeltaRp5;}
double TrackHelper::caloEMDeltaRp3W()
{return _caloEMDeltaRp3W;}
double TrackHelper::caloHadDeltaRp3W()
{return _caloHadDeltaRp3W;}
double TrackHelper::caloEMDeltaRp4W()
{return _caloEMDeltaRp4W;}
double TrackHelper::caloHadDeltaRp4W()
{return _caloHadDeltaRp4W;}
double TrackHelper::caloEMDeltaRp5W()
{return _caloEMDeltaRp5W;}
double TrackHelper::caloHadDeltaRp5W()
{return _caloHadDeltaRp5W;}


//double TrackHelper::someMethod()  const
//{
//  return  //-- some-value --
//}

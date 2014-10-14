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
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "TROOT.h"
#include "TTree.h"

//-----------------------------------------------------------------------------
using namespace std;
using namespace reco;
//-----------------------------------------------------------------------------
// This constructor is called once per job
TrackHelper::TrackHelper()
  : HelperFor<reco::Track>() {

  isRECOfile = config->getUntrackedParameter<bool>("isRECOfile");

  if(isRECOfile){
    // !!! find the tree
    string ntupleName = config->getUntrackedParameter<string>("ntupleName");
    TFile * f = gROOT->GetFile(ntupleName.c_str());
    
    // !!! add a branch
    TTree * t = (TTree*)f->Get("Events");
    string branchName;
    branchName = "recoTrackHelper_" + labelname + "_HitsDeDx";
    t->Branch(branchName.c_str(),&HitsDeDx);
    branchName = "recoTrackHelper_" + labelname + "_HitsPathlength";
    t->Branch(branchName.c_str(),&HitsPathlength);
    branchName = "recoTrackHelper_" + labelname + "_HitsShapetest";
    t->Branch(branchName.c_str(),&HitsShapetest);
    branchName = "recoTrackHelper_" + labelname + "_HitsSubdetId";
    t->Branch(branchName.c_str(),&HitsSubdetId);
    branchName = "recoTrackHelper_" + labelname + "_HitsEta";
    t->Branch(branchName.c_str(),&HitsEta);
    branchName = "recoTrackHelper_" + labelname + "_HitsPhi";
    t->Branch(branchName.c_str(),&HitsPhi);
    branchName = "recoTrackHelper_" + labelname + "_HitsTransverse";
    t->Branch(branchName.c_str(),&HitsTransverse);

  }

}
    
TrackHelper::~TrackHelper() {}

// -- Called once per event
void TrackHelper::analyzeEvent()
{
  
  // 1a.) Calo Isolation (my Version)
  event->getByLabel("towerMaker",towers);
  
  // 1b.) Calo Isolation (Wells version)
  event -> getManyByType(prods);

  if(TrackHelper::isRECOfile){
    // 2.) For DeDx calculation
    // For DeDxNPHarm2
    edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxNPHarm2TrackHandle;
    event->getByLabel("dedxNPHarm2", dEdxNPHarm2TrackHandle);
    dEdxNPTrackMapHarm2 = *dEdxNPHarm2TrackHandle.product();

    // For DeDxHarm2
    edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxHarm2TrackHandle;
    event->getByLabel("dedxHarm2", dEdxHarm2TrackHandle);
    dEdxTrackMapHarm2 = *dEdxHarm2TrackHandle.product();
  
    // For DeDxNPTru40
    edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxNPTru40TrackHandle;
    event->getByLabel("dedxNPTru40", dEdxNPTru40TrackHandle);
    dEdxNPTrackMapTru40 = *dEdxNPTru40TrackHandle.product();
  
    // For DeDxTru40
    edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxTru40TrackHandle;
    event->getByLabel("dedxTru40", dEdxTru40TrackHandle);
    dEdxTrackMapTru40 = *dEdxTru40TrackHandle.product();

    //For DeDxNPASmi
    edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxNPASmiTrackHandle;
    event->getByLabel("dedxNPASmi", dEdxNPASmiTrackHandle);
    dEdxNPTrackMapASmi = *dEdxNPASmiTrackHandle.product();

    //For DeDxASmi
    edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxASmiTrackHandle;
    event->getByLabel("dedxASmi", dEdxASmiTrackHandle);
    dEdxTrackMapASmi = *dEdxASmiTrackHandle.product();
    
    // For my calculation of dE/dx
    edm::Handle<edm::ValueMap<susybsm::HSCPDeDxInfo> > dEdxHitsInfoTrackHandle;
    event->getByLabel("dedxHitInfo", dEdxHitsInfoTrackHandle);
    dEdxHitsTrackMap = *dEdxHitsInfoTrackHandle.product();
    
    event->getByLabel(labelname,trackCollectionHandle);
    
    //3.) Store Hit information
    // !!! clear the dummy hits
    HitsDeDx.clear();
    HitsPathlength.clear();
    HitsShapetest.clear();
    HitsSubdetId.clear();
    HitsEta.clear();
    HitsPhi.clear();
    HitsTransverse.clear();
  }
  

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


  //-----

  // 2.) Save whether high Purity track  
  reco::TrackBase::TrackQuality _highPurityNumber = reco::TrackBase::qualityByName("highPurity");
  if( object->quality(_highPurityNumber) ) _trackHighPurity=1;
  else _trackHighPurity=0;

  //-----

  // 3.) trackRelIso03 implementation
  edm::ParameterSet trackExtractorPSet = config->getParameter<edm::ParameterSet>("TrackExtractorPSet");
  std::string trackExtractorName = trackExtractorPSet.getParameter<std::string>("ComponentName");
  reco::isodeposit::IsoDepositExtractor *muIsoExtractorTrack_;
  muIsoExtractorTrack_ = IsoDepositExtractorFactory::get()->create( trackExtractorName,trackExtractorPSet);
 
  reco::IsoDeposit depTrk = muIsoExtractorTrack_->deposit(*event, *eventsetup , *object);
  reco::IsoDeposit::Vetos noVetos;
  double depTrkRp3 = depTrk.depositWithin(0.3, noVetos, true);
  _trackRelIso03 = max(0.,(depTrkRp3 - object->pt()) / object->pt());

  //-----
  // 4.) For DeDx calculation
  if(isRECOfile){
    // For DeDxNPHarm2 
    reco::TrackRef track  = reco::TrackRef( trackCollectionHandle, oindex);
    dEdxNPHarm2Track = dEdxNPTrackMapHarm2[track];
    // For DeDxNPTru40
    dEdxNPTru40Track = dEdxNPTrackMapTru40[track];
    // For DeDxNPASmi
    dEdxNPASmiTrack = dEdxNPTrackMapASmi[track];
    // For DeDxHarm2 
    dEdxHarm2Track = dEdxTrackMapHarm2[track];
    // For DeDxTru40
    dEdxTru40Track = dEdxTrackMapTru40[track];
    // For DeDxASmi
    dEdxASmiTrack = dEdxTrackMapASmi[track];


    // For my calculation of dE/dx
    dEdxHits = dEdxHitsTrackMap[track];
    
    // 5.) For Hit Information
    // !!! add the hit information

    // get the complete tracking geometry from the event
    edm::ESHandle<TrackerGeometry> trackingGeometry ;
    eventsetup->get<TrackerDigiGeometryRecord>().get(trackingGeometry);
    
    HitsDeDx.push_back(vector<double>());
    HitsPathlength.push_back(vector<double>());
    HitsShapetest.push_back(vector<int>());
    HitsSubdetId.push_back(vector<int>());
    HitsEta.push_back(vector<double>());
    HitsPhi.push_back(vector<double>());
    HitsTransverse.push_back(vector<double>());

    for(unsigned int i=0; i<dEdxHits.charge.size(); i++){
    
      HitsDeDx.back().push_back(dEdxHits.charge[i]);
      HitsPathlength.back().push_back(dEdxHits.pathlength[i]);
      HitsShapetest.back().push_back((int)dEdxHits.shapetest[i]);
      HitsSubdetId.back().push_back((int)dEdxHits.subdetid[i]);
      
      //get the geometry of your detector
      const GeomDet* geomdet = trackingGeometry->idToDet( dEdxHits.detIds[i] );
      Local2DPoint point=Local2DPoint(dEdxHits.localx[i],dEdxHits.localy[i]);
      GlobalPoint _pos = geomdet->toGlobal( point );
      HitsEta.back().push_back(_pos.eta());
      HitsPhi.back().push_back(_pos.phi());
      HitsTransverse.back().push_back(_pos.transverse());

    }
    
  }
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

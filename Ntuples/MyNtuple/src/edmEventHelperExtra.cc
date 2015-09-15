//-----------------------------------------------------------------------------
// Subsystem:   Ntuples
// Package:     MyNtuple
// Description: TheNtupleMaker helper class for edm::Event
// Created:     Mon Jun 29 19:01:41 2015
// Author:      Teresa Lenz      
//-----------------------------------------------------------------------------
#include "Ntuples/MyNtuple/interface/edmEventHelperExtra.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "TROOT.h"
#include "TTree.h"
#include "TFile.h"
//-----------------------------------------------------------------------------
using namespace std;
using namespace edm;
//-----------------------------------------------------------------------------
// This constructor is called once per job
EventHelperExtra::EventHelperExtra()
  : HelperFor<edm::Event>() {

  isSignal = config->getUntrackedParameter<bool>("isSignal");

  string ntupleName = config->getUntrackedParameter<string>("ntupleName");
  TFile * f = gROOT->GetFile(ntupleName.c_str());
  TTree * t = (TTree*)f->Get("Events");
  string branchName;
  branchName = "doubles_pdfWeights_cteq66_PATuple";
  t->Branch(branchName.c_str(),&pdfWeights_cteq66);
  //branchName = "doubles_pdfWeights_NNPDF21_PATuple";
  //t->Branch(branchName.c_str(),&pdfWeights_NNPDF21);
  //branchName = "doubles_pdfWeights_MSTW2008_PATuple";
  //t->Branch(branchName.c_str(),&pdfWeights_MSTW2008);
}
    
EventHelperExtra::~EventHelperExtra() {}


// -- Called once per event
void EventHelperExtra::analyzeEvent()
{

  //as above example

  edm::InputTag trigEventTag("hltTriggerSummaryAOD","","HLT"); //make sure have correct process on MC
  edm::Handle<trigger::TriggerEvent> trigEvent_1;
  edm::Handle<trigger::TriggerEvent> trigEvent_2;
  edm::Handle<trigger::TriggerEvent> trigEvent_3;
  edm::Handle<trigger::TriggerEvent> trigEvent_4;
  edm::Handle<trigger::TriggerEvent> trigEvent_5;
  event->getByLabel(trigEventTag,trigEvent_1);
  event->getByLabel(trigEventTag,trigEvent_2);
  event->getByLabel(trigEventTag,trigEvent_3);
  event->getByLabel(trigEventTag,trigEvent_4);
  event->getByLabel(trigEventTag,trigEvent_5);
  std::string filterName_1("hltL1sL1ETM40");
  std::string filterName_2("hltCentralJet65L1FastJet");
  std::string filterName_3("hltMET65");
  std::string filterName_4("hltCentralPFJet80");
  std::string filterName_5("hltPFMETWOM95");

  _passTrigger  = false;
  int nObj_1    = 0;
  int nObj_2    = 0;
  int nObj_3    = 0;
  int nObj_4    = 0;
  int nObj_5    = 0;

   //it is important to specify the right HLT process for the filter, not doing this is a common bug
  trigger::size_type filterIndex_1 = trigEvent_1->filterIndex(edm::InputTag(filterName_1,"",trigEventTag.process())); 
  trigger::size_type filterIndex_2 = trigEvent_2->filterIndex(edm::InputTag(filterName_2,"",trigEventTag.process())); 
  trigger::size_type filterIndex_3 = trigEvent_3->filterIndex(edm::InputTag(filterName_3,"",trigEventTag.process())); 
  trigger::size_type filterIndex_4 = trigEvent_4->filterIndex(edm::InputTag(filterName_4,"",trigEventTag.process())); 
  trigger::size_type filterIndex_5 = trigEvent_5->filterIndex(edm::InputTag(filterName_5,"",trigEventTag.process())); 
  
  if(filterIndex_1<trigEvent_1->sizeFilters() && filterIndex_2<trigEvent_2->sizeFilters() && filterIndex_3<trigEvent_3->sizeFilters() && filterIndex_4<trigEvent_4->sizeFilters() && filterIndex_5<trigEvent_5->sizeFilters()){ 

    const trigger::Keys& trigKeys_1 = trigEvent_1->filterKeys(filterIndex_1); 
    const trigger::Keys& trigKeys_2 = trigEvent_2->filterKeys(filterIndex_2); 
    const trigger::Keys& trigKeys_3 = trigEvent_3->filterKeys(filterIndex_3); 
    const trigger::Keys& trigKeys_4 = trigEvent_4->filterKeys(filterIndex_4); 
    const trigger::Keys& trigKeys_5 = trigEvent_5->filterKeys(filterIndex_5); 

    const trigger::TriggerObjectCollection & trigObjColl_1(trigEvent_1->getObjects());
    const trigger::TriggerObjectCollection & trigObjColl_2(trigEvent_2->getObjects());
    const trigger::TriggerObjectCollection & trigObjColl_3(trigEvent_3->getObjects());
    const trigger::TriggerObjectCollection & trigObjColl_4(trigEvent_4->getObjects());
    const trigger::TriggerObjectCollection & trigObjColl_5(trigEvent_5->getObjects());

    //now loop of the trigger objects passing filter
    for(trigger::Keys::const_iterator keyIt=trigKeys_1.begin();keyIt!=trigKeys_1.end();++keyIt){ 
      const trigger::TriggerObject& obj_1 = trigObjColl_1[*keyIt];
      if(obj_1.pt()>40) nObj_1++;
    }
    for(trigger::Keys::const_iterator keyIt=trigKeys_2.begin();keyIt!=trigKeys_2.end();++keyIt){ 
      const trigger::TriggerObject& obj_2 = trigObjColl_2[*keyIt];
      if(obj_2.pt()>65) nObj_2++;
    }
    for(trigger::Keys::const_iterator keyIt=trigKeys_3.begin();keyIt!=trigKeys_3.end();++keyIt){ 
      const trigger::TriggerObject& obj_3 = trigObjColl_3[*keyIt];
      if(obj_3.pt()>65) nObj_3++;
    }
    for(trigger::Keys::const_iterator keyIt=trigKeys_4.begin();keyIt!=trigKeys_4.end();++keyIt){ 
      const trigger::TriggerObject& obj_4 = trigObjColl_4[*keyIt];
      if(obj_4.pt()>80) nObj_4++;
    }
    for(trigger::Keys::const_iterator keyIt=trigKeys_5.begin();keyIt!=trigKeys_5.end();++keyIt){ 
      const trigger::TriggerObject& obj_5 = trigObjColl_5[*keyIt];
      if(obj_5.pt()>105) nObj_5++;
    }

    
  }//end filter size check
 
  if( nObj_1>0 && nObj_2>0 && nObj_3>0 && nObj_4>0 && nObj_5>0 ) _passTrigger = true;


  if(isSignal){
    pdfWeights_cteq66.clear();
    edm::Handle<vector<double> > _pdfWeights_cteq66;
    event->getByLabel(edm::InputTag("pdfWeights","cteq66"),_pdfWeights_cteq66);
    pdfWeights_cteq66.insert(pdfWeights_cteq66.begin(),_pdfWeights_cteq66->begin(),_pdfWeights_cteq66->end());

    //pdfWeights_NNPDF21.clear();
    //edm::Handle<vector<double> > _pdfWeights_NNPDF21;
    //event->getByLabel(edm::InputTag("pdfWeights","NNPDF21"),_pdfWeights_NNPDF21);
    //pdfWeights_NNPDF21.insert(pdfWeights_NNPDF21.begin(),_pdfWeights_NNPDF21->begin(),_pdfWeights_NNPDF21->end());

    //pdfWeights_MSTW2008.clear();
    //edm::Handle<vector<double> > _pdfWeights_MSTW2008;
    //event->getByLabel(edm::InputTag("pdfWeights","MSTW2008nlo68cl"),_pdfWeights_MSTW2008);
    //pdfWeights_MSTW2008.insert(pdfWeights_MSTW2008.begin(),_pdfWeights_MSTW2008->begin(),_pdfWeights_MSTW2008->end());
  }
}

// -- Called once per object
//void EventHelperExtra::analyzeObject()
//{
//
//}

// -- User access methods
bool EventHelperExtra::emulated_HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95()
{return _passTrigger;}

//double EventHelperExtra::someMethod()  const
//{
//  return  //-- some-value --
//}

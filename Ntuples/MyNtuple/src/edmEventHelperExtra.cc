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
  branchName = "doubles_pdfWeights_NNPDF21_PATuple";
  t->Branch(branchName.c_str(),&pdfWeights_NNPDF21);
  branchName = "doubles_pdfWeights_MSTW2008_PATuple";
  t->Branch(branchName.c_str(),&pdfWeights_MSTW2008);
}
    
EventHelperExtra::~EventHelperExtra() {}


// -- Called once per event
void EventHelperExtra::analyzeEvent()
{
  if(isSignal){
    pdfWeights_cteq66.clear();
    edm::Handle<vector<double> > _pdfWeights_cteq66;
    event->getByLabel(edm::InputTag("pdfWeights","cteq66"),_pdfWeights_cteq66);
    pdfWeights_cteq66.insert(pdfWeights_cteq66.begin(),_pdfWeights_cteq66->begin(),_pdfWeights_cteq66->end());

    pdfWeights_NNPDF21.clear();
    edm::Handle<vector<double> > _pdfWeights_NNPDF21;
    event->getByLabel(edm::InputTag("pdfWeights","NNPDF21"),_pdfWeights_NNPDF21);
    pdfWeights_NNPDF21.insert(pdfWeights_NNPDF21.begin(),_pdfWeights_NNPDF21->begin(),_pdfWeights_NNPDF21->end());

    pdfWeights_MSTW2008.clear();
    edm::Handle<vector<double> > _pdfWeights_MSTW2008;
    event->getByLabel(edm::InputTag("pdfWeights","MSTW2008nlo68cl"),_pdfWeights_MSTW2008);
    pdfWeights_MSTW2008.insert(pdfWeights_MSTW2008.begin(),_pdfWeights_MSTW2008->begin(),_pdfWeights_MSTW2008->end());
  }
}

// -- Called once per object
//void EventHelperExtra::analyzeObject()
//{
//
//}

// -- User access methods
//double EventHelperExtra::someMethod()  const
//{
//  return  //-- some-value --
//}

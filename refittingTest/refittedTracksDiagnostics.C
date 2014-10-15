#include <iostream>
#include  <cstdio>
#include "TFile.h"
#include "TString.h"
#include "TROOT.h"
#include "TTree.h"
#include "TChain.h"
#include "TBranch.h"
#include "TMath.h"
#include "TCanvas.h"
#include "TChain.h"
#include "TH1.h"
#include "TH1F.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TF1.h"
#include "TGraph.h"
#include "TFile.h"
#include "TString.h"
#include "TVector2.h"
#include "TLegend.h"
#include "TGraphErrors.h"
#include "TROOT.h"
#include "TStyle.h"
#include "plotStyle.h"


void plotTH1(TH1* histo, TString xTitle, TString filename);
void plotTH2(TH1* histo, TString xTitle,TString yTitle, TString filename);


int refittedTracksDiagnostics()
{
  
  //TeresaPlottingStyle::init();

  TFile *f = new TFile("ntuple_refittingDiagnostics.root","READ");
  TTree *t;



  f->GetObject("Events",t);
  cout<<"Entries = "<<t->GetEntries()<<endl<<endl;

  double pxRed[100] = {0};
  double pyRed[100] = {0};
  double ptRed[100] = {0};
  double ptErrorRed[100] = {0};
  double etaRed[100] = {0};
  double phiRed[100] = {0};
  double chi2Red[100] = {0};
  double ndfRed[100] = {0};
  double nValidRed[100] = {0};
  double nMissMiddleRed[100] = {0};
  double nMissInnerRed[100] = {0};
  int	nTrackRed = 0;
  
  double pxRef[100] = {0};
  double pyRef[100] = {0};
  double ptRef[100] = {0};
  double ptErrorRef[100] = {0};
  double etaRef[100] = {0};
  double phiRef[100] = {0};
  double chi2Ref[100] = {0};
  double ndfRef[100] = {0};
  double nValidRef[100] = {0};
  double nMissMiddleRef[100] = {0};
  double nMissInnerRef[100] = {0};
  double trackHighPurityRef[100] = {0};
  int	nTrackRef = 0;



  t->SetBranchAddress("recoTrack_generalTracksReduced.pt",ptRed);
  t->SetBranchAddress("recoTrack_generalTracksReduced.ptError",ptErrorRed);
  t->SetBranchAddress("recoTrack_generalTracksReduced.eta",etaRed);
  t->SetBranchAddress("recoTrack_generalTracksReduced.phi",phiRed);
  t->SetBranchAddress("recoTrack_generalTracksReduced.chi2",chi2Red);
  t->SetBranchAddress("recoTrack_generalTracksReduced.ndof",ndfRed);
  t->SetBranchAddress("recoTrack_generalTracksReduced.px",pxRed);
  t->SetBranchAddress("recoTrack_generalTracksReduced.py",pyRed);
  t->SetBranchAddress("recoTrack_generalTracksReduced.numberOfValidHits",nValidRed);
  t->SetBranchAddress("recoTrack_generalTracksReduced.trackerExpectedHitsInner_numberOfLostHits",nMissMiddleRed);
  t->SetBranchAddress("recoTrack_generalTracksReduced.hitPattern_trackerLayersWithoutMeasurement",nMissInnerRed);
  t->SetBranchAddress("nrecoTrack_generalTracksReduced",&nTrackRed);

  /*
  t->SetBranchAddress("recoTrack_TrackRefitter.pt",ptRef);
  t->SetBranchAddress("recoTrack_TrackRefitter.ptError",ptErrorRef);
  t->SetBranchAddress("recoTrack_TrackRefitter.eta",etaRef);
  t->SetBranchAddress("recoTrack_TrackRefitter.phi",phiRef);
  t->SetBranchAddress("recoTrack_TrackRefitter.chi2",chi2Ref);
  t->SetBranchAddress("recoTrack_TrackRefitter.ndof",ndfRef);
  t->SetBranchAddress("recoTrack_TrackRefitter.px",pxRef);
  t->SetBranchAddress("recoTrack_TrackRefitter.py",pyRef);
  t->SetBranchAddress("recoTrack_TrackRefitter.numberOfValidHits",nValidRef);
  t->SetBranchAddress("recoTrack_TrackRefitter.trackerExpectedHitsInner_numberOfLostHits",nMissMiddleRed);
  t->SetBranchAddress("recoTrack_TrackRefitter.hitPattern_trackerLayersWithoutMeasurement",nMissInnerRed);
  t->SetBranchAddress("nrecoTrack_TrackRefitter",&nTrackRef);
  */

  t->SetBranchAddress("recoTrackHelper_TrackRefitter.pt",ptRef);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.ptError",ptErrorRef);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.eta",etaRef);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.phi",phiRef);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.chi2",chi2Ref);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.ndof",ndfRef);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.px",pxRef);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.py",pyRef);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.numberOfValidHits",nValidRef);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.trackerExpectedHitsInner_numberOfLostHits",nMissMiddleRed);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.hitPattern_trackerLayersWithoutMeasurement",nMissInnerRed);
  t->SetBranchAddress("recoTrackHelper_TrackRefitter.trackHighPurity",trackHighPurityRef);
  t->SetBranchAddress("nrecoTrackHelper_TrackRefitter",&nTrackRef);
  
  
  
  TH2D* hptGeneralTracksTrackRefitterMatched      = new TH2D("hptGeneralTracksTrackRefitterMatched","hptGeneralTracksTrackRefitterMatched",100,0,400,100,0,400);
  TH2D* hptGeneralTracksTrackRefitterUnMatched    = new TH2D("hptGeneralTracksTrackRefitterUnMatched","hptGeneralTracksTrackRefitterUnMatched",100,0,400,100,0,400);
  TH2D* hptGeneralTracksTrackRefitterMatched2     = new TH2D("hptGeneralTracksTrackRefitterMatched2","hptGeneralTracksTrackRefitterMatched2",100,0,25000,100,0,25000);
  TH2D* hptErrorGeneralTracksTrackRefitterMatched = new TH2D("hptErrorGeneralTracksTrackRefitterMatched","hptErrorGeneralTracksTrackRefitterMatched",50,0,5,50,0,5);
  TH2D* hChi2NDFGeneralTracksTrackRefitterMatched = new TH2D("hChi2NDFGeneralTracksTrackRefitterMatched","hChi2NDFGeneralTracksTrackRefitterMatched",50,0,10,50,0,10);
  TH2D* hptErrorNValidTrackRefitterUnMatched      = new TH2D("hptErrorNValidTrackRefitterUnMatched","hptErrorNValidTrackRefitterUnMatched",20,0,2,20,0,20);
  TH2D* hDiffptNValidTrackRefitterUnMatched       = new TH2D("hDiffptNValidTrackRefitterUnMatched","hDiffptNValidTrackRefitterUnMatched",40,0,2,30,0,30);
  TH2D* hptErrorPtTrackRefitterUnMatched          = new TH2D("hptErrorPtTrackRefitterUnMatched","hptErrorPtTrackRefitterUnMatched",20,0,2,100,0,400);
  TH2D* hptErrorNMissMiddleTrackRefitterUnMatched = new TH2D("hptErrorNMissMiddleTrackRefitterUnMatched","hptErrorNMissMiddleTrackRefitterUnMatched",20,0,2,10,0,10);
  TH2D* hptErrorNMissInnerTrackRefitterUnMatched  = new TH2D("hptErrorNMissInnerTrackRefitterUnMatched","hptErrorNMissInnerTrackRefitterUnMatched",20,0,2,10,0,10);
  TH1D* hptErrorTrackRefitterUnMatched            = new TH1D("hptErrorTrackRefitterUnMatched","hptErrorTrackRefitterUnMatched",30,0,3);
  TH1D* hChi2NDFTrackRefitterUnMatched            = new TH1D("hChi2NDFTrackRefitterUnMatched","hChi2NDFTrackRefitterUnMatched",50,0,5);
  TH1D* hRelDiffNHitsUnMatched                    = new TH1D("hRelDiffNHitsUnMatched","hRelDiffNHitsUnMatched",10,0,1);
  TH1D* hDeltaPtOverPtErrorTrackRefitter          = new TH1D("hDeltaPtOverPtErrorTrackRefitter","hDeltaPtOverPtErrorTrackRefitter",30,0,30);
  TH1D* hDeltaPtOverPtErrorGeneralTracks          = new TH1D("hDeltaPtOverPtErrorGeneralTracks","hDeltaPtOverPtErrorGeneralTracks",30,0,30);
  TH1D* hDeltaPtOverPtErrorGeneralTracksAll       = new TH1D("hDeltaPtOverPtErrorGeneralTracksAll","hDeltaPtOverPtErrorGeneralTracksAll",30,0,30);
  TH1D* hEtaTrackRefitterUnMatched                = new TH1D("hEtaTrackRefitterUnMatched","hEtaTrackRefitterUnMatched",50,-5,5);
  TH1D* hPhiTrackRefitterUnMatched                = new TH1D("hPhiTrackRefitterUnMatched","hPhiTrackRefitterUnMatched",50,0,3.1416);
  TH1D* hPurityTrackRefitterUnMatched             = new TH1D("hPurityTrackRefitterUnMatched","hPurityTrackRefitterUnMatched",2,0,2);
  TH1D* hPurityTrackRefitter                      = new TH1D("hPurityTrackRefitter","hPurityTrackRefitter",2,0,2);


  for(int n=0; n<t->GetEntries(); n++){
  
    t->GetEntry(n);


    for(int i=0; i<nTrackRef; i++){

      double dRmin = 100.;
      int idxRed   = -1; 

      if(trackHighPurityRef[i]==0) continue;

      for(int j=0; j<nTrackRed; j++){

	

	//DeltaR matching
	double dPhi = std::abs(TVector2::Phi_mpi_pi(phiRef[i] - phiRed[j]));
	double dEta = std::abs(etaRef[i] - etaRed[j]);
	double dR   = std::sqrt(dPhi*dPhi + dEta*dEta); 
	
	if(dR<0.05){
	  if(dR<dRmin){
	    dRmin  = dR;
	    idxRed = j;
	  }
	}

      }
     
      
      if(idxRed != -1){
	
	if(ptRed[idxRed]>400 && ptRef[i]>400) continue;

	hDeltaPtOverPtErrorGeneralTracksAll->Fill(std::abs(ptRef[i]-ptRed[idxRed])/ptErrorRed[idxRed]);

	hptGeneralTracksTrackRefitterMatched->Fill(ptRed[idxRed],ptRef[i]);
	hptGeneralTracksTrackRefitterMatched2->Fill(ptRed[idxRed],ptRef[i]);
	hDiffptNValidTrackRefitterUnMatched->Fill(std::abs(ptRef[i]/ptRed[idxRed]-1.),nValidRef[i]);
	hPurityTrackRefitter->Fill(trackHighPurityRef[i]);
	
	if(std::abs(ptRed[idxRed]/ptRef[i] -1)>0.1){

	  if(std::abs(ptRef[i]-ptRed[idxRed])/ptErrorRef[i]<2) continue;
	  //if(ptErrorRef[i]/ptRef[i]>0.4) continue;
	  
	  hptErrorGeneralTracksTrackRefitterMatched->Fill(ptErrorRed[idxRed]/ptRed[idxRed],ptErrorRef[i]/ptRef[i]);
	  hChi2NDFGeneralTracksTrackRefitterMatched->Fill(chi2Red[idxRed]/ndfRed[idxRed],chi2Ref[i]/ndfRef[i]);
	  hptErrorTrackRefitterUnMatched ->Fill(ptErrorRef[i]/ptRef[i]);
	  hChi2NDFTrackRefitterUnMatched ->Fill(chi2Ref[i]/ndfRef[i]);
	  hptErrorNValidTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],nValidRef[i]);
	  hptErrorNMissMiddleTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],nMissMiddleRef[i]);
	  hptErrorNMissInnerTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],nMissInnerRef[i]);
	  hptErrorPtTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],ptRef[i]);
	  hRelDiffNHitsUnMatched->Fill(std::abs(nValidRef[i]/nValidRed[idxRed]-1.));
	  hDeltaPtOverPtErrorTrackRefitter->Fill(std::abs(ptRef[i]-ptRed[idxRed])/ptErrorRef[i]);
	  hDeltaPtOverPtErrorGeneralTracks->Fill(std::abs(ptRef[i]-ptRed[idxRed])/ptErrorRed[idxRed]);
	  hEtaTrackRefitterUnMatched->Fill(etaRef[i]);
	  hPhiTrackRefitterUnMatched->Fill(std::abs(phiRef[i]));
	  hPurityTrackRefitterUnMatched->Fill(trackHighPurityRef[i]);
	  hptGeneralTracksTrackRefitterUnMatched->Fill(ptRed[idxRed],ptRef[i]);
	  cout<<"ptRed[idxRed] = "<<ptRed[idxRed]<<" +/- "<<ptErrorRed[idxRed]<<endl;
	  cout<<"ptRef[i] = "<<ptRef[i]<<" +/- "<<ptErrorRef[i]<<endl;
	  cout<<"ptErrorRef[i]/ptRef[i] = "<<ptErrorRef[i]/ptRef[i]<<endl;
	  cout<<"etaRef[i] = "<<etaRef[i]<<endl;
	  cout<<"phiRef[i] = "<<phiRef[i]<<endl<<endl;

	}
      }
      else{

	cout<<"phiRef[i] = "<<phiRef[i]<<endl;
	hPhiTrackRefitterUnMatched->Fill(std::abs(phiRef[i]));	
	hPurityTrackRefitterUnMatched->Fill(trackHighPurityRef[i]);
	hptErrorTrackRefitterUnMatched ->Fill(ptErrorRef[i]/ptRef[i]);
	hChi2NDFTrackRefitterUnMatched ->Fill(chi2Ref[i]/ndfRef[i]);
	hptErrorNValidTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],nValidRef[i]);
	hptErrorNMissMiddleTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],nMissMiddleRef[i]);
	hptErrorNMissInnerTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],nMissInnerRef[i]);
	hptErrorPtTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],ptRef[i]);

      }
      
    }
  
  }



  plotTH2(hptGeneralTracksTrackRefitterMatched,"generalTracksReduced Pt","TrackRefitter Pt","hptGeneralTracksTrackRefitterMatched");
  plotTH2(hptErrorGeneralTracksTrackRefitterMatched,"generalTracksReduced PtError/Pt","TrackRefitter PtError/Pt","hptErrorGeneralTracksTrackRefitterMatched");
  plotTH2(hChi2NDFGeneralTracksTrackRefitterMatched,"generalTracksReduced chi2/NDF","TrackRefitter chi2/NDF","hChi2NDFGeneralTracksTrackRefitterMatched");
  plotTH1(hChi2NDFTrackRefitterUnMatched,"TrackRefitter chi2/NDF","hChi2NDFTrackRefitterUnMatched");
  plotTH1(hptErrorTrackRefitterUnMatched,"TrackRefitter PtError/Pt","hptErrorTrackRefitterUnMatched");
  plotTH2(hptErrorNValidTrackRefitterUnMatched,"TrackRefitter PtError/Pt","TrackRefitter n Valid hits","hptErrorNValidTrackRefitterUnMatched");
  plotTH2(hptErrorPtTrackRefitterUnMatched,"TrackRefitter PtError/Pt","TrackRefitter Pt","hptErrorPtTrackRefitterUnMatched");
  plotTH2(hptErrorNMissMiddleTrackRefitterUnMatched,"TrackRefitter PtError/Pt","TrackRefitter n MissMiddle hits","hptErrorNMissMiddleTrackRefitterUnMatched");
  plotTH2(hptErrorNMissInnerTrackRefitterUnMatched,"TrackRefitter PtError/Pt","TrackRefitter n MissInner hits","hptErrorNMissInnerTrackRefitterUnMatched");
  plotTH1(hChi2NDFTrackRefitterUnMatched,"TrackRefitter chi2/NDF","hChi2NDFTrackRefitterUnMatched");
  plotTH1(hRelDiffNHitsUnMatched,"|Nvalid_{TrackRefitter}/Nvalid_{generalTracks}-1|","hRelDiffNHitsUnMatched");
  plotTH1(hDeltaPtOverPtErrorTrackRefitter,"|pt_{TrackRefitter}-pt_{generalTracks}|/ptError_{TrackRefitter}","hDeltaPtOverPtErrorTrackRefitter");
  plotTH1(hDeltaPtOverPtErrorGeneralTracks,"|pt_{TrackRefitter}-pt_{generalTracks}|/ptError_{generalTracks}","hDeltaPtOverPtErrorGeneralTracks");
  plotTH1(hDeltaPtOverPtErrorGeneralTracksAll,"|pt_{TrackRefitter}-pt_{generalTracks}|/ptError_{generalTracks}","hDeltaPtOverPtErrorGeneralTracksAll");
  plotTH1(hEtaTrackRefitterUnMatched,"eta_{TrackRefitter}","hEtaTrackRefitterUnMatched");
  plotTH1(hPhiTrackRefitterUnMatched,"phi_{TrackRefitter}","hPhiTrackRefitterUnMatched");
  plotTH2(hDiffptNValidTrackRefitterUnMatched,"|pt_{TrackRefitter}/pt_{generalTracks}-1|","Nvalid_{TrackRefitter}","hDiffptNValidTrackRefitterUnMatched");
  plotTH1(hPurityTrackRefitterUnMatched,"HighPurity_{TrackRefitter}","hPurityTrackRefitterUnMatched");
  plotTH1(hPurityTrackRefitter,"HighPurity_{TrackRefitter}","hPurityTrackRefitter");
  plotTH2(hptGeneralTracksTrackRefitterUnMatched,"generalTracksReduced Pt","TrackRefitter Pt","hptGeneralTracksTrackRefitterUnMatched");
  


  return 0;


}




void plotTH1(TH1* histo, TString xTitle, TString filename){

  TCanvas *c = new TCanvas("c"+filename,"c"+filename,0,0,500,500);
  c->cd();
  histo->GetXaxis()->SetTitle(xTitle);
  histo->Draw();
  c->SaveAs("plots/" + filename + ".pdf");

}

void plotTH2(TH1* histo, TString xTitle,TString yTitle, TString filename){

  TCanvas *c = new TCanvas("c"+filename,"c"+filename,0,0,500,500);
  c->cd();
  histo->GetXaxis()->SetTitle(xTitle);
  histo->GetYaxis()->SetTitle(yTitle);
  histo->Draw("COLZ");
  c->SaveAs("plots/" + filename + ".pdf");

}

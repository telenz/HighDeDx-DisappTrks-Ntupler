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
  
  
  
  TH2D* hptGeneralTracksTrackRefitterMatched      = new TH2D("hptGeneralTracksTrackRefitterMatched","hptGeneralTracksTrackRefitterMatched",100,0,400,100,0,400);
  TH2D* hptGeneralTracksTrackRefitterMatched2     = new TH2D("hptGeneralTracksTrackRefitterMatched2","hptGeneralTracksTrackRefitterMatched2",100,0,25000,100,0,25000);
  TH2D* hptErrorGeneralTracksTrackRefitterMatched = new TH2D("hptErrorGeneralTracksTrackRefitterMatched","hptErrorGeneralTracksTrackRefitterMatched",100,0,10,100,0,10);
  TH2D* hChi2NDFGeneralTracksTrackRefitterMatched = new TH2D("hChi2NDFGeneralTracksTrackRefitterMatched","hChi2NDFGeneralTracksTrackRefitterMatched",50,0,10,50,0,10);
  TH2D* hptErrorNValidTrackRefitterUnMatched      = new TH2D("hptErrorNValidTrackRefitterUnMatched","hptErrorNValidTrackRefitterUnMatched",20,0,2,20,0,20);
  TH2D* hptErrorPtTrackRefitterUnMatched          = new TH2D("hptErrorPtTrackRefitterUnMatched","hptErrorPtTrackRefitterUnMatched",20,0,2,100,0,400);
  TH2D* hptErrorNMissMiddleTrackRefitterUnMatched = new TH2D("hptErrorNMissMiddleTrackRefitterUnMatched","hptErrorNMissMiddleTrackRefitterUnMatched",20,0,2,10,0,10);
  TH2D* hptErrorNMissInnerTrackRefitterUnMatched  = new TH2D("hptErrorNMissInnerTrackRefitterUnMatched","hptErrorNMissInnerTrackRefitterUnMatched",20,0,2,10,0,10);
  TH1D* hptErrorTrackRefitterUnMatched            = new TH1D("hptErrorTrackRefitterUnMatched","hptErrorTrackRefitterUnMatched",20,0,2);
  TH1D* hChi2NDFTrackRefitterUnMatched            = new TH1D("hChi2NDFTrackRefitterUnMatched","hChi2NDFTrackRefitterUnMatched",50,0,5);
  TH1D* hRelDiffNHitsUnMatched                    = new TH1D("hRelDiffNHitsUnMatched","hRelDiffNHitsUnMatched",10,0,1);
  TH1D* hDeltaPtOverPtErrorTrackRefitter          = new TH1D("hDeltaPtOverPtErrorTrackRefitter","hDeltaPtOverPtErrorTrackRefitter",50,0,5);
  TH1D* hDeltaPtOverPtErrorGeneralTracks          = new TH1D("hDeltaPtOverPtErrorGeneralTracks","hDeltaPtOverPtErrorGeneralTracks",50,0,5);


  for(int n=0; n<t->GetEntries(); n++){

    t->GetEntry(n);


    for(int i=0; i<nTrackRef; i++){

      double dRmin = 100;
      int idxRed = -1; 

      for(int j=0; j<nTrackRed; j++){

	//DeltaR matching
	double dPhi = std::abs(TVector2::Phi_mpi_pi(phiRef[j] - phiRed[i]));
	double dEta = std::abs(etaRef[j] - etaRed[i]);
	double dR   = std::sqrt(dPhi*dPhi + dEta*dEta); 
	
	if(dR<0.05){
	  if(dR<dRmin){
	    //cout<<"dR = "<<dR<<endl;
	    dRmin=dR;
	    idxRed = i;
	  }
	}

      }
     

      
      if(idxRed != -1){
	
	if(ptRed[idxRed]>400 || ptRef[i]>400) continue;
	hptGeneralTracksTrackRefitterMatched->Fill(ptRed[idxRed],ptRef[i]);
	hptGeneralTracksTrackRefitterMatched2->Fill(ptRed[idxRed],ptRef[i]);
	
	
	if(std::abs(ptRed[idxRed]/ptRef[i] -1)>0.1){
	  
	  /*
	  cout<<"ptErrorRed[idxRed] = "<<ptErrorRed[idxRed]<<endl;
	  cout<<"ptRed[idxRed]      = "<<ptRed[idxRed]<<endl;
	  cout<<"ptErrorRef[i] = "<<ptErrorRef[i]<<endl;
	  cout<<"ptRef[i]      = "<<ptRef[i]<<endl;
	  */
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
	  //cout<<"ptErrorRef[i]/ptRef[i] = "<<ptErrorRef[i]/ptRef[i]<<endl;
	  //cout<<"nValidRef[i] = "<<nValidRef[i]<<endl;
	  
	}
      }
      else{

	
	//hptErrorTrackRefitterUnMatched ->Fill(ptErrorRef[i]/ptRef[i]);
	hChi2NDFTrackRefitterUnMatched ->Fill(chi2Ref[i]/ndfRef[i]);
	hptErrorNValidTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],nValidRef[i]);
	hptErrorNMissMiddleTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],nMissMiddleRef[i]);
	hptErrorNMissInnerTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],nMissInnerRef[i]);
	hptErrorPtTrackRefitterUnMatched->Fill(ptErrorRef[i]/ptRef[i],ptRef[i]);


      }
      
    }
  
  }


  TCanvas *c1 = new TCanvas("c1","c1",0,0,450,450);
  c1->cd();
  hptGeneralTracksTrackRefitterMatched->GetXaxis()->SetTitle("generalTracksReduced Pt");
  hptGeneralTracksTrackRefitterMatched->GetYaxis()->SetTitle("TrackRefitter Pt");
  hptGeneralTracksTrackRefitterMatched->Draw("COLZ");
  c1->SaveAs("plots/hptGeneralTracksTrackRefitterMatched.pdf");

  /*
    TCanvas *c1a = new TCanvas("c1a","c1a",0,0,450,450);
    c1a->cd();
    hptGeneralTracksTrackRefitterMatched2->GetXaxis()->SetTitle("generalTracksReduced Pt");
    hptGeneralTracksTrackRefitterMatched2->GetYaxis()->SetTitle("TrackRefitter Pt");
    hptGeneralTracksTrackRefitterMatched2->Draw("COLZ");
    c1a->SaveAs("plots/hptGeneralTracksTrackRefitterMatchedLargerScale.pdf");
  */

  TCanvas *c2 = new TCanvas("c2","c2",450,0,450,450);
  c2->cd();
  hptErrorGeneralTracksTrackRefitterMatched->GetXaxis()->SetTitle("generalTracksReduced PtError/Pt");
  hptErrorGeneralTracksTrackRefitterMatched->GetYaxis()->SetTitle("TrackRefitter PtError/Pt");
  hptErrorGeneralTracksTrackRefitterMatched->Draw("COLZ");
  c2->SaveAs("plots/hptErrorGeneralTracksTrackRefitterMatched.pdf");

  TCanvas *c3 = new TCanvas("c3","c3",900,0,450,450);
  c3->cd();
  hChi2NDFGeneralTracksTrackRefitterMatched->GetXaxis()->SetTitle("generalTracksReduced chi2/NDF");
  hChi2NDFGeneralTracksTrackRefitterMatched->GetYaxis()->SetTitle("TrackRefitter chi2/NDF");
  hChi2NDFGeneralTracksTrackRefitterMatched->Draw("COLZ");
  c3->SaveAs("plots/hChi2NDFGeneralTracksTrackRefitterMatched.pdf");

  TCanvas *c4 = new TCanvas("c4","c4",1350,0,450,450);
  c4->cd();
  hChi2NDFTrackRefitterUnMatched->GetXaxis()->SetTitle("TrackRefitter chi2/NDF");
  hChi2NDFTrackRefitterUnMatched->Draw();
  c4->SaveAs("plots/hChi2NDFTrackRefitterUnMatched.pdf");

  TCanvas *c5 = new TCanvas("c5","c5",1350,500,450,450);
  c5->cd();
  hptErrorTrackRefitterUnMatched->GetXaxis()->SetTitle("TrackRefitter PtError/Pt");
  hptErrorTrackRefitterUnMatched->Draw();
  c5->SaveAs("plots/hptErrorTrackRefitterUnMatched.pdf");

  TCanvas *c6 = new TCanvas("c6","c6",900,500,450,450);
  c6->cd();
  hptErrorNValidTrackRefitterUnMatched->GetXaxis()->SetTitle("TrackRefitter PtError/Pt");
  hptErrorNValidTrackRefitterUnMatched->GetYaxis()->SetTitle("TrackRefitter n Valid hits");
  hptErrorNValidTrackRefitterUnMatched->Draw("COLZ");
  c6->SaveAs("plots/hptErrorNValidTrackRefitterUnMatched.pdf");

  TCanvas *c7 = new TCanvas("c7","c7",450,500,450,450);
  c7->cd();
  hptErrorPtTrackRefitterUnMatched->GetXaxis()->SetTitle("TrackRefitter PtError/Pt");
  hptErrorPtTrackRefitterUnMatched->GetYaxis()->SetTitle("TrackRefitter Pt");
  hptErrorPtTrackRefitterUnMatched->Draw("COLZ");
  c7->SaveAs("plots/hptErrorPtTrackRefitterUnMatched.pdf");

  TCanvas *c8 = new TCanvas("c8","c8",0,500,450,450);
  c8->cd();
  hptErrorNMissMiddleTrackRefitterUnMatched->GetXaxis()->SetTitle("TrackRefitter PtError/Pt");
  hptErrorNMissMiddleTrackRefitterUnMatched->GetYaxis()->SetTitle("TrackRefitter n MissMiddle hits");
  hptErrorNMissMiddleTrackRefitterUnMatched->Draw("COLZ");
  c8->SaveAs("plots/hptErrorNMissMiddleTrackRefitterUnMatched.pdf");

  TCanvas *c9 = new TCanvas("c9","c9",450,500,450,450);
  c9->cd();
  hptErrorNMissInnerTrackRefitterUnMatched->GetXaxis()->SetTitle("TrackRefitter PtError/Pt");
  hptErrorNMissInnerTrackRefitterUnMatched->GetYaxis()->SetTitle("TrackRefitter n MissInner hits");
  hptErrorNMissInnerTrackRefitterUnMatched->Draw("COLZ");
  c9->SaveAs("plots/hptErrorNMissInnerTrackRefitterUnMatched.pdf");

  

  
  //plotTH1(hChi2NDFTrackRefitterUnMatched,"TrackRefitter PtError/Pt","plots/hptErrorTrackRefitterUnMatched.pdf");
  plotTH1(hRelDiffNHitsUnMatched,"|Nvalid_{TrackRefitter}/Nvalid_{generalTracks}-1|","plots/hRelDiffNHitsUnMatched.pdf");
  plotTH1(hDeltaPtOverPtErrorTrackRefitter,"|pt_{TrackRefitter}-pt_{generalTracks}-1|/ptError_{TrackRefitter}","plots/hDeltaPtOverPtErrorTrackRefitter.pdf");
  plotTH1(hDeltaPtOverPtErrorGeneralTracks,"|pt_{TrackRefitter}-pt_{generalTracks}-1|/ptError_{generalTracks}","plots/hDeltaPtOverPtErrorGeneralTracks.pdf");


  return 0;


}




void plotTH1(TH1* histo, TString xTitle, TString filename){

  TCanvas *c = new TCanvas("c"+filename,"c"+filename,0,0,500,500);
  c->cd();
  histo->GetXaxis()->SetTitle(xTitle);
  histo->Draw();
  c->SaveAs(filename);

}

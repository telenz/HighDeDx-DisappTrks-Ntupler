#-------------------------------------------------------------------------
# Created: Fri May 30 11:55:53 2014 by mkntuplecfi.py
#-------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
from RecoMuon.MuonIsolationProducers.trackExtractorBlocks_cff import *

demo =\
cms.EDAnalyzer("TheNtupleMaker",
               TrackExtractorPSet = cms.PSet(MIsoTrackExtractorBlock),
               ntupleName = cms.untracked.string("ntuple.root"),
               analyzerName = cms.untracked.string("analyzer.cc"),
               isRECOfile = cms.untracked.bool(True),

# NOTE: the names listed below will be the prefixes for
#       the associated C++ variables created by mkanalyzer.py
#       and the asscociated C++ structs.
               buffers =
               cms.untracked.
               vstring(
    'edmEventHelper',
    'edmTriggerResultsHelper',
    'PileupSummaryInfo',
    'Vertex',
    'sdouble',
    'MET',
    'GenParticle',
    'Jet',
    'ElectronPFlow',
    'Electron',    
    'MuonPFlow',
    'Muon',    
    'Tau',
    'Track',    
    'SimTrack',
    'SimVertex'
    ),
               edmEventHelper =
               cms.untracked.
               vstring(
    'edmEventHelper                  info                              1',
    #---------------------------------------------------------------------
    '   bool  isRealData()',
    '   int   run()',
    '   int   event()',
    '   int   luminosityBlock()',
    '   int   bunchCrossing()',
    '   int   orbitNumber()'
    ),

               edmTriggerResultsHelper =
               cms.untracked.
               vstring(
    'edmTriggerResultsHelper TriggerResults::HLT 1',
    #---------------------------------------------------------------------
    ' int value("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v1...20") value_HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v',
    ' int value("HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v1...20") value_HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v',
    ' int value("HLT_MET120_HBHENoiseCleaned_v1...20") value_HLT_MET120_HBHENoiseCleaned_v',
    ' int prescale("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v1...20") prescale_HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v',
    ' int prescale("HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v1...20") prescale_HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v',
    ' int prescale("HLT_MET120_HBHENoiseCleaned_v1...20") prescale_HLT_MET120_HBHENoiseCleaned_v'
    ),
               PileupSummaryInfo =
               cms.untracked.
               vstring(
    'PileupSummaryInfo               addPileupInfo                    10',
   #---------------------------------------------------------------------
    ' int getBunchCrossing()',
    ' int getPU_NumInteractions()',
    ' float getTrueNumInteractions()',
   ),
               Vertex =
               cms.untracked.
               vstring(
    'recoVertex                      offlinePrimaryVertices          100',
    #---------------------------------------------------------------------
    'float  ndof()',
    'float  x()',
    'float  y()',
    'float  z()',
    'float position().rho()',
    ),
               sdouble =
               cms.untracked.
               vstring(
    'sdouble                         kt6CaloJets_rho                   1',
    #---------------------------------------------------------------------
    'float value()',
    ), 
               MET =
               cms.untracked.
               vstring(
    'patMET                          patMETsPFlow                      1',
    #---------------------------------------------------------------------
    'float  energy()',
    'float  et()',
    'float  pz()',
    'float  pt()',
    'float  phi()',
    'float  eta()',
    ),
               GenParticle =
               cms.untracked.
               vstring(
    'recoGenParticle                 genParticles                    2000',
    #---------------------------------------------------------------------
    'int  charge()',
    'float  p()',
    'float  energy()',
    'float  et()',
    'float  pz()',
    'float  pt()',
    'float  phi()',
    'float  eta()',
    'float  mass()',
    'int     pdgId()',
    'int     status()'
    ),
               Jet =
               cms.untracked.
               vstring(
    'patJet                          selectedPatJetsPFlow            200',
    #---------------------------------------------------------------------
    'float  energy()',
    'float  et()',
    'float  pt()',
    'float  pz()',
    'float  phi()',
    'float  eta()',
    'float  chargedHadronEnergyFraction()',
    'float  neutralHadronEnergyFraction()',
    'float  chargedEmEnergyFraction()',
    'float  neutralEmEnergyFraction()',
    ),
               ElectronPFlow =
               cms.untracked.
               vstring(
    'patElectron                     patElectronsLoosePFlow         200',
    #---------------------------------------------------------------------
    'float  energy()',
    'float  et()',
    'float  pz()',
    'float  pt()',
    'float  phi()',
    'float  eta()',
    'float  electronID("mvaNonTrigV0")',
    ),
               Electron =
               cms.untracked.
               vstring(
    'patElectron                     selectedPatElectrons            200',
    #---------------------------------------------------------------------
    'float  energy()',
    'float  et()',
    'float  pz()',
    'float  pt()',
    'float  phi()',
    'float  eta()',
    'float  electronID("mvaNonTrigV0")',
    ),
               MuonPFlow =
               cms.untracked.
               vstring(
    'patMuon                         selectedPatMuonsLoosePFlow      200',
    #---------------------------------------------------------------------
    'float  energy()',
    'float  et()',
    'float  pz()',
    'float  pt()',
    'float  phi()',
    'float  eta()',
    'bool    isPFMuon()',
    'bool    isGlobalMuon()',
    'bool    isTrackerMuon()',
    'bool    isStandAloneMuon()'
    ),   
               Muon =
               cms.untracked.
               vstring(
    'patMuon                         selectedPatMuonsLoose           200',
    #---------------------------------------------------------------------
    'float  energy()',
    'float  et()',
    'float  pz()',
    'float  pt()',
    'float  phi()',
    'float  eta()',
    'bool    isPFMuon()',
    'bool    isGlobalMuon()',
    'bool    isTrackerMuon()',
    'bool    isStandAloneMuon()'
    ),
               Tau =
               cms.untracked.
               vstring(
    'patTau                          selectedPatTaus                 200',
    #---------------------------------------------------------------------
    'float  energy()',
    'float  et()',
    'float  pz()',
    'float  pt()',
    'float  phi()',
    'float  eta()',
    'float  tauID("byLooseCombinedIsolationDeltaBetaCorr")',
    'float  tauID("decayModeFinding")',
    'float  tauID("againstElectronLoose")',
    'float  tauID("againstMuonTight")',
    ),
               Track =
               cms.untracked.
               vstring(
    'recoTrackHelper                       TrackRefitter                   2000',
    #---------------------------------------------------------------------
    'float  pt()',
    'float ptError()',
    'float  px()',
    'float  py()',
    'float  pz()',
    'float  phi()',
    'float  eta()',
    'float  vx()',
    'float  vy()',
    'float  vz()',
    'float chi2()',
    'float ndof()',
    'unsigned short  numberOfValidHits()',
    'unsigned short  hitPattern().trackerLayersWithoutMeasurement()',
    'unsigned short  trackerExpectedHitsInner().numberOfLostHits()',
    'unsigned short  trackerExpectedHitsOuter().numberOfHits()',
    'bool    trackHighPurity()',
    'float  trackRelIso03()',
    'float  caloEMDeltaRp3()',
    'float  caloHadDeltaRp3()',
    'float  caloEMDeltaRp4()',
    'float  caloHadDeltaRp4()',
    'float  caloEMDeltaRp5()',
    'float  caloHadDeltaRp5()',
    'float  dEdxNPASmi()',
    'float  dEdxASmi()',
    'float  dEdxNPHarm2()',
    'float  dEdxNPTru40()',
    'unsigned int     dEdxNPNoM()',
    'float  dEdxHarm2()',
    'float  dEdxTru40()',
    'unsigned int     dEdxNoM()',
    'float  dEdxHitsHarm2(1000)',
    'float  dEdxHitsHarm2(7)',
    'float  dEdxHitsHarm2(5)',
    'float  dEdxHitsHarm2(3)',
    'float  dEdxHitsHarm2(2)',
    'float  dEdxHitsHarm2(1)',
    'float  dEdxHitsTrun40(1000)',
    'float  dEdxHitsTrun40(7)',
    'float  dEdxHitsTrun40(5)',
    'float  dEdxHitsTrun40(3)',
    'float  dEdxHitsTrun40(2)',
    'float  dEdxHitsTrun40(1)',
    'float  dEdxHitsMedian(1000)',
    'float  dEdxHitsMedian(7)',
    'float  dEdxHitsMedian(5)',
    'float  dEdxHitsMedian(3)',
    'float  dEdxHitsMedian(2)',
    'float  dEdxHitsMedian(1)',
    #'string  test()',
    #'int  testINT()',
    ),
               SimTrack =
               cms.untracked.
               vstring(
    'SimTrack                        g4SimHits                      5000',
    #---------------------------------------------------------------------
    'float  charge()',
    'int  vertIndex()',
    'bool  noVertex()',
    'int  genpartIndex()',
    'bool  noGenpart()',
    'int  type()',
    'unsigned int  trackId()',
    'float momentum().pt()',
    'float momentum().phi()',
    'float momentum().eta()',
    'float momentum().energy()',
    ),
               SimVertex =
               cms.untracked.
               vstring(
    'SimVertex                       g4SimHits                      5000',
    #---------------------------------------------------------------------
    'int  parentIndex()',
    'bool  noParent()',
    'unsigned int  vertexId()',
    'float position().x()',
    'float position().y()',
    'float position().z()',
    'float position().t()',
    )
               )

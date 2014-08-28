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
    'Electron',
    'GenParticle',
    'Jet',
    'MET',
    'Muon',
    'PileupSummaryInfo',
    'sdouble',
    'Tau',
    'Track',
    'Vertex'
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
    ' int value("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_*")',
    ' int prescale("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_*")',
    ' int value("HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_*")',
    ' int prescale("HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_*")',
    ' int value("HLT_MET120_HBHENoiseCleaned_*")',
    ' int prescale("HLT_MET120_HBHENoiseCleaned_*")',
    ),

               Electron =
               cms.untracked.
               vstring(
    'patElectron                     patElectronsLoosePFlow          200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'float   electronID("mvaNonTrigV0")',
    ),
               Jet =
               cms.untracked.
               vstring(
    'patJet                          selectedPatJetsPFlow            200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  pz()',
    'double  phi()',
    'double  eta()',
    'float  chargedHadronEnergyFraction()',
    'float  neutralHadronEnergyFraction()',
    'float  chargedEmEnergyFraction()',
    'float  neutralEmEnergyFraction()',
    ),
               GenParticle =
               cms.untracked.
               vstring(
    'recoGenParticle                 genParticles                    2000',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'double  mass()',
    'int     pdgId()',
    ),
               
               MET =
               cms.untracked.
               vstring(
    'patMET                          patMETsPFlow                      1',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    ),
               Muon =
               cms.untracked.
               vstring(
    'patMuon                         selectedPatMuonsLoosePFlow      200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
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
               sdouble =
               cms.untracked.
               vstring(
    'sdouble                         kt6CaloJets_rho                   1',
    #---------------------------------------------------------------------
    'double value()',
    ),
               
               Tau =
               cms.untracked.
               vstring(
    'patTau                          selectedPatTaus                 200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
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
    'double  pt()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  phi()',
    'double  eta()',
    'double  vx()',
    'double  vy()',
    'double  vz()',
    'unsigned short  numberOfValidHits()',
    'unsigned short  hitPattern().trackerLayersWithoutMeasurement()',
    'unsigned short  trackerExpectedHitsInner().numberOfLostHits()',
    'unsigned short  trackerExpectedHitsOuter().numberOfHits()',
    'bool    trackHighPurity()',
    'double  trackRelIso03()',
    'double  caloEMDeltaRp3()',
    'double  caloHadDeltaRp3()',
    'double  caloEMDeltaRp4()',
    'double  caloHadDeltaRp4()',
    'double  caloEMDeltaRp5()',
    'double  caloHadDeltaRp5()',
    #'double  caloEMDeltaRp3W()',
    #'double  caloHadDeltaRp3W()',
    #'double  caloEMDeltaRp4W()',
    #'double  caloHadDeltaRp4W()',
    #'double  caloEMDeltaRp5W()',
    #'double  caloHadDeltaRp5W()',
    #'double  caloEMDeltaRp3W()',
    #'double  caloHadDeltaRp3W()',
    #'double  caloEMDeltaRp4W()',
    #'double  caloHadDeltaRp4W()',
    #'double  caloEMDeltaRp5W()',
    #'double  caloHadDeltaRp5W()'
    'double  dEdxNPHarm2()',
    'double  dEdxNPTru40()',
    'unsigned int     dEdxNPNoM()',
    'double  dEdxHarm2()',
    'double  dEdxTru40()',
    'unsigned int     dEdxNoM()',
    'double  dEdxHitsHarm2(1000)',
    'double  dEdxHitsHarm2(7)',
    'double  dEdxHitsHarm2(5)',
    'double  dEdxHitsHarm2(3)',
    'double  dEdxHitsHarm2(2)',
    'double  dEdxHitsHarm2(1)',
    'double  dEdxHitsTrun40(1000)',
    'double  dEdxHitsTrun40(7)',
    'double  dEdxHitsTrun40(5)',
    'double  dEdxHitsTrun40(3)',
    'double  dEdxHitsTrun40(2)',
    'double  dEdxHitsTrun40(1)',
    'double  dEdxHitsMedian(1000)',
    'double  dEdxHitsMedian(7)',
    'double  dEdxHitsMedian(5)',
    'double  dEdxHitsMedian(3)',
    'double  dEdxHitsMedian(2)',
    'double  dEdxHitsMedian(1)',
    #'string  test()',
    #'int  testINT()',
    ),
               Vertex =
               cms.untracked.
               vstring(
    'recoVertex                      offlinePrimaryVertices          100',
    #---------------------------------------------------------------------
    'double  ndof()',
    'double  x()',
    'double  y()',
    'double  z()',
    'double position().rho()',
    )
               )

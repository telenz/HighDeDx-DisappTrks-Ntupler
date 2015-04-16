#ifndef PATELECTRONHELPER_H
#define PATELECTRONHELPER_H
//-----------------------------------------------------------------------------
// Subsystem:   Ntuples
// Package:     MyNtuple
// Description: TheNtupleMaker helper class for pat::Electron
// Created:     Wed Apr 15 16:15:07 2015
// Author:      Teresa Lenz      
//-----------------------------------------------------------------------------
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include "PhysicsTools/TheNtupleMaker/interface/HelperFor.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
//-----------------------------------------------------------------------------
// Definitions:
//   helper:        object of class ElectronHelper
//   helped object: object of class pat::Electron
//
//
// The following variables are automatically defined and available to
//       all methods:
//
//         blockname          name of config. buffer object (config block) 
//         buffername         name of buffer in config block
//         labelname          name of label in config block (for getByLabel)
//         parameter          parameter (as key, value pairs)
//                            accessed as in the following example:
//
//                            string param = parameter("label");
//
//         0. hltconfig       pointer to HLTConfigProvider
//                            Note: this will be zero if HLTConfigProvider
//                                  has not been properly initialized
//
//         1. config          pointer to global ParameterSet object
//         2. event           pointer to the current event
//         3. object          pointer to the current helped object
//         4. oindex          index of current helped object
//
//         5. index           index of item(s) returned by helper.
//                            Note 1: an item is associated with all
//                                    helper methods (think of it as an
//                                    extension of the helped object)
//                                  
//                            Note 2: index may differ from oindex if,
//                                    for a given helped object, the count
//                                    variable (see below) differs from 1.
//
//         6. count           number of items per helped object (default=1)
//                            Note:
//                                  count = 0  ==> current helped object is
//                                                 to be skipped
//
//                                  count = 1  ==> current helped object is
//                                                 to be kept
//
//                                  count > 1  ==> current helped object is
//                                                 associated with "count"
//                                                 items, where each item
//                                                 is associated with all the
//                                                 helper methods
//
//       variables 0-6 are initialized by TheNtupleMaker.
//       variables 0-5 should not be changed.
//       variable    6 can be changed by the helper to control whether a
//                     helped object should be kept or generates more items
//-----------------------------------------------------------------------------

namespace pat
{
  /// A helper class for pat::Electron.
  class ElectronHelper : public HelperFor<pat::Electron>
  {
  public:
	///
	ElectronHelper();

	virtual ~ElectronHelper();

	// Uncomment if this class does some event-level analysis
	// virtual void analyzeEvent();
	 
	// Uncomment if this class does some object-level analysis
	virtual void analyzeObject();

	// ---------------------------------------------------------
	// -- User access methods go here
	// ---------------------------------------------------------
	float Aeff04();
	
  private:
    // -- User internals
	bool isRECOfile;
	float _Aeff04;

  public:
    // ---------------------------------------------------------
    // -- Access Methods
    // ---------------------------------------------------------

	// WARNING: some methods may fail to compile because of coding
	//          problems in one of the CMSSW base classes. If so,
	//          just comment out the offending method and try again.
  


    // from reco::GsfElectron
    bool ambiguous() const { return object->ambiguous(); }

    // from reco::GsfElectron
    edm::RefVectorIterator<std::vector<reco::GsfTrack>,reco::GsfTrack,edm::refhelper::FindUsingAdvance<std::vector<reco::GsfTrack>,reco::GsfTrack> >
    ambiguousGsfTracksBegin() const
    { return object->ambiguousGsfTracksBegin(); }

    // from reco::GsfElectron
    edm::RefVectorIterator<std::vector<reco::GsfTrack>,reco::GsfTrack,edm::refhelper::FindUsingAdvance<std::vector<reco::GsfTrack>,reco::GsfTrack> >
    ambiguousGsfTracksEnd() const
    { return object->ambiguousGsfTracksEnd(); }

    // from reco::GsfElectron
    std::size_t ambiguousGsfTracksSize() const
    { return object->ambiguousGsfTracksSize(); }

    // from reco::GsfElectron
    int basicClustersSize() const { return object->basicClustersSize(); }

    // from reco::RecoCandidate
    reco::Track* bestTrack() const
    { return (reco::Track*)object->bestTrack(); }

    // from reco::RecoCandidate
    reco::TrackBaseRef bestTrackRef() const { return object->bestTrackRef(); }

    // from reco::RecoCandidate
    reco::RecoCandidate::TrackType bestTrackType() const
    { return object->bestTrackType(); }

    // from reco::LeafCandidate
    math::XYZVector boostToCM() const { return object->boostToCM(); }

    // from reco::GsfElectron
    float caloEnergy() const { return object->caloEnergy(); }

    // from pat::Electron
    float caloIso() const { return object->caloIso(); }

    // from reco::GsfElectron
    math::XYZPoint caloPosition() const { return object->caloPosition(); }

    // from reco::RecoCandidate
    CaloTowerRef caloTower() const { return object->caloTower(); }

    // from reco::GsfElectron
    reco::GsfElectron::P4Kind candidateP4Kind() const
    { return object->candidateP4Kind(); }

    // from reco::LeafCandidate
    int charge() const { return object->charge(); }

    // from pat::Lepton<reco::GsfElectron>
    float chargedHadronIso() const { return object->chargedHadronIso(); }

    // from reco::GsfElectron
    const reco::GsfElectron::ChargeInfo chargeInfo() const
    { return object->chargeInfo(); }

    // from reco::GsfElectron
    reco::GsfElectron::Classification classification() const
    { return object->classification(); }

    // from reco::GsfElectron
    const reco::GsfElectron::ClassificationVariables
    classificationVariables() const
    { return object->classificationVariables(); }

    // from reco::GsfElectron
    reco::GsfElectron::ClosestCtfTrack closestCtfTrack() const
    { return object->closestCtfTrack(); }

    // from pat::Electron
    reco::TrackRef closestCtfTrackRef() const
    { return object->closestCtfTrackRef(); }

    // from reco::GsfElectron
    reco::TrackRef closestTrack() const { return object->closestTrack(); }

    // from reco::RecoCandidate
    reco::TrackRef combinedMuon() const { return object->combinedMuon(); }

    // from reco::GsfElectron
    float convDcot() const { return object->convDcot(); }

    // from reco::GsfElectron
    float convDist() const { return object->convDist(); }

    // from reco::GsfElectron
    const reco::GsfElectron::ConversionRejection
    conversionRejectionVariables() const
    { return object->conversionRejectionVariables(); }

    // from reco::GsfElectron
    int convFlags() const { return object->convFlags(); }

    // from reco::GsfElectron
    reco::TrackBaseRef convPartner() const { return object->convPartner(); }

    // from reco::GsfElectron
    float convRadius() const { return object->convRadius(); }

    // from pat::Electron
    reco::GsfElectronCoreRef core() const { return object->core(); }

    // from reco::GsfElectron
    float correctedEcalEnergy() const { return object->correctedEcalEnergy(); }

    // from reco::GsfElectron
    float correctedEcalEnergyError() const
    { return object->correctedEcalEnergyError(); }

    // from reco::GsfElectron
    const reco::GsfElectron::Corrections corrections() const
    { return object->corrections(); }

    // from reco::GsfElectron
    float ctfGsfOverlap() const { return object->ctfGsfOverlap(); }

    // from reco::LeafCandidate
    reco::Candidate* daughter(size_t x0) const
    { return (reco::Candidate*)object->daughter(x0); }

    // from reco::LeafCandidate
    reco::Candidate* daughter(std::string s) const
    { return (reco::Candidate*)object->daughter(s); }

    // from pat::Electron
    /**
    double dB(pat::Electron::IPTYPE type=None) const
    { return object->dB(type); }
    */

    // from reco::GsfElectron
    float deltaEtaEleClusterTrackAtCalo() const
    { return object->deltaEtaEleClusterTrackAtCalo(); }

    // from reco::GsfElectron
    float deltaEtaSeedClusterTrackAtCalo() const
    { return object->deltaEtaSeedClusterTrackAtCalo(); }

    // from reco::GsfElectron
    float deltaEtaSuperClusterTrackAtVtx() const
    { return object->deltaEtaSuperClusterTrackAtVtx(); }

    // from reco::GsfElectron
    float deltaPhiEleClusterTrackAtCalo() const
    { return object->deltaPhiEleClusterTrackAtCalo(); }

    // from reco::GsfElectron
    float deltaPhiSeedClusterTrackAtCalo() const
    { return object->deltaPhiSeedClusterTrackAtCalo(); }

    // from reco::GsfElectron
    float deltaPhiSuperClusterTrackAtVtx() const
    { return object->deltaPhiSuperClusterTrackAtVtx(); }

    // from reco::GsfElectron
    float dr03EcalRecHitSumEt() const { return object->dr03EcalRecHitSumEt(); }

    // from reco::GsfElectron
    float dr03HcalDepth1TowerSumEt() const
    { return object->dr03HcalDepth1TowerSumEt(); }

    // from reco::GsfElectron
    float dr03HcalDepth1TowerSumEtBc() const
    { return object->dr03HcalDepth1TowerSumEtBc(); }

    // from reco::GsfElectron
    float dr03HcalDepth2TowerSumEt() const
    { return object->dr03HcalDepth2TowerSumEt(); }

    // from reco::GsfElectron
    float dr03HcalDepth2TowerSumEtBc() const
    { return object->dr03HcalDepth2TowerSumEtBc(); }

    // from reco::GsfElectron
    float dr03HcalTowerSumEt() const { return object->dr03HcalTowerSumEt(); }

    // from reco::GsfElectron
    float dr03HcalTowerSumEtBc() const
    { return object->dr03HcalTowerSumEtBc(); }

    // from reco::GsfElectron
    const reco::GsfElectron::IsolationVariables dr03IsolationVariables() const
    { return object->dr03IsolationVariables(); }

    // from reco::GsfElectron
    float dr03TkSumPt() const { return object->dr03TkSumPt(); }

    // from reco::GsfElectron
    float dr04EcalRecHitSumEt() const { return object->dr04EcalRecHitSumEt(); }

    // from reco::GsfElectron
    float dr04HcalDepth1TowerSumEt() const
    { return object->dr04HcalDepth1TowerSumEt(); }

    // from reco::GsfElectron
    float dr04HcalDepth1TowerSumEtBc() const
    { return object->dr04HcalDepth1TowerSumEtBc(); }

    // from reco::GsfElectron
    float dr04HcalDepth2TowerSumEt() const
    { return object->dr04HcalDepth2TowerSumEt(); }

    // from reco::GsfElectron
    float dr04HcalDepth2TowerSumEtBc() const
    { return object->dr04HcalDepth2TowerSumEtBc(); }

    // from reco::GsfElectron
    float dr04HcalTowerSumEt() const { return object->dr04HcalTowerSumEt(); }

    // from reco::GsfElectron
    float dr04HcalTowerSumEtBc() const
    { return object->dr04HcalTowerSumEtBc(); }

    // from reco::GsfElectron
    const reco::GsfElectron::IsolationVariables dr04IsolationVariables() const
    { return object->dr04IsolationVariables(); }

    // from reco::GsfElectron
    float dr04TkSumPt() const { return object->dr04TkSumPt(); }

    // from reco::GsfElectron
    float e1x5() const { return object->e1x5(); }

    // from reco::GsfElectron
    float e2x5Max() const { return object->e2x5Max(); }

    // from reco::GsfElectron
    float e5x5() const { return object->e5x5(); }

    // from reco::GsfElectron
    bool ecalDriven() const { return object->ecalDriven(); }

    // from pat::Electron
    const math::XYZTLorentzVector ecalDrivenMomentum() const
    { return object->ecalDrivenMomentum(); }

    // from reco::GsfElectron
    bool ecalDrivenSeed() const { return object->ecalDrivenSeed(); }

    // from reco::GsfElectron
    float ecalEnergy() const { return object->ecalEnergy(); }

    // from reco::GsfElectron
    float ecalEnergyError() const { return object->ecalEnergyError(); }

    // from pat::Electron
    float ecalIso() const { return object->ecalIso(); }

    // from pat::Lepton<reco::GsfElectron>
    pat::IsoDeposit* ecalIsoDeposit() const
    { return (pat::IsoDeposit*)object->ecalIsoDeposit(); }

    // from pat::Electron
    double ecalRegressionEnergy() const
    { return object->ecalRegressionEnergy(); }

    // from pat::Electron
    double ecalRegressionError() const
    { return object->ecalRegressionError(); }

    // from pat::Electron
    double ecalRegressionScale() const
    { return object->ecalRegressionScale(); }

    // from pat::Electron
    double ecalRegressionSmear() const
    { return object->ecalRegressionSmear(); }

    // from pat::Electron
    double ecalScale() const { return object->ecalScale(); }

    // from pat::Electron
    double ecalSmear() const { return object->ecalSmear(); }

    // from pat::Electron
    double ecalTrackRegressionEnergy() const
    { return object->ecalTrackRegressionEnergy(); }

    // from pat::Electron
    double ecalTrackRegressionError() const
    { return object->ecalTrackRegressionError(); }

    // from pat::Electron
    double ecalTrackRegressionScale() const
    { return object->ecalTrackRegressionScale(); }

    // from pat::Electron
    double ecalTrackRegressionSmear() const
    { return object->ecalTrackRegressionSmear(); }

    // from pat::Electron
    /**
    double edB(pat::Electron::IPTYPE type=None) const
    { return object->edB(type); }
    */

    // from reco::GsfElectron
    float eEleClusterOverPout() const { return object->eEleClusterOverPout(); }

    // from pat::PATObject<reco::GsfElectron>
    std::vector<std::pair<std::string,pat::LookupTableRecord> >
    efficiencies() const
    { return object->efficiencies(); }

    // from pat::PATObject<reco::GsfElectron>
    const pat::LookupTableRecord efficiency(std::string name) const
    { return object->efficiency(name); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<std::string> efficiencyNames() const
    { return object->efficiencyNames(); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::LookupTableRecord> efficiencyValues() const
    { return object->efficiencyValues(); }

    // from reco::GsfElectron
    reco::CaloClusterPtr electronCluster() const
    { return object->electronCluster(); }

    // from pat::Electron
    float electronID(char* name) const { return object->electronID(name); }

    // from pat::Electron
    float electronID(std::string name) const
    { return object->electronID(name); }

    // from pat::Electron
    const std::vector<std::pair<std::string,float> > electronIDs() const
    { return object->electronIDs(); }

    // from reco::LeafCandidate
    double energy() const { return object->energy(); }

    // from reco::GsfElectron
    float eSeedClusterOverP() const { return object->eSeedClusterOverP(); }

    // from reco::GsfElectron
    float eSeedClusterOverPout() const
    { return object->eSeedClusterOverPout(); }

    // from reco::GsfElectron
    float eSuperClusterOverP() const { return object->eSuperClusterOverP(); }

    // from reco::LeafCandidate
    double et() const { return object->et(); }

    // from reco::LeafCandidate
    double eta() const { return object->eta(); }

    // from reco::GsfElectron
    float fbrem() const { return object->fbrem(); }

    // from reco::GsfElectron
    const reco::GsfElectron::FiducialFlags fiducialFlags() const
    { return object->fiducialFlags(); }

    // from pat::Lepton<reco::GsfElectron>
    reco::GenParticle* genLepton() const
    { return (reco::GenParticle*)object->genLepton(); }

    // from pat::PATObject<reco::GsfElectron>
    reco::GenParticle* genParticle(size_t idx=0) const
    { return (reco::GenParticle*)object->genParticle(idx); }

    // from pat::PATObject<reco::GsfElectron>
    /**
    reco::GenParticleRef
    genParticleById(int pdgId, int status, uint8_t autoCharge=0) const
    { return object->genParticleById(pdgId, status, autoCharge); }
    */

    // from pat::PATObject<reco::GsfElectron>
    reco::GenParticleRef genParticleRef(size_t idx=0) const
    { return object->genParticleRef(idx); }

    // from pat::PATObject<reco::GsfElectron>
    std::vector<reco::GenParticleRef> genParticleRefs() const
    { return object->genParticleRefs(); }

    // from pat::PATObject<reco::GsfElectron>
    size_t genParticlesSize() const { return object->genParticlesSize(); }

    // from pat::PATObject<reco::GsfElectron>
    const pat::CandKinResolution getKinResolution(std::string label="") const
    { return object->getKinResolution(label); }

    // from pat::Electron
    reco::GsfTrackRef gsfTrack() const { return object->gsfTrack(); }

    // from reco::GsfElectron
    float hadronicOverEm() const { return object->hadronicOverEm(); }

    // from reco::GsfElectron
    float hadronicOverEm1() const { return object->hadronicOverEm1(); }

    // from reco::GsfElectron
    float hadronicOverEm2() const { return object->hadronicOverEm2(); }

    // from pat::PATObject<reco::GsfElectron>
    bool hasKinResolution(std::string label="") const
    { return object->hasKinResolution(label); }

    // from pat::PATObject<reco::GsfElectron>
    bool hasOverlaps(std::string label) const
    { return object->hasOverlaps(label); }

    // from pat::PATObject<reco::GsfElectron>
    bool hasUserCand(std::string key) const
    { return object->hasUserCand(key); }

    // from pat::PATObject<reco::GsfElectron>
    bool hasUserData(std::string key) const
    { return object->hasUserData(key); }

    // from pat::PATObject<reco::GsfElectron>
    bool hasUserFloat(char* key) const { return object->hasUserFloat(key); }

    // from pat::PATObject<reco::GsfElectron>
    bool hasUserFloat(std::string key) const
    { return object->hasUserFloat(key); }

    // from pat::PATObject<reco::GsfElectron>
    bool hasUserInt(std::string key) const { return object->hasUserInt(key); }

    // from reco::GsfElectron
    float hcalDepth1OverEcal() const { return object->hcalDepth1OverEcal(); }

    // from reco::GsfElectron
    float hcalDepth1OverEcalBc() const
    { return object->hcalDepth1OverEcalBc(); }

    // from reco::GsfElectron
    float hcalDepth2OverEcal() const { return object->hcalDepth2OverEcal(); }

    // from reco::GsfElectron
    float hcalDepth2OverEcalBc() const
    { return object->hcalDepth2OverEcalBc(); }

    // from pat::Electron
    float hcalIso() const { return object->hcalIso(); }

    // from pat::Lepton<reco::GsfElectron>
    pat::IsoDeposit* hcalIsoDeposit() const
    { return (pat::IsoDeposit*)object->hcalIsoDeposit(); }

    // from reco::GsfElectron
    float hcalOverEcal() const { return object->hcalOverEcal(); }

    // from reco::GsfElectron
    float hcalOverEcalBc() const { return object->hcalOverEcalBc(); }

    // from reco::GsfElectron
    const std::vector<CaloTowerDetId> hcalTowersBehindClusters() const
    { return object->hcalTowersBehindClusters(); }

    // from pat::Electron
    double ip3d() const { return object->ip3d(); }

    // from reco::LeafCandidate
    bool isCaloMuon() const { return object->isCaloMuon(); }

    // from reco::LeafCandidate
    bool isConvertedPhoton() const { return object->isConvertedPhoton(); }

    // from reco::GsfElectron
    bool isEB() const { return object->isEB(); }

    // from reco::GsfElectron
    bool isEBEEGap() const { return object->isEBEEGap(); }

    // from reco::GsfElectron
    bool isEBEtaGap() const { return object->isEBEtaGap(); }

    // from reco::GsfElectron
    bool isEBGap() const { return object->isEBGap(); }

    // from reco::GsfElectron
    bool isEBPhiGap() const { return object->isEBPhiGap(); }

    // from reco::GsfElectron
    bool isEcalEnergyCorrected() const
    { return object->isEcalEnergyCorrected(); }

    // from reco::GsfElectron
    bool isEE() const { return object->isEE(); }

    // from reco::GsfElectron
    bool isEEDeeGap() const { return object->isEEDeeGap(); }

    // from reco::GsfElectron
    bool isEEGap() const { return object->isEEGap(); }

    // from reco::GsfElectron
    bool isEERingGap() const { return object->isEERingGap(); }

    // from reco::GsfElectron
    bool isElectron() const { return object->isElectron(); }

    // from pat::Electron
    bool isElectronIDAvailable(char* name) const
    { return object->isElectronIDAvailable(name); }

    // from pat::Electron
    bool isElectronIDAvailable(std::string name) const
    { return object->isElectronIDAvailable(name); }

    // from reco::GsfElectron
    bool isEnergyScaleCorrected() const
    { return object->isEnergyScaleCorrected(); }

    // from reco::GsfElectron
    bool isGap() const { return object->isGap(); }

    // from reco::LeafCandidate
    bool isGlobalMuon() const { return object->isGlobalMuon(); }

    // from reco::GsfElectron
    bool isGsfCtfChargeConsistent() const
    { return object->isGsfCtfChargeConsistent(); }

    // from reco::GsfElectron
    bool isGsfCtfScPixChargeConsistent() const
    { return object->isGsfCtfScPixChargeConsistent(); }

    // from reco::GsfElectron
    bool isGsfScPixChargeConsistent() const
    { return object->isGsfScPixChargeConsistent(); }

    // from reco::LeafCandidate
    bool isJet() const { return object->isJet(); }

    // from reco::LeafCandidate
    bool isMuon() const { return object->isMuon(); }

    // from pat::Lepton<reco::GsfElectron>
    /**
    pat::IsoDeposit* isoDeposit(pat::IsolationKeys key) const
    { return (pat::IsoDeposit*)object->isoDeposit(key); }
    */

    // from reco::GsfElectron
    const reco::GsfElectron::IsolationVariables isolationVariables03() const
    { return object->isolationVariables03(); }

    // from reco::GsfElectron
    const reco::GsfElectron::IsolationVariables isolationVariables04() const
    { return object->isolationVariables04(); }

    // from pat::Electron
    bool isPF() const { return object->isPF(); }

    // from reco::LeafCandidate
    bool isPhoton() const { return object->isPhoton(); }

    // from reco::LeafCandidate
    bool isStandAloneMuon() const { return object->isStandAloneMuon(); }

    // from reco::LeafCandidate
    bool isTrackerMuon() const { return object->isTrackerMuon(); }

    // from reco::LeafCandidate
    bool longLived() const { return object->longLived(); }

    // from reco::LeafCandidate
    double mass() const { return object->mass(); }

    // from reco::LeafCandidate
    bool massConstraint() const { return object->massConstraint(); }

    // from reco::LeafCandidate
    double massSqr() const { return object->massSqr(); }

    // from reco::LeafCandidate
    math::XYZVector momentum() const { return object->momentum(); }

    // from reco::LeafCandidate
    reco::Candidate* mother(size_t x0) const
    { return (reco::Candidate*)object->mother(x0); }

    // from reco::LeafCandidate
    double mt() const { return object->mt(); }

    // from reco::LeafCandidate
    double mtSqr() const { return object->mtSqr(); }

    // from reco::GsfElectron
    float mva() const { return object->mva(); }

    // from reco::GsfElectron
    const reco::GsfElectron::MvaInput mvaInput() const
    { return object->mvaInput(); }

    // from reco::GsfElectron
    const reco::GsfElectron::MvaOutput mvaOutput() const
    { return object->mvaOutput(); }

    // from pat::Lepton<reco::GsfElectron>
    float neutralHadronIso() const { return object->neutralHadronIso(); }

    // from reco::GsfElectron
    int numberOfBrems() const { return object->numberOfBrems(); }

    // from reco::LeafCandidate
    size_t numberOfDaughters() const { return object->numberOfDaughters(); }

    // from reco::LeafCandidate
    size_t numberOfMothers() const { return object->numberOfMothers(); }

    // from pat::Electron
    size_t numberOfSourceCandidatePtrs() const
    { return object->numberOfSourceCandidatePtrs(); }

    // from reco::RecoCandidate
    size_t numberOfTracks() const { return object->numberOfTracks(); }

    // from pat::PATObject<reco::GsfElectron>
    reco::Candidate* originalObject() const
    { return (reco::Candidate*)object->originalObject(); }

    // from pat::PATObject<reco::GsfElectron>
    const edm::Ptr<reco::Candidate> originalObjectRef() const
    { return object->originalObjectRef(); }

    // from reco::GsfElectron
    /**
    bool overlap(reco::Candidate x0) const { return object->overlap(x0); }
    */

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<std::string> overlapLabels() const
    { return object->overlapLabels(); }

    // from pat::PATObject<reco::GsfElectron>
    const edm::PtrVector<reco::Candidate> overlaps(std::string label) const
    { return object->overlaps(label); }

    // from reco::LeafCandidate
    double p() const { return object->p(); }

    // from reco::GsfElectron
    /**
    const math::XYZTLorentzVector p4(reco::GsfElectron::P4Kind kind) const
    { return object->p4(kind); }
    */

    // from reco::GsfElectron
    /**
    float p4Error(reco::GsfElectron::P4Kind kind) const
    { return object->p4Error(kind); }
    */

    // from pat::Lepton<reco::GsfElectron>
    float particleIso() const { return object->particleIso(); }

    // from pat::Electron
    bool passConversionVeto() const { return object->passConversionVeto(); }

    // from reco::GsfElectron
    bool passingCutBasedPreselection() const
    { return object->passingCutBasedPreselection(); }

    // from reco::GsfElectron
    bool passingMvaPreselection() const
    { return object->passingMvaPreselection(); }

    // from reco::GsfElectron
    bool passingPflowPreselection() const
    { return object->passingPflowPreselection(); }

    // from reco::LeafCandidate
    int pdgId() const { return object->pdgId(); }

    // from pat::Electron
    reco::PFCandidateRef pfCandidateRef() const
    { return object->pfCandidateRef(); }

    // from reco::GsfElectron
    const reco::GsfElectron::PflowIsolationVariables
    pfIsolationVariables() const
    { return object->pfIsolationVariables(); }

    // from reco::GsfElectron
    reco::SuperClusterRef pflowSuperCluster() const
    { return object->pflowSuperCluster(); }

    // from reco::GsfElectron
    const reco::GsfElectron::ShowerShape pfShowerShape() const
    { return object->pfShowerShape(); }

    // from reco::GsfElectron
    float pfSuperClusterFbrem() const { return object->pfSuperClusterFbrem(); }

    // from reco::LeafCandidate
    double phi() const { return object->phi(); }

    // from pat::Lepton<reco::GsfElectron>
    float photonIso() const { return object->photonIso(); }

    // from reco::LeafCandidate
    const math::PtEtaPhiMLorentzVector polarP4() const
    { return object->polarP4(); }

    // from reco::LeafCandidate
    double pt() const { return object->pt(); }

    // from pat::Lepton<reco::GsfElectron>
    float puChargedHadronIso() const { return object->puChargedHadronIso(); }

    // from reco::LeafCandidate
    double px() const { return object->px(); }

    // from reco::LeafCandidate
    double py() const { return object->py(); }

    // from reco::LeafCandidate
    double pz() const { return object->pz(); }

    // from pat::Electron
    double r9() const { return object->r9(); }

    // from reco::LeafCandidate
    double rapidity() const { return object->rapidity(); }

    // from pat::Electron
    EcalRecHitCollection* recHits() const
    { return (EcalRecHitCollection*)object->recHits(); }

    // from pat::PATObject<reco::GsfElectron>
    double resolE(std::string label="") const { return object->resolE(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolEt(std::string label="") const
    { return object->resolEt(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolEta(std::string label="") const
    { return object->resolEta(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolM(std::string label="") const { return object->resolM(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolP(std::string label="") const { return object->resolP(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolPhi(std::string label="") const
    { return object->resolPhi(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolPInv(std::string label="") const
    { return object->resolPInv(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolPt(std::string label="") const
    { return object->resolPt(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolPx(std::string label="") const
    { return object->resolPx(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolPy(std::string label="") const
    { return object->resolPy(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolPz(std::string label="") const
    { return object->resolPz(label); }

    // from pat::PATObject<reco::GsfElectron>
    double resolTheta(std::string label="") const
    { return object->resolTheta(label); }

    // from reco::GsfElectron
    float scE1x5() const { return object->scE1x5(); }

    // from reco::GsfElectron
    float scE2x5Max() const { return object->scE2x5Max(); }

    // from reco::GsfElectron
    float scE5x5() const { return object->scE5x5(); }

    // from reco::GsfElectron
    int scPixCharge() const { return object->scPixCharge(); }

    // from reco::GsfElectron
    float scSigmaEtaEta() const { return object->scSigmaEtaEta(); }

    // from reco::GsfElectron
    float scSigmaIEtaIEta() const { return object->scSigmaIEtaIEta(); }

    // from pat::Electron
    reco::CaloClusterPtr seed() const { return object->seed(); }

    // from reco::GsfElectron
    float shFracInnerHits() const { return object->shFracInnerHits(); }

    // from reco::GsfElectron
    const reco::GsfElectron::ShowerShape showerShape() const
    { return object->showerShape(); }

    // from reco::GsfElectron
    float sigmaEtaEta() const { return object->sigmaEtaEta(); }

    // from reco::GsfElectron
    float sigmaIetaIeta() const { return object->sigmaIetaIeta(); }

    // from pat::Electron
    double sigmaIetaIphi() const { return object->sigmaIetaIphi(); }

    // from pat::Electron
    double sigmaIphiIphi() const { return object->sigmaIphiIphi(); }

    // from pat::Electron
    reco::CandidatePtr sourceCandidatePtr(size_t i) const
    { return object->sourceCandidatePtr(i); }

    // from reco::RecoCandidate
    reco::TrackRef standAloneMuon() const { return object->standAloneMuon(); }

    // from reco::LeafCandidate
    int status() const { return object->status(); }

    // from pat::Electron
    reco::SuperClusterRef superCluster() const
    { return object->superCluster(); }

    // from reco::GsfElectron
    float superClusterFbrem() const { return object->superClusterFbrem(); }

    // from reco::GsfElectron
    math::XYZPoint superClusterPosition() const
    { return object->superClusterPosition(); }

    // from reco::LeafCandidate
    double theta() const { return object->theta(); }

    // from reco::LeafCandidate
    int threeCharge() const { return object->threeCharge(); }

    // from pat::Electron
    reco::TrackRef track() const { return object->track(); }

    // from reco::GsfElectron
    const reco::GsfElectron::TrackClusterMatching trackClusterMatching() const
    { return object->trackClusterMatching(); }

    // from reco::GsfElectron
    bool trackerDrivenSeed() const { return object->trackerDrivenSeed(); }

    // from reco::GsfElectron
    const reco::GsfElectron::TrackExtrapolations trackExtrapolations() const
    { return object->trackExtrapolations(); }

    // from reco::GsfElectron
    float trackFbrem() const { return object->trackFbrem(); }

    // from pat::Electron
    float trackIso() const { return object->trackIso(); }

    // from pat::Lepton<reco::GsfElectron>
    pat::IsoDeposit* trackIsoDeposit() const
    { return (pat::IsoDeposit*)object->trackIsoDeposit(); }

    // from reco::GsfElectron
    math::XYZVectorF trackMomentumAtCalo() const
    { return object->trackMomentumAtCalo(); }

    // from reco::GsfElectron
    math::XYZVectorF trackMomentumAtEleClus() const
    { return object->trackMomentumAtEleClus(); }

    // from reco::GsfElectron
    math::XYZVectorF trackMomentumAtVtx() const
    { return object->trackMomentumAtVtx(); }

    // from reco::GsfElectron
    math::XYZVectorF trackMomentumAtVtxWithConstraint() const
    { return object->trackMomentumAtVtxWithConstraint(); }

    // from reco::GsfElectron
    float trackMomentumError() const { return object->trackMomentumError(); }

    // from reco::GsfElectron
    math::XYZVectorF trackMomentumOut() const
    { return object->trackMomentumOut(); }

    // from reco::GsfElectron
    math::XYZPointF TrackPositionAtCalo() const
    { return object->TrackPositionAtCalo(); }

    // from reco::GsfElectron
    math::XYZPointF trackPositionAtVtx() const
    { return object->trackPositionAtVtx(); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone* triggerObjectMatch(size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatch(idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByAlgorithm(char* nameAlgorithm, bool algoCondAccepted=true, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByAlgorithm(nameAlgorithm, algoCondAccepted, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByAlgorithm(char* nameAlgorithm, unsigned int algoCondAccepted, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByAlgorithm(nameAlgorithm, algoCondAccepted, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByAlgorithm(std::string nameAlgorithm, bool algoCondAccepted=true, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByAlgorithm(nameAlgorithm, algoCondAccepted, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByAlgorithm(std::string nameAlgorithm, unsigned int algoCondAccepted, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByAlgorithm(nameAlgorithm, algoCondAccepted, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByCollection(char* coll, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByCollection(coll, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByCollection(std::string coll, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByCollection(coll, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByCondition(char* nameCondition, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByCondition(nameCondition, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByCondition(std::string nameCondition, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByCondition(nameCondition, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByFilter(char* labelFilter, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByFilter(labelFilter, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByFilter(std::string labelFilter, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByFilter(labelFilter, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByFilterID(unsigned int triggerObjectType, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByFilterID(triggerObjectType, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByPath(char* namePath, bool pathLastFilterAccepted=false, bool pathL3FilterAccepted=true, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByPath(char* namePath, unsigned int pathLastFilterAccepted, unsigned int pathL3FilterAccepted=1, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByPath(std::string namePath, bool pathLastFilterAccepted=false, bool pathL3FilterAccepted=true, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted, idx); }

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByPath(std::string namePath, unsigned int pathLastFilterAccepted, unsigned int pathL3FilterAccepted=1, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted, idx); }

    // from pat::PATObject<reco::GsfElectron>
    /**
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByType(trigger::TriggerObjectType triggerObjectType, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByType(triggerObjectType, idx); }
    */

    // from pat::PATObject<reco::GsfElectron>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByType(unsigned int triggerObjectType, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByType(triggerObjectType, idx); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatches() const
    { return object->triggerObjectMatches(); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByAlgorithm(char* nameAlgorithm, bool algoCondAccepted=true) const
    { return object->triggerObjectMatchesByAlgorithm(nameAlgorithm, algoCondAccepted); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByAlgorithm(char* nameAlgorithm, unsigned int algoCondAccepted) const
    { return object->triggerObjectMatchesByAlgorithm(nameAlgorithm, algoCondAccepted); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByAlgorithm(std::string nameAlgorithm, bool algoCondAccepted=true) const
    { return object->triggerObjectMatchesByAlgorithm(nameAlgorithm, algoCondAccepted); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByAlgorithm(std::string nameAlgorithm, unsigned int algoCondAccepted) const
    { return object->triggerObjectMatchesByAlgorithm(nameAlgorithm, algoCondAccepted); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByCollection(char* coll) const
    { return object->triggerObjectMatchesByCollection(coll); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByCollection(std::string coll) const
    { return object->triggerObjectMatchesByCollection(coll); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByCondition(char* nameCondition) const
    { return object->triggerObjectMatchesByCondition(nameCondition); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByCondition(std::string nameCondition) const
    { return object->triggerObjectMatchesByCondition(nameCondition); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByFilter(char* labelFilter) const
    { return object->triggerObjectMatchesByFilter(labelFilter); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByFilter(std::string labelFilter) const
    { return object->triggerObjectMatchesByFilter(labelFilter); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByFilterID(unsigned int triggerObjectType) const
    { return object->triggerObjectMatchesByFilterID(triggerObjectType); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByPath(char* namePath, bool pathLastFilterAccepted=false, bool pathL3FilterAccepted=true) const
    { return object->triggerObjectMatchesByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByPath(char* namePath, unsigned int pathLastFilterAccepted, unsigned int pathL3FilterAccepted=1) const
    { return object->triggerObjectMatchesByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByPath(std::string namePath, bool pathLastFilterAccepted=false, bool pathL3FilterAccepted=true) const
    { return object->triggerObjectMatchesByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByPath(std::string namePath, unsigned int pathLastFilterAccepted, unsigned int pathL3FilterAccepted=1) const
    { return object->triggerObjectMatchesByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted); }

    // from pat::PATObject<reco::GsfElectron>
    /**
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByType(trigger::TriggerObjectType triggerObjectType) const
    { return object->triggerObjectMatchesByType(triggerObjectType); }
    */

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByType(unsigned int triggerObjectType) const
    { return object->triggerObjectMatchesByType(triggerObjectType); }

    // from pat::PATObject<reco::GsfElectron>
    edm::Ptr<reco::Candidate> userCand(std::string key) const
    { return object->userCand(key); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<std::string> userCandNames() const
    { return object->userCandNames(); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<std::string> userDataNames() const
    { return object->userDataNames(); }

    // from pat::PATObject<reco::GsfElectron>
    const std::string userDataObjectType(std::string key) const
    { return object->userDataObjectType(key); }

    // from pat::PATObject<reco::GsfElectron>
    float userFloat(char* key) const { return object->userFloat(key); }

    // from pat::PATObject<reco::GsfElectron>
    float userFloat(std::string key) const { return object->userFloat(key); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<std::string> userFloatNames() const
    { return object->userFloatNames(); }

    // from pat::PATObject<reco::GsfElectron>
    int userInt(std::string key) const { return object->userInt(key); }

    // from pat::PATObject<reco::GsfElectron>
    const std::vector<std::string> userIntNames() const
    { return object->userIntNames(); }

    // from pat::Lepton<reco::GsfElectron>
    /**
    float userIso(uint8_t index=0) const { return object->userIso(index); }
    */

    // from pat::Lepton<reco::GsfElectron>
    /**
    pat::IsoDeposit* userIsoDeposit(uint8_t index=0) const
    { return (pat::IsoDeposit*)object->userIsoDeposit(index); }
    */

    // from pat::Lepton<reco::GsfElectron>
    /**
    float userIsolation(pat::IsolationKeys key) const
    { return object->userIsolation(key); }
    */

    // from pat::Lepton<reco::GsfElectron>
    float userIsolation(std::string key) const
    { return object->userIsolation(key); }

    // from reco::LeafCandidate
    const math::XYZPoint vertex() const { return object->vertex(); }

    // from reco::LeafCandidate
    double vertexChi2() const { return object->vertexChi2(); }

    // from reco::LeafCandidate
    ROOT::Math::SMatrix<double,3,3,ROOT::Math::MatRepSym<double,3> >
    vertexCovariance() const
    { return object->vertexCovariance(); }

    // from reco::LeafCandidate
    double vertexCovariance(int i, int j) const
    { return object->vertexCovariance(i, j); }

    // from reco::LeafCandidate
    double vertexNdof() const { return object->vertexNdof(); }

    // from reco::LeafCandidate
    double vertexNormalizedChi2() const
    { return object->vertexNormalizedChi2(); }

    // from reco::LeafCandidate
    double vx() const { return object->vx(); }

    // from reco::LeafCandidate
    double vy() const { return object->vy(); }

    // from reco::LeafCandidate
    double vz() const { return object->vz(); }

    // from reco::LeafCandidate
    double y() const { return object->y(); }
  };
}
#endif

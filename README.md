# DeDx-DisappTrks-Ntupler
# =======================

# Can be used to get ntuples out of RECO and AOD files
	
	mkdir HighDeDx-DisappTrks-Ntupler
 	cd HighDeDx-DisappTrks-Ntupler
	cmsrel CMSSW_5_3_8_patch1
	cd CMSSW_5_3_8_patch1
	rm -r src
	git clone https://github.com/telenz/HighDeDx-DisappTrks-Ntupler.git src	
	cd src
	cmsenv
	git cms-cvs-history import CMSSW_5_3_1 Configuration/Skimming	
	#git cms-cvs-history import CMSSW_6_2_0_pre7 AnalysisDataFormats/SUSYBSMObjects
	#git mv -f classes_def_for_AnalysisDataFormats_SUSYBSMObjects_src.xml AnalysisDataFormats/SUSYBSMObjects/src/classes_def.xml 	
	
	git cms-cvs-history import V07-00-01 TopQuarkAnalysis/Configuration
	git cms-cvs-history import V06-07-11-01 TopQuarkAnalysis/TopTools
	git cms-cvs-history import  V06-05-06-07 DataFormats/PatCandidates
	git cms-cvs-history import V00-02-14 DataFormats/StdDictionaries
	git cms-cvs-history import V00-00-70 FWCore/GuiBrowsers
	git cms-cvs-history import V08-09-52 PhysicsTools/PatAlgos
	git cms-cvs-history import V03-09-23 PhysicsTools/PatUtils
	git cms-cvs-history import V00-03-15 CommonTools/ParticleFlow
	git cms-cvs-history import V00-00-12 CommonTools/RecoUtils
	git cms-cvs-history import V04-06-09 JetMETCorrections/Type1MET
	git cms-cvs-history import V01-08-00 RecoBTag/SecondaryVertex
	git clone https://github.com/cms-analysis/RecoMET-METAnalyzers.git RecoMET/METAnalyzers
	cd RecoMET/METAnalyzers
	git checkout tags/RecoMET-METAnalyzers-V00-00-08
	cd -
	#git cms-cvs-history import V00-00-07 RecoMET/METFilters
	git cms-cvs-history import V00-00-13-01 RecoMET/METFilters
	# Additional packages for the tracking POG filters{
	git cms-cvs-history import V01-00-11-01 DPGAnalysis/Skims
	git cms-cvs-history import V00-11-17 DPGAnalysis/SiStripTools
	git cms-cvs-history import V00-00-08 DataFormats/TrackerCommon
	git cms-cvs-history import V01-09-05 RecoLocalTracker/SubCollectionProducers	
	#} Additional packages for the tracking POG filters
	git cms-cvs-history import V15-01-11 RecoParticleFlow/PFProducer
	git cms-cvs-history import V02-02-00 RecoVertex/AdaptiveVertexFinder
	git clone git@github.com:latinos/UserCode-sixie-Muon-MuonAnalysisTools Muon/MuonAnalysisTools/
	git clone https://github.com/latinos/UserCode-EGamma-EGammaAnalysisTools.git EGamma/EGammaAnalysisTools
	pushd EGamma/EGammaAnalysisTools/
	git checkout tags/V00-00-08
	wget -r http://nd.edu/~abrinke1/ElectronEffectiveArea.h -O interface/ElectronEffectiveArea.h
	cd data
	cat download.url | xargs wget
	popd

	git cms-cvs-history import V01-04-23 RecoTauTag/RecoTau
	git cms-cvs-history import V01-04-10 RecoTauTag/Configuration
	git cms-cvs-history import V00-04-00 CondFormats/EgammaObjects
	git clone https://github.com/latinos/UserCode-CMG-CMGTools-External CMGTools/External
	cd CMGTools/External/
	git checkout tags/V00-02-10
	cd -
	#git clone https://github.com/cms-ttH/BEAN.git

	cd PhysicsTools
	git clone https://github.com/hbprosper/TheNtupleMaker.git
	cd TheNtupleMaker
	cmsenv
	scripts/initTNM.py
	scram b clean
	scram b -j24
	cd ../..

	scram b -j24

	#the end


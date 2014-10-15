import FWCore.ParameterSet.Config as cms

process = cms.Process('HSCP')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2500)
    )

process.source = cms.Source("PoolSource",
                            fileNames =
                            cms.untracked.vstring("file:../TTJets_Summer12_S10_1303.root"
                                                  )
                            )

process.output = cms.OutputModule("PoolOutputModule",
                 outputCommands = cms.untracked.vstring( (
                                  'keep *',
                                  ) ),
                 fileName = cms.untracked.string('hscpfile.root'),
                 )


process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load("SUSYBSMAnalysis.HSCP.HSCParticleProducer_cff")
process.HSCParticleProducer.useBetaFromEcal = cms.bool(False)

globalTagMC   = 'START53_V7C'
process.GlobalTag.globaltag = globalTagMC   + '::All'
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")


process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")


process.TrackRefitter.src    = "generalTracksReduced"
process.generalTracksReduced = cms.EDFilter("TrackSelector",
                                 src = cms.InputTag("generalTracks"),
                                 cut = cms.string("pt > 30"),
                                 filter = cms.bool(False)
                                 )


process.GlobalTag.toGet = cms.VPSet(
    cms.PSet( record = cms.string('SiStripDeDxMip_3D_Rcd'),
              tag = cms.string('MC7TeV_Deco_3D_Rcd_38X'),
             connect = cms.untracked.string("sqlite_file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC7TeV_Deco_SiStripDeDxMip_3D_Rcd.db")),	    
    )


process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")
process.load("Ntuples.MyNtuple.ntuple_cfi_RECO_refittingDiagnostics")

process.path     = cms.Path(process.offlineBeamSpot + process.generalTracksReduced + process.TrackRefitter + process.HSCParticleProducerSeq)
process.endPath1 = cms.EndPath(process.output + process.demo)

process.demo.ntupleName= cms.untracked.string('ntuple_refittingDiagnostics.root')

##--## HSCP

process.dedxHarm2.calibrationPath      = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")
process.dedxTru40.calibrationPath      = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")
process.dedxProd.calibrationPath       = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")
process.dedxASmi.calibrationPath       = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")
process.dedxNPHarm2.calibrationPath    = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")
process.dedxNPTru40.calibrationPath    = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")
process.dedxNSHarm2.calibrationPath    = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")
process.dedxNSTru40.calibrationPath    = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")
process.dedxNPProd.calibrationPath     = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")
process.dedxNPASmi.calibrationPath     = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")
process.dedxHitInfo.calibrationPath    = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC8TeVGains.root")

process.dedxHarm2.UseCalibration       = cms.bool(True)
process.dedxTru40.UseCalibration       = cms.bool(True)
process.dedxProd.UseCalibration        = cms.bool(True)
process.dedxASmi.UseCalibration        = cms.bool(True)
process.dedxNPHarm2.UseCalibration     = cms.bool(True)
process.dedxNPTru40.UseCalibration     = cms.bool(True)
process.dedxNSHarm2.UseCalibration     = cms.bool(True)
process.dedxNSTru40.UseCalibration     = cms.bool(True)
process.dedxNPProd.UseCalibration      = cms.bool(True)
process.dedxNPASmi.UseCalibration      = cms.bool(True)
process.dedxHitInfo.UseCalibration     = cms.bool(True)





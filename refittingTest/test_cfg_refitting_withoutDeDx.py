import FWCore.ParameterSet.Config as cms

process = cms.Process('HSCP')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2500)
    )

process.source = cms.Source("PoolSource",
                            fileNames =
                            cms.untracked.vstring("file:TTJets_Summer12_S10_1303.root"
                                                  )
                            )

process.output = cms.OutputModule("PoolOutputModule",
                 outputCommands = cms.untracked.vstring( (
                                  'keep *',
                                  ) ),
                 fileName = cms.untracked.string('hscpfile.root'),
                 )


process.load("FWCore.MessageService.MessageLogger_cfi")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
	
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.Services_cff')


#globalTagMC   = 'START53_V7G'
#globalTagMC   = 'START53_V7A'
globalTagMC   = 'START53_V7C'
process.GlobalTag.globaltag = globalTagMC   + '::All'
#process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")



process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")


process.TrackRefitter.src = "generalTracksReduced"
process.generalTracksReduced = cms.EDFilter("TrackSelector",
                                 src = cms.InputTag("generalTracks"), 
                                 cut = cms.string("pt > 30"),
                                 filter = cms.bool(False)
                                 )


process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")
process.load("Ntuples.MyNtuple.ntuple_cfi_RECO_refittingDiagnostics")

process.path     = cms.Path(process.offlineBeamSpot + process.generalTracksReduced + process.TrackRefitter)
process.endPath1 = cms.EndPath(process.output + process.demo)


process.demo.ntupleName= cms.untracked.string('ntuple_refittingDiagnostics.root')

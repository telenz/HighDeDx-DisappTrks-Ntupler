#$Revision: 1.1 $
import FWCore.ParameterSet.Config as cms

process = cms.Process("TheNtupleMaker")

process.load("FWCore.MessageService.MessageLogger_cfi")
# See TheNtupleMaker twiki for a brief explanation
#process.MessageLogger.destinations = cms.untracked.vstring("cerr")
#process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.default.limit = 5

# This is required in order to configure HLTConfigProducer
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")

#This is required to store hit position information
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
globalTagMC   = 'START53_V7G'
process.GlobalTag.globaltag = globalTagMC   + '::All'
process.GlobalTag.toGet = cms.VPSet(
   cms.PSet( record = cms.string('SiStripDeDxMip_3D_Rcd'),
            tag = cms.string('MC7TeV_Deco_3D_Rcd_38X'),
            connect = cms.untracked.string("sqlite_file:/nfs/dust/cms/user/tlenz/WellsCode/Files/MC7TeV_Deco_SiStripDeDxMip_3D_Rcd.db")),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
                            fileNames =
                            cms.untracked.vstring("file:ttH_pat2bean_53x.root"
                                                  )
                            )
process.load("Ntuples.MyNtuple.ntuple_cfi_RECO")

process.p = cms.Path(process.demo)


import sys
import copy
import FWCore.ParameterSet.Config as cms


process = cms.Process( 'ProtonAnalysis' )

globalTagData = 'FT53_V21A_AN6'
globalTagMC   = 'START53_V27'


# === Parse external arguments === #
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing("analysis")

options.register ('runOnMC',
		  1,
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.bool )

options.register ('runOnRECO',
		  1,
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.bool )

options.parseArguments()

runOnMC = options.runOnMC
runOnRECO = options.runOnRECO


# === Print some basic info about the job setup === #
print ''
print ' ========================================='
print '     ALCARECO Production Job'
print ' ========================================='
print ''
print '     Run on MC......%d' % runOnMC
print '     Run on RECO....%d' % runOnRECO 
print ''
print ' ========================================='
print ''
process.load( "Configuration.StandardSequences.FrontierConditions_GlobalTag_cff" )
import FWCore.ParameterSet.Config as cms


from Configuration.Geometry.GeometryIdeal_cff import *
from Configuration.StandardSequences.MagneticField_cff import *
from Configuration.StandardSequences.FrontierConditions_GlobalTag_cff import *
from Configuration.AlCa.GlobalTag import GlobalTag
if runOnMC:
  process.GlobalTag = GlobalTag( process.GlobalTag, globalTagMC + '::All' )
else:
  process.GlobalTag = GlobalTag( process.GlobalTag, globalTagData + '::All' )


process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(1000),
  )

process.source = cms.Source("PoolSource",
                            fileNames =
                            cms.untracked.vstring("file:ALCARECO.root"
                                                  )
                            )
if(runOnMC):
  process.source.fileNames = cms.untracked.vstring("file:ALCARECO_MC.root")
else:
  process.source.fileNames = cms.untracked.vstring("file:ALCARECO.root")
  
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('out_alcareco.root'),
                               dropMetaData = cms.untracked.string('ALL'),
                               outputCommands = cms.untracked.vstring('drop *', 
                                                                      'keep *')
                               )

if(runOnMC):
  process.out.fileName = cms.untracked.string('out_alcareco_mc.root')
else:
  process.out.fileName = cms.untracked.string('out_alcareco_data.root')

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000;
process.MessageLogger.cerr.default.limit = 5

##--## HSCP
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.Services_cff')

process.load("SUSYBSMAnalysis.HSCP.HSCParticleProducer_cff")  #

process.HSCParticleProducer.useBetaFromEcal = cms.bool(False)
 
process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.genParticles.abortOnUnknownPDGCode = cms.untracked.bool(False)

if runOnMC:
  process.GlobalTag.toGet = cms.VPSet(
    cms.PSet( record = cms.string('SiStripDeDxMip_3D_Rcd'),
              tag = cms.string('MC7TeV_Deco_3D_Rcd_38X'),
              connect = cms.untracked.string("sqlite_file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/MC7TeV_Deco_SiStripDeDxMip_3D_Rcd.db")),	    
    )
else:
  process.GlobalTag.toGet = cms.VPSet(
    cms.PSet( record = cms.string('SiStripDeDxMip_3D_Rcd'),
              tag = cms.string('Data7TeV_Deco_3D_Rcd_38X'),
              connect = cms.untracked.string("sqlite_file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data7TeV_Deco_SiStripDeDxMip_3D_Rcd.db")),
    )

if runOnMC:
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
else:
  process.dedxHarm2.calibrationPath      = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  process.dedxTru40.calibrationPath      = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  process.dedxProd.calibrationPath       = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  process.dedxASmi.calibrationPath       = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  process.dedxNPHarm2.calibrationPath    = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  process.dedxNPTru40.calibrationPath    = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  process.dedxNSHarm2.calibrationPath    = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  process.dedxNSTru40.calibrationPath    = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  process.dedxNPProd.calibrationPath     = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  process.dedxNPASmi.calibrationPath     = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  process.dedxHitInfo.calibrationPath    = cms.string("file:/nfs/dust/cms/user/tlenz/HighDeDx-DisappTrks-Ntupler/CMSSW_5_3_8_patch1/src/SUSYBSMAnalysis/HSCP/data/Data8TeVGains.root")
  
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

process.HSCParticleProducerSeq.remove(process.HSCParticleProducer)
process.HSCParticleProducerSeq.remove(process.MuonOnlySeq)
process.HSCParticleProducerSeq.remove(process.muontiming)
process.HSCParticleProducerSeq.remove(process.dt4DSegmentsMT)

if(runOnMC):
  process.generalTracksReduced = cms.EDFilter("TrackSelector",
                                              src = cms.InputTag("generalTracks"), 
                                              cut = cms.string("p > 0.5 && p < 2.5 && trackerExpectedHitsInner.numberOfLostHits==0 && hitPattern.trackerLayersWithoutMeasurement==0"),
                                              filter = cms.bool(False)
                                              )
else:
  process.generalTracksReduced = cms.EDFilter("TrackSelector",
                                            src = cms.InputTag("ALCARECOSiStripCalMinBias"), 
                                            cut = cms.string("p > 0.5 && p < 2.5 && trackerExpectedHitsInner.numberOfLostHits==0 && hitPattern.trackerLayersWithoutMeasurement==0"),
                                            filter = cms.bool(False)
                                            )


process.pPF = cms.Path()
if(runOnRECO):
  process.TrackRefitter.src =  cms.InputTag("generalTracksReduced")
  process.pPF += process.generalTracksReduced+process.HSCParticleProducerSeq
else:
  process.pPF += process.generalTracksReduced
##--## HSCP

process.genParticlesReduced  = cms.EDFilter("GenParticleSelector",
                                            src = cms.InputTag("genParticles"), 
                                            cut = cms.string("p > 0.2 && p < 10 && status !=2 && charge!=0"),
                                            filter = cms.bool(False)
                                            )
if(runOnMC):
  process.pPF += process.genParticlesReduced

process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")
process.load("Ntuples.MyNtuple.ntuple_cfi_ALCARECO")
  
process.pPF += process.demo

process.outpath  = cms.EndPath(process.out)
#process.schedule = cms.Schedule(process.pPF,process.outpath)
process.schedule = cms.Schedule(process.pPF)


## Dump python config if wished
outfile = open('dumpALCARECO.py','w'); print >> outfile,process.dumpPython(); outfile.close()
#if(runOnMC):
#  outfile = open('dumpALCARECO_MC.py','w'); print >> outfile,process.dumpPython(); outfile.close()
#else:
#  outfile = open('dumpALCARECO_data.py','w'); print >> outfile,process.dumpPython(); outfile.close()

import FWCore.ParameterSet.Config as cms

#Trigger bit requirement
import HLTrigger.HLTfilters.triggerResultsFilter_cfi as hlt
EXODisplacedPhoton = hlt.triggerResultsFilter.clone()
EXODisplacedPhoton.triggerConditions = cms.vstring('HLT_DisplacedPhoton65*',)
EXODisplacedPhoton.hltResults = cms.InputTag( "TriggerResults", "", "HLT" )
EXODisplacedPhoton.l1tResults = cms.InputTag("")
EXODisplacedPhoton.throw = cms.bool( False )
